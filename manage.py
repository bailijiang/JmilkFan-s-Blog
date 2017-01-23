# import Flask Script object
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from jmilkfansblog import app, models

manager = Manager(app)
migrate = Migrate(app, models.db)

manager.add_command("runserver", Server())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag,)


if __name__ == '__main__':
    manager.run()
