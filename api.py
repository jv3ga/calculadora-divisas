import requests

menu = -1
while menu != 0:
    print('Seleccione una opcion: ')
    print('1 - Convertir precio de criptomoneda')
    print('2 - Buscar criptomoneda')
    print('0 - Salir')
    menu = int(input('Opción seleccionada: '))
    if menu == 1:
        asset = input('Introduce la moneda que quieras convertir: ').upper()
        url = 'https://data.messari.io/api/v1/assets/{}/metrics'.format(asset)
        data = requests.request('GET', url)
        price_usd = data.json()['data']['market_data']['price_usd']
        price_btc = data.json()['data']['market_data']['price_btc']
        print('El precio en BTC es de {btc}, y en USD {usd}'.format(
            btc=price_btc,
            usd=price_usd
        ))
        cantidad = int(input('Introduce la cantidad que deseas convertir: '))
        total_btc = cantidad * price_btc
        total_usd = cantidad * price_usd
        print('{cantidad} {asset} a BTC = {total_btc}'.format(
            cantidad=cantidad,
            asset=asset,
            total_btc=total_btc
        ))
        print('{cantidad} {asset} a USD = {total_usd}'.format(
            cantidad=cantidad,
            asset=asset,
            total_usd=total_usd
        ))
    elif menu == 2:
        print('2')
    elif menu == 0:
        print('Adiós')
    else:
        print('Opción no disponible')