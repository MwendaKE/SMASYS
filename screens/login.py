from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    dialog = None
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        pass