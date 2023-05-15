
import pandas as pd

directory="outputtex/"

df = pd.read_csv('database.csv', delimiter=',', header=0)
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
df = df.sort_values("fecha")

df[['Nombre']] = df[['Nombre']].replace('_', ' ', regex=True)
estaciones = df["Nombre"].unique()
data=df.groupby(['Nombre'])

for estacion in estaciones:
        data_estacion=data.get_group(estacion)
        data_estacion = data_estacion.dropna(axis=1, how='all')
        data_estacion = data_estacion.drop(labels=['estacion'], axis=1)
        data_estacion = data_estacion.iloc[:, 1:]
        data_estacion = data_estacion.reset_index(drop=True)
        data_estacion.index += 1
        data_estacion=data_estacion.rename_axis("No.")
        data_estacion=data_estacion.to_latex()
        tex = '''

        \\documentclass[12pt]{article}
        \\usepackage{booktabs}
        \\usepackage{graphicx}
        \\usepackage[a3paper, margin=2cm , landscape]{geometry}

        \\usepackage{eso-pic}
        \\usepackage[ddmmyyyy]{datetime}
        \\newcommand\BackgroundPic{\\put(0,0){\\parbox[b][\\paperheight]{\\paperwidth}{\\vfill\centering\includegraphics[width=\\paperwidth,height=\\paperheight,keepaspectratio]{logo.pdf}\\vfill}}}
        
        \\title{DATOS CLIMÁTICOS DE LA ESTACIÓN '''+estacion+'''\\\\
        \\LARGE{Sección de Climatología}\\\\
        \\LARGE{Departamento de Investigación y Servicios Meteorológicos}}
        \\date{PDF generado el \\today}
        
        
        \\begin{document} 
        \\AddToShipoutPicture*{\BackgroundPic}
        \\maketitle
        \\begin{center}
       '''+data_estacion+'''
        
        \\end{center}
        \\end{document}
        '''
    
    # Imprimir el código HTML

        with open(f'{directory}{estacion}.tex', 'w') as f:
            f.write(tex)







