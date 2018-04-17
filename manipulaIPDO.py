import pandas as pd
import acessaIPDO
import montaURL_IPDO

writer = pd.ExcelWriter("RelatorioIPDO.xlsx") #para usar essa função, é necessário instalar o pacote "xlsxwriter" ou "openpyxl"

#definições relativas às tabelas em análise para indexação
dia = 3
linhaDoDia = dia + 5
#para a Energia Armazenada:
capacidadeMaxima = 3
armazenamentoAoFinalDoDia = 4
percentualArmazenado = 5
variacaoDiaAnterior = 6
variacaoMensal = 7
#para ENA:
linNorteENA = 2
linNordesteENA = 3
linSulENA = 4
linSudesteENA = 5

#define o index das series coletadas
indexSerieDiaria = ['Producao Total', 'Hidraulica', 'Termica', 'Eolica', 'Solar', 'Intercambio', 'Carga']
indexEA = ['Sul', 'Sudeste', 'Norte', 'Nordeste']
indexENA = ['% MLT do dia', '%MLT no mês', 'ENA Bruta no dia', 'ENA Bruta no mês']


#DADOS DE PRODUÇÃO E CARGA
#acessa as planilhas por subsistema: (arquivo .xlsx, nome da planilha)
dadosDiariosS = pd.read_excel(acessaIPDO.destino, "03-Dados Diários Acumulados S")
dadosDiariosSE = pd.read_excel(acessaIPDO.destino, "04-Dados Diários Acumulados SE")
dadosDiariosNE = pd.read_excel(acessaIPDO.destino, "05-Dados Diários Acumulados NE")
dadosDiariosN = pd.read_excel(acessaIPDO.destino, "06-Dados Diários Acumulados N")
dadosDiariosSIN = pd.read_excel(acessaIPDO.destino, "07-Dados Diários Acumulados SIN")

#exporta os dados das planilhas para series diárias
sul = pd.Series(dadosDiariosS.iloc[linhaDoDia,1:], name= 'Sul')
sul.set_axis(indexSerieDiaria, inplace = True)
sudeste = pd.Series(dadosDiariosSE.iloc[linhaDoDia,1:], name = 'Sudeste')
sudeste.set_axis(indexSerieDiaria, inplace = True)
nordeste = pd.Series(dadosDiariosNE.iloc[linhaDoDia,1:], name = 'Nordeste')
nordeste.set_axis(indexSerieDiaria, inplace = True)
norte = pd.Series(dadosDiariosN.iloc[linhaDoDia,1:], name = 'Norte')
norte.set_axis(indexSerieDiaria, inplace = True)
sin = pd.Series(dadosDiariosSIN.iloc[linhaDoDia,1:], name = 'SIN')
sin.set_axis(indexSerieDiaria, inplace = True)

#cria o Dataframe com os dados
dadosCarga = [sul, sudeste, nordeste, norte, sin]
dfCarga = pd.DataFrame(dadosCarga)
#print(df.head(6))

#exporta para Excel
nomeCarga = "Produção e carga " + str(dia) + montaURL_IPDO.mes
dfCarga.to_excel(writer, sheet_name=nomeCarga)
writer.save()

#ENERGIA ARMAZENADA
#acessa dados por subsistema: (arquivo .xlsx, nome da planilha)
energiaArmazenada = pd.read_excel(acessaIPDO.destino, "20-Variação Energia Armazenada")
capacidadeMax = pd.Series(energiaArmazenada.iloc[capacidadeMaxima,1:], name= "Capacidade Maxima do Subsistema")
capacidadeMax.set_axis(indexEA, inplace=True)
#print(capacidadeMax)
energiaDia = pd.Series(energiaArmazenada.iloc[armazenamentoAoFinalDoDia,1:], name= 'Armazenamento ao final do dia')
energiaDia.set_axis(indexEA, inplace=True)
#print(energiaDia)
variacaoEA = pd.Series(energiaArmazenada.iloc[variacaoDiaAnterior,1:], name= "Variação em relação ao dia anterior")
variacaoEA.set_axis(indexEA, inplace=True)
#print(variacaoEA)

#cria o Dataframe com os novos dados
dadosEA = [capacidadeMax, energiaDia, variacaoEA]
dfEA = pd.DataFrame(dadosEA)
#print(dfEA.head(6))

#exporta para Excel
nomeEA = "Energia Armazenada " + str(dia) + montaURL_IPDO.mes
dfEA.to_excel(writer, sheet_name= nomeEA)
writer.save()

#ENA
#acessa dados por subsistema: (arquivo .xlsx, nome da planilha)
energiaNaturalAfluente = pd.read_excel(acessaIPDO.destino, "21-Energia Natural Afluente")
print(energiaNaturalAfluente.head(10))
enaNorte = pd.Series(energiaArmazenada.iloc[linNorteENA,1:], name= "Norte")
enaNorte.set_axis(indexENA, inplace=True)
#print(enaNorte)
enaNordeste = pd.Series(energiaArmazenada.iloc[linNordesteENA,1:], name= "Nordeste")
enaNordeste.set_axis(indexENA, inplace=True)
#print(enaNordeste)
enaSul = pd.Series(energiaArmazenada.iloc[linSulENA,1:], name= "Sul")
enaSul.set_axis(indexENA, inplace=True)
#print(enaSul)
enaSudeste = pd.Series(energiaArmazenada.iloc[linSudesteENA,1:], name= "Sudeste")
enaSudeste.set_axis(indexENA, inplace=True)
#print(enaSudeste)


#cria o Dataframe com os novos dados
dadosENA = [enaNorte, enaNordeste, enaSul, enaSudeste]
dfENA = pd.DataFrame(dadosENA)
#print(dfENA.head(6))

#exporta para Excel
nomeENA = "ENA " + str(dia) + montaURL_IPDO.mes
dfENA.to_excel(writer, sheet_name= nomeENA)
writer.save()