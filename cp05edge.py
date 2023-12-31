import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import parser
import matplotlib.dates as mdates

# Solicitar ao usuário o número de leituras a serem recuperadas
lastN = 82

url = f"http://46.17.108.113:8666/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:001/attributes/luminosity?lastN={lastN}"

payload = {}
headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = json.loads(response.text)

    # Extrair dados de luminosidade e tempo
    luminosity_values = []
    time_values = []

    for value in data["contextResponses"][0]["contextElement"]["attributes"][0]["values"]:
        luminosity_values.append(value["attrValue"])
        time_values.append(parser.parse(value["recvTime"]))  # Usar dateutil.parser para analisar a data e a hora

    # Criar o gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(time_values, luminosity_values, marker='o', linestyle='-')
    plt.title('Luminosidade nos últimos 15 minutos')
    plt.xlabel('Tempo')
    plt.ylabel('Luminosidade')
    plt.xticks(rotation=45)

    # Definir intervalo das marcas de tempo para exibir minutos
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

    plt.grid(True)
    plt.tight_layout()

    # Mostrar o gráfico
    plt.show()
else:
    print(f"A solicitação retornou um status code {response.status_code}. Verifique as configurações e tente novamente.")