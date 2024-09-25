from kivy.app import App

from kivy.properties import ObjectProperty
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import ThreeLineListItem

from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, OneLineListItem

from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivy.config import Config
from kivymd.uix.pickers import MDColorPicker

from modules.datamanager import Setting
from modules.msgmanager import show_toast, show_error

from operator import itemgetter
from datetime import datetime
import re, os, shutil


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        sto = Setting()
        settings = sto.get_settings()
        
        self.ids.scode.text = settings["school_code"]
            
        self.ids.sname.text = settings["school_name"]
        self.ids.sname.text_color_normal = settings["school_name_color"] if settings["school_name_color"] else "FFA500"
        self.ids.sname_color.text = settings["school_name_color"]
        self.ids.sname_color.text_color_normal = settings["school_name_color"] if settings["school_name_color"] else "FFA500"
        
        self.ids.scaption.text = settings["school_caption"]
        self.ids.scaption.text_color_normal = settings["school_caption_color"] if settings["school_caption_color"] else "FFA500"
        self.ids.scaption_color.text = settings["school_caption_color"]
        self.ids.scaption_color.text_color_normal = settings["school_caption_color"] if settings["school_caption_color"] else "FFA500"
        
        self.ids.saddress.text = settings["school_address"]
        self.ids.sphone.text = settings["school_phone_number"]
        self.ids.smotto.text = settings["school_motto"]
        self.ids.smission.text = settings["school_mission"]
        self.ids.svision.text = settings["school_vision"]
        
        if self.ids.scode.text:
            self.ids.scode.disabled = True
            
        else:
            self.ids.scode.disabled = False
            
    def update_settings(self):
        current_code = App.get_running_app().school_code
        current_db = App.get_running_app().database_name
        
        show_error("SCHOOL CODE/DB",f"CODE: {current_code}, DB: {current_db}")
        
        scode = self.ids.scode.text
        
        sname = self.ids.sname.text
        sname_color = self.ids.sname_color.text
        
        scaption = self.ids.scaption.text
        scaption_color = self.ids.scaption_color.text 
        
        saddress = self.ids.saddress.text
        sphone = self.ids.sphone.text
        smotto = self.ids.smotto.text
        smission = self.ids.smission.text
        svision = self.ids.svision.text
        
        if scode == "" or scode.isspace():
            show_error("Settings", "School code is required!")
            return
            
        else:
            if len(scode) < 6:
                show_error("Settings", "School code must be a set of digits not less than 6!")
                return
                
            if not scode.isdigit():
                show_error("Settings", "School code must be a set of digits!")
                return
                
        if (sname == "" or sname.isspace() or 
            saddress == "" or saddress.isspace()):
                
            show_error("Settings", "School name and address are required!")
            return
          
        sdb_name = f"SMASYSX{scode}XDB"
        
        if current_code == "00000" or current_db == "XXXXXSAMSYSXDB":
            sdb_name = f"SMASYSX{scode}XDB"
        
            sto = Setting()
            sto.update_primary_settings(scode, sdb_name, sname, sname_color, scaption, scaption_color, saddress, sphone, smotto, smission, svision)
        
            App.get_running_app().config.set("SCHOOL", "code", scode)
            App.get_running_app().config.set("SCHOOL", "database", sdb_name)
            
            App.get_running_app().enable_database_and_home_activities()
          
            show_toast("Initial school settings set successfully.")
            
        else:
            sto = Setting()
            sto.update_secondary_settings(sname, sname_color, scaption, scaption_color, saddress, sphone, smotto, smission, svision)
        
            show_toast("Updated school settings successfully.")
           
        self.manager.current = "home"
        
    # SCHOOL NAME COLOR PICKER
    
    def open_color_picker_sname(self):
        self.color_picker = MDColorPicker(size_hint=(.8, .8))
        self.color_picker.bind(on_release=self.get_selected_color_sname)
        self.color_picker.open()
        
    def get_selected_color_sname(self, instance, type_color, selected_color):
        color_rgba, color_hex = self.convert_to_true_rgba(selected_color)
       
        self.ids.sname_color.text = str(color_hex)
        self.ids.sname_color.text_color_normal = color_hex
        self.ids.sname.text_color_normal = color_hex
        
        self.color_picker.dismiss()
   
        return
        
    # SCHOOL CAPTION COLOR PICKER
    
    def open_color_picker_scaption(self):
        self.color_picker = MDColorPicker(size_hint=(.8, .8))
        self.color_picker.bind(on_release=self.get_selected_color_scaption)
        self.color_picker.open()
        
    def get_selected_color_scaption(self, instance, type_color, selected_color):
        color_rgba, color_hex = self.convert_to_true_rgba(selected_color)
        
        if color_rgba == None or color_hex == None:
            show_error("Color", "Unknown color selected. Please select absolute color")
            
            return
              
        self.ids.scaption_color.text = str(color_hex)
        self.ids.scaption_color.text_color_normal = color_hex
        self.ids.scaption.text_color_normal = color_hex
        
        self.color_picker.dismiss()
   
        return
        
    def convert_to_true_rgba(self, clist):
        if len(clist) == 4:
            r,g,b,a = clist
            
        else:
            show_error("Color", "Please select absolute color")
            
            return None, None
        
        new_color_rgba = (int(r*255), int(g*255), int(b*255), round(a*1, 2))
        new_color_hexa = '#{:02x}{:02x}{:02x}'.format(new_color_rgba[0], new_color_rgba[1], new_color_rgba[2])
        
        return new_color_rgba, new_color_hexa 
        
        