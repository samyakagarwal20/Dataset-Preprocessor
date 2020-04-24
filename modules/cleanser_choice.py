try:
    import tkinter.messagebox as msgbox
except ImportError:
    print("Error loading messagebox module!!")
try:
    import pandas as pd
except ImportError as err:
    msgbox.showerror("Error",f"Error loading module : {err}"+"\nShuting Down the Program!!")
    inst.destroy()
try:
    import tkinter as tk
except ImportError:
    msgbox.showerror("Error","Error loading the tkinter package")
    

def check_cleansed(obj):
    if True in obj.df.isna().any().values:
        return False
    else:
        return True


class Empty_na_value_entry_Error(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Empty_entry_value_Error(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Empty_dataset_Error(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg
        

class Cleanser_automatic:
    def clean_operation_automatic(obj):
        if True in obj.df.isna().any().values:
            obj.df.interpolate(method="linear",limit_direction="forward",axis=0,inplace=True)
            print(obj.df)
            msgbox.showinfo("Success","Dataset Cleansed Successfully!!")
        else:
            msgbox.showinfo("","The loaded dataset is already cleansed!!\nYou can perform the analysis on it.")

class Cleanser_manual:

    def num_missing(x):
        return sum(x.isna())

    def _message_print(obj,index_list,values_list):
        print_data=list()
        for i,j in zip(index_list,values_list):
            print_data.append(i+"\t\t\t"+str(j))
        msgbox.showinfo("",("\n").join(print_data))

    def suppress(obj):
        try:
            if obj.fillna_value.get():
                obj.fill_na_value_window.withdraw()
                val=obj.fillna_value.get()
                if val:
                    if val.isdigit():
                        obj.df.fillna(int(val),inplace=True)
                        msgbox.showinfo("Success","Operation performed successfully!!")
                        print(obj.df)
                    else:
                        obj.df.fillna(val,inplace=True)
                        msgbox.showinfo("Success","Operation performed successfully!!")
                        print(obj.df)
            else:
                raise Empty_na_value_entry_Error("The textbox can't be left empty!!\nFill any data in it.")
        except Empty_na_value_entry_Error as e:
            print("inside except block")
            msgbox.showerror("Error",e.msg)

    def multiple_values(obj,col_names,entry_list):
        try:
            for c,v in zip(col_names,entry_list):
                if v.get()=="":
                    raise Empty_entry_value_Error(f"Fill out the entry for {c} column value of type {obj.df.dtypes[c]}!!")
                else:
                    obj.df.fillna(value={c:v},inplace=True)
        except Empty_entry_value_Error as e:
                msgbox.showerror("Error",e.msg)
        else:
            obj.fill_na_value_window.withdraw()
            print(obj.df)
            msgbox.showinfo("Success","Operation performed successfully!!")
    
    def manual_choice_option_1(obj):
        if True in obj.df.isna().any().values:
            msgbox.showinfo("","The loaded dataset needs to be cleansed!!")
            return False
        else:
            msgbox.showinfo("","The loaded dataset is already cleansed!!\nYou can perform the analysis on it.")
            return True
            
    def manual_choice_option_2(obj):
        try:
            index_list=obj.df.apply(Cleanser_manual.num_missing,axis=0).index.tolist()
            if index_list:
                index_list.pop(0)
                values_list=obj.df.apply(Cleanser_manual.num_missing,axis=0).values.tolist()
                Cleanser_manual._message_print(obj,index_list,values_list)
            else:
                raise Empty_dataset_Error("Operation Unsuccessfull!!\nThe dataset doesn't contain any column.")
        except Empty_dataset_Error as e:
            msgbox.showerror("Error",e.msg)
            
    def manual_choice_option_3(obj):
        print(obj.df.dropna(axis=0,inplace=True),"\n")
        msgbox.showinfo("Success","Operation performed successfully!!")
        print(obj.df)
        
    def manual_choice_option_4(obj):
        obj.df.dropna(axis=1,inplace=True)
        msgbox.showinfo("Success","Operation performed successfully!!")
        print(obj.df)
        
    def manual_choice_option_5(obj):
        print("inside function")
        obj.fill_na_value_window=tk.Toplevel(obj)
        obj.fillna_value=tk.StringVar()
        print("inserting widgets")
        tk.ttk.Label(obj.fill_na_value_window,text="Enter the value to be inserted").grid(row=1,column=0,padx=10,pady=10)
        tk.ttk.Entry(obj.fill_na_value_window,textvariable=obj.fillna_value,width=15).grid(row=1,column=1,padx=10,pady=10)
        tk.ttk.Button(obj.fill_na_value_window,text="Ok",command=lambda : Cleanser_manual.suppress(obj),width=10).grid(row=2,columnspan=2)
        
    def manual_choice_option_6(obj):
        ls=obj.df.columns[obj.df.isna().any()]
        entry_widgets=list()
        variables=list()
        obj.fill_na_value_window=tk.Toplevel(obj)
        r=1
        for x in ls:
            tk.ttk.Label(obj.fill_na_value_window,text=x).grid(row=r,column=0,padx=10,pady=8)
            entry=tk.ttk.Entry(obj.fill_na_value_window,width=15)
            entry.grid(row=r,column=1,padx=10,pady=8)
            entry_widgets.append(entry)
            r=r+1
        tk.ttk.Button(obj.fill_na_value_window,text="Ok",command=lambda : Cleanser_manual.multiple_values(obj,ls,entry_widgets),width=10).grid(row=r,columnspan=2,pady=10)
        
    def manual_choice_option_7(obj):
        if True in obj.df.isna().any().values:
            obj.df.interpolate(method="linear",limit_direction="forward",axis=0,inplace=True)
            msgbox.showinfo("Success","Operation performed successfully!!")
            print(obj.df)
        else:
            msgbox.showinfo("","The loaded dataset is already cleansed!!\nYou can perform the analysis on it.")

