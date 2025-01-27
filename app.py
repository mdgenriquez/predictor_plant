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

if data is not None:
    # Validar columnas necesarias
    if "SMILES" not in data.columns or "Name" not in data.columns:
        st.error("El archivo CSV debe contener las columnas 'SMILES' y 'Name'.")
    else:
        st.title("Predictor plant")     
