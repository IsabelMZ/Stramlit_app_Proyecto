import pandas as pd
import streamlit as st
import numpy as np
st.title('Datos positivos Covid-19')
st.write('Esta es una web donde podrá visualizar casos positvos de covid-19 por ubicación, sexo, edad, etc.')

#dataset_link = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'

###Hay que obtener la data de un link

#df = pd.read_csv(dataset_link, header=None) ###Lee el dataframe respectivo

df = pd.read_csv(r'C:/Users/Enzo/Desktop/data_completa.csv',sep=";", skip_blank_lines=True, date_parser=True)

from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

diccionario = {}
lista = np.linspace(1,100,100)
for e in lista:
    diccionario[e] = df[df['EDAD'] == e].shape[0]

ejex = lista.tolist()
ejey = list(diccionario.values())
b = (
   Bar()
    .add_xaxis(ejex)
    .add_yaxis(
        "Edades y tipo de prueba aplicada", ejey
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Datos", subtitle="Edades"
        )#,
        #toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)
