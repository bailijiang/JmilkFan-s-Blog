# import Flask Script object
from flask_script import Manager, Server
import main
import models

manager = Manager(main.app)


manager.add_command("runserver", Server())

@manager.shell
def make_shell_context():


    return dict(app=main.app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag)

if __name__ == '__main__':
    manager.run()