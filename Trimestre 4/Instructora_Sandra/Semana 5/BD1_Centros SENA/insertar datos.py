# Cargar nuevamente el nuevo archivo CSV proporcionado
import pandas as pd


csv_path = "./BD1_Centros SENA/BD1.csv"
df = pd.read_csv(csv_path)

# Asegurar los tipos correctos de datos para columnas clave
df['CENTRO_FORMACION'] = df['CENTRO_FORMACION'].astype(str)
df['NOMBRE_REGIONAL'] = df['NOMBRE_REGIONAL'].astype(str)
df['CODIGO_REGIONAL'] = df['CODIGO_REGIONAL'].astype(str)
df['NOMBRE_DEPARTAMENTO'] = df['NOMBRE_DEPARTAMENTO'].astype(str)
df['NOMBRE_MUNICIPIO'] = df['NOMBRE_MUNICIPIO'].astype(str)

# Generar los comandos INSERT INTO con geometría POINT (PostgreSQL/PostGIS)
insert_statements = []

for _, row in df.iterrows():
    values = (
        row['CENTRO_FORMACION'].replace("'", "''"),
        int(row['CODIGO_CENTRO']),
        float(row['LATITUD']),
        float(row['LONGITUD']),
        row['NOMBRE_REGIONAL'].replace("'", "''"),
        row['CODIGO_REGIONAL'].replace("'", "''"),
        row['NOMBRE_DEPARTAMENTO'].replace("'", "''"),
        int(row['CODIGO_DEPARTAMENTO']),
        row['NOMBRE_MUNICIPIO'].replace("'", "''"),
        int(row['CODIGO_MUNICIPIO'])
    )
    
    insert_sql = f"""INSERT INTO centros_formacion_sena (
        centro_formacion, codigo_centro, latitud, longitud, 
        nombre_regional, codigo_regional, nombre_departamento, 
        codigo_departamento, nombre_municipio, codigo_municipio
    ) VALUES (
        '{values[0]}', {values[1]}, {values[2]}, {values[3]}, 
        '{values[4]}', '{values[5]}', '{values[6]}', 
        {values[7]}, '{values[8]}', {values[9]}
    );"""
    
    insert_statements.append(insert_sql)

# Guardar los comandos en un archivo .sql
sql_output_path = "./BD1_Centros SENA/insertar_datos.sql"
with open(sql_output_path, "w", encoding="utf-8") as f:
    for stmt in insert_statements:
        f.write(stmt + "\n")

sql_output_path
