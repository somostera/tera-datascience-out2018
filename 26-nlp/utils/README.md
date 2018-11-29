### Instalação do tensorboard

Nessa pasta, rode os comandos:

* `mkdir visualize_result`

* `python w2v_visualizer.py ../data/gensim.model visualize_result`

* `pip install --upgrade numpy`

* `conda install -c anaconda tensorflow-tensorboard`

* `python -m tensorboard.main --logdir=visualize_result/`
