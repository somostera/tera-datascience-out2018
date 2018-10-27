
# coding: utf-8

# # Visualização de dados para tomada de decisão

# ![](https://media.giphy.com/media/zw69pUViBZCZW/giphy.gif)

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import re
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('kaggle-survey-2017/multipleChoiceResponses.csv', encoding="ISO-8859-1")


# ### Será que o trabalho remoto impacta no tempo que um cientista passa coletando dados?

# In[3]:


# Vamos ver as categorias da variável RemoteWork
df['RemoteWork'].value_counts()


# In[4]:


# Vamos ver as categorias da variável TimeGatheringData
df['TimeGatheringData'].value_counts()


# In[7]:


df['TimeGatheringData'] = df['TimeGatheringData'].fillna(-1)


# In[8]:


# Agora vamos usar o swarplot. Ele pode demorar um pouquinho...
sns.swarmplot(x="RemoteWork", y="TimeGatheringData", data=df)


# Parece que não muda muito... 

# ### E se eu quiser saber se o tempo que a pessoa passa gerando visualizações impacta no tempo que ela gasta em visualização em um projeto?

# In[10]:


# WorkDataVisualizations
df['WorkDataVisualizations'].value_counts()


# In[13]:


# Agora vamos preencher os nulos com o valor 'NULL'
df['WorkDataVisualizations'] = df['WorkDataVisualizations'].fillna('NULL')
work_visualization = []
for s in df['WorkDataVisualizations']:
    work_visualization.append(re.sub(' of projects', '', s))
    
df['work_visualization'] = work_visualization


# In[14]:


# Vamos verificar os novos valores mais limpos agora
_ = sns.swarmplot(x='work_visualization', y="TimeVisualizing", data=df,
             order=['100%', '51-75%', '26-50%', '10-25%', 
                    'Less than 10%', 'None', 'NULL'])


# In[18]:


# Agora podemos fazer um swarplot de work_visualization com TimeVisualizing


# ### Desafio 3
# 
# Fazer um Heatmap mostrando a [correlação](https://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_Pearson) dos tempos das etapas de um projeto de Data Science. 
# 
# São elas:
# 
#  - TimeGatheringData
#  - TimeVisualizing
#  - TimeModelBuilding
#  - TimeFindingInsights
#  - TimeProduction
# 
# Siga os passos [desse tutorial](https://seaborn.pydata.org/examples/many_pairwise_correlations.html). Atenção! Use apenas essas variáveis.

# ![crazy_finn](https://media.giphy.com/media/KI9oNS4JBemyI/giphy.gif)

# In[16]:


# Resolva o desafio aqui
import numpy as np

sns.set(style="white")

# Generate a large random dataset
d = df[['TimeGatheringData', 'TimeVisualizing', 'TimeModelBuilding', 
        'TimeFindingInsights', 'TimeProduction']]

# Compute the correlation matrix
corr = d.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

