#Navigation_drawer_code
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.fitimage import FitImage  # Import FitImage

Window.size = (300, 500)

navigation_helper = """
Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("toggle")]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, dp(16), dp(16), 0)
            MDNavigationDrawerMenu:
                MDNavigationDrawerLabel:
                    text: "Mail"
                MDNavigationDrawerItem:
                    icon: "account"  # Use your custom icon name
                    text: "Inbox"
                    trailing_text: "24"
                MDNavigationDrawerDivider:
                MDNavigationDrawerLabel:
                    text: "En-tête"
                MDNavigationDrawerItem:
                    icon: "inbox"
                    text: "Boîte de réception"
                    trailing_text: "24"
                MDNavigationDrawerDivider:
                MDNavigationDrawerLabel:
                    text: "Sections"
                MDNavigationDrawerItem:
                    icon: "send"
                    text: "Éléments envoyés"
                MDNavigationDrawerItem:
                    icon: "delete"
                    text: "Corbeille"
                MDNavigationDrawerItem:
                    icon: "OKFILE.png"  # Icône de la corbeille
                    font_size: "500sp"  # Ajustez la taille de l'icône ici
                    
                
"""

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

DemoApp().run()
