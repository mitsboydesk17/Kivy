import random
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
from kivy.animation import Animation
from kivy.core.window import Window

COR_FUNDO = (0.05, 0.05, 0.1, 1)
COR_CARD = (0.12, 0.12, 0.25, 1)
COR_TITULO = (1, 1, 1, 1)
COR_ANO = (0.5, 0.7, 1, 1)
COR_BOTAO = (0, 0.6, 1, 1)
COR_BOTAO_HOVER = (0, 0.8, 1, 1)
COR_TOGGLE = (0, 0.5, 1, 1)
COR_TOGGLE_ACTIVE = (0, 0.8, 1, 1)

Window.clearcolor = COR_FUNDO

class FilmeSorteador:
    def __init__(self):
        self.filmes = {
            "Ação": [("Matrix", 1999, "matrix.jpg"),
                     ("Vingadores: Ultimato", 2019, "ultimato.jpg"),
                     ("Homem-Aranha", 2002, "homemaranha.jpg")],
            "Animação": [("Toy Story", 1995, "toystory.jpg"),
                         ("O Rei Leão", 1994, "reileao.jpg"),
                         ("Shrek", 2001, "shrek.jpg")],
            "Ficção": [("Avatar", 2009, "avatar.jpg"),
                       ("Interestelar", 2014, "inter.jpg"),
                       ("Jurassic Park", 1993, "park.webp")],
            "Romance": [("Titanic", 1997, "titanic.jpg"),
                        ("A Culpa é das Estrelas", 2014, "aculpadasestrelas.jpg")],
            "Comédia": [("Shrek", 2001, "shrek.jpg"),
                        ("De Volta para o Futuro", 1985, "paraofuturo.jpg")]
        }

    def sortear(self, genero):
        if genero in self.filmes:
            return random.choice(self.filmes[genero])
        return ("Nenhum filme disponível", "", "")

class CardFilme(BoxLayout):
    def __init__(self, filme_info, **kwargs):
        super().__init__(orientation="horizontal", size_hint_y=None, padding=10, spacing=10, **kwargs)
        self.bind(minimum_height=self.setter('height'))
        with self.canvas.before:
            Color(*COR_CARD)
            self.rect = RoundedRectangle(radius=[15])
        self.bind(pos=self.update_rect, size=self.update_rect)

        titulo, ano, imagem_file = filme_info

        img_path = os.path.join("images", imagem_file) if imagem_file else None
        if img_path and os.path.exists(img_path):
            self.img = Image(source=img_path, size_hint=(0.35, None), height=150, allow_stretch=True, keep_ratio=True)
        else:
            self.img = Image(size_hint=(0.35, None), height=150)
        self.add_widget(self.img)

        info_layout = BoxLayout(orientation="vertical", spacing=5)
        self.label_titulo = Label(
            text=titulo,
            font_size=20,
            color=COR_TITULO,
            bold=True,
            halign="left",
            valign="middle",
            size_hint_y=None,
            text_size=(400, None)
        )
        self.label_titulo.bind(texture_size=self._update_height)
        self.label_ano = Label(
            text=str(ano),
            font_size=16,
            color=COR_ANO,
            halign="left",
            valign="middle",
            size_hint_y=None
        )
        self.label_ano.bind(texture_size=self._update_height)
        info_layout.add_widget(self.label_titulo)
        info_layout.add_widget(self.label_ano)
        self.add_widget(info_layout)

    def _update_height(self, instance, value):
        instance.height = instance.texture_size[1]

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class FilmeUI(BoxLayout):
    def __init__(self, sorteador: FilmeSorteador, **kwargs):
        super().__init__(orientation="vertical", spacing=15, padding=20, **kwargs)
        self.sorteador = sorteador
        self.genero_escolhido = None
    
        self.scroll = ScrollView(size_hint=(1, 0.55))
        self.grid = GridLayout(cols=1, spacing=15, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.add_widget(self.scroll)

        self.boas_vindas = Label(
            text="🎬 Bem-vindo ao App de Filmes!\nDigite seu nome e escolha um gênero.",
            font_size=20,
            color=COR_TITULO,
            halign="center",
            valign="middle",
            size_hint_y=None
        )
        self.grid.add_widget(self.boas_vindas)

        self.nome_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.1),
            font_size=18,
            foreground_color=COR_TITULO,
            background_color=COR_CARD,
            cursor_color=COR_TITULO
        )
        self.add_widget(self.nome_input)

        self.toggle_layout = BoxLayout(size_hint=(1,0.1), spacing=10)
        self.toggle_buttons = []
        for genero in self.sorteador.filmes.keys():
            tb = ToggleButton(text=genero, background_color=COR_TOGGLE, color=COR_TITULO)
            tb.bind(on_press=self.selecionar_genero)
            self.toggle_layout.add_widget(tb)
            self.toggle_buttons.append(tb)
        self.add_widget(self.toggle_layout)

        self.botao_layout = BoxLayout(size_hint=(1,0.12), spacing=10)
        self.botao_sugerir = Button(text="Sugerir Filme", background_color=COR_BOTAO, font_size=18, bold=True)
        self.botao_sugerir.bind(on_press=self.on_sugerir)
        self.botao_sugerir.bind(on_press=self.animar_botao)
        self.botao_layout.add_widget(self.botao_sugerir)

        self.botao_limpar = Button(text="Limpar", background_color=(0.7,0.1,0.1,1), font_size=18, bold=True)
        self.botao_limpar.bind(on_press=self.limpar)
        self.botao_layout.add_widget(self.botao_limpar)

        self.add_widget(self.botao_layout)

    def selecionar_genero(self, instance):
        for tb in self.toggle_buttons:
            if tb != instance:
                tb.state = 'normal'
        self.genero_escolhido = instance.text if instance.state == 'down' else None

    def animar_botao(self, instance):
        anim = Animation(background_color=COR_BOTAO_HOVER, duration=0.1) + Animation(background_color=COR_BOTAO, duration=0.1)
        anim.start(instance)

    def on_sugerir(self, instance):
        nome = self.nome_input.text.strip()
        genero = self.genero_escolhido

        if not nome:
            self.boas_vindas.text = "❌ Por favor, digite seu nome!"
            return
        if not genero:
            self.boas_vindas.text = "❌ Por favor, selecione um gênero!"
            return

        self.boas_vindas.text = f"Olá {nome}! Sua sugestão de filme de {genero} é:"
        filme_info = self.sorteador.sortear(genero)
        card = CardFilme(filme_info)
        self.grid.add_widget(card)

    def limpar(self, instance):
        self.nome_input.text = ""
        self.genero_escolhido = None
        for tb in self.toggle_buttons:
            tb.state = 'normal'

        self.grid.clear_widgets()

        self.boas_vindas = Label(
            text="🎬 Bem-vindo ao App de Filmes!\nDigite seu nome e escolha um gênero.",
            font_size=20,
            color=COR_TITULO,
            halign="center",
            valign="middle",
            size_hint_y=None
        )
        self.grid.add_widget(self.boas_vindas)

class FilmeApp(App):
    def build(self):
        Window.clearcolor = COR_FUNDO
        sorteador = FilmeSorteador()
        return FilmeUI(sorteador)

if __name__ == "__main__":
    FilmeApp().run()
