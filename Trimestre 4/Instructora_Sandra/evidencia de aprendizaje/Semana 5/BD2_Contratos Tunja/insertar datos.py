import pandas as pd
import re

def clean_string(text):
    """Limpia strings para SQL eliminando caracteres problemáticos"""
    if pd.isna(text):
        return 'NULL'
    text = str(text)
    text = text.replace("'", "''")  # Escapar comillas simples
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Eliminar caracteres no ASCII
    return f"'{text.strip()}'"

def generate_sql_inserts(csv_file, num_rows=8943):
    # Leer el archivo CSV
    df = pd.read_csv(csv_file)
    
    # Limitar a las primeras num_rows filas
    df = df.head(num_rows)
    
    sql_script = []
    
    # 1. Insertar datos en Entidades
    entidades = {}
    for _, row in df.iterrows():
        nit = clean_string(row['Nit Entidad'])
        nombre = clean_string(row['Nombre Entidad'])
        
        if nit not in entidades:
            entidades[nit] = nombre
            sql_script.append(f"INSERT INTO Entidades (nombre, nit, tipo_entidad) VALUES ({nombre}, {nit}, 'Municipio');")
    
    # 2. Insertar datos en Proveedores
    proveedores = {}
    for _, row in df.iterrows():
        doc_proveedor = clean_string(row['Documento Proveedor'])
        nombre_proveedor = clean_string(row['Proveedor Adjudicado'])
        tipo_doc = clean_string(row['TipoDocProveedor'])
        
        if doc_proveedor != 'NULL' and doc_proveedor not in proveedores:
            tipo_proveedor = "'PYME'" if row['Es Pyme'] == 'Si' else "'No PYME'"
            proveedores[doc_proveedor] = nombre_proveedor
            sql_script.append(f"INSERT INTO Proveedores (nombre, nit, tipo_proveedor) VALUES ({nombre_proveedor}, {doc_proveedor}, {tipo_proveedor});")
    
    # 3. Insertar datos en Procesos
    procesos = {}
    for _, row in df.iterrows():
        codigo_proceso = clean_string(row['Proceso de Compra'])
        if codigo_proceso not in procesos:
            nit_entidad = clean_string(row['Nit Entidad'])
            objeto = clean_string(row['Descripcion del Proceso'])
            fecha = clean_string(row['Fecha de Firma'])
            estado = clean_string(row['Estado Contrato'])
            
            # Obtener ID de entidad
            sql_script.append(f"INSERT INTO Procesos (codigo_proceso, objeto, id_entidad, fecha_apertura, estado_proceso) VALUES ({codigo_proceso}, {objeto}, (SELECT id_entidad FROM Entidades WHERE nit = {nit_entidad}), {fecha}, {estado});")
            procesos[codigo_proceso] = True
    
    # 4. Insertar datos en Contratos
    for _, row in df.iterrows():
        num_contrato = clean_string(row['Referencia del Contrato'])
        codigo_proceso = clean_string(row['Proceso de Compra'])
        doc_proveedor = clean_string(row['Documento Proveedor'])
        objeto = clean_string(row['Descripcion del Proceso'])
        fecha_firma = clean_string(row['Fecha de Firma'])
        valor = row['Valor del Contrato'] if not pd.isna(row['Valor del Contrato']) else 'NULL'
        estado = clean_string(row['Estado Contrato'])
        
        if doc_proveedor != 'NULL':
            sql_script.append(f"INSERT INTO Contratos (numero_contrato, id_proceso, id_proveedor, objeto, fecha_firma, valor_contrato, estado_contrato) VALUES ({num_contrato}, (SELECT id_proceso FROM Procesos WHERE codigo_proceso = {codigo_proceso}), (SELECT id_proveedor FROM Proveedores WHERE nit = {doc_proveedor}), {objeto}, {fecha_firma}, {valor}, {estado});")
    
    return '\n'.join(sql_script)

# Uso del script
csv_file = './BD2_Contratos Tunja/BD2.csv'
sql_output = generate_sql_inserts(csv_file, num_rows=8943)

# Guardar en un archivo SQL
with open('./BD2_Contratos Tunja/insert_data.sql', 'w', encoding='utf-8') as f:
    f.write(sql_output)

print("Script SQL generado con éxito en 'insert_data.sql'")