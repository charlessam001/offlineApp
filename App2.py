from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFloatingActionButton, MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
#from kivy.lang import Builder

#username_helper = """
#MDTextField:
#hint_text:"Enter username"
#helper_text:"or click on forgot button"
#helper_text_mode:"on_focus"
#pos_hint: {'center_x': 0.5, 'center_y': 0.7}
#size_hint_x:None
#width: 300

#"""


class SecondApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        self.username = MDTextField(hint_text='Enter username',helper_text_mode='on_focus', size_hint_x=None,
                               helper_text="or click to other", pos_hint={'center_x': 0.5, 'center_y': 0.7})
        label = MDLabel(text="GOOD MORNING CHARLES", halign="center",
                        theme_text_color="Custom", text_color=(238/255.0,98/255.0,81/255.0,1), font_style="Caption")
        btn = MDFloatingActionButton(icon="language-python", text="python", pos_hint={'center_x': 0.5, 'center_y': 0.4})
        btn2 = MDRectangleFlatButton(text="Show", pos_hint={'center_x': 0.5, 'center_y': 0.3}, on_release= self.show_data)
        screen.add_widget(label)
        screen.add_widget(btn)
        screen.add_widget(btn2)
        screen.add_widget(self.username)
        return screen

    def show_data(self, obj):
        print(self.username.text)





