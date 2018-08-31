import urllib.request,json
from datetime import datetime

from .models import Source
from .models import Articles

# Getting api key
api_key = None
#Getting the movie base url
base_url = None
#Getting the article base url
