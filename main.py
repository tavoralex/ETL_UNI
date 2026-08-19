import requests

url='https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201|201202|201203|201204|201301|201302|201303|201304/variaveis/4099?localidades=N3[26]&classificacao=2[all]'
response=requests.get(url)
data=response.json()

print(data)


#from src.extract import Extract
#
#extract=Extract()
#pnadc=extract.extract_pnadc()

from src.extract import Extract
from src.load import Load

extract=Extract()
pnadc=extract.extract_pnadc(variaveis='4099', cod_estado='29', sexo='5')
load=Load()
load.load_json('bahia', pnadc)

#Variáveis:
#1641- Pessoas de 14 anos ou mais de idade
#4087- Coeficiente de variação - Pessoas de 14 anos ou mais de idade
#4104- Distribuição percentual das pessoas de 14 anos ou mais de idade
#4105- Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade
#4088- Pessoas de 14 anos ou mais de idade, na força de trabalho, na semana de referência
#4089- Coeficiente de variação - Pessoas de 14 anos ou mais de idade, na força de trabalho, na semana de referência
#4106- Distribuição percentual das pessoas de 14 anos ou mais de idade, na força de trabalho, na semana de referência
#4107- Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade, na força de trabalho, na semana de referência
#4090- Pessoas de 14 anos ou mais de idade ocupadas na semana de referência
#4091- Coeficiente de variação - Pessoas de 14 anos ou mais de idade ocupadas na semana de referência
#4108- Distribuição percentual das pessoas de 14 anos ou mais de idade ocupadas na semana de referência
#4109- Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade ocupadas na semana de referência
#4092- Pessoas de 14 anos ou mais de idade, desocupadas na semana de referência
#4093- Coeficiente de variação - Pessoas de 14 anos ou mais de idade, desocupadas na semana de referência
#4110- Distribuição percentual das pessoas de 14 anos ou mais de idade, desocupadas na semana de referência
#4111- Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade, desocupadas na semana de referência
#4094- Pessoas de 14 anos ou mais de idade, fora da força de trabalho, na semana de referência
#4095- Coeficiente de variação - Pessoas de 14 anos ou mais de idade, fora da força de trabalho, na semana de referência
#4112- Distribuição percentual das pessoas de 14 anos ou mais de idade, fora da força de trabalho, na semana de referência
#4113- Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade, fora da força de trabalho, na semana de referência
#4096- Taxa de participação na força de trabalho, na semana de referência, das pessoas de 14 anos ou mais de idade
#4100- Coeficiente de variação - Taxa de participação na força de trabalho, na semana de referência, das pessoas de 14 anos ou mais de idade
#4097- Nível da ocupação, na semana de referência, das pessoas de 14 anos ou mais de idade
#4101- Coeficiente de variação - Nível da ocupação, na semana de referência, das pessoas de 14 anos ou mais de idade
#4098- Nível da desocupação, na semana de referência, das pessoas de 14 anos ou mais de idade
#4102- Coeficiente de variação - Nível de desocupação, na semana de referência, das pessoas de 14 anos ou mais de idade
#4099- Taxa de desocupação, na semana de referência, das pessoas de 14 anos ou mais de idade
#4103- Coeficiente de variação - Taxa de desocupação, na semana de referência, das pessoas de 14 anos ou mais de idade
#12466- Taxa de informalidade das pessoas de 14 anos ou mais de idade ocupadas na semana de referência
#12467- Coeficiente de variação - Taxa de informalidade das pessoas de 14 anos ou mais de idade ocupadas na semana de referência
#4723- Pessoas de 14 anos ou mais de idade ocupadas, em situação de informalidade, na semana de referência
#4724- Coeficiente de variação - Pessoas de 14 anos ou mais de idade ocupadas, em situação de informalidade, na semana de referência
#4726- Distribuição percentual das pessoas de 14 anos ou mais de idade ocupadas, em situação de informalidade, na semana de referência
#4774- Coeficiente de variação - Distribuição percentual das pessoas de 14 anos ou mais de idade ocupadas, em situação de informalidade, na semana de referência

#Códigos dos estados:
#11 - Rondônia
#12 - Acre
#13 - Amazonas
#14 - Roraima
#15 - Pará
#16 - Amapá
#17 - Tocantins
#21 - Maranhão
#22 - Piauí
#23 - Ceará
#24 - Rio Grande do Norte
#25 - Paraíba
#26 - Pernambuco
#27 - Alagoas
#28 - Sergipe
#29 - Bahia
#31 - Minas Gerais
#32 - Espírito Santo
#33 - Rio de Janeiro
#35 - São Paulo
#41 - Paraná
#42 - Santa Catarina
#43 - Rio Grande do Sul
#50 - Mato Grosso do Sul
#51 - Mato Grosso
#52 - Goiás
#53 - Distrito Federal