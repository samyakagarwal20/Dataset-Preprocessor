try:
    import tkinter.messagebox as msgbox
except ImportError:
    print("Error loading messagebox module\n")


class Empty_manual_selection_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg
        
class Empty_cleaning_choice_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg


class Empty_cleansing_mode_selection_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg

class Already_cleansed_Error(Exception):
    """Raised when the sheet name for the excel workbook is not entered"""
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg


class Clean_choice:
    def cleaning_main_choice(obj):
        try:
            if obj.cleaning_mode.get()=="Automatic":
                obj.select_button_click_status=True
                obj.label_frame6.grid_remove()
            elif obj.cleaning_mode.get()=="Manual":
                obj.select_button_click_status=True
                obj.label_frame6.grid()
            else:
                raise Empty_cleaning_choice_Error("Select any one mode of cleaning to proceed...")
        except Empty_cleaning_choice_Error as e:
            msgbox.showerror("Error",e.msg)
        else:
            obj.cleanser_bt.grid()

    def manual_choice_select_button(obj):
        try:
            if obj.manual_clean_choice.get()==obj.manual_choice_list[0]:
                obj.manual_option=1
            elif obj.manual_clean_choice.get()==obj.manual_choice_list[1]:
                obj.manual_option=2
            elif obj.manual_clean_choice.get()==obj.manual_choice_list[2]:
                obj.manual_option=3
            elif obj.manual_clean_choice.get()==obj.manual_choice_list[3]:
                obj.manual_option=4
            elif obj.manual_clean_choice.get()==obj.manual_choice_list[4]:
                obj.manual_option=5
            elif obj.manual_clean_choice.get()==obj.manual_choice_list[5]:
                obj.manual_option=6
            elif obj.manual_clean_choice.get()==obj.manual_choice_list[6]:
                obj.manual_option=7
            else:
                print("inside else condition\n")
                raise Empty_manual_selection_Error("Select any one of the available option and then press the Choose button.")
        except Empty_manual_selection_Error as e:
            msgbox.showerror("Error",e.msg)
    
    def cleanser_button_click(obj):
        try:
            if obj.select_button_click_status==True and obj.cleaning_mode.get()=="Automatic":
                try:
                    from modules.cleanser_choice import Cleanser_automatic as cla
                except ImportError:
                    msgbox.showerror("Error","Error loading cleanser_manual_choice from modules!!")
                else:
                    cla.clean_operation_automatic(obj)
            elif obj.select_button_click_status==True and obj.cleaning_mode.get()=="Manual":
                try:
                    from modules.cleanser_choice import Cleanser_manual as clm
                except ImportError:
                    msgbox.showerror("Error","Error loading cleanser_manual_choice from modules!!")
                else:
                    try:
                        from modules.cleanser_choice import check_cleansed
                    except ImportError:
                        msgbox.showerror("Error","Error importing the check_cleansed() from cleanser_choice module.")
                    else:
                        try:
                            obj.cleaned_status=check_cleansed(obj)
                            if obj.cleaned_status:
                                if obj.manual_option==1:
                                    obj.cleaned_status=clm.manual_choice_option_1(obj)
                                elif obj.manual_option==2:
                                    clm.manual_choice_option_2(obj)
                                elif obj.manual_option=="":
                                    raise Empty_manual_selection_Error("Select any one of the available option and then press the Choose button.")
                                else:
                                    raise Already_cleansed_Error("Cannot perform any such operation!!\nThe dataset is already cleansed.")
                            else:
                                if obj.manual_option==1:
                                    obj.cleaned_status=clm.manual_choice_option_1(obj)
                                elif obj.manual_option==2:
                                    clm.manual_choice_option_2(obj)
                                elif obj.manual_option==3:
                                    clm.manual_choice_option_3(obj)
                                elif obj.manual_option==4:
                                    clm.manual_choice_option_4(obj)
                                elif obj.manual_option==5:
                                    clm.manual_choice_option_5(obj)
                                elif obj.manual_option==6:
                                    clm.manual_choice_option_6(obj)
                                elif obj.manual_option==7:
                                    clm.manual_choice_option_7(obj)
                                else:
                                    raise Empty_manual_selection_Error("Select any one of the available option and then press the Choose button.")
                        except Empty_manual_selection_Error as e:
                            msgbox.showerror("Error",e.msg)
                        except Already_cleansed_Error as e:
                            msgbox.showerror("Error",e.msg)
            else:
                raise Empty_cleansing_mode_selection_Error("Select any one of the available option and then press the Choose button.")
        except Empty_cleansing_mode_selection_Error as e:
            msgbox.showerror("Error",e.msg)
