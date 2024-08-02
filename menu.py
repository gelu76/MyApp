from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file("menu.kv")

class MenuScreen(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()