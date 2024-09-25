from kivy.app import App

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.dialog import MDDialog

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import MDList, OneLineAvatarIconListItem, OneLineListItem, TwoLineListItem, IRightBody
from kivymd.uix.label import MDLabel
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd import images_path

from modules.datamanager import LibraryCollection, Library, LibraryItemCounter
from modules.msgmanager import show_error, show_toast


import re, os


class LibraryCollectionAddDialogContent(MDBoxLayout):
    pass
    
  
class LibraryCollectionListItem(OneLineAvatarIconListItem):
    dialog = None
    
    def __init__(self, colname, *args, **kwargs):
        super(LibraryCollectionListItem, self).__init__(**kwargs)
        
        self.colname = colname
        self.iname = "" 
        
    def on_release(self):
        #=======
        app = App.get_running_app()
        app.root.ids.manager.get_screen('libitems').colname = self.colname
        
        app.root.ids.manager.current = "libitems"
            
        return
        
        
class CollectionCountLabel(IRightBody, MDLabel):
    pass
    
    
class LibraryScreen(Screen):
    dialog = None
    
    def __init__(self, **kwargs):
        super(LibraryScreen, self).__init__(**kwargs)
    
    def on_pre_enter(self):
        self.refresh_library_screen()
        
        return
        
    def on_pre_leave(self):
        self.ids.libcollections_container.clear_widgets()
        
        return
        
    def refresh_library_screen(self):
        self.ids.libcollections_container.clear_widgets()
       
        lib = Library()
        libcollections = sorted([l["collection_name"] for l in lib.get_collections()])
        library_counter = lib.get_all_items_count()
        
        self.ids.librarycount_label.text = str(library_counter)
        
        #---NEW---
        
        if libcollections:
            for colname in libcollections:
                colcount = lib.get_collection_count(colname)
            
                listitem = LibraryCollectionListItem(colname, text=colname)
                listitem.ids.collcount_label.text = str(colcount)
                
                self.ids.libcollections_container.add_widget(listitem)
            
        else:
            self.ids.libcollections_container.add_widget(OneLineListItem(text="No library records found."))
            return
            
    def add_library_collection(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Add Library Collection",
                type = "custom",
                content_cls = LibraryCollectionAddDialogContent(),
                auto_dismiss = False,
                        
                buttons = [
                    MDFlatButton(
                        text = "CANCEL",
                        theme_text_color = "Custom",
                        pos_hint = {'center_x': .5, 'center_y': .5},
                        on_release = lambda _: self.close_dialog(),
                        ),
                    MDFlatButton(
                        text = "ADD",
                        theme_text_color = "Custom",
                        pos_hint = {'center_x': .5, 'center_y': .5},
                        on_release = lambda _: self.add_collection(),
                        ),
                ],
            )
            
        self.dialog.open()
        
        return
        
    def add_collection(self):
        colname = self.dialog.content_cls.ids.colname.text
        
        if (colname == "" or colname.isspace()):
            show_error("Error", f"This field is required!")
            
            return
            
        else:
           if (len(colname) > 20):
               show_error("Error", f"Your text length must be less than 20")
               
               return
               
        self.close_dialog()
            
        lib = LibraryCollection()
        lib.add_collection(colname.title())
        
        show_toast(f"Added library collection '{colname}'")
        
        self.refresh_library_screen()
        
        return
        
    def close_dialog(self):
        self.dialog.dismiss()
        self.dialog = None
        
        return
        
    def get_library_classes(self):
        classes = ["GENERAL","PRIMARY SCHOOL","JUNIOR SCHOOL","FORM 1","FORM 2","FORM 3","FORM 4","SENIOR SCHOOL","COLLEGE"]
        
        return classes
        
    