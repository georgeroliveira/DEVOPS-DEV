import os


class Config:
    """Configuração base do TaskManager"""

    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

    PORT = int(os.getenv('PORT', '5000'))
    HOST = os.getenv('HOST', '0.0.0.0')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

    VERSION = '0.1.0'

    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = 'WARNING'


config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}


def get_config():
    """Retorna a configuração baseada na variável ENVIRONMENT"""
    env = os.getenv('ENVIRONMENT', 'development')
    return config_map.get(env, config_map['default'])