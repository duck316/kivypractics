from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import kivy

kivy.require("1.9.2")

class ScreenOne(BoxLayout):
    def __init__(self):
        super(ScreenOne, self).__init__()





        self.Scroll = ScrollView()
        self.CuadroAzul = ScreenTwo()
        self.CuadroBlanco = ScreenTree()
        self.add_widget(self.CuadroAzul)
        # ----------------------------------------------
        self.MyLab = MyLabel()
        self.MyButton = MyBtn()
        self.CuadroAzul.add_widget(self.MyButton)
        # self.MyButton.bind(on_press=self.CuadroBlanco.add_btn)
        self.MyButton.bind(on_press=self.CuadroBlanco.crealabel)

        # ----------------------------------------------
        # self.CuadroBlanco.add_widget(self.Scroll)
        self.add_widget(self.CuadroBlanco)
        # ---------------------------------
        # self.btn = Button(text="Search 1", size_hint=(.5, 1))
        # self.add_widget(self.btn, index=0)
        # self.btn.bind(on_press=self.CuadroBlanco.add_btn)
        # ---------------------------------


class ScreenTwo(BoxLayout):
    def __init__(self):
        super(ScreenTwo, self).__init__()
        self.SCtree = ScreenTree()
        self.kvTInput = TextInput()
        self.add_widget(self.kvTInput, index=1)


class ScreenTree(GridLayout):
    def __init__(self):
        super(ScreenTree, self).__init__()
    pass

    def add_btn(self, *args):
        self.etiqueta = MyLabel()
        # self.content = MyBtn()
        self.add_widget(self.etiqueta, index=0)
        # self.add_widget(self.content, index=0)

    def crealabel(self, *args):
        lista_prueba = (
            {"titulo": "Titulo Prueba 1", "resumen": "resumen Prueba 1", "imagen": "logo.png"},
            {"titulo": "Titulo Prueba 2", "resumen": "resumen Prueba 2", "imagen": "logo.png"},
            {"titulo": "Titulo Prueba 3", "resumen": "resumen Prueba 3", "imagen": "logo.png"},
            {"titulo": "Titulo Prueba 4", "resumen": "resumen Prueba 4", "imagen": "logo.png"},
            {"titulo": "Titulo Prueba 5", "resumen": "resumen Prueba 5", "imagen": "logo.png"},
            {"titulo": "Titulo Prueba 6", "resumen": "resumen Prueba 6", "imagen": "logo.png"},
            {"titulo": "Titulo Prueba 7", "resumen": "resumen Prueba 7", "imagen": "logo.png"},
            {"titulo": "Titulo Prueba 8", "resumen": "resumen Prueba 8", "imagen": "logo.png"},
            {"titulo": "Titulo Prueba 9", "resumen": "resumen Prueba 9", "imagen": "logo.png"},
            {"titulo": "Titulo Prueba 10", "resumen": "resumen Prueba 10","imagen": "logo.png"}
        )

        num_rows = 25

        for i in range(int(len(lista_prueba))):
            self.ids.details.rows = num_rows
            self.ids.b_img.add_widget(Button(background_normal=lista_prueba[i]["imagen"]))
            self.ids.details.add_widget(Label(text='[color=000000]'+lista_prueba[i]["titulo"]+'[/color]',
                                  markup = True))
            self.ids.details.add_widget(Label(text='[color=000000]'+lista_prueba[i]["resumen"]+'[/color]',
                                  markup = True))
            num_rows= num_rows+ 2



class MyLabel(Label):
    def __init__(self):
        super(MyLabel, self).__init__()
        pass


class MyBtn(Button):
    def __init__(self):
        super(MyBtn, self).__init__()
        self.text = "Search"
        self.size_hint = size_hint=(.5, 1)
        # self.bind(on_press=ScreenTree.add_btn)


class LookUpApp(App):
    title = "LookUP"

    def build(self):
        return ScreenOne()


if __name__ == '__main__':
    LookUpApp().run()