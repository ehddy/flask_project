from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

db = SQLAlchemy()
migrate = Migrate()

# 애플리케이션 팩토리 
def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    # markdown nl2br는 줄바꿈 문자를 <br>로 대체, fenced_code는 코드 표시 기능을 위해 추가
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models 
    from .views import main_views, question_views, answer_views, plotly_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(plotly_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터 
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime



    # # 애너테이션
    # @app.route('/')
    # # 라우팅 함수
    # def hello_pybo():
    #     return 'Hello, Pybo!'

    return app
