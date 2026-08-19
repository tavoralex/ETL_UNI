import requests

class Extract():
    def __init__(self):
        pass
    
    def extract_pnadc(self, variaveis, cod_estado, sexo):
        url = f'https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201|201202|201203|201204|201301|201302|201303|201304/variaveis/{variaveis}?localidades=N3[{cod_estado}]&classificacao=2[{sexo}]'
        response = requests.get(url)
        data = response.json()
        
        return data
