from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder

from matplotlib import pyplot as plt
from kivy.uix.image import CoreImage
from kivy.core.window import Window

from modules.datamanager import Setting
from modules.datamanager import Student
from modules.datamanager import Staff
from modules.msgmanager import show_error


import io
import re
import numpy as np


# Make the keyboard to be below the text input field
Window.softinput_mode = "below_target"


class SMaSysApp(MDApp): 
    school_code = ""
    database_name = ""
    current_term = "TERM 1"
    current_year = "2024"
    download_path = "/sdcard/Download/SMASYS" # For mobile devices
    
    def build_config(self, config):
        config.setdefaults("SCHOOL", {
            "code": "00000",
            "database": "XXXXXSAMSYSXDB"
        })
        
    def build(self):
        config = self.config
        self.school_code = config.get('SCHOOL', 'code')
        self.database_name = config.get('SCHOOL', 'database')
        
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = 'M3'
        
        manager = Builder.load_file('main.kv')
       
        return manager
    
    def on_start(self, *args):
        app = App.get_running_app()
            
        if not os.path.exists(self.download_path):
            os.mkdir(self.download_path)
            
        if self.school_code == "00000" or self.database_name == "XXXXXSAMSYSXDB":
            self.disable_home_activities()
            app.root.ids.manager.current = "settings"
            return
            
        else:
            self.update_homecount_statistics()
            self.update_home_bar_graph()
            app.root.ids.manager.current = "home"
            
            return
        
    def get_school_database(self):
        settobj = Setting()
        settings = settobj.get_settings()
        sch_code = settings["school_code"]
        sch_dbname = settings["school_dbname"]
        
        if sch_code == "" or sch_dbname == "":
            return False
            
        else:
            return sch_dbname
            
    def disable_home_activities(self):
        app = App.get_running_app()
        
        app.root.ids.bottom_nav.disabled = True
        app.root.ids.search_btn.disabled = True
        app.root.ids.top_dots.disabled = True
        
        return
        
    def enable_database_and_home_activities(self):
        app = App.get_running_app()
        
        app.root.ids.bottom_nav.disabled = False
        app.root.ids.search_btn.disabled = False
        app.root.ids.top_dots.disabled = False
        
        return
      
    def update_homecount_statistics(self):
        """ Update the home screen with student, teachers, and school administrators numbers"""
        
        app = App.get_running_app()
        
        student_count = self.get_student_total_count()
        teacher_count = self.get_teachers_count()
        admin_count = self.get_admins_count()
        
        app.root.ids.home.ids.student_count.text = str(student_count)
        app.root.ids.home.ids.teacher_count.text = str(teacher_count)
        app.root.ids.home.ids.admin_count.text = str(admin_count)
        
        return
        
    def update_home_bar_graph(self):
        """ Update the home screen graph """
        
        # CODE HIDDEN
        
    def get_student_total_count(self):
        std = Student()
        
        boys, girls = std.get_student_total_count()
        
        return boys + girls
        
    def get_teachers_count(self):
        stf = Staff()
        
        return stf.get_teachers_count()
        
    def get_admins_count(self):
        stf = Staff()
        
        return stf.get_admins_count()
        
    def get_school_gender_count_per_class(self):
        std = Student()
        
       # CODE HIDDEN
        
        return boys_data, girls_data
        
    def open_search_screen(self):
        app = App.get_running_app()
        
        app.root.ids.home.open_search_screen()
        
        return

if __name__ == '__main__':
    app = SMaSysApp()
    app.run()
