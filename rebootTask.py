import requests
username = 'ufcmma'
token = '2af37dbf8d5072276ddd22999d425b1644559725'
host = 'www.pythonanywhere.com'
domain = 'ufcmma.pythonanywhere.com'



response = requests.post(
    'https://{host}/api/v0/user/{username}/webapps/{domain}/reload/'.format(
        host=host, username=username, domain=domain
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('Reboot successful')
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))