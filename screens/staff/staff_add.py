from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from kivy.metrics import dp

from modules.datamanager import Staff
from modules.msgmanager import show_error, show_toast
from modules import listsmanager

class SubjectCombinationDialogContent(MDGridLayout):
    pass
 
   
class AddStaffScreen(Screen):
    id_no = ObjectProperty()
    full_name = ObjectProperty()
    gender = ObjectProperty()
    ethnicity = ObjectProperty()
    loe = ObjectProperty()
    role = ObjectProperty()
    class_ = ObjectProperty()
    phone = ObjectProperty()
    combination = ObjectProperty()
    doe = ObjectProperty()
    
    dialog = None
    subjects_selected = []
    
    def __init__(self, **kwargs):
        super(AddStaffScreen, self).__init__(**kwargs)
   
   # DATE OF EMPLOYMENT
   
    def on_doe_date(self, instance, value, date_range):
        self.doe.text = str(value)
        
    def open_doe_date_picker(self):
        date = MDDatePicker()
        date.bind(on_save=self.on_doe_date)
        date.open()
        
    # ETHNICITY
      
    def open_ethnicity_menu(self):
        ethnic_list = open("./assets/files/kenyantribes.txt").readlines()
        values = sorted([value.strip().upper() for value in ethnic_list])
        
        items = []
        
        for value in values:
            item = {
                "viewclass": "OneLineIconListItem",
                "text": value,
                "height": dp(50),
                "on_release": lambda x=value: self.set_ethnic_value(x),  
            }
            
            items.append(item)
            
        self.dropdown = MDDropdownMenu(
            caller = self.ids.ethnicity,
            items = items,
            )
           
        self.dropdown.open()
        
    def set_ethnic_value(self, value):
        self.ethnicity.text = value
        self.dropdown.dismiss()
    
    # LOE
       
    def open_loe_menu(self):
        loes = listsmanager.staff_loes
        items = []
        
        for value in loes:
            item = {
                "viewclass": "OneLineIconListItem",
                "text": value,
                "height": dp(50),
                "on_release": lambda x=value: self.set_loe_value(x),  
            }
            
            items.append(item)
            
        self.dropdown = MDDropdownMenu(
            caller = self.ids.loe,
            items = items,
            )
           
        self.dropdown.open()
        
    def set_loe_value(self, value):
        self.loe.text = value
        self.dropdown.dismiss()
        
    # CLASS
    
    def open_class_menu(self):
        classes = listsmanager.staff_classes
        
        items = []
         
        for value in classes:
            item = {
                "viewclass": "OneLineIconListItem",
                "text": value,
                "height": dp(50),
                "on_release": lambda x=value: self.set_class_value(x),  
             }
            
            items.append(item)
        
        self.dropdown = MDDropdownMenu(
            caller = self.ids.class_,
            items = items,
            )
           
        self.dropdown.open()
        
    def set_class_value(self, value):
        self.class_.text = value
        self.dropdown.dismiss()
        
        
    # ROLE
    
    def open_role_menu(self):
        roles = listsmanager.staff_roles
        
        items = []
         
        for value in roles:
            item = {
                "viewclass": "OneLineIconListItem",
                "text": value,
                "height": dp(50),
                "on_release": lambda x=value: self.set_role_value(x),  
             }
            
            items.append(item)
        
        self.dropdown = MDDropdownMenu(
            caller = self.ids.role,
            items = items,
            )
           
        self.dropdown.open()
        
    def set_role_value(self, value):
        self.role.text = value
        self.dropdown.dismiss()
        
        
    # SUBJECT COMBINATION
    
    def open_subject_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Subject Combination",
                type = "custom",
                content_cls = SubjectCombinationDialogContent(),
                auto_dismiss = False,
                buttons = [
                    MDFlatButton(
                        text = "CANCEL",
                        theme_text_color ="Custom",
                        on_release = lambda _: self.dialog.dismiss(),
                        ),
                    
                    MDFlatButton(
                        text = "ADD",
                        theme_text_color = "Custom",
                        on_release = self.set_selected_subjects,
                        ),
                ],
            )
        self.dialog.open()
        
    def subject_checkbox_clicked(self, instance, active, subject):
        if active == True:
            self.subjects_selected.append(subject)
            
        else:
            self.subjects_selected.remove(subject)
            
    def set_selected_subjects(self, obj):
        self.ids.combination.text = str(",".join(self.subjects_selected))
        
        self.dialog.dismiss()
        
        return
        
    # GENDER
    
    def open_gender_menu(self):
        values = [{
                "viewclass": "OneLineIconListItem",
                "text": "MALE",
                "height": dp(50),
                "on_release": lambda x="MALE": self.set_gender_value(x),
                },
                {
                "viewclass": "OneLineIconListItem",
                "text": "FEMALE",
                "height": dp(50),
                "on_release": lambda x="FEMALE": self.set_gender_value(x),
                },
               ]
               
        self.dropdown = MDDropdownMenu(
            caller = self.ids.gender,
            items = values,
            )
           
        self.dropdown.open()
        
    def set_gender_value(self, value):
        self.gender.text = value
        self.dropdown.dismiss()
     
    # ADD STAFF
     
    def add_staff(self):
        if  (self.id_no.text == "" or self.id_no.text.isspace() or
             self.full_name.text == "" or self.full_name.text.isspace() or
             self.gender.text == "" or self.gender.text.isspace() or
             self.class_.text == "" or self.class_.text.isspace()
             ):
                 
            show_error("Add Staff", "Fields marked with '*' are required!")
            
        else:
            if not self.id_no.text.isdigit():
                show_error("Add Staff", "ID Number must be an integer!")
                
                return
              
            try:
                stf = Staff()
                stf.add_staff(self.id_no.text, 
                                self.full_name.text.title(), 
                                self.gender.text,
                                self.ethnicity.text, 
                                self.loe.text, 
                                self.role.text,
                                self.class_.text, 
                                self.phone.text, 
                                self.combination.text, 
                                self.doe.text, 
                                )
                                
                show_toast(f"Added {self.full_name.text} ID No. {self.id_no.text}")
            
            except Exception as e:
                show_error("Add Staff", str(e))
                
                
            self.id_no.text = "" 
            self.full_name.text = "" 
            self.gender.text = ""
            self.ethnicity.text = ""
            self.loe.text = ""
            self.class_.text = ""
            self.phone.text = ""
            self.combination.text = "" 
            self.doe.text = ""
            
        return