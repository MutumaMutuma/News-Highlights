import os

class Config:
    '''
    The general configuration which is the parent class
    '''

    MOVIE_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}
'''
We then create a dictionary config_options to help us access different configuration option classes.
'''