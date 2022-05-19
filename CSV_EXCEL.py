import json

import pandas as pd


with open('datapreliminar.json') as file:
    data = json.load(file)

df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
print("Decoded JSON Data From File")
for key, value in data.items():
    print(key, ":", value)
    dispositivo = key
    for key,value in value.items():
        df=df.append({'Dispositivo' : dispositivo, 'Captura' : key } , ignore_index=True)
        df2=df2.append(value , ignore_index=True)
        df3 = pd.concat([df,df2],axis=1)
        print(key, ":", value)
        print("CEL")
    print("TIPO CEL")

df3.to_csv ('prueba.csv', index = None)