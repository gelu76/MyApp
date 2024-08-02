from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from users import UsersScreen
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView

Builder.load_file("main.kv")

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        scroll_view=ScrollView()

        menu_items = BoxLayout(orientation='vertical', size_hint_y=None)
        menu_items.bind(minimum_height=menu_items.setter('height'))

        # Adaugă elementele în ordinea dorită
        self.add_widget(OneLineListItem(text="Home", on_press=self.on_home_press))
        self.add_widget(OneLineListItem(text="Users", on_press=self.on_users_press))
        self.add_widget(OneLineListItem(text="Settings"))
        self.add_widget(OneLineListItem(text="About"))

        # Adaugă BoxLayout-ul în ScrollView
        scroll_view.add_widget(menu_items)

        # Adaugă ScrollView-ul în ContentNavigationDrawer
        self.add_widget(scroll_view)


    def on_home_press(self, instance):
        self.nav_drawer.set_state("close")
        self.screen_manager.current = "main"

    def on_users_press(self, instance):
        self.nav_drawer.set_state("close")
        self.screen_manager.current = "users"  # Correctly switch to "users" screen

class MainScreen(Screen):
    pass

class MainScreenContent(Screen):
    pass