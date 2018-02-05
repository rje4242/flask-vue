import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from app.api import models

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


def main():
    manager.run()


if __name__ == '__main__':
    main()
