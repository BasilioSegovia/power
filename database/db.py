import sqlite3
import database.constants as k

def crearTablas():    
    try:
        cn = sqlite3.connect(k.DB)
        cursor = cn.cursor()
        cursor.execute(k.CREATE_TBL_ARTEFACTOS) 
        cn.commit() 

        cursor.execute(k.CREATE_TBL_ENT_EDU) 
        cn.commit() 

        cursor.execute(k.CREATE_TBL_PROVINCIA) 
        cn.commit() 

        cursor.execute(k.CREATE_TBL_DPTO) 
        cn.commit() 

        cursor.execute(k.CREATE_TBL_LOCALIDAD) 
        cn.commit() 
    except Exception as e:
        print (e)

    try:
        cn  = sqlite3.connect(k.DB)
        cursor = cn.cursor()
        cursor.execute(f"select * from {k.TBL_ARTEFACTOS}")
        datos = cursor.fetchall()
        
        keys = [k.F_ARTEFACTOS_ID,k.F_ARTEFACTOS_ARTEFACTO,k.F_ARTEFACTOS_WATTS,k.F_ARTEFACTOS_IMG_NAME]    
        rs= [dict(zip(keys,value)) for value in datos]
        
        return rs
    
    except Exception as e:
        print (e)


