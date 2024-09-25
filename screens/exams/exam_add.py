from kivy.uix.screenmanager import Screen

class AddExamScreen(Screen):
    def __init__(self, **kwargs):
        super(AddExamScreen, self).__init__(**kwargs)
    
    def add_exam(self, year, term, exam, form):
        pass