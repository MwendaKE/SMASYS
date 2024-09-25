from kivy.app import App

from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineIconListItem
from modules.datamanager import Student
from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from modules.msgmanager import show_error, show_toast
from modules.datamanager import Student, Exam, Grading

import re
from operator import itemgetter


class ExamAddDialogContent(MDBoxLayout):
    pass
    
    
class OneLineStudentListItem(OneLineIconListItem):
    dialog = None
    
    def __init__(self, *args, **kwargs):
        super(OneLineStudentListItem, self).__init__(**kwargs)
        self.args = args
        
        self.adm_no = self.args[0][0]
        
        self.year = self.args[0][1]
        self.term = self.args[0][2]
        self.exam = self.args[0][3]
        self.form = self.args[0][4]
        
        self.out_of = ""
        
    def on_release(self):
        std = Student()
        sname = std.get_student_name(self.adm_no)
        
        if not self.dialog:
            self.dialog = MDDialog(
                title = f"{sname} | {self.adm_no}",
                type = "custom",
                content_cls = ExamAddDialogContent(),
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
                        on_release = lambda _: self.add_exam(),
                        ),
                    ],
                )
                
            
        self.dialog.open()
        
    def add_exam(self):
        eng = self.dialog.content_cls.ids.eng.text
        kis = self.dialog.content_cls.ids.kis.text
        mat = self.dialog.content_cls.ids.mat.text
        
        bio = self.dialog.content_cls.ids.bio.text
        phy = self.dialog.content_cls.ids.phy.text
        che = self.dialog.content_cls.ids.che.text
        
        his = self.dialog.content_cls.ids.his.text
        geo = self.dialog.content_cls.ids.geo.text
        cre = self.dialog.content_cls.ids.cre.text
        
        agr = self.dialog.content_cls.ids.agr.text
        com = self.dialog.content_cls.ids.com.text
        bus = self.dialog.content_cls.ids.bus.text
        
        if (eng == "" or eng.isspace() or
           kis == "" or kis.isspace() or
           mat == "" or mat.isspace()
        ):
            show_error("Add Marks", "Fields marked with * are required.")
        
        else:
            self.dialog.dismiss()
            
            marks = {"ENG": eng, 
                     "KIS": kis, 
                     "MAT": mat,
                     "BIO": bio,
                     "PHY": phy,
                     "CHE": che,
                     "HIS": his,
                     "GEO": geo,
                     "CRE": cre,
                     "AGR": agr,
                     "COM": com,
                     "BUS": bus
            }
            
            exm = Exam()
            
            if exm.exam_exists(self.adm_no, self.year, self.term, self.exam, self.form):
                show_error("Add Marks", f"Duplicate Exam: Exam already added for ADM. {self.adm_no}.")
                
            else:
                exm.add_exam(self.adm_no, self.year, self.term, self.exam, self.form, marks)
                show_toast(f"Added marks for ADM No. {self.adm_no}")
                
        return
        
    def wash_value(self, value):
        if re.match("^[\d]+$", value):
            clean_value = int(value)
            
        else:
            clean_value = -1
        
        return clean_value
        
        
class StudentAddExamListScreen(Screen):
    year = ""
    term = ""
    exam = ""
    form = ""
    
    def __init__(self, **kwargs):
        super(StudentAddExamListScreen, self).__init__(**kwargs)
     
    def update_exam_list(self, year, term, exam, form):
        self.year = year
        self.term = term
        self.exam = exam
        self.form = form
        
        self.ids.std_examadd_list_container.clear_widgets()
        
        student_list = []
        
        std = Student()
        students_list_obj = std.get_students(self.form)
        
        for student in students_list_obj:
            adm_no = student["_id"]
            sname = student["full_name"]
            
            student_list.append((adm_no, sname))
        
        student_list = sorted(student_list, key=itemgetter(0))
        
        self.ids.exam_type_title.text = f"Exam Add List • {form.capitalize()} • {term.capitalize()} • {exam.capitalize()}"
            
        for adm_no, sname in student_list:
            self.ids.std_examadd_list_container.add_widget(OneLineStudentListItem([adm_no, self.year, self.term, self.exam, self.form], text=f"{adm_no}     {sname}"))
        
        return
        
    