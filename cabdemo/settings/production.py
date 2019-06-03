from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7@-qr1ld5e44q@m@!zegp#6dzfak9)yuua#p0md4@v#n$o*&-x'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['dolfin.merucabs.com:5443/outstationdemo'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
