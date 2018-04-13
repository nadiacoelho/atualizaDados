import pandas as pd
import numpy as np
import acessaIPDO
import montaURL

colunaCarga = 7
colunaProducao = 1

dia = 5
primeiraLinha = 6
linha = primeiraLinha + dia - 2
print(linha)

#teste = pd.read_excel("teste.xlsx")
#print(teste[teste["account number"]==737550].head())

#acessa planilha de interesse: (arquivo .xlsx, nome da planilha)

dadosDiariosN = pd.read_excel(acessaIPDO.destino, "06-Dados Diários Acumulados N")
dadosDiariosNE = pd.read_excel(acessaIPDO.destino, "05-Dados Diários Acumulados NE")
dadosDiariosSE = pd.read_excel(acessaIPDO.destino, "04-Dados Diários Acumulados SE")
dadosDiariosS = pd.read_excel(acessaIPDO.destino, "03-Dados Diários Acumulados S")
dadosDiariosSIN = pd.read_excel(acessaIPDO.destino, "07-Dados Diários Acumulados SIN")
planRelatorio = pd.read_excel("RelatorioComparativo.xlsx")

#Escreve as cargas realizadas
#print(planRelatorio.head(5))
norte = dadosDiariosN.iloc[linha, colunaCarga]
nordeste = dadosDiariosNE.iloc[linha, colunaCarga]
sul = dadosDiariosS.iloc[linha, colunaCarga]
sudeste = dadosDiariosSE.iloc[linha, colunaCarga]

print("Norte", norte)
print("Nordeste", nordeste)
print("Sul", sul)
print("Sudeste", sudeste)


planRelatorio.loc['N','Carga Realizada'] = norte
planRelatorio.loc['NE','Carga Realizada'] = nordeste
planRelatorio.loc['S','Carga Realizada'] = sul
planRelatorio.loc['SE','Carga Realizada'] = sudeste
