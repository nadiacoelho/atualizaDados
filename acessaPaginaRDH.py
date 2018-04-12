import requests
import urllib.request
import userSettings
import montaURL

destino = 'testepython.docx'
enderecoLogin = 'https://idpcafe.usp.br/idp/profile/SAML2/Redirect/SSO?execution=e5s1'
enderecoDownload = 'https://edisciplinas.usp.br/mod/resource/view.php?id=2274900'
usuario = '8994265'
senha = 'Nacopo@1996'

#enderecoLogin = montaURL.enderecoLogin
#enderecoDownload = montaURL.enderecoXLSX
#usuario = userSettings.usuario
#senha = userSettings.senha

#resp = requests.post(endereco, data = {'username': usuario , 'password': senha})

with requests.Session() as s:
    s.get(enderecoLogin)
    s.auth = (usuario , senha)
    resp = requests.get(enderecoDownload)

print(resp.status_code)
print(resp.content)