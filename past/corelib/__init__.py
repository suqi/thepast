#-*- coding:utf-8 -*-

from past import config 
from past.model.user import User
from past.utils import randbytes

def auth_user_from_session(session_):
    user = None
    if config.SITE_COOKIE in session_:
        cookies = session_[config.SITE_COOKIE]
        user_id, session_id = cookies.split(":")
        _user = User.get(user_id)
        if _user and _user.session_id == session_id:
            user = _user

    return user 

def set_user_cookie(user, session_):
    if not user:
        return None
    session_id = user.session_id if user.session_id else randbytes(8)
    session_[config.SITE_COOKIE] = "%s:%s" % (user.id, session_id)


def logout_user(user):
    if not user:
        return 
    user.clear_session()

