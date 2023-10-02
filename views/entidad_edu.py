import flet as ft
import pandas as pd

def EntidadView(page):    
    def exportar(e):
        #df = pd.read_csv("assets/provincias.csv")
        #df.to_clipboard (excel=True) 

        #df.to_excel("assets/provincias.xlxs")
        
        df = pd.read_csv("assets/localidades.csv")
        df.to_clipboard (excel=True)
        
        #df.to_excel("assets/localidades.xlxs")

        #df = pd.read_csv("assets/departamentos.csv")
        #df.to_excel("assets/departamentos.xlsx")
        
    mc= ft.Container(  ft.Stack(controls=
        [
            ft.Column (controls=    [          
                ft.TextField(
                    label="Institución",
                    hint_text="Nombre de la Institución",
                    border_color=ft.colors.GREY),
                ft.TextField(
                    label="C.U.E.",
                    hint_text="Código Único de Establecimiento",
                    border_color=ft.colors.GREY_100),
                ft.Dropdown(
                    label="Provincia",
                    hint_text="Ingresa la provincia",                    
                    options=[
                        ft.dropdown.Option("Corrientes"),
                        ft.dropdown.Option("Misiones"),
                    ],
                    autofocus = True),
                ft.Dropdown(
                        label ="Departamento",
                        hint_text= "Selecciona el Dpto",
                        options=[
                            ft.dropdown.Option("Santo Tome")
                        ],
                        autofocus=True                    
                    ),
                ft.ElevatedButton (
                    text="print CSV",on_click=exportar)
            ])
        ]),      
        width=500,
        height=700,  
        padding = 10,
        border_radius = 10        
        )
    
    return mc