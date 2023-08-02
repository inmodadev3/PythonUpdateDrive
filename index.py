import os
import shutil
from Conexion import conectar

def main():

    #VARIABLES
    query = 'SELECT strIdProducto,intPrecio1,strDescripcion FROM tblProductos'
    ruta_principal = 'C:/Users/venim/OneDrive/Documentos/INSUMOS MEDICOS'
    ruta_nueva_carpeta ='C:/Users/venim/OneDrive/Documentos/nuevos_archivos'

    #CONEXION A LA BASE DE DATOS
    connection = conectar()
    cursor = connection.cursor()
    ## REALIZAR LA CONSULTA DELA BASE DE DATOS
    cursor.execute(query)
    rows = cursor.fetchall()
    ### Crear un diccionario de precios a partir de los resultados de la base de datos
    precios_dict = {row[0]: int(row[1]) for row in rows}
    
    os.makedirs(ruta_nueva_carpeta, exist_ok=True)  # Crear la carpeta si no existe
    shutil.rmtree(ruta_nueva_carpeta) #Eliminar Registros de la carpeta



    for ruta_actual, carpetas, archivos in os.walk(ruta_principal):
        ruta = ruta_actual.split('\\')
        ultimo_elemento = ruta[-1]
        precio = precios_dict.get(ultimo_elemento)
          # Obtener el precio del diccionario
        if precio is not None:
            subrutas = ruta[1:-1]
            subruta_despues_principal = os.path.join(*subrutas)
            nueva_carpeta = os.path.join(ruta_nueva_carpeta, subruta_despues_principal, f'{ultimo_elemento}_{precio}$')
            os.makedirs(nueva_carpeta, exist_ok=True)  # Crear la carpeta si no existe
            for archivo in archivos:
                archivo_origen = os.path.join(ruta_actual, archivo)
                archivo_destino = os.path.join(nueva_carpeta, archivo)
                shutil.copy(archivo_origen, archivo_destino)
                
            
            
    print("Finalizo")
    connection.close()

if __name__ == "__main__":
    main()
