from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
import random

filmes = {
    "Ação": [
        {"nome": "Mad Max", "img": "images/madmax.jpg"},
        {"nome": "John Wick", "img": "images/john.jpg"}
    ],
    "Comédia": [
        {"nome": "Deadpool", "img": "images/dead.jpg"},
        {"nome": "Superbad", "img": "images/super.png"}
    ],
    "Animação": [
        {"nome": "Toy Story", "img": "images/toy.jpg"},
        {"nome": "Shrek", "img": "images/shrek.png"}
    ]
}

class TelaSugestao(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.usuario = ""
        self.filmes_favoritos = []

        with self.canvas.before:
            Color(0.1, 0.1, 0.2, 1)
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[0])
        self.bind(pos=self.update_bg, size=self.update_bg)

        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))

        self.label_boas_vindas = Label(text="", font_size=dp(28), size_hint_y=None, height=dp(60), color=(1, 0.9, 0.3, 1))
        layout.add_widget(self.label_boas_vindas)

        box_spinner = BoxLayout(size_hint_y=None, height=dp(50), padding=dp(5))
        with box_spinner.canvas.before:
            Color(0.2, 0.2, 0.4, 1)
            self.spinner_bg = RoundedRectangle(pos=box_spinner.pos, size=box_spinner.size, radius=[10])
        box_spinner.bind(pos=self.update_spinner_bg, size=self.update_spinner_bg)
        self.spinner_genero = Spinner(
            text="Selecione o gênero",
            values=list(filmes.keys()),
            font_size=dp(18),
            size_hint=(1, 1),
            background_color=(0, 0, 0, 0)
        )
        box_spinner.add_widget(self.spinner_genero)
        layout.add_widget(box_spinner)

        btn_sugerir = Button(
            text="Sugerir Filme",
            font_size=dp(20),
            size_hint_y=None,
            height=dp(50),
            background_color=(0.3, 0.7, 0.3, 1),
            color=(1, 1, 1, 1)
        )
        btn_sugerir.bind(on_release=self.sugerir_filme)
        layout.add_widget(btn_sugerir)

        self.label_filme = Label(text="", font_size=dp(22), size_hint_y=None, height=dp(50), color=(0.9, 0.9, 1, 1))
        layout.add_widget(self.label_filme)

        self.box_imagem = BoxLayout(size_hint_y=0.5, padding=dp(10))
        layout.add_widget(self.box_imagem)

        nav = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        btn_voltar = Button(text="Voltar", background_color=(0.8, 0.2, 0.2, 1), color=(1,1,1,1))
        btn_voltar.bind(on_release=lambda x: setattr(self.manager, 'current', 'boasvindas'))

        btn_favoritos = Button(text="Favoritos", background_color=(0.8, 0.5, 0.2, 1), color=(1,1,1,1))
        btn_favoritos.bind(on_release=self.ir_para_favoritos)

        nav.add_widget(btn_voltar)
        nav.add_widget(btn_favoritos)
        layout.add_widget(nav)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def update_spinner_bg(self, instance, *args):
        self.spinner_bg.pos = instance.pos
        self.spinner_bg.size = instance.size

    def on_pre_enter(self):
        self.label_boas_vindas.text = f"Olá, {self.usuario}!"

    def sugerir_filme(self, instance):
        genero = self.spinner_genero.text
        if genero in filmes:
            filme = random.choice(filmes[genero])
            self.label_filme.text = f"Filme sugerido: {filme['nome']}"
            self.box_imagem.clear_widgets()
            self.box_imagem.add_widget(Image(source=filme['img'], allow_stretch=True))
            if filme not in self.filmes_favoritos:
                self.filmes_favoritos.append(filme)

    def ir_para_favoritos(self, instance):
        tela_fav = self.manager.get_screen('favoritos')
        tela_fav.filmes_favoritos = self.filmes_favoritos
        tela_fav.atualizar()
        setattr(self.manager, 'current', 'favoritos')


class TelaFavoritos(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filmes_favoritos = []

        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        self.scroll = ScrollView(size_hint=(1, 0.9))
        self.grid = GridLayout(cols=1, spacing=dp(10), size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)

        btn_voltar = Button(
            text="Voltar",
            size_hint_y=None,
            height=dp(50),
            background_color=(0.8, 0.2, 0.2, 1),
            color=(1,1,1,1)
        )
        btn_voltar.bind(on_release=lambda x: setattr(self.manager, 'current', 'sugestao'))
        layout.add_widget(btn_voltar)

        self.add_widget(layout)

    def atualizar(self):
        self.grid.clear_widgets()
        for f in self.filmes_favoritos:
            box = BoxLayout(size_hint_y=None, height=dp(200), spacing=dp(10))
            box.add_widget(Image(source=f['img'], allow_stretch=True))
            box.add_widget(Label(text=f['nome'], font_size=dp(20), color=(1,1,1,1)))
            self.grid.add_widget(box)
