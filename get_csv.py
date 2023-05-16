import os
from pysus.online_data import SINAN, parquets_to_dataframe

def gen_csv(disease, year):
    if not os.path.exists(f"./databases/{disease}/{disease}-{year}.csv"):
        df = parquets_to_dataframe(SINAN.download(disease, year))
        df.to_csv(f"./databases/{disease}/{disease}-{year}.csv", index = False)

for disease in SINAN.list_diseases():

    if disease != "Dengue":
        for year in (2019,2020,2021,2022):
            try:
                print(f"Gerando CSV - {disease}-{year}...")
                gen_csv(disease, year)
            except:
                print(f"Erro ao tentar baixar {disease}")


