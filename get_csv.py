import os
from pysus.online_data import SINAN, parquets_to_dataframe

def gen_csv(disease, year):

    if not os.path.exists(f"./databases/{disease}/{disease}-{year}.csv"):

        df = parquets_to_dataframe(SINAN.download(disease, year))
        df.to_csv(f"./databases/{disease}/{disease}-{year}.csv", index = False)

list_diseases = SINAN.list_diseases()
list_diseases.remove("Dengue")

for disease in list_diseases:
    for year in SINAN.get_available_years(disease):
        try:
            print(f"Gerando CSV - {disease}-{year}...")
            gen_csv(disease, year)
        except:
            print(f"Erro ao tentar baixar {disease}")

