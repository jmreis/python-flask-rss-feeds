import feedparser
from flask import Flask
from flask import render_template


app = Flask(__name__)

RSS_FEEDS = {
	'g1' : 'http://g1.globo.com/dynamo/brasil/rss2.xml',
	'uol' : 'https://rss.uol.com.br/feed/noticias.xml',
	'folha' : 'https://feeds.folha.uol.com.br/emcimadahora/rss091.xml',
	'r7' : 'http://noticias.r7.com/feed.xml',

	
}


#@app.route('/')
@app.route('/g1')
def g1_feeds():
	return get_news('g1')


@app.route('/uol')
def uol_feeds():
	return get_news('uol')


@app.route('/terra')
def terra_feeds():
	return get_news('terra')


@app.route('/folha')
def folha_feeds():
	return get_news('folha')


@app.route('/r7')
def r7_feeds():
	return get_news('r7')


@app.route('/estadao')
def estadao_feeds():
	return get_news('estadao')


@app.route('/msn')
def msn_feeds():
	return get_news('msn')


@app.route('/ig')
def ig_feeds():
	return get_news('ig')


@app.route('/yahoo')
def yahoo_feeds():
	return get_news('yahoo')


@app.route("/")
@app.route("/<publication>")
def get_news(publication="g1"):
	feed = feedparser.parse(RSS_FEEDS[publication])
	first_article = feed['entries'][0]
	return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
	app.run(host='0.0.0.0')