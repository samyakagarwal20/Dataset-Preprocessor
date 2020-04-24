import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox           # for message box widget
from tkinter import Menu                      # importing the menu class of tkinter to add a menu widget to our application
from modules.click_events import Event_handler as ceh
from modules.threads import Thread_handler as th

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dataset Preprocessor")
        self.resizable(width=False,height=False)
        #Getting the filepath of the current running script
        from os import path
        self.fDir=path.dirname(__file__)
        self.iconphoto(True,tk.PhotoImage(file=path.join(self.fDir,'icon.png')))
        self.create_widgets()
        
    def create_widgets(self):
        
        #defining variables
        self.radiobutton_value=tk.StringVar()
        self.entry_csv=tk.StringVar()
        self.entry_excel=tk.StringVar()
        self.excel_sheet_name=tk.StringVar()
        self.entry_mysql=tk.StringVar()
        self.username=tk.StringVar()
        self.password=tk.StringVar()
        self.dbname=tk.StringVar()
        self.tablename=tk.StringVar()
        self.cleaning_mode=tk.StringVar()
        self.manual_clean_choice=tk.StringVar()
        self.select_button_click_status=False
        self.cleaned_status=False
        self.manual_option=""
        
        #Adding a menubar
        self.menu_bar=Menu(self)
        self.config(menu=self.menu_bar)
        #Adding the file menu to the menubar 
        self.file_menu=Menu(self.menu_bar,tearoff=0)
        self.file_menu.add_command(label="Exit",command=lambda : ceh._quit(self))
        self.menu_bar.add_cascade(label="File",menu=self.file_menu)
        #Adding the help menu to the menubar
        self.help=Menu(self.menu_bar,tearoff=0)
        self.help.add_command(label="Query",command=lambda : th.query_thread(self))
        self.help.add_separator()
        self.help.add_command(label="Support",command=th.support_thread)
        self.menu_bar.add_cascade(label="Help",menu=self.help)
        #Adding the About menu to the menubar
        self.about=Menu(self.menu_bar,tearoff=0)
        self.about.add_command(label="Developer",command=lambda : th.developer_thread(self))
        self.about.add_separator()
        self.about.add_command(label="Application",command=lambda : th.application_thread(self))
        self.menu_bar.add_cascade(label="About",menu=self.about)
        
        #Adding the tabbed widgets
        self.tabcontrol=ttk.Notebook(self)
        self.tab1=ttk.Frame(self.tabcontrol)
        self.tabcontrol.add(self.tab1,text="Dataset Loader")
        self.tab2=ttk.Frame(self.tabcontrol)
        self.tabcontrol.add(self.tab2,text="Cleanser")
        self.tabcontrol.pack(expand=1,fill=tk.BOTH)
        
        #Adding the labelframes in Dataset loader tab
        self.label_frame1=ttk.LabelFrame(self.tab1,text="Modes for loading the dataset")
        self.label_frame1.grid(row=1,padx=25,pady=10,sticky='WE')
        self.label_frame2=ttk.LabelFrame(self.label_frame1,text="Load Comma Seperated Value(.csv) file")
        self.label_frame2.grid(row=3,padx=10,pady=10)
        self.label_frame3=ttk.LabelFrame(self.label_frame1,text="Load Excel(.xlsx) file")
        self.label_frame3.grid(row=5,padx=10,pady=10)
        self.label_frame4=ttk.LabelFrame(self.label_frame1,text="Load Using MySQL server")
        self.label_frame4.grid(row=7,padx=10,pady=10)
        self.label_frame2.grid_remove()
        self.label_frame3.grid_remove()
        self.label_frame4.grid_remove()
        
        #Adding wigets to self.label_frame1
        self.label_radio_choice=ttk.Label(self.label_frame1,text="Select an option to load dataset from : ")
        self.label_radio_choice.grid(row=1,column=0,padx=10,pady=10,sticky=tk.W)
        self.radio_csv=ttk.Radiobutton(self.label_frame1,text=".csv file",variable=self.radiobutton_value,value="csv",command=lambda : th.view_label_frame2_thread(self))
        self.radio_csv.grid(row=2,column=0,padx=10,pady=10,sticky=tk.W)
        self.radio_excel=ttk.Radiobutton(self.label_frame1,text=".xlsx file",variable=self.radiobutton_value,value="excel",command=lambda : th.view_label_frame3_thread(self))
        self.radio_excel.grid(row=4,column=0,padx=10,pady=10,sticky=tk.W)
        self.radio_mysql=ttk.Radiobutton(self.label_frame1,text="MySQL database",variable=self.radiobutton_value,value="mysql",command=lambda : th.view_label_frame4_thread(self))
        self.radio_mysql.grid(row=6,column=0,padx=10,pady=10,sticky=tk.W)
        
        #Adding widgets to self.label_frame2
        self.label2=ttk.Label(self.label_frame2,text="Select File : ")
        self.label2.grid(row=1,column=0,padx=10,pady=10)
        self.entry2=ttk.Entry(self.label_frame2,textvariable=self.entry_csv,width=42)
        self.entry2.grid(row=1,column=1,padx=(0,10),pady=10)
        self.button2=ttk.Button(self.label_frame2,text="Browse",command=lambda : th.browse_csv_thread(self))
        self.button2.grid(row=1,column=2,padx=(0,10),pady=10)
        #Adding the dataset loader button to label_frame2
        self.loader_bt=ttk.Button(self.label_frame2,text="Load Dataset",command=lambda : th.load_data_thread(self),width=20)
        self.loader_bt.grid(row=2,columnspan=3,pady=10)
        
        #Adding widgets to self.label_frame3
        self.label3=ttk.Label(self.label_frame3,text="Select File : ")
        self.label3.grid(row=1,column=0,padx=10,pady=10)
        self.entry3=ttk.Entry(self.label_frame3,textvariable=self.entry_excel,width=42)
        self.entry3.grid(row=1,column=1,padx=(0,10),pady=10)
        self.button3=ttk.Button(self.label_frame3,text="Browse",command=lambda : th.browse_xlsx_thread(self))
        self.button3.grid(row=1,column=2,padx=(0,10),pady=10)
        self.label3_sheet_name=ttk.Label(self.label_frame3,text="Sheet name : ")
        self.label3_sheet_name.grid(row=2,column=0,padx=10,pady=10)
        self.entry3_sheet_name=ttk.Entry(self.label_frame3,textvariable=self.excel_sheet_name,width=35)
        self.entry3_sheet_name.grid(row=2,column=1,columnspan=2,padx=(0,10),pady=10,sticky=tk.W)
        #Adding the dataset loader button to label_frame3
        self.loader_bt=ttk.Button(self.label_frame3,text="Load Dataset",command=lambda : th.load_data_thread(self),width=20)
        self.loader_bt.grid(row=3,columnspan=3,pady=10)
        
        #Adding widgets to self.label_frame4
        self.label4_username=ttk.Label(self.label_frame4,text="MySQL Username ")
        self.label4_username.grid(row=1,column=0,padx=10,pady=(10,0))
        self.entry4_username=ttk.Entry(self.label_frame4,textvariable=self.username)
        self.entry4_username.grid(row=2,column=0,padx=10,pady=4)
        self.label4_password=ttk.Label(self.label_frame4,text="MySQL Password ")
        self.label4_password.grid(row=1,column=1,padx=10,pady=(10,0))
        self.entry4_password=ttk.Entry(self.label_frame4,textvariable=self.password,show="*")
        self.entry4_password.grid(row=2,column=1,padx=10,pady=4)
        self.label4_host=ttk.Label(self.label_frame4,text="MySQL Host ")
        self.label4_host.grid(row=1,column=2,padx=10,pady=(10,0))
        self.entry4_host=ttk.Entry(self.label_frame4)
        self.entry4_host.insert(0,"127.0.0.1")
        self.entry4_host.configure(state="readonly")
        self.entry4_host.grid(row=2,column=2,padx=10,pady=4)
        self.label4_database=ttk.Label(self.label_frame4,text="MySQL Database : ")
        self.label4_database.grid(row=3,column=0,padx=10,pady=6)
        self.entry4_database=ttk.Entry(self.label_frame4,textvariable=self.dbname)
        self.entry4_database.grid(row=3,column=1,columnspan=2,padx=(0,10),pady=6,sticky=(tk.W+tk.E))
        self.label4_table=ttk.Label(self.label_frame4,text="MySQL Table name : ")
        self.label4_table.grid(row=4,column=0,padx=10,pady=6)
        self.entry4_table=ttk.Entry(self.label_frame4,textvariable=self.tablename)
        self.entry4_table.grid(row=4,column=1,columnspan=2,padx=(0,10),pady=6,sticky=(tk.W+tk.E))
        #Adding the dataset loader button to label_frame4
        self.loader_bt=ttk.Button(self.label_frame4,text="Load Dataset",command=lambda : th.load_data_thread(self),width=20)
        self.loader_bt.grid(row=5,columnspan=3,pady=10)

        #Adding the labelframes in the cleanser tab
        self.label_frame5=ttk.LabelFrame(self.tab2,text="Mode of data cleansing")
        self.label_frame5.grid(row=1,padx=10,pady=10)
        self.label_frame6=ttk.LabelFrame(self.label_frame5,text="Manual Cleansing Operations")
        self.label_frame6.grid(row=2,columnspan=3,padx=10,pady=10)
        self.label_frame5.grid_remove()
        self.label_frame6.grid_remove()
        
        #Adding widgets to label_frame5
        self.label_clean=ttk.Label(self.label_frame5,text="Mode of cleansing : ")
        self.label_clean.grid(row=1,column=0,padx=30,pady=20)
        self.modes_of_cleaning=["Automatic","Manual"]
        self.combobox_clean=ttk.Combobox(self.label_frame5,textvariable=self.cleaning_mode,values=self.modes_of_cleaning,width=20,state="readonly")
        self.combobox_clean.grid(row=1,column=1,padx=(0,20),pady=20)
        self.clean_choice_select_bt=ttk.Button(self.label_frame5,text="Choose",command=lambda : th.cleaning_main_choice_thread(self),width=14)
        self.clean_choice_select_bt.grid(row=1,column=2,padx=(10,10),pady=20)

        #Adding widgets to self.label_frame6
        self.label_manual_clean_choice=tk.Label(self.label_frame6,text="Select your choice : ")
        self.label_manual_clean_choice.grid(row=1,column=0,padx=10,pady=10)
        self.manual_choice_list=["Check if dataset is cleansed","Getting the no. of NaN values per column",
                           "Drop the rows with NaN values","Drop the columns with NaN values",
                           "Fill NaN values by a specific value","Fill NaN values column-wise",
                           "Predict the possible values"]
        self.combobox_manual_clean=ttk.Combobox(self.label_frame6,textvariable=self.manual_clean_choice,values=self.manual_choice_list,state="readonly",width=30)
        self.combobox_manual_clean.grid(row=1,column=1,padx=0,pady=20)
        self.manual_choice_select_bt=ttk.Button(self.label_frame6,text="Choose",command=lambda : th.manual_choice_select_button_thread(self),width=14)
        self.manual_choice_select_bt.grid(row=1,column=2,padx=(10,10),pady=20)
        
        #Adding the dataset cleanser button
        self.cleanser_bt=ttk.Button(self.label_frame5,text="Clean Dataset",command=lambda : th.cleanser_button_click_thread(self),width=20)
        self.cleanser_bt.grid(row=3,columnspan=3,pady=20)
        self.cleanser_bt.grid_remove()

        #Creating a Frame for the button
        self.bt_frame=ttk.Frame(self.tab2)
        self.bt_frame.grid(row=2,padx=10,pady=(10,0),sticky='WE')
        self.bt_frame.grid_remove()
        
        #Adding the buttons to the frame widget
        self.export_bt=ttk.Button(self.bt_frame,text="Export Dataset",command=lambda : th.export_data_thread(self))
        self.export_bt.pack(padx=8,side=tk.RIGHT)
        self.view_bt=ttk.Button(self.bt_frame,text="View Dataset",command=lambda : th.view_data_thread(self))
        self.view_bt.pack(padx=8,side=tk.RIGHT)
        self.finish_bt=ttk.Button(self.bt_frame,text="Finish",command=lambda : ceh._quit(self),width=12)
        self.finish_bt.pack(padx=8,side=tk.RIGHT)
        

if __name__=='__main__':
    app=Application()
    app.mainloop()
