import pandas as pd

directory="outputcsv/"
df = pd.read_csv('database.csv', delimiter=',', header=0)

# convertir la columna FECHA a formato datetime y ordenar el dataframe
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
df = df.sort_values("fecha")

# Obtener la fecha más reciente en el dataframe
latest_date = df['fecha'].max()

# Obtener el primer día del último mes
thirty_days_ago = latest_date - pd.Timedelta(days=6)

# Filtrar los datos para que solo incluyan los de los últimos 30 días
last_30_days_data = df[df['fecha'] >= thirty_days_ago]
last_30_days_data = last_30_days_data.sort_values("fecha")

last_30_days_data[['Nombre']] = last_30_days_data[['Nombre']].replace('_', ' ', regex=True)
# Obtener la lista de estaciones disponibles en el dataframe
estaciones = last_30_days_data["Nombre"].unique()

data=last_30_days_data.groupby(['Nombre'])
 
for estacion in estaciones:
    # Filtrar los datos para la estación actual
    data_estacion=data.get_group(estacion)
    data_estacion = data_estacion.dropna(axis=1, how='all')
    #data_estacion = data_estacion.drop(labels=['Unnamed: 0'], axis=1)
    data_estacion = data_estacion.iloc[:, 1:]
    data_estacion = data_estacion.reset_index(drop=True)
    data_estacion.index += 1
    data_estacion=data_estacion.rename_axis("No.")
    data_estacion.to_csv(f"{directory}{estacion}.csv")
