# Aula #26 – Processamento de Linguagem Natural & Análise de Sentimento

Nessa aula, vamos aprender sobre processamento de linguagem natural (NLP) através de duas atividades:

* análise de sentimento em um dataset de reviews de restaurante; e

* construção de uma ferramenta para medir a combinação de ingredientes usando um dataset de receitas.

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
