
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


# ## Histogramas

# Vamos analisar a idade dos cientistas de dados dessa pesquisa. Qual a idade média? Quantos anos tem a pessoa mais velha dessa pesquisa? 

# Para conseguir usar o `countplot` vamos transformar `Age` para inteiro para poder enxergar os numeros melhor

# In[2]:


# vamos preencher os nulos da variável "Age" com zeros


# Vamos ver um histograma da idade dos participantes

# In[1]:


# Agora fazer um countplot com essa variável


# Ficou horrível...
# 
# Vamos adicionar o titulo e aumentar o gráfico

# In[3]:


# Um countplot maior e na horizontal


# E se eu não quiser um eixo x mais limpo? Só para ver a distribuição em si?

# In[4]:


# agora um distplot


# E para remover a curva de tendencia?

# In[5]:


# remover o kde


# **Nota**: Distplot não aceita Nulos. O grande número de pessoas que ficaram com idade zero na verdade são pessoas que não preencheram. 

# ### Desafio 1
# 
# Ao invés de substituir os valores nulos pelo número zero, substitua-os pelo valor médio da idade no dataset. Plot a idade novamente. Além disso, troque as cores do gráfico. Para isso use [o guia de paletas do seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html#palette-tutorial).
# 
# ![monstros_sa](https://media.giphy.com/media/zxxXYJqTlpBnO/giphy.gif)

# In[ ]:


# faça o desafio aqui


# ### Como seria o mesmo histograma usando apenas matplotlib?

# In[6]:


# com matplotlib

