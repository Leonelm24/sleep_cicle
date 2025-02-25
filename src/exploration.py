import pandas as pd


def describir_dataset(df):
    print(f"\n📌 Este DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.\n")

    print("🔍 Valores nulos por columna:")
    print(df.isna().sum())

    print("\n📊 Tipos de datos en cada columna:")
    print(df.dtypes)

    print("\n📈 Cantidad de valores únicos por columna:")
    print(df.nunique())

    print("\n📉 Estadísticas descriptivas:")
    print(df.describe())


# Cargar el dataset
df = pd.read_csv("C:\\py\\ciclo_sueno\\data\\sleep_cycle_productivity.csv")

# Exploración inicial
describir_dataset(df)
