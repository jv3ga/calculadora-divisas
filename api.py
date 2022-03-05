import requests

def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

menu = -1
while menu != 0:
    print('Seleccione una opcion: ')
    print('1 - Convertir precio de criptomoneda')
    print('2 - Mostar listado de criptomonedas')
    print('0 - Salir')
    menu = input('Opción seleccionada: ')
    if not is_int(menu):
        print('Selecciona una opción numérica')
    else:
        menu = int(menu)
        if menu == 1:
            asset = input('Introduce la moneda que quieras convertir: ').upper()
            url = 'https://data.messari.io/api/v1/assets/{}/metrics'.format(asset)
            data = requests.request('GET', url)
            if data.ok:
                price_usd = data.json()['data']['market_data']['price_usd']
                price_btc = data.json()['data']['market_data']['price_btc']
                name = data.json()['data']['name']
                print('Criptodivisa seleccionada: {}'.format(name))
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
                input('Presiona una tecla para continuar')
            else:
                print('No se encuentra el simbolo seleccionado')
                input('Presiona una tecla para continuar')
        elif menu == 2:
            limit = input('¿Cuántos quieres mostrar? (máximo 500)')
            if not is_int(limit):
                print('Debes indicar un número entero')
            else:
                url = 'https://data.messari.io/api/v2/assets?fields=name,symbol&limit={}'.format(
                    limit
                )
                data = requests.request('GET', url)
                if data.ok:
                    for key in data.json()['data']:
                        print('Nombre: {name}:  -- Símbolo: {symbol}'.format(
                            name=key['name'],
                            symbol=key['symbol']
                        ))
                else:
                    input('Se ha producido un error. Presiona una tecla para continuar')
        elif menu == 0:
            print('Adiós')
        else:
            print('Opción no disponible')