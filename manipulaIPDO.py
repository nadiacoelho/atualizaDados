import pandas as pd
import acessaIPDO
import montaURL


dia = 2
linhaDoDia = dia + 5 #os dados começam na linha 6

#define o index das series coletadas
indexSerieDiaria = ['Producao Total', 'Hidraulica', 'Termica', 'Eolica', 'Solar', 'Intercambio', 'Carga']

#acessa planilha de interesse: (arquivo .xlsx, nome da planilha)
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

#cria o Dataframe com os novos dados
dados = [sul, sudeste, nordeste, norte, sin]
df = pd.DataFrame(dados)
print(df.head(6))

data = str(dia) + montaURL.mes
#exporta para Excel
writer = pd.ExcelWriter("RelatorioIPDO.xlsx")
df.to_excel(writer, sheet_name=data)
writer.save()