def caso_who(ruta_archivo_csv: str)-> dict:
    import pandas as pd
    import numpy as np
    try:
        if (ruta_archivo_csv[-4: -1] + ruta_archivo_csv[-1]) == '.csv':
            df = pd.read_csv(ruta_archivo_csv)
            df['date'] = df['date'].astype('datetime64[ns]')
            df['razon'] = ((df['total_cases_per_million'] * df['population']) / 10 ** 6) / ((df['hospital_beds_per_thousand'] * df['population']) / 10 ** 3)
            df2 = df.groupby(['date', 'continent'])['razon'].mean().unstack()
            df2.round(decimals = 15)
            resultado = df2.to_dict()
        else:
            resultado = 'Extensión inválida.'
        return resultado
    except:
        return 'Error al leer el archivo de datos.'

print(caso_who("https://raw.githubusercontent.com/tikuro/Covid/main/owid-covid-data.csv"))