
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

# In[11]:


# Vamos ver as categorias da variável RemoteWork


# In[12]:


# Vamos ver as categorias da variável TimeGatheringData


# In[13]:


# Agora vamos usar o swarplot. Ele pode demorar um pouquinho...


# Parece que não muda muito... 

# ### E se eu quiser saber se o tempo que a pessoa passa gerando visualizações impacta no tempo que ela gasta em visualização em um projeto?

# In[14]:


# Vamos ver as categorias da variável WorkToolsSelect


# In[15]:


# Agora vamos preencher os nulos com o valor 'NULL'


# In[16]:


# Podemos substituir o pedaço ' of projects' da string original para o nosso gráfico ficar mais limpo


# In[17]:


# Vamos verificar os novos valores mais limpos agora


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

# In[19]:


# Resolva o desafio aqui

