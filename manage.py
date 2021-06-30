from app import app
import route
import config
if __name__ == "__main__":
    app.run(
        host=config.app.config['HOST'],
        port=config.app.config['PORT'],
        debug=config.app.config['DEBUG']
    )
else:
    pass
