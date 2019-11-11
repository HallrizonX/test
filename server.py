import gunicorn.app.base
from main.wsgi import application


class Application(gunicorn.app.base.BaseApplication):
    def load_config(self):
        return {
            'workers': 30,
            'bind': 'unix:/root/projects/chat/chat.sock',
        }

    def load(self):
        return application


def run():
    Application().run()


if __name__ == '__main__':
    import multiprocessing

    server = multiprocessing.Process(target=run)
    server.start()
