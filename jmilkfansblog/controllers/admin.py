from flask_admin import BaseView, expose
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from jmilkfansblog.forms import CKTextAreaField
from flask_login import login_required, current_user
from jmilkfansblog.extensions import admin_permission

class CustomView(BaseView):

    @expose('/')
    @login_required
    @admin_permission.require(http_exception=403)
    def index(self):
        return self.render('admin/custom.html')

    @expose('/second_page')
    @login_required
    @admin_permission.require(http_exception=403)
    def second_page(self):
        return self.render('admin/second_page.html')

class CustomModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated() and admin_permission.can()

class CustomFileAdmin(FileAdmin):
    pass


class PostView(CustomModelView):
    # Using the CKTextAreaField to replace the Field name is 'text'
    form_overrides = dict(text=CKTextAreaField)

    # Using Search box
    column_searchable_list = ('text', 'title')

    # Using Add Filter box
    column_filters = ('publish_date',)

    # Custom the template for PostView
    # Using js Editor of CKeditor
    create_template = 'admin/post_edit.html'
    edit_template = 'admin/post_edit.html'

class CustomFileAdmin(FileAdmin):

    def is_accessible(self):
        return current_user.is_authenticated() and admin_permission.can()