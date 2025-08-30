from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle

class TelaBoasVindas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        with self.canvas.before:
            Color(0.05, 0.05, 0.2, 1) 
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[0])
        self.bind(pos=self.update_bg, size=self.update_bg)


        layout = BoxLayout(orientation='vertical', padding=dp(40), spacing=dp(30))

        self.titulo = Label(
            text=" Bem-vindo ao MovieApp",
            font_size=dp(32),
            color=(1, 0.9, 0.3, 1),  
            size_hint_y=None,
            height=dp(60)
        )
        layout.add_widget(self.titulo)

        box_input = BoxLayout(size_hint_y=None, height=dp(50), padding=dp(5))
        with box_input.canvas.before:
            Color(0.2, 0.2, 0.4, 1)  
            self.input_bg = RoundedRectangle(pos=box_input.pos, size=box_input.size, radius=[10])
        box_input.bind(pos=self.update_input_bg, size=self.update_input_bg)

        self.entrada_nome = TextInput(
            hint_text="Digite seu nome",
            font_size=dp(18),
            multiline=False,
            background_color=(0,0,0,0),
            foreground_color=(1,1,1,1),
            padding=[dp(10), dp(10), dp(10), dp(10)]
        )
        box_input.add_widget(self.entrada_nome)
        layout.add_widget(box_input)
        
        btn_continuar = Button(
            text="➡ Continuar",
            font_size=dp(22),
            size_hint_y=None,
            height=dp(50),
            background_color=(0.1, 0.5, 0.8, 1),
            color=(1,1,1,1)
        )
        btn_continuar.bind(on_release=self.ir_para_sugestao)
        layout.add_widget(btn_continuar)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def update_input_bg(self, instance, *args):
        self.input_bg.pos = instance.pos
        self.input_bg.size = instance.size

    def ir_para_sugestao(self, instance):
        nome = self.entrada_nome.text.strip()
        if nome:
            self.manager.get_screen('sugestao').usuario = nome
            setattr(self.manager, 'current', 'sugestao')
