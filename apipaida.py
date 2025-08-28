import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.2, 1)

class PiadaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.label_piada = Label(
            text="Clique no botão para receber uma piada!",
            font_size=22,
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle"
        )
        self.layout.add_widget(self.label_piada)

        self.botao = Button(
            text="Nova Piada",
            size_hint=(1, 0.2),
            background_color=(0, 0.6, 1, 1),
            font_size=20
        )
        self.botao.bind(on_press=self.buscar_piada)
        self.layout.add_widget(self.botao)

        return self.layout

    def buscar_piada(self, instance):
        url = "https://official-joke-api.appspot.com/random_joke"
        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                setup = dados.get("setup", "")
                punchline = dados.get("punchline", "")
                self.label_piada.text = f"{setup}\n\n{punchline}"
            else:
                self.label_piada.text = "Erro ao buscar piada :("
        except Exception as e:
            self.label_piada.text = f"Erro: {str(e)}"

if __name__ == "__main__":
    PiadaApp().run()
