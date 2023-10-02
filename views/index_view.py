
import flet as ft
import constants

def IndexView(page):
    
    content = ft.Column(               
            [
                ft.Row ([
                    ft.Text(
                        constants.PROYECT_TITLE,
                        size=50)
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row ([
                    ft.Text(
                        constants.PROYECT_DESC,
                        size=30)
                ], 
                alignment=ft.MainAxisAlignment.CENTER
                )
            ]
    )
    return content

