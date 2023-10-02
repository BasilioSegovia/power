
import flet as ft
import constants

def LoginView(page):
    mc = ft.Container(
        border_radius=10,
        padding=20,    
        margin=ft.margin.only(bottom=30),
        width=450,
        height=400,
        bgcolor=ft.colors.GREY,    
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,
                                    end=ft.alignment.bottom_center,
                                    colors=[ft.colors.GREY_900,ft.colors.WHITE]),
        content=ft.Column(controls=[
                ft.TextField(
                    label=constants.USER_LABEL ,                
                    width=400,    
                    bgcolor=ft.colors.WHITE,                
                    ),
                ft.TextField(
                    label=constants.USER_CLAVE,
                    password=True, 
                    can_reveal_password=True,
                    bgcolor=ft.colors.WHITE,
                    width=400,                
                    ),                        
                ft.Row(controls=
                    [ft.ElevatedButton(text=constants.BTN_ACEPTAR),
                    ft.ElevatedButton(text=constants.BTN_CANCELAR)
                    ],
                    alignment=ft.alignment.bottom_center),
                ft.Row(controls=
                    [ft.ElevatedButton(text="Registrarse",on_click=lambda _: page.go('/registrarse')) ],
                    alignment=ft.alignment.bottom_center)
                ],                
                spacing=40,
            ),
            )

    def aceptar():
        
        pass
    def cancelar():
        pass
    
    return mc