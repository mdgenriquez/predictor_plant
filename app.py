import streamlit as st
import pandas as pd

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"Error al cargar el archivo CSV: {e}")
        return None

csv_path = "base_datos_plant_smile.csv"  # Nombre del archivo
data = load_data(csv_path)
