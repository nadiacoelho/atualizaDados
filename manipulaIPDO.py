import pandas as pd
import acessaIPDO
import montaURL_IPDO

pd.set_option('display.width', 100)
writer = pd.ExcelWriter(r'C:\Users\Nadia.Pontes\PycharmProjects\atualizaDados\RelatorioIPDO.xlsx', engine= 'openpyxl') #para usar essa função, é necessário instalar o pacote "xlsxwriter" ou "openpyxl"

#definições relativas às tabelas em análise para indexação
dia = montaURL_IPDO.d

linhaDoDia = dia + 3
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

destino = "IPDO_1ABR2018.xlsx"
#DADOS DE PRODUÇÃO E CARGA
#acessa as planilhas por subsistema: (arquivo .xlsx, nome da planilha)
dadosDiariosS = pd.read_excel(destino, "03-Dados Diários Acumulados S")
dadosDiariosSE = pd.read_excel(destino, "04-Dados Diários Acumulados SE")
dadosDiariosNE = pd.read_excel(destino, "05-Dados Diários Acumulados NE")
dadosDiariosN = pd.read_excel(destino, "06-Dados Diários Acumulados N")
dadosDiariosSIN = pd.read_excel(destino, "07-Dados Diários Acumulados SIN")

# dadosDiariosS = pd.read_excel(acessaIPDO.destino, "03-Dados Diários Acumulados S")
# dadosDiariosSE = pd.read_excel(acessaIPDO.destino, "04-Dados Diários Acumulados SE")
# dadosDiariosNE = pd.read_excel(acessaIPDO.destino, "05-Dados Diários Acumulados NE")
# dadosDiariosN = pd.read_excel(acessaIPDO.destino, "06-Dados Diários Acumulados N")
# dadosDiariosSIN = pd.read_excel(acessaIPDO.destino, "07-Dados Diários Acumulados SIN")

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
print(dfCarga.head(6))

# #exporta para Excel
# nomeCarga = "Produção e carga " + str(dia) + montaURL_IPDO.mes
# dfCarga.to_excel(writer, sheet_name=nomeCarga, index=False)
# writer.save()
#
# #ENERGIA ARMAZENADA
# #acessa dados por subsistema: (arquivo .xlsx, nome da planilha)
# energiaArmazenada = pd.read_excel(destino, "20-Variação Energia Armazenada")
#
# capacidadeMax = pd.Series(energiaArmazenada.iloc[capacidadeMaxima,1:], name= "Capacidade Maxima do Subsistema")
# capacidadeMax.set_axis(indexEA, inplace=True)
#
# energiaDia = pd.Series(energiaArmazenada.iloc[armazenamentoAoFinalDoDia,1:], name= 'Armazenamento ao final do dia')
# energiaDia.set_axis(indexEA, inplace=True)
#
# variacaoEA = pd.Series(energiaArmazenada.iloc[variacaoDiaAnterior,1:], name= "Variação em relação ao dia anterior")
# variacaoEA.set_axis(indexEA, inplace=True)
#
# #cria o Dataframe com os novos dados
# dadosEA = [capacidadeMax, energiaDia, variacaoEA]
# dfEA = pd.DataFrame(dadosEA)
#
# #exporta para Excel
# nomeEA = "Energia Armazenada " + str(dia) + montaURL_IPDO.mes
# dfEA.to_excel(writer, sheet_name= nomeEA, index = True)
# writer.save()
#
# #ENA
# #acessa dados por subsistema: (arquivo .xlsx, nome da planilha)
# energiaNaturalAfluente = pd.read_excel(destino, "21-Energia Natural Afluente")
#
# enaNorte = pd.Series(energiaNaturalAfluente.iloc[linNorteENA,1:], name= "Norte")
# enaNorte.set_axis(indexENA, inplace=True)
#
# enaNordeste = pd.Series(energiaNaturalAfluente.iloc[linNordesteENA,1:], name= "Nordeste")
# enaNordeste.set_axis(indexENA, inplace=True)
#
# enaSul = pd.Series(energiaNaturalAfluente.iloc[linSulENA,1:], name= "Sul")
# enaSul.set_axis(indexENA, inplace=True)
#
# enaSudeste = pd.Series(energiaNaturalAfluente.iloc[linSudesteENA,1:], name= "Sudeste")
# enaSudeste.set_axis(indexENA, inplace=True)
#
# #cria o Dataframe com os novos dados
# dadosENA = [enaNorte, enaNordeste, enaSul, enaSudeste]
# dfENA = pd.DataFrame(dadosENA)
#
# #exporta para Excel
# nomeENA = "ENA " + str(dia) + montaURL_IPDO.mes
# dfENA.to_excel(writer, sheet_name= nomeENA, index = True)
# writer.save()