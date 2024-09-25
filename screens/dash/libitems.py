from kivy.app import App

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, IRightBody
from kivymd.uix.label import MDLabel

from modules.datamanager import LibraryCollection, Library, LibraryItemCounter
from modules.msgmanager import show_error, show_toast

import re


class LibraryItemAddDialogContent(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super(LibraryItemAddDialogContent, self).__init__(**kwargs)
        self.init()
        
    def init(self):
        collections = []
        types = ["TEXT BOOK","SET BOOK","NOVEL","REVISION BOOK","GENERAL","OTHER"]
        classes = ["GENERAL","PRIMARY SCHOOL","JUNIOR SCHOOL","FORM 1","FORM 2","FORM 3","FORM 4","SENIOR SCHOOL","COLLEGE"]
        
        lib = LibraryCollection()
        libcollections = lib.get_collections()
        
        for collection in libcollections:
            colname = collection["collection_name"]
            
            collections.append(colname)
            
        self.ids.item_type.values = types
        self.ids.item_class.values = classes
        
        return
        
        
class LibraryItemEditDialogContent(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super(LibraryItemEditDialogContent, self).__init__(**kwargs)
        
    def increment_counter(self):
        try:
            count = int(self.ids.item_count.text)
            count += 1
            
            self.ids.item_count.text = str(count)
            
        except:
            pass
            
    def decrement_counter(self):
        try:
            count = int(self.ids.item_count.text)
            count -= 1
            
            self.ids.item_count.text = str(count)
            
        except:
            pass
        
        
class LibraryItemClassLabel(MDLabel):
    pass
    
    
class CollectionItemListItem(TwoLineListItem):
    dialog = None
    
    def __init__(self, iid, *args, **kwargs):
        super(CollectionItemListItem, self).__init__(**kwargs)
        
        self.iid = iid
        self.iname = "" 
        
    def on_release(self):
        lib = Library()
        libitem = lib.get_library_item(self.iid)
        
        self.iname = libitem["item_name"]
        itype = libitem["item_type"]
        iclass = libitem["class_grade"]
        icoll = libitem["collection"]
        
        lib = LibraryItemCounter()
        counter = lib.get_counter(self.iname)
        
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Edit Library Item",
                type = "custom",
                content_cls = LibraryItemEditDialogContent(),
                auto_dismiss = False,
                        
                buttons = [
                    MDFlatButton(
                        text = "CANCEL",
                        theme_text_color = "Custom",
                        pos_hint = {'center_x': .5, 'center_y': .5},
                        on_release = lambda _: self.close_dialog(),
                        ),
                    MDFlatButton(
                        text = "SAVE",
                        theme_text_color = "Custom",
                        pos_hint = {'center_x': .5, 'center_y': .5},
                        on_release = lambda _: self.update_item(),
                        ),
                ],
            )
           
        self.dialog.content_cls.ids.item_name.text = self.iname
        self.dialog.content_cls.ids.item_type.text = itype
        self.dialog.content_cls.ids.item_class.text = iclass
        self.dialog.content_cls.ids.item_coll.text = icoll
        self.dialog.content_cls.ids.item_count.text = str(counter)
        
        self.dialog.open()
        
        return
        
    def update_item(self):
        iname = self.dialog.content_cls.ids.item_name.text
        itype = self.dialog.content_cls.ids.item_type.text
        iclass = self.dialog.content_cls.ids.item_class.text
        icoll = self.dialog.content_cls.ids.item_coll.text
        counter = self.dialog.content_cls.ids.item_count.text
        
        if re.match("^[\d]+$", counter):
            counter = int(counter)
            
        else:
            show_error("Error", f"Item counter must be an integer!")
            return
            
        if (iname == "" or iname.isspace()):
            show_error("Error", f"Every field in this dialog is required!")
            return
            
        if (len(iname) > 40):
           show_error("Error", f"Your 'Item Name *' length must be less than 40 characters!")   
           return
               
        self.close_dialog()
        
        iname = iname.title()
           
        lib = Library()
        lib.update_libitem(self.iid, iname)
        
        lib = LibraryItemCounter()
        cid = lib.get_counter_id(self.iname)
        
        lib.update_counter_num(cid, counter)
        lib.update_counter_iname(cid, iname)
        
        show_toast(f"Updated item name and counter successfully!")
        
        app = App.get_running_app()
        app.root.ids.libitems.refresh_libitems_screen()
        
        return
        
    def close_dialog(self):
        self.dialog.dismiss()
        self.dialog = None
        
        return
        
 
class LibraryItemsScreen(Screen):
    collection_name = ObjectProperty()
    
    dialog = None
    
    def __init__(self, **kwargs):
        super(LibraryItemsScreen, self).__init__(**kwargs)
        self.colname  = ""
        
    def on_pre_enter(self):
        self.refresh_libitems_screen()
        
        return
        
    def on_pre_leave(self):
        self.ids.libitems_container.clear_widgets()
        
        return
        
    def refresh_libitems_screen(self):
        self.ids.libitems_container.clear_widgets()
        
        app = App.get_running_app()
        
        lib = Library()
        libitems = lib.get_library_items(self.colname)
        counter = lib.get_collection_count(self.colname)
        libclasses = set()
        collection_items = []
       
        for libitem in libitems:
            iid = libitem["_id"]
            iname = libitem["item_name"] 
            itype = libitem["item_type"]
            iclass = libitem["class_grade"]
                
            icounter = lib.get_item_count(iname)
            
            collection_items.append((iid, iname, itype, iclass, icounter))     
            libclasses.add(iclass)
            
        self.ids.libcollection_name.text = self.colname
        self.ids.libitemscount_label.text = str(counter)
        
        if not collection_items:
            return
            
        for cls in sorted(libclasses):
            gridlayout = MDGridLayout(cols=1, spacing=2, adaptive_height=True)
            iclass_label = LibraryItemClassLabel()
            mdlist = MDList()
            
            for iid, iname, itype, iclass, icounter in collection_items:
                if iclass == cls:
                    iclass_label.text = iclass
                    mdlist.add_widget(CollectionItemListItem(iid, text=f"[size=30]{iname}[/size]", secondary_text=f"[size=26][color=008080]Category: {itype.title()} | Count: {icounter}[/color][/size]"))
                
            gridlayout.add_widget(iclass_label)
            gridlayout.add_widget(mdlist)
            
            self.ids.libitems_container.add_widget(gridlayout)
       
        return
   
    def add_library_item(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = f"Add [color=FFA500]{self.collection_name.text}[/color] Item",
                type = "custom",
                content_cls = LibraryItemAddDialogContent(),
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
                        on_release = lambda _: self.add_item(),
                        ),
                ],
            )
            
        self.dialog.content_cls.ids.item_collection.text = self.collection_name.text 
        
        self.dialog.open()
        
        return
        
    def add_item(self):
        iname = self.dialog.content_cls.ids.item_name.text
        icoll = self.dialog.content_cls.ids.item_collection.text
        itype = self.dialog.content_cls.ids.item_type.text
        iclass = self.dialog.content_cls.ids.item_class.text
        
        
        if (iname == "" or iname.isspace()):
            show_error("Error", f"Every field in this dialog is required!")
            
            return
            
        if (icoll == "Select Collection" or itype == "Select Type" or iclass == "Select Class"):
            show_error("Error", f"Please fill all the fields!")
            
            return
          
        if (len(iname) > 40):
           show_error("Error", f"Your 'Item Name *' length must be less than 40 characters!")
               
           return
               
        self.close_dialog()
        
        iname = iname.title()
         
        lib = Library()
        lib.add_item(icoll, iname, itype, iclass)
        
        counter = LibraryItemCounter()
        counter.add_counter(iname)
        
        show_toast(f"Added new library item successfully")
        
        self.refresh_libitems_screen()
        
        return
        
    def close_dialog(self):
        self.dialog.dismiss()
        self.dialog = None
        
        return