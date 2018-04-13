import pandas as pd
import numpy as np
import acessaIPDO

planIPDO = pd.read_excel(acessaIPDO.destino)
planRelatorio = pd.read_excel("RelatorioComparativo.xlsx")

planIPDO[planIPDO["Norte"]=="Carga (*)"].head()