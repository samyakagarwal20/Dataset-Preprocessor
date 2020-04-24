class Invalid_table_info_Error(Exception):
    """Raised when the sheet name for the excel workbook is not valid"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Cursor_creation_Error(Exception):
    """Raised when the sheet name for the excel workbook is not valid"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class MySQL_empty_dataset_load_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Connection:
    def connect(obj):
        try:
            import tkinter.messagebox as msgbox
        except ImportError:
            print("Error loading messagebox module!!")
            return False
        else:
            try:
                import MySQLdb as mysql
                print("module MySQLdb imported successfully")
            except ImportError:
                msgbox.showerror("Error","Error establishing the connection with the database!!\nThe module MySQLdb cannot be imported.")
                return False
            else:
                try:
                    import MySQLdb._exceptions
                    con=mysql.connect(host=obj.entry4_host.get(),user=obj.username.get(),passwd=obj.password.get(),db=obj.dbname.get())
                    if con:
                        print(con)
                        msgbox.showinfo("Success","Connection established successfully with MySQL database!!")
                except MySQLdb._exceptions.OperationalError:
                    msgbox.showerror("Error","Error establishing connection with the database!!\nPlease enter valid details to continue...")
                    return False
                else:
                    try:
                        import pandas as pd
                    except ImportError:
                        msgbox.showerror("Error","Error importing the pandas module!!\nThe dataset cannot be loaded.")
                        con.close()
                        return False
                    else:
                        try:
                            cursor=con.cursor()
                            if cursor:
                                cursor.execute("SHOW TABLES FROM "+obj.dbname.get())
                                tables_tuple_of_tuple=cursor.fetchall()
                                tables_list=list()
                                for tables_tuple in tables_tuple_of_tuple:
                                    for table in tables_tuple:
                                        tables_list.append(table)
                                try:
                                    if obj.tablename.get() in tables_list:
                                        obj.df=pd.read_sql("SELECT * FROM "+obj.tablename.get(),con)
                                        try:
                                            if not obj.df.empty:
                                                msgbox.showinfo("Success","Dataset loaded successfully!!\nYou can now proceed to the cleansing section")
                                                cursor.close()
                                                con.close()
                                                return True
                                            else:
                                                raise MySQL_empty_dataset_load_Error("The loaded dataset is empty!!\nSuch a dataset can't be used for Analysis.")
                                        except MySQL_empty_dataset_load_Error as e:
                                            msgbox.showerror("Error",e.msg)
                                            cursor.close()
                                            con.close()
                                            return False
                                    else:
                                        raise Invalid_table_info_Error("Error loading the dataset!!\nThe table name entered doesn't exists in the list of tables of "+obj.dbname.get()+" database")
                                except Invalid_table_info_Error as e:
                                    msgbox.showerror("Error",e.msg)
                                    cursor.close()
                                    con.close()
                                    return False
                            else:
                                raise Cursor_creation_Error("Error creating the cursor for the database!!")
                        except Cursor_creation_Error as e:
                            msgbox.showerror("Error",e.msg)
                            con.close()
                            return False







