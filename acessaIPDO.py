import urllib.request
import montaURL

#Destino e origem do arquivo:
destino = 'IPDO_' + str(montaURL.d) + montaURL.mes + str(montaURL.a) + '.xlsx'
enderecoDownload = 'http://sdro.ons.org.br/SDRO/DIARIO/2018_04_10/Html/DIARIO_10-04-2018.xlsx'

#Fazer download e salvar:
urllib.request.urlretrieve(enderecoDownload, destino)