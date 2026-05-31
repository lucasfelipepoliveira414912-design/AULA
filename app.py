import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker('pt_BR')

n = 50000

produtos = [
    "Notebook Dell",
    "Mouse Logitech",
    "Monitor LG",
    "SSD Kingston",
    "Teclado Mecânico",
    "Headset HyperX"
]

df = pd.DataFrame({
    "venda_id": np.arange(1, n + 1),
    "cliente": [fake.name() for _ in range(n)],
    "cidade": [fake.city() for _ in range(n)],
    "produto": np.random.choice(produtos, n),
    "quantidade": np.random.randint(1, 6, n),
    "valor_unitario": np.random.uniform(50, 5000, n).round(2)
})

df["valor_total"] = (df["quantidade"] * df["valor_unitario"]).round(2)

st.title("Dashboard de Vendas")

st.dataframe(df.head())# AULA