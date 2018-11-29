# Aula #26 – Processamento de Linguagem Natural & Análise de Sentimento

Nessa aula, vamos aprender sobre processamento de linguagem natural (NLP) através de duas atividades:

* análise de sentimento em um dataset de reviews de restaurante (`nlp_parte_1.ipynb`); e

* construção de uma ferramenta para medir a combinação de ingredientes usando um dataset de receitas (`nlp_parte_2.ipynb`).

## Pré-aula

Para essa aula, o ideal é que vocês instalem os recursos mencionados abaixo pois, sem eles, será difícil acompanhar a aula.

Foram adicionados novos pacotes no _environment_ da Tera. Para que eles funcionem, você deve recriar o _environment_.

* `conda env remove -n tera-out2018`

* `git pull`

* `conda env create -f tera-out2018.yml`

* `source activate tera-out2018`

### Spacy

Já dentro do _env_, instalar modelo `en_core_web_sm`:

* `python -m spacy download en_core_web_sm`

Observação 1: Caso deseje, você pode rodar os comandos diretamente da célula do jupyter notebook, adicionando uma exclamação na frente do comando (e.g. !ls).

Observação 2: pode acontecer de ao instalar, aparecer um erro ao criar o link simbólico (_symlink_) para a pasta de dados do `spacy`. Isso, porém, não impede que usemos o modelo. Basta que importemos o modelo como se fosse um módulo. Leia mais no [github do spacy](https://github.com/explosion/spaCy/issues/915).

## Pós-aula

Durante a aula, mostrei a visualização do word2vec que treinamos usando o `t-SNE` no `tensorboard`. Incluí um notebook a mais (além dos notebooks com as respostas) chamado `nlp_parte_extra`, que tem um passo-a-passo para rodar o tensorboard. O passo-a-passo assume que vocês estão no `env` da Tera, mas também seria possível fazer fora do ambiente, bastando instalar as bibliotecas `gensim` (3.4.0), `tensorflow` (1.5.0), `numpy` (1.15.4) e `tensorflow-tensorboard` (1.5.1). Que tal tentar criar um ambiente com essas bibliotecas?


### Links indicados para leitura

Falamos de muitas coisas durante a aula e acho que seria muito bom continuar (e reforçar) o aprendizado com os seguintes links:

* [conselhos para aplicar NLP na indústria](https://medium.freecodecamp.org/industrial-strength-natural-language-processing-de2588b6b1ed)
Super recomendo a leitura para todos, já que esses conselhos e observações complementam o que já discutimos durante a aula: não há necessidade de complicar demais uma aplicação.


* [vídeo detalhado sobre o funcionamento do word2vec](https://www.youtube.com/watch?v=ERibwqs9p38)
Essa é uma aula do curso de deep learning para NLP de Stanford e fala sobre o word2vec, incluindo um passo-a-passo de algumas fórmulas.

* [indo além do word2vec](https://towardsdatascience.com/https-medium-com-tanaygahlot-moving-beyond-the-distributional-model-for-word-representation-b0823f1769f8)
Esse post fala sobre algumas soluções para: (i) palavras raras; (ii) múltiplos sentidos de uma palavra; (iii) presença de relações linguísticas entre algumas palavras.

* [usando nltk para pré-processar texto](https://machinelearningmastery.com/clean-text-machine-learning-python/)
Na aula, fizemos praticamente todo o pré-processamento usando o `spacy`. Esse post descreve como fazer grande parte do que fizemos na aula "manualmente" ou usando a biblioteca `nltk`.

* [aplicação do word2vec para encontrar questões similares no Quora](https://towardsdatascience.com/finding-similar-quora-questions-with-word2vec-and-xgboost-1a19ad272c0d)
Esse é um exemplo de uma aplicação que pode ser construída usando `word2vec`. Além de usar o `word2vec`, também é utilizado o `WMD`, que é um método poderoso para calcular a similaridade entre sentenças.

* [Várias referências de recursos de NLP](https://github.com/keon/awesome-nlp)
Além de recursos para aprendizado, também tem links para bibliotecas de NLP de várias linguagens, inclusive `Javascript`, por exemplo!