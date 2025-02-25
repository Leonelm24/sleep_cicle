import seaborn as sns
import matplotlib.pyplot as plt

def histograma_sueño(df):
    """Histograma de las horas totales de sueño"""
    sns.histplot(df["Total Sleep Hours"], bins=30)
    plt.title("Distribución de Horas de Sueño")
    plt.xlabel("Horas de sueño")
    plt.ylabel("Frecuencia")
    plt.show()

def relacion_sueño_productividad(df):
    """Diagrama de dispersión entre horas de sueño y productividad"""
    sns.scatterplot(x=df["Total Sleep Hours"], y=df["Productivity Score"])
    plt.title("Relación entre Horas de Sueño y Productividad")
    plt.xlabel("Horas de Sueño")
    plt.ylabel("Productivity Score")
    plt.show()

def impacto_cafe_productividad(df):
    """Gráfico de barras para el impacto de la cafeína en la productividad"""
    sns.boxplot(x=df["Caffeine Intake (mg)"], y=df["Productivity Score"])
    plt.title("Impacto del Consumo de Cafeína en la Productividad")
    plt.xlabel("Caffeine Intake (mg)")
    plt.ylabel("Productivity Score")
    plt.xticks(rotation=45)
    plt.show()


