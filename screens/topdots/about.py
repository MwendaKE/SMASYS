from kivy.app import App

from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.list import OneLineRightIconListItem, OneLineListItem, TwoLineListItem, IRightBody
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.screenmanager import Screen

from modules.datamanager import Student, Hostel, Staff
from modules.msgmanager import show_toast, show_error
from modules import listsmanager

      
class SmasysAboutScreen(Screen):
    desc = "SMASYS is a school management software. It helps simplify the administrative tasks, keep track of students, staff and parents, and maintain detailed academic records including transcripts and exam results."
    git = "MwendaKE"
    email = "erickmwenda256@gmail.com"
    phone = "+ 254 702 623 729 / + 254 799 678 038"
    company = "MwendaSoft"
    website = "mwendasoft.com"
    
    def __init__(self, **kwargs):
        super(SmasysAboutScreen, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        pass