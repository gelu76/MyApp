from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_file("login.kv")

class LoginScreen(Screen):
    def verify_credentials(self):
        username = self.ids.username.text
        password = self.ids.password.text

        if username == "gelu" and password == "1234":
            app = MDApp.get_running_app()
            app.switch_to_main()
        else:
            print("Invalid credentials")
