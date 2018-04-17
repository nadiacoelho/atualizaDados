import urllib.request
import montaURL_IPDO

#Destino e origem do arquivo:
destino = 'IPDO_' + str(montaURL_IPDO.d - 1) + montaURL_IPDO.mes + str(montaURL_IPDO.a) + '.xlsx'
enderecoDownload = 'http://sdro.ons.org.br/SDRO/DIARIO/2018_04_15/Html/DIARIO_15-04-2018.xlsx'

#Fazer download e salvar:
urllib.request.urlretrieve(enderecoDownload, destino)