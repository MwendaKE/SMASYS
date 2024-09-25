from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from kivy.metrics import dp

from modules.datamanager import Student, Hostel
from modules.msgmanager import show_error, show_toast
from modules import listsmanager


class SubjectEditDialogContent(MDGridLayout):
    pass
    
    
class HostelAddEditDialogContent(MDBoxLayout):
    pass
    
    
class EditStudentScreen(Screen):
    adm_no = ObjectProperty()
    full_name = ObjectProperty()
    gender = ObjectProperty()
    date_of_birth = ObjectProperty()
    date_of_admission = ObjectProperty()
    kcpe = ObjectProperty()
    form = ObjectProperty()
    hostel = ObjectProperty()
    performance = ObjectProperty()
    discipline = ObjectProperty()
    subjects = ObjectProperty()
    guardian = ObjectProperty()
    kcse = ObjectProperty()
    role = ObjectProperty()
    graduated = ObjectProperty()
    graduated_year = ObjectProperty()
    transfered = ObjectProperty()
    transfered_date = ObjectProperty()
    
    dialog = None
    subjects_selected = []
    
    def __init__(self, **kwargs):
        super(EditStudentScreen, self).__init__(**kwargs)
    
    # REFACTORED CODE
    
    def get_student_role_values(self): 
        return listsmanager.student_roles
        
    def get_student_hostels(self):
        values = []
        
        hs = Hostel()
        hostels = hs.get_hostels()
        
        for hostel in hostels:
            hostel_name = hostel["hostel_name"]
            values.append(hostel_name)
                
        return values
        
    ### HOSTEL MENU ###
    
    def open_hostel_menu(self):
        hostels = self.get_student_hostels()
        menu_items = []
        
        for hostel in hostels:
            item = {"viewclass": "OneLineListItem",
                       "text": hostel,
                       "height": dp(50),
                       "on_release": lambda x=hostel: self.set_hostel_text(x),
                      }
            menu_items.append(item)
             
        self.hostel_menu = MDDropdownMenu(
            caller=self.ids.hostel,
            items=menu_items,
            width_mult=4,
            position="bottom",
        )
        self.hostel_menu.open()
            
    def set_hostel_text(self, text):
        self.ids.hostel.text = text
        self.hostel_menu.dismiss()
        
    ##### STUDENT ROLE MENU ######
    
    def open_student_role_menu(self):
        roles = self.get_student_role_values()
        menu_items = []
        
        for role in roles:
            item = {"viewclass": "OneLineListItem",
                       "text": role,
                       "height": dp(50),
                       "on_release": lambda x=role: self.set_role_text(x),
                      }
            menu_items.append(item)
             
        self.role_menu = MDDropdownMenu(
            caller=self.ids.role,
            items=menu_items,
            width_mult=4,
            position="bottom",
        )
        self.role_menu.open()
            
    def set_role_text(self, text):
        self.ids.role.text = text
        self.role_menu.dismiss()
        
    ##### CLASS MENU ######
    
    def open_class_menu(self):
        classes = self.get_classes()
        menu_items = []
        
        for class_ in classes:
            item = {"viewclass": "OneLineListItem",
                       "text": class_,
                       "height": dp(50),
                       "on_release": lambda x=class_: self.set_class_text(x),
                      }
            menu_items.append(item)
             
        self.class_menu = MDDropdownMenu(
            caller=self.ids.form,
            items=menu_items,
            width_mult=4,
            position="bottom",
        )
        self.class_menu.open()
            
    def set_class_text(self, text):
        self.ids.form.text = text
        self.class_menu.dismiss()
        
    ##### GENDER MENU ######
    
    def open_gender_menu(self):
        genders = ["MALE","FEMALE"]
        menu_items = []
        
        for gender in genders:
            item = {"viewclass": "OneLineListItem",
                       "text": gender,
                       "height": dp(50),
                       "on_release": lambda x=gender: self.set_gender_text(x),
                      }
            menu_items.append(item)
             
        self.gender_menu = MDDropdownMenu(
            caller=self.ids.gender,
            items=menu_items,
            width_mult=4,
            position="bottom",
        )
        self.gender_menu.open()
            
    def set_gender_text(self, text):
        self.ids.gender.text = text
        self.gender_menu.dismiss()
        
    ##### GRAD MENU ######
    
    def open_grad_menu(self):
        grads = ["GRADUATED","NOT GRADUATED"]
        menu_items = []
        
        for grad in grads:
            item = {"viewclass": "OneLineListItem",
                       "text": grad,
                       "height": dp(50),
                       "on_release": lambda x=grad: self.set_grad_text(x),
                      }
            menu_items.append(item)
             
        self.grad_menu = MDDropdownMenu(
            caller=self.ids.grad,
            items=menu_items,
            width_mult=4,
            position="bottom",
        )
        self.grad_menu.open()
            
    def set_grad_text(self, text):
        self.ids.grad.text = text
        self.grad_menu.dismiss()
        
    ##### TRANS MENU ######
    
    def open_trans_menu(self):
        trans = ["TRANSFERED","NOT TRANSFERED"]
        menu_items = []
        
        for tran in trans:
            item = {"viewclass": "OneLineListItem",
                       "text": tran,
                       "height": dp(50),
                       "on_release": lambda x=tran: self.set_trans_text(x),
                      }
            menu_items.append(item)
             
        self.trans_menu = MDDropdownMenu(
            caller=self.ids.trans,
            items=menu_items,
            width_mult=4,
            position="bottom",
        )
        self.trans_menu.open()
            
    def set_trans_text(self, text):
        self.ids.trans.text = text
        self.trans_menu.dismiss()

    ###########
        
    def get_classes(self):
          return listsmanager.school_classes
       
    def add_hostels(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Add Hostel",
                type = "custom",
                content_cls = HostelAddEditDialogContent(),
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
                        on_release = lambda _: self.add_hostel(),
                        ),
                ],
            )
            
        self.dialog.open()
    
    def add_hostel(self):
        hname = self.dialog.content_cls.ids.hostelname.text
        
        if hname == "" or hname.isspace():
            show_error("Add Hostel", "Hostel name is required!")
            return
            
        if len(hname) > 20:
            show_error("Add Hostel", "Please enter less than 20 characters!")
            return
            
        if hname.lower() in [x.lower() for x in self.get_student_hostels()]: 
            show_error("Add Hostel", "Hostel exists.")
            self.dialog.dismiss()
            
            return 
        
        self.dialog.content_cls.ids.hostelname.text = ""
        
        self.dialog.dismiss()
        
        hs = Hostel()
        hs.add_hostel(hname.title())
        
        values = self.get_student_hostels()
        self.ids.hostel.values = values
        
        self.ids.hostel.text = hname
        
        show_toast(f"Added hostel '{hname}'")
         
        return
    # ------
    
    def on_dob_date(self, instance, value, date_range):
        self.date_of_birth.text = str(value)
        
    def open_dob_date_picker(self):
        date = MDDatePicker()
        date.bind(on_save=self.on_dob_date)
        date.open()
        
    def on_doa_date(self, instance, value, date_range):
        self.date_of_admission.text = str(value)
        
    def open_doa_date_picker(self):
        date = MDDatePicker()
        date.bind(on_save=self.on_doa_date)
        date.open()
    
    # TRANSFERED DATES #
 
    def open_trans_date_picker(self):
        date = MDDatePicker()
        date.bind(on_save=self.on_trans_date)
        date.open()
        
    def on_trans_date(self, instance, value, date_range):
        self.transfered_date.text = str(value)
  
    # SUBJECTS #
        
    def open_subjects_picker(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Subject Selection",
                type = "custom",
                content_cls = SubjectEditDialogContent(),
                auto_dismiss = False,
                buttons = [
                    MDFlatButton(
                        text = "CANCEL",
                        theme_text_color ="Custom",
                        on_release = lambda _: self.dialog.dismiss(),
                        ),
                    
                    MDFlatButton(
                        text = "OK",
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
        self.ids.subjects.text = str(",".join(self.subjects_selected))
        
        self.dialog.dismiss()
        
        return
        
    def save_student(self):
        if  (self.adm_no.text == "" or self.adm_no.text.isspace() or
             self.full_name.text == "" or self.full_name.text.isspace() or
             self.gender.text == "Select Gender" or 
             self.form.text == "Select Class"
             ):
                 
            show_error("Edit Student", "Please fill all the required (*) fields!")
            
        else:
            subjects = self.subjects.text.split(",")
            
            if self.hostel.text == "Select Hostel":
                self.hostel.text = ""
                
            if not self.adm_no.text.isdigit():
                show_error("Edit Student", "Adm Number must be an integer!")
                
                return
                
            if self.graduated.text == "GRADUATED":
                graduated = True
                
            else:
                graduated = False
                
            if self.transfered.text == "TRANSFERED":
                transfered = True
                
            else:
                transfered = False
                
            try:
                std = Student()
                std.update_student(self.adm_no.text, 
                                self.full_name.text.title(), 
                                self.gender.text, 
                                self.date_of_birth.text, 
                                self.date_of_admission.text, 
                                self.kcpe.text, 
                                self.form.text, 
                                self.hostel.text, 
                                self.performance.text, 
                                self.discipline.text, 
                                self.subjects.text, 
                                self.guardian.text, 
                                self.kcse.text,
                                self.role.text,
                                graduated,
                                self.graduated_year.text,
                                transfered,
                                self.transfered_date.text)
                                
                show_toast(f"Edited {self.full_name.text} ADM No. {self.adm_no.text}")
            
            except Exception as e:
                show_error("Edit Student", str(e))
                
            self.manager.current = "students"
        
        return
        
    def set_current_student(self):
        pass
        