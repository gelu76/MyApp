from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from login import LoginScreen
from main import MainScreen
from users import UsersScreen

Builder.load_file("login.kv")
Builder.load_file("main.kv")
Builder.load_file("users.kv")

class CustomNavigationDrawer(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'  # Force vertical layout 

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class NavigationScreen(Screen):
    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)
        self.name = 'navigation'
        self.sm = sm
        nav_drawer = CustomNavigationDrawer()
        nav_drawer.add_widget(ContentNavigationDrawer(screen_manager=self.sm, nav_drawer=nav_drawer))
        self.add_widget(nav_drawer)

class MainApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(UsersScreen(name='users'))
        # **Ensure NavigationScreen is added ONLY ONCE**
        self.sm.add_widget(NavigationScreen(sm=self.sm)) 
        return self.sm

    def switch_to_main(self):
        self.sm.current = 'main'

    def toggle_nav_drawer(self):
        if self.sm.current == 'main':
            screen = self.sm.get_screen('main')
        elif self.sm.current == 'users':
            screen = self.sm.get_screen('users')
        else:
            return
        nav_drawer = screen.ids.nav_drawer
        nav_drawer.set_state("toggle")

if __name__ == '__main__':
    MainApp().run()