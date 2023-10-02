
import flet as ft

# views
from views.index_view import IndexView
from views.profile_view import ProfileView
from views.settings_view import SettingsView
from views.login_view import LoginView
from views.calculoconsumo import CalculoView
from views.artefactos import ArtefactosView
from views.entidad_edu import EntidadView

class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft                
        self.routes = {
            "/": IndexView(page),
            "/artefactos": ArtefactosView(page),
            "/calculo": CalculoView(page),
            "/settings": SettingsView(page),
            "/login": LoginView(page),
            "/registrarse": EntidadView(page),
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
