from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from tela1 import TelaBoasVindas
from tela2 import TelaSugestao, TelaFavoritos

class MovieApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(TelaBoasVindas(name='boasvindas'))
        sm.add_widget(TelaSugestao(name='sugestao'))
        sm.add_widget(TelaFavoritos(name='favoritos'))
        return sm

if __name__ == "__main__":
    MovieApp().run()
