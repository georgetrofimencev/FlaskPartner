from betronic import create_app
from flask_restful import Api
from flask_mail import Mail
from core.setup_api import setup_api


#  *** returns app instance ***
app = create_app()

#  *** initialize Flask tools ***
api = Api(app)
mail = Mail()

#  *** setup api resources ***
setup_api(api)

#  *** connects flask extensions to the app ***
mail.init_app(app)


if __name__ == '__main__':
    app.run()
