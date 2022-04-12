from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Mail = []
Login = []
Passwodr = []

class Contpage1(Screen):
    def loginf(self):
        if self.log_main.text in Login and self.passw_main.text in Passwodr:
            self.lavel_main.text = "Ты вошел"
        else:
            self.lavel_main.text = "Ошибка"

class Contpage2(Screen):
    def Registration(self):
        if self.passwordC2.text ==self.password2C2.text:
            Mail.append(self.mailC2.text)
            Login.append(self.loginC2.text)
            Passwodr.append(self.passwordC2.text)
            print(Mail,Login,Passwodr)
            self.labelreg.text = "Жми назад"

        else:
            self.labelreg.text = "Разные пароли"


class Contpage3(Screen):
    pass


class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    theme_cls = ThemeManager()
    title = "PX"

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.root = Builder.load_file('page1.kv')


if __name__ == '__main__':
    MainApp().run()
