from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from modules.datamanager import Student, Exam, Grading, Comment
from modules.msgmanager import show_error, show_toast

import re


class GeneralGradingLayout(MDBoxLayout):
    pass
    

class MathsAndScienceGradingBoxLayout(MDBoxLayout):
    pass
    
   
class LanguagesGradingLayout(MDBoxLayout):
    pass
    
    
class HumanitiesGradingLayout(MDBoxLayout):
    pass
    

class CommentsGradingLayout(MDBoxLayout):
    pass
    
    
class GradingScreen(Screen):
    grading_spinner = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(GradingScreen, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        self.update_grading_screen()
        return
        
    def update_grading_screen(self):
        grading = Grading()
        
        grd_data = grading.get_grading_data()
        science = [dict["SCIENCE"] for dict in grd_data if "SCIENCE" in dict][0]
        
        grd_data = grading.get_grading_data()
        languages = [dict["LANGUAGES"] for dict in grd_data if "LANGUAGES" in dict][0]
        
        grd_data = grading.get_grading_data()
        humanities = [dict["HUMANITIES"] for dict in grd_data if "HUMANITIES" in dict][0]
        
        grd_data = grading.get_grading_data()
        general = [dict["GENERAL"] for dict in grd_data if "HUMANITIES" in dict][0]
        
        if self.grading_spinner.text == "GENERAL":
            self.ids.all_grading_container.clear_widgets()
            
            # GENERAL 
            
            ep_from = str(general["E"][0][0])
            ep_to = str(general["E"][0][1])
            ep_rm = str(general["E"][2])
            
            dm_from = str(general["D-"][0][0])
            dm_to = str(general["D-"][0][1])
            dm_rm = str(general["D-"][2])
            
            dp_from = str(general["D"][0][0])
            dp_to = str(general["D"][0][1])
            dp_rm = str(general["D"][2])
             
            ds_from = str(general["D+"][0][0])
            ds_to = str(general["D+"][0][1])
            ds_rm = str(general["D+"][2])
            
            cm_from = str(general["C-"][0][0])
            cm_to = str(general["C-"][0][1])
            cm_rm = str(general["C-"][2])
            
            cp_from = str(general["C"][0][0])
            cp_to = str(general["C"][0][1])
            cp_rm = str(general["C"][2])
            
            cs_from = str(general["C+"][0][0])
            cs_to = str(general["C+"][0][1])
            cs_rm = str(general["C+"][2])
            
            bm_from = str(general["B-"][0][0])
            bm_to = str(general["B-"][0][1])
            bm_rm = str(general["B-"][2])
            
            bp_from = str(general["B"][0][0])
            bp_to = str(general["B"][0][1])
            bp_rm = str(general["B"][2])
            
            bs_from = str(general["B+"][0][0])
            bs_to = str(general["B+"][0][1])
            bs_rm = str(general["B+"][2])
            
            am_from = str(general["A-"][0][0])
            am_to = str(general["A-"][0][1])
            am_rm = str(general["A-"][2])
            
            ap_from = str(general["A"][0][0])
            ap_to = str(general["A"][0][1])
            ap_rm = str(general["A"][2])
            
            # ------
            self.generalwidget = GeneralGradingLayout()
           
            self.generalwidget.ids.ep_f.text = ep_from
            self.generalwidget.ids.ep_t.text = ep_to
            self.generalwidget.ids.ep_r.text = ep_rm
              
            self.generalwidget.ids.dm_f.text = dm_from
            self.generalwidget.ids.dm_t.text = dm_to
            self.generalwidget.ids.dm_r.text = dm_rm
            
            self.generalwidget.ids.dp_f.text = dp_from
            self.generalwidget.ids.dp_t.text = dp_to
            self.generalwidget.ids.dp_r.text = dp_rm
            
            self.generalwidget.ids.ds_f.text = ds_from
            self.generalwidget.ids.ds_t.text = ds_to
            self.generalwidget.ids.ds_r.text = ds_rm
            
            self.generalwidget.ids.cm_f.text = cm_from
            self.generalwidget.ids.cm_t.text = cm_to
            self.generalwidget.ids.cm_r.text = cm_rm
            
            self.generalwidget.ids.cp_f.text = cp_from
            self.generalwidget.ids.cp_t.text = cp_to
            self.generalwidget.ids.cp_r.text = cp_rm
            
            self.generalwidget.ids.cs_f.text = cs_from
            self.generalwidget.ids.cs_t.text = cs_to
            self.generalwidget.ids.cs_r.text = cs_rm
               
            self.generalwidget.ids.bm_f.text = bm_from
            self.generalwidget.ids.bm_t.text = bm_to
            self.generalwidget.ids.bm_r.text = bm_rm
            
            self.generalwidget.ids.bp_f.text = bp_from
            self.generalwidget.ids.bp_t.text = bp_to
            self.generalwidget.ids.bp_r.text = bp_rm
               
            self.generalwidget.ids.bs_f.text = bs_from
            self.generalwidget.ids.bs_t.text = bs_to
            self.generalwidget.ids.bs_r.text = bs_rm
            
            self.generalwidget.ids.am_f.text = am_from
            self.generalwidget.ids.am_t.text = am_to
            self.generalwidget.ids.am_r.text = am_rm
            
            self.generalwidget.ids.ap_f.text = ap_from
            self.generalwidget.ids.ap_t.text = ap_to
            self.generalwidget.ids.ap_r.text = ap_rm
            
            self.ids.all_grading_container.add_widget(self.generalwidget)
      
        elif self.grading_spinner.text == "MATH & SCIENCE":
            self.ids.all_grading_container.clear_widgets()
            
            # SCIENCE 
            
            e1_from = str(science["E"][0][0])
            e1_to = str(science["E"][0][1])
            
            dm1_from = str(science["D-"][0][0])
            dm1_to = str(science["D-"][0][1])
            
            dp1_from = str(science["D"][0][0])
            dp1_to = str(science["D"][0][1])
            
            ds1_from = str(science["D+"][0][0])
            ds1_to = str(science["D+"][0][1])
            
            cm1_from = str(science["C-"][0][0])
            cm1_to = str(science["C-"][0][1])
            
            cp1_from = str(science["C"][0][0])
            cp1_to = str(science["C"][0][1])
            
            cs1_from = str(science["C+"][0][0])
            cs1_to = str(science["C+"][0][1])
            
            bm1_from = str(science["B-"][0][0])
            bm1_to = str(science["B-"][0][1])
            
            bp1_from = str(science["B"][0][0])
            bp1_to = str(science["B"][0][1])
            
            bs1_from = str(science["B+"][0][0])
            bs1_to = str(science["B+"][0][1])
            
            am1_from = str(science["A-"][0][0])
            am1_to = str(science["A-"][0][1])
            
            ap1_from = str(science["A"][0][0])
            ap1_to = str(science["A"][0][1])
            
            # ------
            
            self.mathsciwidget = MathsAndScienceGradingBoxLayout()
           
            self.mathsciwidget.ids.ep1_f.text = e1_from
            self.mathsciwidget.ids.ep1_t.text = e1_to
                
            self.mathsciwidget.ids.dm1_f.text = dm1_from
            self.mathsciwidget.ids.dm1_t.text = dm1_to
            
            self.mathsciwidget.ids.dp1_f.text = dp1_from
            self.mathsciwidget.ids.dp1_t.text = dp1_to
                
            self.mathsciwidget.ids.ds1_f.text = ds1_from
            self.mathsciwidget.ids.ds1_t.text = ds1_to
            
            self.mathsciwidget.ids.cm1_f.text = cm1_from
            self.mathsciwidget.ids.cm1_t.text = cm1_to
                
            self.mathsciwidget.ids.cp1_f.text = cp1_from
            self.mathsciwidget.ids.cp1_t.text = cp1_to
            
            self.mathsciwidget.ids.cs1_f.text = cs1_from
            self.mathsciwidget.ids.cs1_t.text = cs1_to
                
            self.mathsciwidget.ids.bm1_f.text = bm1_from
            self.mathsciwidget.ids.bm1_t.text = bm1_to
            
            self.mathsciwidget.ids.bp1_f.text = bp1_from
            self.mathsciwidget.ids.bp1_t.text = bp1_to
                
            self.mathsciwidget.ids.bs1_f.text = bs1_from
            self.mathsciwidget.ids.bs1_t.text = bs1_to
            
            self.mathsciwidget.ids.am1_f.text = am1_from
            self.mathsciwidget.ids.am1_t.text = am1_to
                
            self.mathsciwidget.ids.ap1_f.text = ap1_from
            self.mathsciwidget.ids.ap1_t.text = ap1_to
            
            self.ids.all_grading_container.add_widget(self.mathsciwidget)
      
        elif self.grading_spinner.text == "LANGUAGES":
            self.ids.all_grading_container.clear_widgets()
            
            # LANGUAGES 
            
            e2_from = str(languages["E"][0][0])
            e2_to = str(languages["E"][0][1])
            
            dm2_from = str(languages["D-"][0][0])
            dm2_to = str(languages["D-"][0][1])
            
            dp2_from = str(languages["D"][0][0])
            dp2_to = str(languages["D"][0][1])
            
            ds2_from = str(languages["D+"][0][0])
            ds2_to = str(languages["D+"][0][1])
            
            cm2_from = str(languages["C-"][0][0])
            cm2_to = str(languages["C-"][0][1])
            
            cp2_from = str(languages["C"][0][0])
            cp2_to = str(languages["C"][0][1])
            
            cs2_from = str(languages["C+"][0][0])
            cs2_to = str(languages["C+"][0][1])
            
            bm2_from = str(languages["B-"][0][0])
            bm2_to = str(languages["B-"][0][1])
            
            bp2_from = str(languages["B"][0][0])
            bp2_to = str(languages["B"][0][1])
            
            bs2_from = str(languages["B+"][0][0])
            bs2_to = str(languages["B+"][0][1])
            
            am2_from = str(languages["A-"][0][0])
            am2_to = str(languages["A-"][0][1])
            
            ap2_from = str(languages["A"][0][0])
            ap2_to = str(languages["A"][0][1])
            
            # ------
            
            self.languageswidget = LanguagesGradingLayout()
            
            self.languageswidget.ids.ep2_f.text = e2_from
            self.languageswidget.ids.ep2_t.text = e2_to
                
            self.languageswidget.ids.dm2_f.text = dm2_from
            self.languageswidget.ids.dm2_t.text = dm2_to
            
            self.languageswidget.ids.dp2_f.text = dp2_from
            self.languageswidget.ids.dp2_t.text = dp2_to
                
            self.languageswidget.ids.ds2_f.text = ds2_from
            self.languageswidget.ids.ds2_t.text = ds2_to
            
            self.languageswidget.ids.cm2_f.text = cm2_from
            self.languageswidget.ids.cm2_t.text = cm2_to
                
            self.languageswidget.ids.cp2_f.text = cp2_from
            self.languageswidget.ids.cp2_t.text = cp2_to
            
            self.languageswidget.ids.cs2_f.text = cs2_from
            self.languageswidget.ids.cs2_t.text = cs2_to
                
            self.languageswidget.ids.bm2_f.text = bm2_from
            self.languageswidget.ids.bm2_t.text = bm2_to
            
            self.languageswidget.ids.bp2_f.text = bp2_from
            self.languageswidget.ids.bp2_t.text = bp2_to
                
            self.languageswidget.ids.bs2_f.text = bs2_from
            self.languageswidget.ids.bs2_t.text = bs2_to
            
            self.languageswidget.ids.am2_f.text = am2_from
            self.languageswidget.ids.am2_t.text = am2_to
                
            self.languageswidget.ids.ap2_f.text = ap2_from
            self.languageswidget.ids.ap2_t.text = ap2_to
            
            self.ids.all_grading_container.add_widget(self.languageswidget)
      
        elif self.grading_spinner.text == "HUMANITIES":
            self.ids.all_grading_container.clear_widgets()
            
            # HUMANITIES 
            
            e3_from = str(humanities["E"][0][0])
            e3_to = str(humanities["E"][0][1])
            
            dm3_from = str(humanities["D-"][0][0])
            dm3_to = str(humanities["D-"][0][1])
            
            dp3_from = str(humanities["D"][0][0])
            dp3_to = str(humanities["D"][0][1])
            
            ds3_from = str(humanities["D+"][0][0])
            ds3_to = str(humanities["D+"][0][1])
            
            cm3_from = str(humanities["C-"][0][0])
            cm3_to = str(humanities["C-"][0][1])
            
            cp3_from = str(humanities["C"][0][0])
            cp3_to = str(humanities["C"][0][1])
            
            cs3_from = str(humanities["C+"][0][0])
            cs3_to = str(humanities["C+"][0][1])
            
            bm3_from = str(humanities["B-"][0][0])
            bm3_to = str(humanities["B-"][0][1])
            
            bp3_from = str(humanities["B"][0][0])
            bp3_to = str(humanities["B"][0][1])
            
            bs3_from = str(humanities["B+"][0][0])
            bs3_to = str(humanities["B+"][0][1])
            
            am3_from = str(humanities["A-"][0][0])
            am3_to = str(humanities["A-"][0][1])
            
            ap3_from = str(humanities["A"][0][0])
            ap3_to = str(humanities["A"][0][1])
            
            # ------
            
            self.humanitieswidget = HumanitiesGradingLayout()
      
            self.humanitieswidget.ids.ep3_f.text = e3_from
            self.humanitieswidget.ids.ep3_t.text = e3_to
                
            self.humanitieswidget.ids.dm3_f.text = dm3_from
            self.humanitieswidget.ids.dm3_t.text = dm3_to
            
            self.humanitieswidget.ids.dp3_f.text = dp3_from
            self.humanitieswidget.ids.dp3_t.text = dp3_to
                
            self.humanitieswidget.ids.ds3_f.text = ds3_from
            self.humanitieswidget.ids.ds3_t.text = ds3_to
            
            self.humanitieswidget.ids.cm3_f.text = cm3_from
            self.humanitieswidget.ids.cm3_t.text = cm3_to
                
            self.humanitieswidget.ids.cp3_f.text = cp3_from
            self.humanitieswidget.ids.cp3_t.text = cp3_to
            
            self.humanitieswidget.ids.cs3_f.text = cs3_from
            self.humanitieswidget.ids.cs3_t.text = cs3_to
                
            self.humanitieswidget.ids.bm3_f.text = bm3_from
            self.humanitieswidget.ids.bm3_t.text = bm3_to
            
            self.humanitieswidget.ids.bp3_f.text = bp3_from
            self.humanitieswidget.ids.bp3_t.text = bp3_to
                
            self.humanitieswidget.ids.bs3_f.text = bs3_from
            self.humanitieswidget.ids.bs3_t.text = bs3_to
            
            self.humanitieswidget.ids.am3_f.text = am3_from
            self.humanitieswidget.ids.am3_t.text = am3_to
                
            self.humanitieswidget.ids.ap3_f.text = ap3_from
            self.humanitieswidget.ids.ap3_t.text = ap3_to
            
            self.ids.all_grading_container.add_widget(self.humanitieswidget)
      
        else:
            self.ids.all_grading_container.clear_widgets()
            
            # COMMENTS
            
            comments = []
            
            cobj = Comment()
            
            for comment in cobj.get_comments():
                comments.append(comment)
            
            self.commentswidget = CommentsGradingLayout()
       
            self.commentswidget.ids.princi_comment_x.text = [data["GRADE X"]["head_teacher"] for data in comments if "GRADE X" in data][0]
            self.commentswidget.ids.classtr_comment_x.text = [data["GRADE X"]["class_teacher"] for data in comments if "GRADE X" in data][0]
        
            self.commentswidget.ids.princi_comment_e.text = [data["GRADE E"]["head_teacher"] for data in comments if "GRADE E" in data][0]
            self.commentswidget.ids.classtr_comment_e.text = [data["GRADE E"]["class_teacher"] for data in comments if "GRADE E" in data][0]
        
            self.commentswidget.ids.princi_comment_d.text = [data["GRADE D"]["head_teacher"] for data in comments if "GRADE D" in data][0]
            self.commentswidget.ids.classtr_comment_d.text = [data["GRADE D"]["class_teacher"] for data in comments if "GRADE D" in data][0]
            
            self.commentswidget.ids.princi_comment_c.text = [data["GRADE C"]["head_teacher"] for data in comments if "GRADE C" in data][0]
            self.commentswidget.ids.classtr_comment_c.text = [data["GRADE C"]["class_teacher"] for data in comments if "GRADE C" in data][0]
        
            self.commentswidget.ids.princi_comment_b.text = [data["GRADE B"]["head_teacher"] for data in comments if "GRADE B" in data][0]
            self.commentswidget.ids.classtr_comment_b.text = [data["GRADE B"]["class_teacher"] for data in comments if "GRADE B" in data][0]
        
            self.commentswidget.ids.princi_comment_a.text = [data["GRADE A"]["head_teacher"] for data in comments if "GRADE A" in data][0]
            self.commentswidget.ids.classtr_comment_a.text = [data["GRADE A"]["class_teacher"] for data in comments if "GRADE A" in data][0]
        
            self.ids.all_grading_container.add_widget(self.commentswidget)
      
    def update_grading(self):
        if self.grading_spinner.text == "MATH & SCIENCE":
            e1_from = self.mathsciwidget.ids.ep1_f.text 
            e1_to = self.mathsciwidget.ids.ep1_t.text
                
            dm1_from = self.mathsciwidget.ids.dm1_f.text
            dm1_to = self.mathsciwidget.ids.dm1_t.text
            
            dp1_from = self.mathsciwidget.ids.dp1_f.text  
            dp1_to = self.mathsciwidget.ids.dp1_t.text  
                
            ds1_from = self.mathsciwidget.ids.ds1_f.text  
            ds1_to = self.mathsciwidget.ids.ds1_t.text 
            
            cm1_from = self.mathsciwidget.ids.cm1_f.text 
            cm1_to = self.mathsciwidget.ids.cm1_t.text 
                
            cp1_from = self.mathsciwidget.ids.cp1_f.text  
            cp1_to = self.mathsciwidget.ids.cp1_t.text 
            
            cs1_from = self.mathsciwidget.ids.cs1_f.text  
            cs1_to = self.mathsciwidget.ids.cs1_t.text  
                
            bm1_from = self.mathsciwidget.ids.bm1_f.text  
            bm1_to = self.mathsciwidget.ids.bm1_t.text  
            
            bp1_from = self.mathsciwidget.ids.bp1_f.text  
            bp1_to = self.mathsciwidget.ids.bp1_t.text  
                
            bs1_from = self.mathsciwidget.ids.bs1_f.text  
            bs1_to = self.mathsciwidget.ids.bs1_t.text  
            
            am1_from = self.mathsciwidget.ids.am1_f.text  
            am1_to = self.mathsciwidget.ids.am1_t.text 
                
            ap1_from = self.mathsciwidget.ids.ap1_f.text 
            ap1_to = self.mathsciwidget.ids.ap1_t.text
            
            science = {"E": [[self.wash_value(e1_from), self.wash_value(e1_to)],1],
                       "D-": [[self.wash_value(dm1_from), self.wash_value(dm1_to)],2],
                       "D": [[self.wash_value(dp1_from), self.wash_value(dp1_to)],3], 
                       "D+": [[self.wash_value(ds1_from), self.wash_value(ds1_to)],4],
                       "C-": [[self.wash_value(cm1_from), self.wash_value(cm1_to)],5],
                       "C": [[self.wash_value(cp1_from), self.wash_value(cp1_to)],6],
                       "C+": [[self.wash_value(cs1_from), self.wash_value(cs1_to)],7],
                       "B-": [[self.wash_value(bm1_from), self.wash_value(bm1_to)],8],
                       "B": [[self.wash_value(bp1_from), self.wash_value(bp1_to)],9],
                       "B+": [[self.wash_value(bs1_from), self.wash_value(bs1_to)],10],
                       "A-": [[self.wash_value(am1_from), self.wash_value(am1_to)],11],
                       "A": [[self.wash_value(ap1_from), self.wash_value(ap1_to)],12],
              }
              
            grading = Grading()
            grading.update_grading_sciences(science)
            
            show_toast("Updated maths & science grading system.")
            
        elif self.grading_spinner.text == "LANGUAGES":
            e2_from = self.languageswidget.ids.ep2_f.text  
            e2_to = self.languageswidget.ids.ep2_t.text 
                
            dm2_from = self.languageswidget.ids.dm2_f.text  
            dm2_to = self.languageswidget.ids.dm2_t.text  
            
            dp2_from = self.languageswidget.ids.dp2_f.text 
            dp2_to = self.languageswidget.ids.dp2_t.text  
                
            ds2_from = self.languageswidget.ids.ds2_f.text  
            ds2_to = self.languageswidget.ids.ds2_t.text  
            
            cm2_from = self.languageswidget.ids.cm2_f.text  
            cm2_to = self.languageswidget.ids.cm2_t.text  
               
            cp2_from = self.languageswidget.ids.cp2_f.text 
            cp2_to = self.languageswidget.ids.cp2_t.text 
            
            cs2_from = self.languageswidget.ids.cs2_f.text  
            cs2_to = self.languageswidget.ids.cs2_t.text  
               
            bm2_from = self.languageswidget.ids.bm2_f.text
            bm2_to = self.languageswidget.ids.bm2_t.text  
            
            bp2_from = self.languageswidget.ids.bp2_f.text  
            bp2_to = self.languageswidget.ids.bp2_t.text  
                
            bs2_from = self.languageswidget.ids.bs2_f.text 
            bs2_to = self.languageswidget.ids.bs2_t.text 
           
            am2_from = self.languageswidget.ids.am2_f.text  
            am2_to = self.languageswidget.ids.am2_t.text  
                
            ap2_from = self.languageswidget.ids.ap2_f.text 
            ap2_to = self.languageswidget.ids.ap2_t.text  
            
            languages = {"E": [[self.wash_value(e2_from), self.wash_value(e2_to)],1],
                       "D-": [[self.wash_value(dm2_from), self.wash_value(dm2_to)],2],
                       "D": [[self.wash_value(dp2_from), self.wash_value(dp2_to)],3], 
                       "D+": [[self.wash_value(ds2_from), self.wash_value(ds2_to)],4],
                       "C-": [[self.wash_value(cm2_from), self.wash_value(cm2_to)],5],
                       "C": [[self.wash_value(cp2_from), self.wash_value(cp2_to)],6],
                       "C+": [[self.wash_value(cs2_from), self.wash_value(cs2_to)],7],
                       "B-": [[self.wash_value(bm2_from), self.wash_value(bm2_to)],8],
                       "B": [[self.wash_value(bp2_from), self.wash_value(bp2_to)],9],
                       "B+": [[self.wash_value(bs2_from), self.wash_value(bs2_to)],10],
                       "A-": [[self.wash_value(am2_from), self.wash_value(am2_to)],11],
                       "A": [[self.wash_value(ap2_from), self.wash_value(ap2_to)],12],
              }  
            
            grading = Grading()
            grading.update_grading_languages(languages)
            
            show_toast("Updated languages grading system.")
            
        elif self.grading_spinner.text == "HUMANITIES":
            e3_from = self.humanitieswidget.ids.ep3_f.text  
            e3_to = self.humanitieswidget.ids.ep3_t.text 
                
            dm3_from = self.humanitieswidget.ids.dm3_f.text  
            dm3_to = self.humanitieswidget.ids.dm3_t.text  
            
            dp3_from = self.humanitieswidget.ids.dp3_f.text  
            dp3_to = self.humanitieswidget.ids.dp3_t.text  
                
            ds3_from = self.humanitieswidget.ids.ds3_f.text  
            ds3_to = self.humanitieswidget.ids.ds3_t.text  
            
            cm3_from = self.humanitieswidget.ids.cm3_f.text  
            cm3_to = self.humanitieswidget.ids.cm3_t.text  
                
            cp3_from = self.humanitieswidget.ids.cp3_f.text  
            cp3_to = self.humanitieswidget.ids.cp3_t.text  
            
            cs3_from = self.humanitieswidget.ids.cs3_f.text 
            cs3_to = self.humanitieswidget.ids.cs3_t.text  
                
            bm3_from = self.humanitieswidget.ids.bm3_f.text  
            bm3_to = self.humanitieswidget.ids.bm3_t.text 
            
            bp3_from = self.humanitieswidget.ids.bp3_f.text 
            bp3_to = self.humanitieswidget.ids.bp3_t.text  
                
            bs3_from = self.humanitieswidget.ids.bs3_f.text  
            bs3_to = self.humanitieswidget.ids.bs3_t.text  
            
            am3_from = self.humanitieswidget.ids.am3_f.text  
            am3_to = self.humanitieswidget.ids.am3_t.text  
                
            ap3_from = self.humanitieswidget.ids.ap3_f.text  
            ap3_to = self.humanitieswidget.ids.ap3_t.text
            
            humanities = {"E": [[self.wash_value(e3_from), self.wash_value(e3_to)],1],
                       "D-": [[self.wash_value(dm3_from), self.wash_value(dm3_to)],2],
                       "D": [[self.wash_value(dp3_from), self.wash_value(dp3_to)],3], 
                       "D+": [[self.wash_value(ds3_from), self.wash_value(ds3_to)],4],
                       "C-": [[self.wash_value(cm3_from), self.wash_value(cm3_to)],5],
                       "C": [[self.wash_value(cp3_from), self.wash_value(cp3_to)],6],
                       "C+": [[self.wash_value(cs3_from), self.wash_value(cs3_to)],7],
                       "B-": [[self.wash_value(bm3_from), self.wash_value(bm3_to)],8],
                       "B": [[self.wash_value(bp3_from), self.wash_value(bp3_to)],9],
                       "B+": [[self.wash_value(bs3_from), self.wash_value(bs3_to)],10],
                       "A-": [[self.wash_value(am3_from), self.wash_value(am3_to)],11],
                       "A": [[self.wash_value(ap3_from), self.wash_value(ap3_to)],12],
              }  
              
            
            grading = Grading()
            grading.update_grading_humanities(humanities)
            
            show_toast("Updated humanities grading system.")
            
        elif self.grading_spinner.text == "COMMENTS":
            cobj = Comment()
            cobj.update_comments(self.commentswidget.ids.princi_comment_x.text, 
                                 self.commentswidget.ids.classtr_comment_x.text,
                                 self.commentswidget.ids.princi_comment_e.text, 
                                 self.commentswidget.ids.classtr_comment_e.text, 
                                 self.commentswidget.ids.princi_comment_d.text, 
                                 self.commentswidget.ids.classtr_comment_d.text, 
                                 self.commentswidget.ids.princi_comment_c.text, 
                                 self.commentswidget.ids.classtr_comment_c.text, 
                                 self.commentswidget.ids.princi_comment_b.text, 
                                 self.commentswidget.ids.classtr_comment_b.text, 
                                 self.commentswidget.ids.princi_comment_a.text, 
                                 self.commentswidget.ids.classtr_comment_a.text)
            
            show_toast("Updated comments system.")
            
    def wash_value(self, value):
        if re.match("^[\d]+$", value):
            clean_value = int(value)
            
        else:
            clean_value = -1
        
        return clean_value
      