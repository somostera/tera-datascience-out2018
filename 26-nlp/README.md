# Aula #26 – Processamento de Linguagem Natural & Análise de Sentimento

Nessa aula, vamos aprender sobre processamento de linguagem natural (NLP) através de duas atividades:

* análise de sentimento em um dataset de reviews de restaurante; e

* construção de uma ferramenta para medir a combinação de ingredientes usando um dataset de receitas.

## Pré-aula

Para essa aula, o ideal é que vocês instalem os recursos mencionados abaixo pois, sem eles, será difícil acompanhar a aula.

### Spacy

Instalar modelo `en_core_web_sm`:

* `python -m spacy download en_core_web_sm`

### ipywidgets

Instalar `ipywidgets` no `jupyter lab`:

* `conda install -c conda-forge -y ipywidgets nodejs==8.12.0`

* `jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.34`

Se o comando de instalar a extensão no jupyter não funcionar, rodar o comando `jupyter lab --version` para checar a versão e escolher o comando apropriado na [página do github do jupyter-widgets](https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager#version-compatibility).

Nota: Caso deseje, você pode rodar os comandos diretamente da célula do `jupyter notebook`, adicionando uma exclamação na frente do comando (e.g. `!ls`). Nunca testei tentar instalar a extensão com o `jupyter` aberto; é possível que essa operação não funcione.