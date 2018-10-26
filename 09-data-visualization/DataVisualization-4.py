
# coding: utf-8

# # Visualização de dados para tomada de decisão

# ![](https://media.giphy.com/media/zw69pUViBZCZW/giphy.gif)

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import re
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


df = pd.read_csv('kaggle-survey-2017/multipleChoiceResponses.csv', encoding="ISO-8859-1")


# ### E se eu quiser ter uma ideia do tempo que é investido criando-se modelos?

# ## Boxplot

# In[7]:


# Boxplot de TimeModelBuilding
_ = sns.boxplot(df['TimeModelBuilding']).set_title("% Time spent building models")


# Eu também posso usar boxplots com variáveis categóricas...

# ### E Se eu quiser verificar o salário das pessoas por gênero?

# Primeiramente, vamos usar apenas as pessoas que tenham valores de salário que é representado pela variável `CompensationAmount`

# In[21]:


# Vamos ver as categorias da variável GenderSelect


# In[22]:


# Agora vamos precisar carregar o exchange rate e dar merge dele com o nosso dataframe original


# In[23]:


# Agora vamos transformar o CompensationAmount para que tudo fique em dólares


# In[24]:


# Podemos usar o `describe` para ver as estatisticas dessa coluna


# In[25]:


# Agora sim, podemos plotar o nosso boxplot com categorias 


# Tem um outlier nesse conj. de dados que está atrapalhando a nossa visualização... Podemos removê-lo usando boolean indexes. Vamos usar pessoas que ganham até 2000000.

# In[26]:


# Agora podemos plotar o gráfico sem esses outliers


# Agora vamos colocar os titulos em 45º

# In[27]:


# titulos em 45º


# ## Scatterplots (Dispersão)

# ### E se eu quiser ver a distribuição da probabilidade das pessoas que aprenderam algo (da profissão) no Trabalho e que foram auto didatas? 

# In[9]:


# E se eu quiser ver LearningCategorySelftTaught e LearningCategoryWork ao mesmo tempo?
sns.jointplot(x='LearningCategorySelftTaught', y='LearningCategoryWork', data=df);


# E o que eu posso fazer se eu quiser ver as probabilidades de todas as categorias `LearningCategory(...)` todas juntas?

# In[18]:


# E as categorias LearningCategorySelftTaught, LearningCategoryWork, LearningCategoryOnlineCourses, LearningCategoryUniversity, LearningCategoryOther 
df['LearningCategorySelftTaught'] = df['LearningCategorySelftTaught'].fillna(0)
df['LearningCategoryWork'] = df['LearningCategoryWork'].fillna(0)
df['LearningCategoryOnlineCourses'] = df['LearningCategoryOnlineCourses'].fillna(0)
df['LearningCategoryUniversity'] = df['LearningCategoryUniversity'].fillna(0)
df['LearningCategoryOther'] = df['LearningCategoryOther'].fillna(0)
sns.kdeplot(df['LearningCategorySelftTaught'])
sns.kdeplot(df['LearningCategoryWork'])
sns.kdeplot(df['LearningCategoryOnlineCourses'])
sns.kdeplot(df['LearningCategoryUniversity'])
#sns.kdeplot(df['LearningCategoryOther'])


# ## Desafio 4
# 
# Existem ainda várias perguntas que ficaram sem resposta, do tipo:
# 
#  1. Quais os maiores desafios de um cientista de dados? (`WorkChallengesSelect`)
#  - Quais os algoritmos mais utilizados em data science? (`WorkAlgorithmsSelect`)
#  - Quais os setores que mais empregam cientistas de dados? (`EmployerIndustry`)
#  - Qual o tamanho das empresas que contratam cientistas de dados? (`EmployerSize`)
#  
# Organizem-se em duplas para resolver esses desafios.

# ![challenge](https://media.giphy.com/media/d4zHnLjdy48Cc/giphy.gif)

# ## Gráficos mais complexos

#  - Uma das análises desse dataset no blog do kaggle -> http://blog.kaggle.com/2017/10/30/introducing-kaggles-state-of-data-science-machine-learning-report-2017/
#  - Joyplots -> http://blog.kaggle.com/2017/07/20/joyplots-tutorial-with-insect-data/
#  - Plots de mapas -> http://blog.kaggle.com/2016/11/30/seventeen-ways-to-map-data-in-kaggle-kernels/
