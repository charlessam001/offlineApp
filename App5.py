#Code for toolbar
from kivymd.app import MDApp
#from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
#from kivymd.uix.snackbar import Snackbar

Window.size = (300, 500)


screen_helper = """
MDNavigationLayout:
    
    MDTopAppBar:
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_bar.set_state("open")]]
        elevation: 10

    ScreenManager:
        id: screen_manager
        Screen:
            name: "tipscreen1"
            MDFloatLayout:
                MDLabel:
                    text: "Screen 1"
                    halign : 'center'
        Screen:
            name: "tipscreen2"
            MDFloatLayout:
                MDLabel:
                    text: "Screen 2"
        
        
"""

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(screen_helper)

    def callback_1(self, icon):
        # Votre logique ici
        pass

    def callback_2(self, icon):
        # Votre logique ici
        pass

if __name__ == "__main__":
    MyApp().run()
