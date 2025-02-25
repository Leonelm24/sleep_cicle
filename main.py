import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

import src.exploration as exp
import src.transformation as trs
import src.visualization as viz

if __name__ == "__main__":
    # Cargar el dataset
    df = pd.read_csv("C:\\py\\ciclo_sueno\\data\\sleep_cycle_productivity.csv")

    # Exploración inicial
    exp.describir_dataset(df)

    # Aplicar transformaciones
    df_1 = trs.aplicar_transformaciones(df)

    # Generar visualizaciones
    viz.histograma_sueño(df_1)
    viz.relacion_sueño_productividad(df_1)
    viz.impacto_cafe_productividad(df_1)

    # Guardar el dataset transformado
    df_1.to_csv("sleep_cycle_productivity_transformed.csv", index=False)

    print("\n✅ ¡Pipeline completado! El archivo transformado ha sido guardado.")
