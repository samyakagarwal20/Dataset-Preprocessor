from tkinter import font as tkfont

class Empty_export_file_path_Error(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Existing_table_Error(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Database_exists_Error(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg
        
class Empty_database_name_Error(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Empty_table_name_Error(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Database_creation_choice_Error(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg
        

class Event_handler:
    def window_maker(obj,w,h):
        try:
            import tkinter as tk
            from tkinter import ttk
            import tkinter.messagebox as msgbox
        except ImportError:
            msgbox.showerror("Error","Error importing the tkinter module!!")
        else:
            obj.new_window=tk.Toplevel(obj)
            obj.canvas_main=tk.Canvas(obj.new_window,width=w,height=h,bg="black")
            obj.canvas_main.grid(row=1)

    def window_creator(obj):
        try:
            import tkinter as tk
            from tkinter import ttk
            import tkinter.messagebox as msgbox
        except ImportError:
            msgbox.showerror("Error","Error loading the tkinter module")
        else:
            obj.mysql_data_window=tk.Toplevel(obj)
            obj.mysql_data_window.title("Export")
            obj.database_name=tk.StringVar()
            obj.table_name=tk.StringVar()
            ttk.Label(obj.mysql_data_window,text="MySQL Database Name : ").grid(row=1,column=0,padx=10,pady=10)
            ttk.Label(obj.mysql_data_window,text="MySQL Table Name : ").grid(row=2,column=0,padx=10,pady=10)
            ttk.Entry(obj.mysql_data_window,textvariable=obj.database_name).grid(row=1,column=1,padx=(0,10),pady=10)
            ttk.Entry(obj.mysql_data_window,textvariable=obj.table_name).grid(row=2,column=1,padx=(0,10),pady=10)
            ttk.Button(obj.mysql_data_window,text="Export",command=lambda : Event_handler.mysql_export(obj)).grid(row=3,columnspan=2,pady=10)

    def mysql_export(obj):
        try:
            import tkinter.messagebox as msgbox
        except ImportError:
            print("Error loading messagebox module!!")
        else:
            try:
                from sqlalchemy import create_engine
            except ImportError:
                msgbox.showerror("Error","Error establishing the connection with the database!!\nThe module SQLAlchemy cannot be imported.")
            else:
                try:
                    if obj.database_name.get()=="":
                        raise Empty_database_name_Error("The database name entry cannot be left empty!!\nEnter a valid database name to continue..")
                    elif obj.table_name.get()=="":
                        raise Empty_table_name_Error("The table name entry cannot be left empty!!\nEnter a valid table name to continue..")
                except Empty_database_name_Error as e:
                    msgbox.showerror("Error",e.msg)
                except Empty_table_name_Error as e:
                    msgbox.showerror("Error",e.msg)
                else:
                    try:
                        import MySQLdb._exceptions
                        engine=create_engine(f"mysql://{obj.username.get()}:{obj.password.get()}@{obj.entry4_host.get()}/{obj.dbname.get()}")
                        con=engine.connect()
                        if con:
                            print(con)
                            msgbox.showinfo("Success","Connection established successfully with MySQL database!!")
                    except MySQLdb._exceptions.OperationalError:
                        msgbox.showerror("Error","Error establishing connection with the database!!\nPlease enter valid details to continue...")
                    else:
                        try:
                            import pandas as pd
                        except ImportError:
                            msgbox.showerror("Error","Error importing the pandas module!!\nThe dataset cannot be loaded.")
                            con.close()
                        else:
                            db_tuple=con.execute("Show Databases")
                            db_list=list()
                            print(obj.database_name.get())
                            for i_tuple in db_tuple:
                                for j in i_tuple:
                                    db_list.append(j)
                            if not obj.database_name.get() in db_list:
                                choice=msgbox.askyesnocancel("Create Database","The database entered by you doesn't exists in the list of already created databases.\nWould you like to create one with that name ?")
                                try:
                                    if choice:
                                        con.execute("CREATE DATABASE IF NOT EXISTS "+obj.database_name.get())
                                        msgbox.showinfo("Database creation","Database created successfully!!")
                                        con.execute("USE "+obj.database_name.get())
                                        import pandas.io.sql
                                        obj.df.to_sql(obj.table_name.get(),con)
                                        obj.mysql_data_window.withdraw()
                                        msgbox.showinfo("Success","Dataset exported successfully!!")
                                        con.close()
                                    else:
                                        raise Database_creation_choice_Error("Error exporting the data to the database.\nOperation Aborted")
                                except Database_creation_choice_Error as e:
                                    msgbox.showerror("Error",e.msg)
                                    obj.mysql_data_window.withdraw()
                                    con.close()
                            else:
                                con.execute("USE "+obj.database_name.get())
                                try:
                                    table_tuple=con.execute("SHOW TABLES")
                                    table_list=list()
                                    for i_tuple in table_tuple:
                                        for j in i_tuple:
                                            table_list.append(j)
                                    if not obj.table_name.get() in table_list:
                                        obj.df.to_sql(obj.table_name.get(),con,index=False)
                                        obj.mysql_data_window.withdraw()
                                        msgbox.showinfo("Success","Dataset exported successfully!!")
                                        con.close()
                                    else:
                                        raise Existing_table_Error("A table with the same name already exists in the database!!\nEnter a new name for the table to proceed.")
                                except Existing_table_Error as e:
                                    msgbox.showerror("Error",e.msg)
                                    con.close()
                                
    def view_label_frame2(obj):
        obj.label_frame2.grid()
        obj.label_frame3.grid_remove()
        obj.label_frame4.grid_remove()
        
    def view_label_frame3(obj):
        obj.label_frame3.grid()
        obj.label_frame2.grid_remove()
        obj.label_frame4.grid_remove()
        
    def view_label_frame4(obj):
        obj.label_frame4.grid()
        obj.label_frame2.grid_remove()
        obj.label_frame3.grid_remove()

    def load_data(obj):
        try:
            from modules.loader import load as ld
        except ImportError:
            msgbox.showerror("Error","Error loading the loader module!!")
        obj.df_empty_status=None
        obj.df_load_status=ld.load_dataset(obj)
        if obj.df_load_status:
            print(obj.df)
            obj.label_frame5.grid()
            obj.bt_frame.grid()
            obj.label_frame6.grid_remove()
            obj.cleaning_mode.set("")
            obj.manual_clean_choice.set("")
            obj.cleanser_bt.grid_remove()
            obj.tabcontrol.select(1)
        else:
            obj.label_frame5.grid_remove()
            obj.bt_frame.grid_remove()

    def view_data(obj):
        if obj.df_load_status:
            try:
                import tkinter as tk
                from tkinter import ttk
                import tkinter.messagebox as msgbox
            except ImportError:
                msgbox.showerror("Error","Error importing the tkinter module!!")
            else:
                obj.dataset_display=tk.Toplevel(obj)
                obj.dataset_display.title("Dataset")
                obj.df_contain=tk.Text(obj.dataset_display,width=100)
                rows,columns=obj.df.shape
                obj.df_contain.insert(tk.END,str(obj.df.iloc[:rows,:columns]))
                obj.df_contain.pack()

    def export_data(obj):
        try:
            import tkinter as tk
            import tkinter.messagebox as msgbox
        except ImportError:
            msgbox.showerror("Error","Error loading the tkinter package!!")
        else:
            try:
                from tkinter import filedialog as fd
            except ImportError:
                msgbox.showerror("Error","Error loading the filedialog module!!")
            if obj.value=="csv":
                try:
                    export_file_path=fd.asksaveasfile(filetypes=[("CSV File","*.csv"),("All Files","*.*")],defaultextension="*.csv",initialdir=obj.fDir,initialfile="Untitled")
                    if export_file_path:
                        try:
                            import pandas as pd
                        except ImportError:
                            msgbox.showerror("Error","Error loading the pandas module!!")
                        else:
                            try:
                                obj.df.to_csv(export_file_path,encoding="utf-8")
                                msgbox.showinfo("Success","Dataset exported successfully!!")
                            except UnicodeEncodeError as e:
                                msgbox.showerror("Error",f"Error : {e}")
                    else:
                        raise Empty_export_file_path_Error("Operation Unsuccessfull\nDataset not exported.!!")
                except Empty_export_file_path_Error as e:
                    msgbox.showerror("Error",e.msg)
            elif obj.value=="excel":
                try:
                    export_file_path=fd.asksaveasfile(filetypes=[("Excel File","*.xlsx *.xls"),("All Files","*.*")],defaultextension="*.xlsx",initialdir=obj.fDir,initialfile="Untitled")
                    if export_file_path:
                        try:
                            import pandas as pd
                        except ImportError:
                            msgbox.showerror("Error","Error loading the pandas module!!")
                        else:
                            obj.df.to_excel(export_file_path,encoding="utf-8")
                            msgbox.showinfo("Success","Dataset exported successfully!!")
                    else:
                        raise Empty_export_file_path_Error("Operation Unsuccessfull\nDataset not exported.!!")
                except Empty_export_file_path_Error as e:
                    msgbox.showerror("Error",e.msg)
                except ModuleNotFoundError as e:
                    msgbox.showerror("Error",f"Error : {e}")
                except TypeError as e:
                    msgbox.showerror("Error",f"Error : {e}")
            else:
                Event_handler.window_creator(obj)
                
            
    def query(obj):
        try:
            import tkinter as tk
            from tkinter import ttk
            import tkinter.messagebox as msgbox
        except ImportError:
            msgbox.showerror("Error","Error importing the tkinter module!!")
        else:
            query_window=tk.Toplevel()
            query_window.title("Query")
            email_id=tk.StringVar()
            subject=tk.StringVar()
            ttk.Label(query_window,text="Email id : ").grid(row=1,column=0,padx=10,pady=10)
            ttk.Label(query_window,text="Subject : ").grid(row=2,column=0,padx=10,pady=10)
            ttk.Label(query_window,text="Query : ").grid(row=3,column=0,padx=10,pady=10)
            ttk.Entry(query_window,textvariable=email_id,width=40).grid(row=1,column=1,padx=(0,10),pady=1,sticky=tk.W)
            ttk.Entry(query_window,textvariable=subject,width=40).grid(row=2,column=1,padx=(0,10),pady=10,sticky=tk.W)
            tk.Text(query_window,wrap=tk.WORD,width=30,height=6).grid(row=3,column=1,padx=(0,10),pady=10,sticky=tk.W)
            ttk.Button(query_window,text="Submit",width=10).grid(row=4,columnspan=2,pady=10)
        
    def support():
        try:
            import tkinter as tk
            from tkinter import ttk
            import tkinter.messagebox as msgbox
        except ImportError:
            msgbox.showerror("Error","Error importing the tkinter module!!")
        else:
            msgbox.showinfo("Support","For any technical assistance , email us at kaymasagarwal@gmail.com\nContact no : +91-8126145915")

    def developer(obj):
        try:
            import tkinter as tk
            from tkinter import ttk
            import tkinter.messagebox as msgbox
        except ImportError:
            msgbox.showerror("Error","Error importing the tkinter module!!")
        else:
            width=600
            height=300
            Event_handler.window_maker(obj,width,height)
            obj.new_window.title("Developer Information")
            obj.canvas_main.create_rectangle(20,20,580,280,fill="gold")
            try:
                from PIL import Image,ImageTk
            except ImportError:
                msgbox.showerror("Error","Error loading the PIL module!!")
            else:
                obj.image=ImageTk.PhotoImage(Image.open(r"C:\Users\Lenovo\Desktop\resized.jpg"))
                obj.canvas_main.create_image(40,40,image=obj.image,anchor='nw')
                #Creating a font object
                font1=tkfont.Font(family="Purisa",size=16)
                content="""This application is developed by Samyak Agarwal , currently pursuing my 5th semester of B.Tech CSE from AMITY UNIVERSITY HARYANA . I am originally from Kotdwara , Uttarakhand ."""
                obj.canvas_main.create_text(260,40,text=content,anchor='nw',width=320,font=font1)

    def application(obj):
        try:
            import tkinter as tk
            from tkinter import ttk
            import tkinter.messagebox as msgbox
        except ImportError:
            msgbox.showerror("Error","Error importing the tkinter module!!")
        else:
            width=620
            height=400
            Event_handler.window_maker(obj,width,height)
            obj.new_window.title("Application Information")
            obj.canvas_main.create_rectangle(20,20,600,480,fill="gold")
            font1=tkfont.Font(family="Purisa",size=15)
            content="""This application is a GENERIC DATASET PREPROCESSOR . This application is implemented on the concept of DATA SCIENCE by using PYTHON as the programming language . The python package which is used to build this application is TKINTER . This application is capable of loading any dataset from either of the following : .csv file , .xlsx file or mysql database . Furthermore , after the dataset has been loaded successfully , it becomes ready to be cleansed either autoatically or manually depending upon the choice of the user."""
            obj.canvas_main.create_text(40,40,text=content,anchor='nw',width=560,font=font1)

            
    def _quit(obj):
        try:
            import tkinter.messagebox as msgbox
        except ImportError:
            msgbox.showerror("Error","Error loading rhe tkinter module!!")
        else:
            ch=msgbox.askyesno("Exit","Are you sure that you want to quit the application ?")
            if ch:
                obj.quit()
                obj.destroy()
                exit()
            else:
                pass
