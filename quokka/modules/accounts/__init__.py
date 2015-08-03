# coding: utf8
from quokka.core.app import QuokkaModule
from .views import AccountView

module = QuokkaModule('accounts', __name__, template_folder='templates')
module.add_url_rule('/accounts/new/',
                    view_func=AccountView.as_view('accounts'))
