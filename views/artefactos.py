import flet as ft
import database.constants as k
import sqlite3


def ArtefactosView(page):
    cn = sqlite3.connect(k.DB)
    cursor = cn.cursor()

    cursor.execute(f"select * from {k.TBL_ARTEFACTOS}")
    datos=cursor.fetchall()

    if not datos=="":
        keys = [k.F_ARTEFACTOS_ID,k.F_ARTEFACTOS_ARTEFACTO,k.F_ARTEFACTOS_WATTS]
        results = [dict(zip(keys,value)) for value in datos]
        

    body  = ft.Stack(
        controls=[ft.TextButton(
            text = results
        )]
    )
    return body

 