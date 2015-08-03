#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from quokka.core.templates import render_template
from flask.ext.wtf.recaptcha import RecaptchaField
from .models import User
from flask.ext.wtf import Form


class UserForm(Form):
    recaptcha = RecaptchaField()


class AccountView(MethodView):

    form = model_form(
        User,
        base_class=UserForm
    )

    def render_context(self, form):
        return render_template('content/account.html',
                               form=form)

    def get(self):
        return self.render_context(form=self.form())
