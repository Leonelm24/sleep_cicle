import seaborn as sns
import matplotlib.pyplot as plt

def plot_class_age (df):
    sns.boxplot(x="pclass", y="age", data=df)
    plt.title("Clase según edad")
    plt.savefig("edadyclase.png")

def plot_sex_survival (df):
    sns.countplot(x="sex", hue="survived", data=df)
    plt.title("Superviviencia")
    plt.savefig("supervivencia.png")