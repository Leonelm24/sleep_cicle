def describe_df (df):
    print(f"Este dataset tiene: {df.shape[0]} filas y {df.shape[1]} columnas")
    print(f"Tiene un total de: {df.isna().sum().values.sum()} valores nulos")