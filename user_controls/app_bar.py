import flet as ft
import constants as str

def NavBar(page):
    NavBar = ft.AppBar(
            leading=ft.Icon(ft.icons.TAG_FACES_ROUNDED),
            leading_width=40,
            title=ft.Text(str.TITLE),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[                
                ft.IconButton(ft.icons.HOME,tooltip="Home", on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.CALCULATE,tooltip = "Calculadora", on_click=lambda _: page.go('/calculo')),
                ft.IconButton(ft.icons.ADD, tooltip="Artefactos",on_click=lambda _: page.go('/artefactos')),
                ft.IconButton(ft.icons.SETTINGS_ROUNDED,tooltip="Configuración", on_click=lambda _: page.go('/settings')),
                ft.IconButton(ft.icons.LOGIN_SHARP, tooltip="Acceso", on_click=lambda _: page.go('/login'))
            ]
        )

    return NavBar
