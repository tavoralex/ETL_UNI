import requests

class Extract():
    def __init__(self):
        pass
    def extract_pnadc(self):
        url = "https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202601/variaveis/4096|12466?localidades=N3[29]&classificacao=2[all]"
        response = requests.get(url)
        data = response.json()
        return data