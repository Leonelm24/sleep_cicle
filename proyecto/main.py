import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

import src.exploration as exp
import src.transformation as trs
import src.visualization as viz

# https://realpython.com/if-name-main-python/
if __name__ == "__main__":

    df = sns.load_dataset("titanic")
    exp.describe_df(df)

    df_1 = trs.edad(df)
    df_2 = trs.sex_encoding(df_1)

    viz.plot_sex_survival(df_2)
    viz.plot_class_age(df_2)