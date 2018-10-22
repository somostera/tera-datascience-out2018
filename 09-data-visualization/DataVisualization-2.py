
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

