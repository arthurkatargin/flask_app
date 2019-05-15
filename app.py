from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_ckeditor import CKEditor
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# ADMIN #
from models import *


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


# class AdminView(AdminMixin, ModelView):
#     pass


# class HomeAdminView(AdminMixin, AdminIndexView):
#     pass


# class PostAdminView(AdminMixin, BaseModelView):
#     pass


# class GostAdminView(AdminMixin, BaseModelView):
#     pass


admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Gost, db.session))

# Security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
