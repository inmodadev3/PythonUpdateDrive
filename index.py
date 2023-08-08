import os
import shutil

def main():
    ruta_principal = 'C:/Users/venim/OneDrive/Documentos/INSUMOS MEDICOS'
    ruta_nueva_carpeta = 'C:/Users/venim/OneDrive/Documentos/nuevos_archivos'

    # Eliminar la carpeta de destino y su contenido antes de comenzar a copiar archivos
    if os.path.exists(ruta_nueva_carpeta):
        print("Existe")
        shutil.rmtree(ruta_nueva_carpeta)

    os.makedirs(ruta_nueva_carpeta, exist_ok=True)  # Crear la carpeta si no existe

    for ruta_actual, carpetas, archivos in os.walk(ruta_principal):
        ruta = ruta_actual.split('\\')
        subrutas = ruta[1:-1]
        subruta_despues_principal = '\\'.join(subrutas)
        nueva_carpeta = os.path.join(ruta_nueva_carpeta, subruta_despues_principal)
        os.makedirs(nueva_carpeta, exist_ok=True)  # Crear la carpeta si no existe
        for archivo in archivos:
            archivo_origen = os.path.join(ruta_actual, archivo)
            archivo_destino = os.path.join(nueva_carpeta, archivo)
            shutil.copy(archivo_origen, archivo_destino)

    print("Finalizo")

if __name__ == "__main__":
    main()
