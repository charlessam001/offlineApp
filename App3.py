# a propos des listesC
#1 _builder_basic_main
"""
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

list_helper = """
#ScrollView:
    #MDList:
        #OneLineListItem:
            #text: 'Item1'
        #OneLineListItem:
            #text: 'Item2'
"""



class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        list_item = Builder.load_string(list_helper)
        screen.add_widget(list_item)
        return screen


DemoApp().run()

"""
# builder_main
"""
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

list_helper = """
#ScrollView:
    #MDList:
        #OneLineListItem:
            #text: 'Item1'
        #OneLineListItem:
            #text: 'Item2'
"""



class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        list_item = Builder.load_string(list_helper)
        screen.add_widget(list_item)
        return screen


DemoApp().run()

"""
#main_for_list
"""
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        Salutation = ['Jambo', 'Bonjour', 'Hello']
        Lalangue = ['Swahili', 'Francaise', 'Anglaise']


        # Creating a Simple List
        scroll = ScrollView()

        list_view = MDList()
        for i in range(3):

             #items = ThreeLineListItem(text='la langue  ' + str(i) ,
                                      #secondary_text=Lalangue[i] +' ' + str(i)  + 'th language',
                                      #tertiary_text=Salutation[i])

             icons = IconLeftWidget(icon="android")
             items = OneLineIconListItem(text=str(i) + ' item')
             items.add_widget(icons)
             list_view.add_widget(items)

        scroll.add_widget(list_view)
        # End List

        screen.add_widget(scroll)
        return screen


DemoApp().run()


"""

#personal_modification

"""
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        Salutation = ['Jambo', 'Bonjour', 'Hello']
        Lalangue = ['Swahili', 'Francaise', 'Anglaise']


        # Creating a Simple List
        scroll = ScrollView()

        list_view = MDList()
        for i in range(3):
             lidesicon = ['android', 'language-python', 'language-java']
             
                       
             icons = IconLeftWidget(icon=lidesicon[i])
             items = ThreeLineIconListItem(text='la langue  ' + str(i) ,
                                      secondary_text=Lalangue[i] +' ' + str(i)  + 'th language',
                                      tertiary_text=Salutation[i])

             
             #items = OneLineIconListItem(text=str(i) + ' item')
             items.add_widget(icons)
             list_view.add_widget(items)

        scroll.add_widget(list_view)
        # End List

        screen.add_widget(scroll)
        return screen


DemoApp().run()
"""
