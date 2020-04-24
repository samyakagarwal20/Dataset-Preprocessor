try:
    import tkinter as tk
except ImportError:
    print("Error loading tkinter module!!")
try:
    import tkinter.messagebox as msgbox
except ImportError:
    print("Error loading messagebox module!!")
try:
    import xlrd
except ImportError:
    print("Error loading the xlrd module!!")
try:
    import copy
except ImportError:
    msgbox("Error loading the copy module!!")

class NameError(Exception):
    """Raised when the sheet name for the excel workbook is not valid"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Invalid_sheet_name_Error(Exception):
    """Raised when the sheet name for the excel workbook is not valid"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Empty_sheet_name_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Empty_username_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Empty_password_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Empty_database_name_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Empty_table_name_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg


class load:
    """This class contains the functions to load the dataset into a dataframe"""
    copy_path=None
    def browse_csv(inst):
        """This method acquires the path of the .csv file selected by the user and insert into the entry widget"""
        try:
            from tkinter import filedialog as fd
        except ImportError as err:
            msgbox.showerror("Error",f"Error loading module : {err}")
        else:
            inst.temp_path=""
            inst.filepath=fd.askopenfilename(title="Select .csv file",initialdir=inst.fDir,filetypes=[("CSV files",".csv")])
            global copy_path
            copy_path=inst.filepath
            if inst.filepath:
                inst.temp_path=copy.deepcopy(inst.filepath)
                inst.entry2.configure(state="active")
                inst.entry2.delete(0,tk.END)
                inst.entry2.insert(0,inst.temp_path)
                inst.entry2.configure(state="readonly")
                inst.entry3.configure(state="active")
                inst.entry3.delete(0,tk.END)
                inst.excel_sheet_name.set(None)
                inst.entry3_sheet_name.delete(0,tk.END)
                inst.entry4_username.delete(0,tk.END)
                inst.entry4_password.delete(0,tk.END)
                inst.entry4_database.delete(0,tk.END)
                inst.entry4_table.delete(0,tk.END)
            else:
                inst.entry2.configure(state="active")
                inst.entry2.delete(0,tk.END)
                inst.entry2.insert(0,inst.temp_path)
                inst.entry2.configure(state="readonly")
                inst.entry3.configure(state="active")
                inst.entry3.delete(0,tk.END)
                inst.excel_sheet_name.set(None)
                inst.entry3_sheet_name.delete(0,tk.END)
                inst.entry4_username.delete(0,tk.END)
                inst.entry4_password.delete(0,tk.END)
                inst.entry4_database.delete(0,tk.END)
                inst.entry4_table.delete(0,tk.END)

    def browse_xlsx(inst):
        """This method acquires the path of the .xlsx or .xls file selected by the user and insert into the entry widget"""
        try:
            from tkinter import filedialog as fd
        except ImportError as err:
            msgbox.showerror("Error",f"Error loading module : {err}")
        else:
            inst.temp_path=""
            inst.filepath=fd.askopenfilename(title="Select .xlsx file",initialdir=inst.fDir,filetypes=[("Excel files",".xlsx .xls")])
            global copy_path
            copy_path=inst.filepath
            if inst.filepath:
                inst.temp_path=copy.deepcopy(inst.filepath)
                inst.entry3.configure(state="active")
                inst.entry3.delete(0,tk.END)
                inst.entry3.insert(0,inst.temp_path)
                inst.entry3.configure(state="readonly")
                inst.entry2.configure(state="active")
                inst.entry2.delete(0,tk.END)
                inst.entry4_username.delete(0,tk.END)
                inst.entry4_password.delete(0,tk.END)
                inst.entry4_database.delete(0,tk.END)
                inst.entry4_table.delete(0,tk.END)
            else:
                inst.entry3.configure(state="active")
                inst.entry3.delete(0,tk.END)
                inst.entry3.insert(0,inst.temp_path)
                inst.entry3.configure(state="readonly")
                inst.entry2.configure(state="active")
                inst.entry2.delete(0,tk.END)
                inst.entry4_username.delete(0,tk.END)
                inst.entry4_password.delete(0,tk.END)
                inst.entry4_database.delete(0,tk.END)
                inst.entry4_table.delete(0,tk.END)

    def load_dataset(inst):
        """This method loads the dataset into the pandas dataframe either from .csv file , .xlsx file or from the MySQL database"""
        inst.value=inst.radiobutton_value.get()
        global copy_path
        print(inst.value)
        print("Scope in global :",'copy_path' in globals())
        try:
            import pandas as pd
        except ImportError as err:
            msgbox.showerror("Error",f"Error loading module : {err}"+"\nShuting Down the Program!!")
            inst.destroy()
        else:
            if inst.value=="csv":
                try:
                    if 'copy_path' in globals():
                        try:
                            if inst.temp_path:
                                try:
                                    if inst.temp_path.split(".")[-1]=="csv":
                                        try:
                                            import pandas.io.common
                                            inst.df=pd.read_csv(inst.temp_path)
                                            if not inst.df.empty:
                                                msgbox.showinfo("Success","Dataset Loaded Successfully!!\nYou can proceed to the cleaning section")
                                                return True
                                        except pandas.io.common.EmptyDataError:
                                            msgbox.showerror("Error","The dataset cannot be loaded!!\nThe .csv file selected for loading the file is empty.\nSelect any other file to load the dataset.")
                                            return False
                                    elif inst.temp_path=="":
                                        raise NameError("You need to select the file first to load the dataset")
                                except NameError as e:
                                    msgbox.showerror("Error",e.msg)
                                    return False
                            else:
                                raise NameError("You need to select the file first to load the dataset!!")
                        except NameError as e:
                            msgbox.showerror("Error",e.msg)
                            return False
                    else:
                        raise NameError("You need to select the file first to load the dataset!!")
                except NameError as e:
                    msgbox.showerror("Error",e.msg)
                    return False
            elif inst.value=="excel":
                try:
                    if 'copy_path' in globals():
                        try:
                            if inst.temp_path:
                                try:
                                    if inst.temp_path.split('.')[-1]=="xlsx":
                                        book=xlrd.open_workbook(inst.temp_path)
                                        inst.excel_sheet_name.set(inst.entry3_sheet_name.get())
                                        try:
                                            if inst.excel_sheet_name.get()=="":
                                                raise Empty_sheet_name_Error("The spreadsheet name can't be left empty!!")
                                            elif inst.excel_sheet_name.get() in book.sheet_names():
                                                inst.df=pd.read_excel(inst.temp_path,sheet_name=inst.excel_sheet_name.get())
                                                msgbox.showinfo("Success","Dataset Loaded Successfully!!\nYou can proceed to the cleaning section")
                                                return True
                                            else:
                                                raise Invalid_sheet_name_Error("Enter a valid sheet name from the workbook!!")
                                        except Invalid_sheet_name_Error as e:
                                            msgbox.showerror("Error",e.msg)
                                            inst.entry3_sheet_name.focus()
                                            return False
                                        except Empty_sheet_name_Error as e:
                                            msgbox.showerror("Error",e.msg)
                                            inst.entry3_sheet_name.focus()
                                            return False
                                    else:
                                        raise NameError("You need to select the file first to load the dataset!!")
                                except NameError as e:
                                    msgbox.showerror("Error",e.msg)
                                    return False
                            else:
                                raise NameError("You need to select the file first to load the dataset!!")
                        except NameError as e:
                            msgbox.showerror("Error",e.msg)
                            return False
                    else:
                        raise NameError("You need to select the file first to load the dataset!!")
                except NameError as e:
                    msgbox.showerror("Error",e.msg)
                    return False
            elif inst.value=="mysql":
                try:
                    if inst.username.get()=="":
                        raise Empty_username_Error("The username cannot be empty!!")
                    elif inst.password.get()=="":
                        raise Empty_password_Error("The password cannot be empty!!")
                    elif inst.dbname.get()=="":
                        raise Empty_database_name_Error("The database name cannot be empty!!")
                    elif inst.tablename.get()=="":
                        raise Empty_table_name_Error("The table name cannot be empty!!")
                except Empty_username_Error as e:
                    msgbox.showerror("Error",e.msg)
                    return False
                except Empty_password_Error as e:
                    msgbox.showerror("Error",e.msg)
                    return False
                except Empty_database_name_Error as e:
                    msgbox.showerror("Error",e.msg)
                    return False
                except Empty_table_name_Error as e:
                    msgbox.showerror("Error",e.msg)
                    return False
                else:
                    try:
                        from modules.mysql_db_loader import Connection as ct
                    except ImportError:
                        msgbox.showerror("Error","Error establishing the connection with database!!\nThe module db_connection cannot be imported.")
                    else:
                        status=ct.connect(inst)
                        if status:
                            inst.entry2.configure(state="active")
                            inst.entry2.delete(0,tk.END)
                            inst.entry3.configure(state="active")
                            inst.entry3.delete(0,tk.END)
                            inst.entry3_sheet_name.delete(0,tk.END)
                            return True
                        else:
                            return False
