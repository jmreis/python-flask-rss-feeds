python-flask-rss-feeds
=====

## Skills

 
![](https://camo.githubusercontent.com/c676b5f90a1650624a0a9832d7954edda1db39ad3347d90c8c51e88ff2f92252/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d4646443433423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d6461726b677265656e) ![flask](https://camo.githubusercontent.com/68390254ad6054b8e98b68fbcae09a3b78751427686f3e003a33c2bbc913b14c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466c61736b2d3030303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d666c61736b266c6f676f436f6c6f723d7768697465) <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> ![docker](https://camo.githubusercontent.com/63350538fde994bc287ccd4908809301e157980e6564bf78d2c5cec22c0a5914/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3243413545303f7374796c653d666f722d7468652d6261646765266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465) 


<!--
<code><img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="python"/></code>
<code><img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/flask/flask.png" alt="flask"/></code>
<code><img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" alt="html"/></code>
<code><img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png" alt="css"/></code>
<code><img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/docker/docker.png" alt="docker"/></code>
<code><img height="32" src="https://coffops.com/wp-content/uploads/2021/04/2elgd5zp07wkeilkna63-576x445.png" alt="heroku"/>
<code>
-->

---

Aplica????o em [Python](https://www.python.org/doc/) usando o framework web [Flask](https://flask.palletsprojects.com/en/2.0.x/),
o m??dulo [feedparser](https://pythonhosted.org/feedparser/) e container com [Docker](https://docs.docker.com/).

[RSS](https://pt.wikipedia.org/wiki/RSS) (Really Simple Syndication) ?? um formato de distribui????o de informa????es em tempo real pela internet, no qual um subconjunto de "dialetos" XML que servem para agregar conte??do podem ser acessados mediante programas ou sites agregadores. ?? usado principalmente em sites de not??cias e blogues.


A abreviatura do RSS ?? usada para se referir aos seguintes padr??es:

    Rich Site Summary (RSS 0.91)
    RDF Site Summary (RSS 0.9 e 1.0)
    Really Simple Syndication (RSS 2.0)

A tecnologia do RSS permite aos usu??rios da internet se inscreverem em sites que fornecem "feeds" RSS. Estes s??o tipicamente sites que mudam ou atualizam o seu conte??do regularmente. Para isso, s??o utilizados Feeds RSS que recebem estas atualiza????es, desta maneira o utilizador pode permanecer informado de diversas atualiza????es em diversos sites sem precisar visit??-los um a um.

Os feeds RSS oferecem conte??do Web ou resumos de conte??do juntamente com os links para as vers??es completas deste conte??do e outros metadados. Esta informa????o ?? entregue como um arquivo XML chamado "RSS feed", "webfeed", "Atom" ou ainda canal RSS.
(Wikipedia)

A aplica????o disponibiliza os pricipais canais de RSS feeds de not??cias em tempo real e de acordo com a escolha do usu??rio. Foi desenvolvida usando docker e [docker-compose](https://docs.docker.com/compose/) 
para implementa????o do ambiente de desenvolvimento.


## Requisitos
----------

- docker
- docker-compose


## Instala????o
----------

Use git:

```bash

    $ git clone https://github.com/jmreis/python-flask-rss-feeds

    $ cd python-flask-rss-feeds

    $ docker-compose up --build

```

## Deploy

Foi realizado o deploy no Heroku, veja em https://flask-rss-feeds.herokuapp.com.
