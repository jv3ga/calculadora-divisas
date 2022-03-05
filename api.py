import requests
import json

url = 'https://data.messari.io/api/v1/assets?fields=id,name,slug,symbol,metrics/market_data/price_usd'
data = requests.request('GET', url)
json_string = json.dumps(data.text)
json_object = json.loads(json_string)
print(json_object)
# menu = -1
menu = 0
while menu != 0:
    print('Seleccione una opcion: ')
    print('1 - Convertir precio de criptomoneda')
    print('2 - Buscar criptomoneda')
    print('0 - Salir')
    menu = int(input('Opción seleccionada: '))
    if menu == 1:
        print('Introduce la moneda que quieras convertir')
    elif menu == 2:
        print('2')
    elif menu == 0:
        print('Adiós')
    else:
        print('Opción no disponible')