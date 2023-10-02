import flet as ft
import constants
import database.constants as k
import sqlite3

cards = []
totales=[]

def CalculoView(page):
   
    #Datos
    cn  = sqlite3.connect(k.DB)
    cursor = cn.cursor()
    cursor.execute(f"select * from {k.TBL_ARTEFACTOS}")
    datos = cursor.fetchall()    
    keys = [k.F_ARTEFACTOS_ID,k.F_ARTEFACTOS_ARTEFACTO,k.F_ARTEFACTOS_WATTS,k.F_ARTEFACTOS_IMG_NAME]    
    rs= [dict(zip(keys,value)) for value in datos]
 
    for value in rs:
        card=MyCard(
            value[k.F_ARTEFACTOS_ID],
            f"assets/artefactos/{value[k.F_ARTEFACTOS_IMG_NAME]}",
            value[k.F_ARTEFACTOS_ARTEFACTO],
            value[k.F_ARTEFACTOS_WATTS]
        )
        cards.append(card)

    #Marco
    resultado = Resultado()

    gridCard = ft.GridView(
        controls=cards,
        expand=1,
        runs_count=5,
        child_aspect_ratio=1.77,
        max_extent=500,
        spacing=5,
        run_spacing=5,        
    )
    
    mc =ft.Column([
            ft.Row([resultado]),
            
            ft.Container(        
                content=gridCard,        
                border_radius=5,
            )
        ])
  
    return mc

class MyCard(ft.UserControl):
    def __init__(self, idCard,img,title,watts):
        super().__init__()

        self.txtcant=ft.TextField(label="Cant", width=60, height=40, value=1,color="black")
        self.horas = ft.TextField(label="Horas",width= 60,height=40,value=1,color="black")
        self.txtResult =ft.Text(value="0", size=20)
        self.btnCalcular = ft.TextButton (text=constants.BTN_CALCULAR,on_click=self.calcular)
        self.title = title
        self.subtitle = f"Consumo: {watts}"
        self.idCard = idCard
        self.img = img
        self.watts = watts

    def build(self):        
        c= ft.Card(
            content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text(self.title,color="black"),
                        subtitle=ft.Text(self.subtitle,color="balck"),
                    ),                    
                    ft.Row([
                        ft.Column([
                            ft.Image(
                            src=self.img,
                            width=250,
                            height=100,                            
                            fit=ft.ImageFit.CONTAIN,
                            ),
                        ft.Row(
                            [
                                ft.Container( 
                                    self.txtResult,
                                    border_radius=8,
                                    bgcolor=ft.colors.GREY_800,padding=5),
                            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            )  
                        ]),
                        ft.Column([
                            ft.Row([self.txtcant]),
                            ft.Row([self.horas]),
                            ft.Row([self.btnCalcular])
                        ])
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  
                    ),
                    
                ],
                ),        
            padding=5,
            bgcolor=ft.colors.GREY,
            border_radius=8
            )
        )
        return c 
    
    def calcular(self,e):
        consumo = 0.0
        cant = float(self.txtcant.value)
        horas = float(self.horas.value)
        wt   = self.watts

        consumo =  cant * wt * horas

        self.txtResult.value = f"Consumo: {consumo} watts/hs"
        totales.append(consumo)
        self.update()            
        
class Resultado(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.msj = ft.Text(value="")
        self.txtRes = ft.Text("Total Consumido")
        self.dlg = ft.AlertDialog(title=self.msj,open=False)
        
    def build(self):
        mc = ft.Row(controls=
            [
                self.txtRes,            
                ft.IconButton(ft.icons.ADD,on_click=self.saludar),               
                self.dlg
            ]
        )        
        return  mc
    
    def saludar(self,e):
        consumo=sum(totales)
        self.txtRes.value= "Mi Consumo: {}".format(consumo)
        self.msj.value= f"Total consumo: {consumo} watts/hr"
        self.dlg.open = True        
        self.update()
