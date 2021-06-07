from flask import Flask, render_template, wrappers
from webapp.weather import weather_by_city

from webapp.model import db, News
CITY = {'moscow':('55.89','37.47'),'murmansk':('68.97', '33.07')}

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/<city>/')
    def index(city):
        print(city)
        title = 'Новости Python'
        get_city = CITY.get(city, CITY['moscow'])
        weather = weather_by_city(*get_city)
        get_news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title = title, weather_text = weather, news_list = get_news_list)

    return app

    