from models import *

def get_latest_version():
    return Version.objects.latest('release_date')
