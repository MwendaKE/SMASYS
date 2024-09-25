from kivy.app import App
from kivy.uix.screenmanager import Screen
from modules.datamanager import Student, ManualDuty, Staff

from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu

from kivy.metrics import dp


from modules.msgmanager import show_error


class ViewStudentQueryNameDialogContent(MDBoxLayout):
    pass
    
    
class ViewStudentQueryDialogContent(MDBoxLayout):
    pass
    

class ViewStaffQueryDialogContent(MDBoxLayout):
    pass
    
    
class SearchQueryDialogContent(MDBoxLayout):
    pass
    

class HomeScreen(Screen):
    app = App.get_running_app()
    
    dialog = None
    dialog2 = None
    
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        
    def on_pre_enter(self, *args):
        try:
            self.app.update_homecount_statistics()
            self.app.update_home_bar_graph()
        
        except:
            pass
      
        return
        
    def get_school_gender_count_per_class(self):
        std = Student()
        
        f1b, f1g = std.get_form1_gender_count()
        f2b, f2g = std.get_form2_gender_count()
        f3b, f3g = std.get_form3_gender_count()
        f4b, f4g = std.get_form4_gender_count()
        
        boys_data = [f1b, f2b, f3b, f4b]
        girls_data = [f1g, f2g, f3g, f4g]
        
        return boys_data, girls_data
        
    def get_student_total_count(self):
        std = Student()
        
        boys, girls = std.get_student_total_count()
        
        return boys + girls
        
    def open_search_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Search Dialog",
                type = "custom",
                content_cls = SearchQueryDialogContent(),
                auto_dismiss = False,
                        
                buttons = [
                    MDFlatButton(
                        text = "CANCEL",
                        theme_text_color = "Custom",
                        pos_hint = {'center_x': .5, 'center_y': .5},
                        on_release = lambda _: self.close_dialog(),
                        ),
                    MDFlatButton(
                        text = "SEARCH",
                        theme_text_color = "Custom",
                        pos_hint = {'center_x': .5, 'center_y': .5},
                        on_release = lambda _: self.search_query(),
                        ),
                ],
            )
            
        self.dialog.open()
        
        return
        
    def search_query(self):
        search_type = self.dialog.content_cls.ids.query_type_spinner.text
        search_by = self.dialog.content_cls.ids.query_by_spinner.text
        search_query = self.dialog.content_cls.ids.search_query.text
        
        if search_type == "STUDENTS":
            if search_query.isspace() or search_query == "":
                return
        
            if search_by == "ID":
                adm_no = search_query
                
                #--
                std = Student()
                student = std.get_student_data(adm_no)
                    
                if student:
                    self.view_student(student)
                        
                else:
                    show_error("Query", f"The Student ID '{adm_no}' does not exist!")
   
            if search_by == "NAME":
                name = search_query
                results = []
                
                std = Student()
                students = std.get_students_data(name)
                
                if students:
                    for student in students:
                        adm_no = student["_id"]
                        name = student["full_name"]
                        form = student["form"]
                            
                        results.append((adm_no, name, form))
                            
                    self.view_students(results)
      
                else:
                    show_error("Query", f"The NAME '{name}' is not found!")
    
                return
        
        else:
            if search_query.isspace() or search_query == "":
                return
        
            if search_by == "ID":
                staffid = search_query
                
                stf = Staff()
                staff = stf.get_staff_data(staffid)
                
                if staff:
                    self.view_staff(staff)
                        
                else:
                    show_error("Query", f"The Staff ID '{staffid}' does not exist!")
     
        return
        
    def view_student(self, student):
        adm_no = student["_id"]
        sname = student["full_name"]
        gender = student["gender"]
        dob = student["dob"]
        doa = student["doa"]
        kcpe = student["kcpe"]
        form = student["form"]
        hostel = student["hostel"]
        performance = student["performance"]
        discipline = student["discipline"]
        subjects = student["subjects"]
        guardian = student["parent"]
        kcse = student["kcse"]
        
        role = student["role"] 
        
        transfered = student["transfered"]
        transfered_date = student["transfered_date"]
        graduated = student["graduated"]
        graduated_year = student["graduated_year"]
        
        if graduated == True:
            graduated = "GRADUATED"
            
        else:
            graduated = "NOT GRADUATED"
            
        if transfered == True:
            transfered = "TRANSFERED"
            
        else:
            transfered = "NOT TRANSFERED"
       
        mduty = self.process_stduty(adm_no, self.app.current_term, self.app.current_year)
        
        if not self.dialog2:
            self.dialog2 = MDDialog(
                title = "Student Search",
                type = "custom",
                content_cls = ViewStudentQueryDialogContent(),
                auto_dismiss = False,
                buttons = [
                    MDFlatButton(
                        text = "CLOSE",
                        theme_text_color ="Custom",
                        on_release = lambda _: self.close_dialog2(),
                        ),
                    ],
                )
                
        self.dialog2.content_cls.ids.adm_no.text = adm_no
        self.dialog2.content_cls.ids.fname.text = sname
        self.dialog2.content_cls.ids.gender.text = gender
        self.dialog2.content_cls.ids.dob.text = dob
        self.dialog2.content_cls.ids.doa.text = doa
        self.dialog2.content_cls.ids.kcpe.text = kcpe
        self.dialog2.content_cls.ids.form.text = form
        self.dialog2.content_cls.ids.hostel.text = hostel
        self.dialog2.content_cls.ids.performance.text = performance
        self.dialog2.content_cls.ids.discipline.text = discipline
        self.dialog2.content_cls.ids.subjects.text = subjects
        self.dialog2.content_cls.ids.guardian.text = guardian
        self.dialog2.content_cls.ids.kcse.text = kcse
        
        self.dialog2.content_cls.ids.role.text = role
        self.dialog2.content_cls.ids.mduty.text = mduty
        self.dialog2.content_cls.ids.trans.text = transfered
        self.dialog2.content_cls.ids.trans_date.text = transfered_date
        self.dialog2.content_cls.ids.grad.text = graduated
        self.dialog2.content_cls.ids.grad_year.text = graduated_year
           
        self.dialog2.open()
        
        return
        
    def view_staff(self, staff):
        id_ = staff["_id2"] if staff["_id2"] else staff["_id"]
        fname = staff["full_name"]
        gender = staff["gender"]
        ethnicity = staff["ethnicity"]
        loe = staff["loe"]
        role = staff["role"]
        class_ = staff["class"]
        phone = staff["phone"]
        sub_combination = staff["sub_combination"]
        doe = staff["doe"]
        transfered = staff["transfered"]
        transfered_date = staff["transfered_date"]
        
        if transfered == True:
            transfered = "TRANSFERED"
            
        else:
            transfered = "NOT TRANSFERED"
            
        if not self.dialog2:
            self.dialog2 = MDDialog(
                title = "Staff Search",
                type = "custom",
                content_cls = ViewStaffQueryDialogContent(),
                auto_dismiss = False,
                buttons = [
                    MDFlatButton(
                        text = "CLOSE",
                        theme_text_color ="Custom",
                        on_release = lambda _: self.close_dialog2(),
                        ),
                    ],
                )
            
        self.dialog2.content_cls.ids.staffid.text = id_
        self.dialog2.content_cls.ids.fname.text = fname
        self.dialog2.content_cls.ids.gender.text = gender
        self.dialog2.content_cls.ids.ethnicity.text = ethnicity
        self.dialog2.content_cls.ids.loe.text = loe
        self.dialog2.content_cls.ids.role.text = role
        self.dialog2.content_cls.ids.class_.text = class_
        self.dialog2.content_cls.ids.phone.text = phone
        self.dialog2.content_cls.ids.combination.text = sub_combination
        self.dialog2.content_cls.ids.doe.text = doe
        self.dialog2.content_cls.ids.trans.text = transfered
        self.dialog2.content_cls.ids.trans_date.text = transfered_date
        
        self.dialog2.open() 
         
        return
        
    def process_stduty(self, sid, term, year):
        ass_duty = "Not Assigned"
        
        md = ManualDuty()
        
        duties = md.get_manual_duties(term, year)
        
        if duties:
            for duty in duties:
                mduty = duty["manual_duty"]
                assigned = duty["assigned_students"]
            
                if sid in assigned:
                    return mduty
                 
                else:
                    continue
                    
        return ass_duty
            
    def view_students(self, data):
        if not self.dialog2:
            self.dialog2 = MDDialog(
                title = f"Student Search",
                type = "custom",
                content_cls = ViewStudentQueryNameDialogContent(),
                auto_dismiss = False,
                buttons = [
                    MDFlatButton(
                        text = "CLOSE",
                        theme_text_color ="Custom",
                        on_release = lambda _: self.close_dialog2(),
                        ),
                    ],
                )
                
        
        for row in data:
             adm_no, name, form = row
             self.dialog2.content_cls.ids.stds_container.add_widget(ThreeLineListItem(text=f"[color=008080]{name.upper()}[/color]", secondary_text=f"Adm No: {adm_no}", tertiary_text=f"Class: {form.capitalize()}"))
        
        self.dialog2.open()
        
        return
        
    def close_dialog(self):
        self.dialog.dismiss()
        self.dialog = None
        
        return
        
    def close_dialog2(self):
        self.dialog2.dismiss()
        self.dialog2 = None
        
        return
        
    #--------
     
    def open_top_menu(self):
        values = [{
                "viewclass": "OneLineListItem",
                "text": "SCH Settings",
                "height": dp(50),
                "on_release": lambda x="School": self.open_settings_screen(x),
                },
                {
                "viewclass": "OneLineListItem",
                "text": "STF View",
                "height": dp(50),
                "on_release": lambda x="STF": self.open_stf_screen(x),
                },
                {
                "viewclass": "OneLineListItem",
                "text": "About Smasys",
                "height": dp(50),
                "on_release": lambda x="Smasys": self.open_smasys_about(x),
                },
               ]
               
        self.dropdown = MDDropdownMenu(
            caller = self.app.root.ids.top_dots,
            items = values,
            position = "bottom",
            width_mult = 3,
            elevation = 1,
            radius = [0],
           )
           
        self.dropdown.open()
        
    def open_smasys_about(self, x):
        self.dropdown.dismiss()
        
        self.manager.current = "about"
    	
    def open_stf_screen(self, x):
    	self.dropdown.dismiss()
    	
    	self.manager.current = "stf"
    	
    def open_settings_screen(self, x):
    	self.dropdown.dismiss()
    	
    	self.manager.current = "settings"
   	
    def open_menu_x(self, value):
        self.dropdown.dismiss()
     
    # ------
    
    def open_students_screen(self):
        self.manager.current = "students"
        
    def open_subjects_screen(self):
        self.manager.current = "subjects"
        
    def open_exams_screen(self):
        self.manager.current = "exams"
        
    def open_grading_screen(self):
        self.manager.current = "grading"
        
    def open_payments_screen(self):
        self.manager.current = "payments"
   
    def open_home_screen(self):
        self.manager.current = "home"
        
    def open_staff_screen(self):
        self.manager.current = "staff"
        
    def open_search_screen(self):
        self.manager.current = "search"
        
    def open_calendar_screen(self):
        self.manager.current = "calenda"
        
    def open_routine_screen(self):
        self.manager.current = "routine"
        
    def open_duties_screen(self):
        self.manager.current = "duties"
        
    def open_library_screen(self):
        self.manager.current = "library"
      
        
        
        