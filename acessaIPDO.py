import urllib.request
import montaURL_IPDO

#Destino e origem do arquivo:
destino = 'IPDO_' + str(montaURL_IPDO.d) + montaURL_IPDO.mes + str(montaURL_IPDO.a) + '.xlsx'
enderecoDownload = montaURL_IPDO.enderecoIPDO

#Fazer download e salvar:
urllib.request.urlretrieve(enderecoDownload, destino)