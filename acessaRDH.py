import requests
import urllib.request
import userSettings
import montaURL

#Destino e origem do arquivo:
destino = 'RDH_' + str(montaURL.d) + montaURL.mes + str(montaURL.a) + '.xlsx'
enderecoDownload = montaURL.enderecoRDH

#Dados de login:
enderecoLogin = montaURL.enderecoLogin
usuario = userSettings.usuario
senha = userSettings.senha

enderecoLogin = 'https://pops.ons.org.br/ons.pop.federation/?wa=wsignin1.0&wtrealm=+https%3a%2f%2fcdre.ons.org.br%2f_trust%2f&wctx=https%3a%2f%2fcdre.ons.org.br%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F&wreply=https%3a%2f%2fcdre.ons.org.br%2f_trust%2fdefault.aspx'
#Fazer login e baixar arquivo:

#tentativa com Sessions:
s = requests.Session()
r1 = s.post(enderecoLogin, {"username" : usuario , "password" : senha, "submit.Signin" : "true"})
home = 'https://cdre.ons.org.br/default.aspx'
r2 = requests.get(home)
print(r1.status_code)
print(r1.url)
print (r2.status_code)
print(r2.url)
print(enderecoLogin)

##### Esse comando funciona para url não protegida (IPDO):
#urllib.request.urlretrieve(enderecoDownload, destino)