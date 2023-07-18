#%%
from faker import Faker
import pandas as pd
import random
from pyUFbr.baseuf import ufbr
import os

# %%
fake = Faker('pt_BR')
df = pd.DataFrame(
    columns=[
        'nome',
        'placa',
        'total_multas',
        'genero',
        'endereco',
        'cidade',
        'estado',
        'ultima_multa'
    ]
)

for _ in range(1000):    
    estado = random.choice(ufbr.list_uf)
    cidade = random.choice(ufbr.list_cidades(estado))
    genero = random.choice(["Homem", "Mulher", "Não binário"])
    name = fake.name_male() if genero == "Homem" else fake.name_female()
    df.loc[df.shape[0]] = [
        name,
        fake.license_plate(),
        random.randint(0,100),
        genero,
        fake.street_address(),
        cidade,
        estado,
        fake.date_this_decade()
    ]


# %%
df.to_csv("multas.csv", index=False)
# %%
df['PARTITION'] = df['estado']
column_values = df['PARTITION'].unique()

for value in column_values:
    value_df = df[df['PARTITION'] == value]
    
    folder_name = f"multas_partitioned/state={value}" 

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    print(f"estado_partitioned/state={value}.csv")
    value_df.to_csv(f"{folder_name}/{value}.csv", index=False, sep=";")
# %%
