import os
import feedparser
from flask import Flask
from flask import render_template



app = Flask(__name__)

RSS_FEEDS = {
	'g1' : 'http://g1.globo.com/dynamo/brasil/rss2.xml',
	'uol' : 'https://rss.uol.com.br/feed/noticias.xml',
	'folha' : 'https://feeds.folha.uol.com.br/emcimadahora/rss091.xml',
	'r7' : 'http://noticias.r7.com/feed.xml',
	'aominuto' : 'https://www.noticiasaominuto.com.br/rss/ultima-hora',
	'yahoo' : 'https://br.noticias.yahoo.com/rss'
}


@app.route('/')
@app.route('/g1')
def g1_feeds():
	return get_news('g1')


@app.route('/uol')
def uol_feeds():
	return get_news('uol')


@app.route('/folha')
def folha_feeds():
	return get_news('folha')


@app.route('/r7')
def r7_feeds():
	return get_news('r7')


@app.route('/oaminuto')
def aominuto_feeds():
	return get_news('aominuto')


@app.route('/yahoo')
def yahoo_feeds():
	return get_news('yahoo')


#@app.route("/")
@app.route("/<publication>")
def get_news(publication='g1'):
	feed = feedparser.parse(RSS_FEEDS[publication])
	first_article = feed['entries'][0]
	return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
  	app.run(host = '0.0.0.0', port = port)
