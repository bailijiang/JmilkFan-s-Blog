# import Flask Script object
from flask.ext.script import Manager, Server
import main


manager = Manager(main.app)


manager.add_command("server", Server())

@manager.shell
def make_shell_context():


    return dict(app=main.app)

if __name__ == '__main__':
    manager.run()