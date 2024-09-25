from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.toast import toast


class WaitingDialog:
    def show_waiting_dialog(self, text="Please wait..."):
        self.dialog = MDDialog(
                text = text,
                type = "custom",
                auto_dismiss = False,
                ) 
        self.dialog.open()
        
    def close_waiting_dialog(self):
        self.dialog.dismiss()
        
def show_error(title, text):
    dialog = MDDialog(
                title = "Student" if not title else title, 
                text = "Fields marked with '*' are mandatory!" if not text else text,
                type = "custom",
                auto_dismiss = False,
                        
                buttons = [
                    MDFlatButton(
                        text = "OKAY",
                        theme_text_color = "Custom",
                        pos_hint = {'center_x': .5, 'center_y': .5},
                        on_release = lambda _: dialog.dismiss(),
                        ),
                ],
            )
            
    dialog.open()
    
def show_message(title, text):
    dialog = MDDialog(
                title = "Student" if not title else title, 
                text = "Fields marked with '*' are mandatory!" if not text else text,
                type = "custom",
                auto_dismiss = False,
                        
                buttons = [
                    MDFlatButton(
                        text = "OKAY",
                        theme_text_color = "Custom",
                        pos_hint = {'center_x': .5, 'center_y': .5},
                        on_release = lambda _: dialog.dismiss(),
                        ),
                ],
            )
            
    dialog.open()
      
def show_toast(msg):
    toast(msg)
    
