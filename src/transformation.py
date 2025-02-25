import pandas as pd

def transformar_dataset(df):
    df["Date"] = pd.to_datetime(df["Date"])

    # Convertir 'Sleep Start Time' y 'Sleep End Time' a formato de hora
    df["Sleep Start Time"] = pd.to_datetime(df["Sleep Start Time"]).dt.time
    df["Sleep End Time"] = pd.to_datetime(df["Sleep End Time"]).dt.time

    # Codificar 'Gender' en valores numéricos
    df["Gender_num"] = df["Gender"].map({"Male": 0, "Female": 1})

    # Rellenar valores nulos con la media en variables numéricas
    df.fillna(df.mean(numeric_only=True), inplace=True)

    return df


def clasificar_edad(df):
    """Clasifica la edad en grupos: Niño, Adolescente, Adulto, Mayor"""
    df["Age Group"] = pd.cut(df["Age"],
                             bins=[0, 12, 18, 60, 100],
                             labels=["Niño", "Adolescente", "Adulto", "Mayor"])
    return df


def categorizar_productividad(df):
    """Crea una columna con niveles de productividad"""
    df["Productivity Level"] = pd.cut(df["Productivity Score"],
                                      bins=[0, 40, 70, 100],
                                      labels=["Baja", "Media", "Alta"])
    return df


def categorizar_horario_sueño(df):
    """Clasifica el horario de inicio del sueño en momentos del día"""
    df["Sleep Start Hour"] = pd.to_datetime(df["Sleep Start Time"], errors='coerce').dt.hour
    df["Sleep Category"] = pd.cut(df["Sleep Start Hour"],
                                  bins=[0, 4, 9, 21, 24],
                                  labels=["Madrugada", "Mañana", "Noche", "Madrugada"],
                                  right=False)
    return df


def categorizar_estres(df):
    """Crea una columna que agrupa niveles de estrés"""
    df["Stress Category"] = pd.cut(df["Stress Level"],
                                   bins=[0, 3, 6, 10],
                                   labels=["Bajo", "Medio", "Alto"])
    return df


def categorizar_calidad_sueño(df):
    """Clasifica la calidad del sueño en Baja, Media y Alta"""
    df["Sleep Quality Level"] = pd.cut(df["Sleep Quality"],
                                       bins=[0, 3, 6, 10],
                                       labels=["Baja", "Media", "Alta"])
    return df


def categorizar_cafeina(df):
    """Clasifica la ingesta de cafeína en niveles"""
    df["Caffeine Level"] = pd.cut(df["Caffeine Intake (mg)"],
                                  bins=[0, 100, 250, 1000],
                                  labels=["Bajo", "Medio", "Alto"])
    return df


def calcular_balance_trabajo_sueño(df):
    """Crea una métrica que compara horas de sueño vs. horas de trabajo"""
    df["Work-Sleep Ratio"] = df["Work Hours (hrs/day)"] / df
