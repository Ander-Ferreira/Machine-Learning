import pandas as pd
import numpy as np


#Cria um dataframe
marketing = pd.read_csv('marketing.csv', delimiter =',')


print(marketing.head(5))

marketing.describe(include='all')

print(marketing['converted'].head(5))

#Estou selecionando a coluna 'converted' e sobrescrevendo com formato booleano
marketing['converted'] = marketing['converted'].astype('bool')

#marketing=['is_house_ads'] = np.where(marketing['marketing_channel'] == 'House Ads', True, False)

#fillna('') atribui valores aos espaços vazios da tabela











