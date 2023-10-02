import flet as ft
import constants

from views.FletRouter import Router
from user_controls.app_bar import NavBar
from database.db import crearTablas

crearTablas()

if __name__== __name__:
    def main(page: ft.Page):
        page.appbar = NavBar(page)
        page.theme_mode = "dark"
        """page.theme = ft.Theme(
            color_scheme= ft.ColorScheme(
                primary=ft.colors.GREEN,
                secondary=ft.colors.GREEN_200,
                tertiary=ft.colors.GREEN_300,                               
            )
        )"""
        page.window_maximized = True    
        page.title= constants.TITLE
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.padding = 20
        page.scroll = ft.ScrollMode.AUTO
        myRouter = Router(page)

        page.on_route_change = myRouter.route_change

        page.add(
            myRouter.body
        )

        page.go('/')

ft.app(target=main, assets_dir="assets")


