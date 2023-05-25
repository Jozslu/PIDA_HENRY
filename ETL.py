# importando las librería a utilizar
import pandas as pd
import numpy as np 

# Cargando el dataset.
df = pd.read_csv("AccidentesAviones.csv", index_col= 0, sep= ",", header= 0)
df.name = "df"

# Creando las funciones para normalizar los campos.
def normalizar_string(df= pd.DataFrame(),campo= str()):
    """
    Esta función normalizará el campo solicitado en el tipo "object" del dataframe.
    """
    df[campo] = df[campo].astype(str).replace('?', np.nan)

def normalizar_int(df= pd.DataFrame(),campo= str()):
    """
    Esta función normalizará el campo solicitado en el tipo "int" del dataframe.
    """
    df[campo] = df[campo].replace('?', np.nan).astype(float).astype('Int64')
    # Definir un rango límite para los valores válidos
    rango_min = df[campo].mean() - (2 * df[campo].std())
    rango_max = df[campo].mean() + (2 * df[campo].std())

    # Eliminar filas con valores fuera del rango
    df = df[(df[campo] >= rango_min) & (df[campo] <= rango_max)]

def normalizar_fecha(df= pd.DataFrame(),campo= str()):
    """
    Esta función normalizará en el formato fecha: "AAAA-mm-dd", del campo solicitado en el dataframe.
    """
    if (df.name == "df") & (campo == "fecha"):
        df['fecha'] = df['fecha'].replace('?', np.nan)
        df['fecha'] = pd.to_datetime(df['fecha'])
    
    elif (df.name == "df") & (campo == "HORA declarada"):
        df['HORA declarada'] = df['HORA declarada'].replace('?', np.nan)
        df['HORA declarada'].fillna('', inplace=True)
        df['HORA declarada'] = pd.to_datetime(df['HORA declarada'], errors='coerce')

# Normalizando con las funciones los campos del dataset.
normalizar_int(df,"all_aboard")
normalizar_int(df,"PASAJEROS A BORDO")
normalizar_int(df,"crew_aboard")
normalizar_int(df,"cantidad de fallecidos")
normalizar_int(df,"passenger_fatalities")
normalizar_int(df,"crew_fatalities")
normalizar_int(df,"ground")

normalizar_string(df,"Ruta")
normalizar_string(df,"OperadOR")
normalizar_string(df,"flight_no")
normalizar_string(df,"route")
normalizar_string(df,"ac_type")
normalizar_string(df,"registration")
normalizar_string(df,"cn_ln")
normalizar_string(df,"summary")

normalizar_fecha(df,"fecha")
normalizar_fecha(df,"HORA declarada")

# Exportamos a un dataset final de nombre "data_normalizada" para el EDA
df.to_csv("data_normalizada.csv", index= False)

# Seleccionamos solo las columnas con las que vamos a trabajar el análsis
columnas_deseadas = ["fecha", "cantidad de fallecidos", "all_aboard", "OperadOR", "Ruta", "PASAJEROS A BORDO"]
# Seleccionar las columnas deseadas
df_seleccionado = df[columnas_deseadas]
# Exportamos a un dataset final de nombre "data_final"para el análisis
df_seleccionado.to_csv("data_final.csv", index= False)

print("ACABAMOS EL ETL")
