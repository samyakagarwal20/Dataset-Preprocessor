from threading import Thread
from modules.click_events import Event_handler as ceh
from modules.loader import load as ld
from modules.cleanser_main import Clean_choice as cl

class Thread_handler:
    def browse_csv_thread(obj):
        browse_csv_thread=Thread(target=lambda : ld.browse_csv(obj))
        browse_csv_thread.start()

    def browse_xlsx_thread(obj):
        browse_xlsx_thread=Thread(target=lambda : ld.browse_xlsx(obj))
        browse_xlsx_thread.start()

    def cleaning_main_choice_thread(obj):
        cleaning_main_choice_thread=Thread(target=lambda : cl.cleaning_main_choice(obj))
        cleaning_main_choice_thread.start()

    def manual_choice_select_button_thread(obj):
        manual_choice_select_button_thread=Thread(target=lambda : cl.manual_choice_select_button(obj))
        manual_choice_select_button_thread.start()

    def cleanser_button_click_thread(obj):
        cleanser_button_click_thread=Thread(target=lambda : cl.cleanser_button_click(obj))
        cleanser_button_click_thread.start()

    def view_label_frame2_thread(obj):
        view_label_frame2_thread=Thread(target=lambda : ceh.view_label_frame2(obj))
        view_label_frame2_thread.start()

    def view_label_frame3_thread(obj):
        view_label_frame3_thread=Thread(target=lambda : ceh.view_label_frame3(obj))
        view_label_frame3_thread.start()

    def view_label_frame4_thread(obj):
        view_label_frame4_thread=Thread(target=lambda : ceh.view_label_frame4(obj))
        view_label_frame4_thread.start()

    def load_data_thread(obj):
        load_data_thread=Thread(target=lambda : ceh.load_data(obj))
        load_data_thread.start()

    def view_data_thread(obj):
        view_data_thread=Thread(target=lambda : ceh.view_data(obj))
        view_data_thread.start()

    def export_data_thread(obj):
        export_data_thread=Thread(target=lambda : ceh.export_data(obj))
        export_data_thread.start()

    def query_thread(obj):
        query_thread=Thread(target=lambda : ceh.query(obj))
        query_thread.start()

    def support_thread():
        support_thread=Thread(target=ceh.support)
        support_thread.start()

    def developer_thread(obj):
        developer_thread=Thread(target=lambda : ceh.developer(obj))
        developer_thread.start()

    def application_thread(obj):
        application_thread=Thread(target=lambda : ceh.application(obj))
        application_thread.start()

