from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import json

# Import KivyMD components
from kivymd.app import MDApp

# Load the kv file
Builder.load_file('login.kv')

# Define your screens
class LoginScreen(Screen):
    pass

class SuccessScreen(Screen):
    pass

class FailScreen(Screen):
    pass

# Main App
class MyApp(MDApp):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SuccessScreen(name='success'))
        sm.add_widget(FailScreen(name='fail'))
        return sm

    def login(self, username, password):
        with open('/app/users.json') as f:
            users = json.load(f)['users']

        if any(u['username'] == username and u['password'] == password for u in users):
            self.root.current = 'success'
        else:
            self.root.current = 'fail'

# Run the app
if __name__ == '__main__':
    MyApp().run()
