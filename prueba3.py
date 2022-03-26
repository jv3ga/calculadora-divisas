from secretito import BINANCE_API as API_KEY, BINANCE_SECRET as API_SECRET
from binance import Client

request_client = Client(api_key=API_KEY, api_secret=API_SECRET)
data = request_client.get_account()
for asset in data['balances']:
    if float(asset['free']) != 0 or float(asset['locked']) != 0:
        moneda = asset['asset']
        cantidad  = asset['free']
        price = 0
        print('Moneda:{}: - Cantidad: {} - Precio: {}'.format(
            moneda, cantidad, price
            )
        )