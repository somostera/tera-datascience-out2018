# Aula \#5 - Desafio em Grupo & Checkpoint \#1

O objetivo desta aula é praticar o conhecimento que já foi adquirido e ganhar familiaridade com Python e as
principais bibliotecas usadas em _data science_.

## Pré-requisitos de sistema

* Python 3
* [JupyterLab](https://github.com/jupyterlab/jupyterlab) ou [Jupyter Notebook](http://jupyter.org/install)

## Sobre Jupyter Notebooks

Esta aula está organizada em torno de uma ferramenta chamada [Jupyter Notebook](https://jupyter.org/).
Para dicas sobre algumas funcionalidades dentro dos notebooks, veja (pelo menos uma dessas) duas sugestões de leitura:

* [Making the Best of Jupyter](https://github.com/NirantK/best-of-jupyter/blob/master/README.md);
* [Boost Your Jupyter Notebook Productivity](https://towardsdatascience.com/jupyter-notebook-hints-1f26b08429ad).

### Mas por que usar notebooks em _data science_?

* esse [post do Netflix](https://medium.com/netflix-techblog/notebook-innovation-591ee3221233) sobre como os notebooks são usados pelos _data scientists_. Além de dar uma introdução sobre os diferentes tipos de funções dentro da carreira de dados, mostra alguns recursos bem legais que podem ser utilizados em notebooks.

## Materiais complementares à aula

### Testes e Debugging

Vocês se lembram como nos notebooks que usamos em aula testávamos nossas funções para checar se elas tinham o comportamento que esperávamos delas? (todas aquelas células que esperávamos que dessem `True` se a executássemos) Na verdade, existem maneiras mais sistemáticas de se testar um código para poder garantir que ele esteja funcionando. Um bom ponto de partida é a leitura desse [guia](https://docs.python-guide.org/writing/tests/).

Mesmo com testes, nem sempre é fácil encontrar um erro dentro de nossos programas. Uma ferramenta que ajuda nessa tarefa é o pdb (Python DeBugger). O projeto [pdb-tutorial](https://github.com/spiside/pdb-tutorial) no git tem um tutorial que pode te ajudar a entender para que ele serve e como usá-lo de maneira efetiva.

### Estilo de código

* [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

* [Black – Code Formatter](https://github.com/ambv/black) formata o código automaticamente

* você também pode instalar plugins no seu editor de texto favorito para te ajudar a checar o estilo do seu código (procure, por exemplo, por pep8 checker <nome-do-seu-editor> no Google!)

### Orientação a objeto

Os vídeos do CS Dojo são mais  curtos e práticos, mostrando como criar o objeto dentro do Jupyter Notebook. Os vídeos da aula do MIT são mais extensos e cobrem a parte de conceitos e usam métodos especiais das classes em Python.

* [CS Dojo – video 1](https://www.youtube.com/watch?v=wfcWRAxRVBA&t=0s&list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg&index=10)

* [CS Dojo – video 2](https://www.youtube.com/watch?v=WOwi0h_-dfA&t=0s&list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg&index=11)

* [MIT – Introduction to Computer Science and Programming in Python – Orientação a objetos](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-8-object-oriented-programming/)

* [MIT – Introduction to Computer Science and Programming in Python – Classes e herança](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-9-python-classes-and-inheritance/)

Uma aplicação comum de orientação a objetos é a criação de classes a partir de outras classes base, para que todos os objetos criados continuem com a mesma interface (a mesma “cara”). Um exemplo desse tipo de aplicação é a criação de tipos de exceções customizadas (você pode ler um pouco sobre isso [aqui](https://julien.danjou.info/python-exceptions-guide/)). Outro exemplo é a criação de modelos derivados do [estimador base da biblioteca scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html) para que você possa aproveitar outras ferramentas do scikit-learn (veja um exemplo [aqui](http://danielhnyk.cz/creating-your-own-estimator-scikit-learn/)).

### Recursos extras

* [vídeo que fala sobre otimização de código em Python](https://www.youtube.com/watch?v=zQeYx87mfyw)

* [sphinx autodoc – geração de documentação automática](http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) – há um tempo atrás, criei um tutorial para aprender a usá-lo; você pode encontrá-lo em meu [github](https://github.com/cimarieta/sphinx-autodoc-example).

* newsletters interessantes: [data science weekly](https://www.datascienceweekly.org/),
  [kdnuggets](https://www.kdnuggets.com/)
