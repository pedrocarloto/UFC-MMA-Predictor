import requests
username = 'ufcmma'
token = '2af37dbf8d5072276ddd22999d425b1644559725'
host = 'www.pythonanywhere.com'


response = requests.get(
    'https://{host}/api/v0/user/{username}/cpu/'.format(
        host=host, username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))