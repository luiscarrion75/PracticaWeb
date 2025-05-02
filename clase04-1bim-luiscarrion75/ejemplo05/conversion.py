import pandas as pd
import json

# Paso 1: Leer el CSV con la codificación adecuada
try:
    df = pd.read_csv('atp_tennis.csv', encoding='utf-8')
except UnicodeDecodeError:
    print("Error con UTF-8, intentando con latin1")
    df = pd.read_csv('atp_tennis.csv', encoding='latin1')

# Paso 2: Convertir DataFrame a lista de diccionarios
registros = df.to_dict(orient='records')

# Paso 3: Crear estructura con clave "docs"
estructura_json = {"docs": registros}

# Paso 4: Guardar a un archivo JSON con formato legible
with open('atp_tennis.json', 'w', encoding='utf-8') as f:
    json.dump(estructura_json, f, indent=4, ensure_ascii=False)

print("JSON generado con la estructura 'docs'.")
