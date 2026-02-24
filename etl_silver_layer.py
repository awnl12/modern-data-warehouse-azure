import pandas as pd
import hashlib
import datetime
import os



ruta = 'DATA/Telco-Customer-Churn.csv'

def cargar_datos(ruta):
    try:
        df = pd.read_csv(ruta)
        print("Datos cargados exitosamente.")
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def transformar_datos(df):
    #Limpia, estandariza y anominiza los datos, luego los guarda en formato Parquet
    #Capa Silver: Transformación de datos para análisis y modelado


    try:
        #Eliminar Duplicados
        df = df.drop_duplicates(subset='customerID', keep='first')

        #Inicio del proceso de transformación de datos
        print("Iniciando proceso de transformación de datos...")

        #Estandarizaciando nombre de todas las columnas a minúscula
        df.columns = df.columns.str.lower()

        #Reemplazando espacios en blanco por guiones bajos en los nombres de las columnas
        df.columns = df.columns.str.replace(' ', '_')

        #Estandarizando columna totalcharges a tipo numérico, eliminando espacios en blanco y convirtiendo a NaN los valores no convertibles
        df['totalcharges'] = df['totalcharges'].str.strip()
        df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
        df['totalcharges'] = df['totalcharges'].fillna(0)

        #Estaderizando columna churn
        df['churn'] = df['churn'].str.strip().str.lower()
        df['churn'] = df['churn'].map({'yes': 1, 'no': 0})

        #Enmascarando id cliente
        def enmascarar_columna(campo):
            return hashlib.sha256(str(campo).encode('utf-8')).hexdigest()
        df['customerid'] = df['customerid'].apply(enmascarar_columna)

        #Transformaacion formato parquet
        fecha = datetime.date.today()
        df.to_parquet(f'DATA/Telco-Customer-Churn-cleaned-{fecha}.parquet', index=False)
        print("Proceso de transformación de datos finalizado. Archivo guardado en formato Parquet.")
    
    except Exception as e:
        print(f"Error durante la transformación de datos: {e}")
        return None
    
    return df

if __name__ == "__main__":
    df_crudo = cargar_datos(ruta)
    if df_crudo is not None:
        df_limpio = transformar_datos(df_crudo)

    usuario = os.environ.get("USERNAME")
    fecha = datetime.date.today()
    print(f"Proceso de ETL finalizado por el usuario: {usuario} en la fecha: {fecha}")


    print("Proceso de ETL finalizado exitosamente.")
    print(df_limpio.head(10))
    print("Información del DataFrame limpio:")
    print(df_limpio.info())
