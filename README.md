python-flask-rss-feeds
=====

Aplicação em [Python](https://www.python.org/doc/) usando o framework web [Flask](https://flask.palletsprojects.com/en/2.0.x/),
o módulo [feedparser](https://pythonhosted.org/feedparser/) e container com [Docker](https://docs.docker.com/).

[RSS](https://pt.wikipedia.org/wiki/RSS) (Really Simple Syndication) é um formato de distribuição de informações em tempo real pela internet, no qual um subconjunto de "dialetos" XML que servem para agregar conteúdo podem ser acessados mediante programas ou sites agregadores. É usado principalmente em sites de notícias e blogues.

A abreviatura do RSS é usada para se referir aos seguintes padrões:

    Rich Site Summary (RSS 0.91)
    RDF Site Summary (RSS 0.9 e 1.0)
    Really Simple Syndication (RSS 2.0)

A tecnologia do RSS permite aos usuários da internet se inscreverem em sites que fornecem "feeds" RSS. Estes são tipicamente sites que mudam ou atualizam o seu conteúdo regularmente. Para isso, são utilizados Feeds RSS que recebem estas atualizações, desta maneira o utilizador pode permanecer informado de diversas atualizações em diversos sites sem precisar visitá-los um a um.

Os feeds RSS oferecem conteúdo Web ou resumos de conteúdo juntamente com os links para as versões completas deste conteúdo e outros metadados. Esta informação é entregue como um arquivo XML chamado "RSS feed", "webfeed", "Atom" ou ainda canal RSS.
(Wikipedia)

A aplicação disponibiliza os pricipais canais de RSS feeds de notícias em tempo real e de acordo com a escolha do usuário. Foi desenvolvida usando docker e [docker-compose](https://docs.docker.com/compose/) 
para implementação do ambiente de desenvolvimento.


Requisitos
----------

- docker
- docker-compose


Instalação
----------

Use git:

```bash

    $ git clone https://github.com/jmreis/python-flask-rss-feeds

    $ cd python-flask-rss-feeds

    $ docker-compose up --build

```

