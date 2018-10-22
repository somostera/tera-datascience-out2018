
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


# ### Quais são as áreas de graduação dos cientistas de dados?

# In[7]:


#Countplot com MajorSelect


# Para ficar mais facil de ver podemos ordenar as barras

# In[8]:


# ordene o eixo y


# Agora ficou bem mais fácil de tirar conclusões sobre os cursos.
# 
# A maioria dos cientistas de dados estudou ciência da computação, matemática ou engenharia.

# E se trocarmos os y por um x?

# ### Qual o maior grau de educação dos cientistas de dados?

# In[9]:


# Use o campo FormalEducation


# ### Desafio 2
# ##### Quais os empregos anteriores dos cientistas de dados?
# 
# Para fazer esse desafio você vai consultar a coluna `PastJobTitlesSelect`. Veja que essa coluna possui varios valores. Você precisará criar um método para reduzir a granularidade dessa coluna.

# Dica: A solução fica mais fácil se você usar [expressões regulares](https://pt.wikipedia.org/wiki/Express%C3%A3o_regular). Para testá-las use [esse site](https://regexr.com/)

# ![finn_mathematical](https://media.giphy.com/media/ccQ8MSKkjHE2c/giphy.gif)

# In[10]:


# Resolva o desafio aqui


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


# ### E se eu quiser ter uma ideia do tempo que é investido criando-se modelos?

# ## Boxplot

# In[20]:


# Boxplot de TimeModelBuilding


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

# In[ ]:


# E se eu quiser ver LearningCategorySelftTaught e LearningCategoryWork ao mesmo tempo?


# E o que eu posso fazer se eu quiser ver as probabilidades de todas as categorias `LearningCategory(...)` todas juntas?

# In[28]:


# E as categorias LearningCategorySelftTaught, LearningCategoryWork, LearningCategoryOnlineCourses, LearningCategoryUniversity, LearningCategoryOther 


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
