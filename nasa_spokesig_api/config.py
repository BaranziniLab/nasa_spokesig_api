from os.path import expanduser
from os.path import exists
from configparser import ConfigParser
from functools import lru_cache


def config_path():
    for path in (expanduser('~/.nasa_spokesig_api.conf'), '/etc/nasa_spokesig_api.conf'):
        if exists(path):
            return path
        
    raise ValueError(
        'Config not found at ~/.nasa_spokesig_api.conf or /etc/nasa_spokesig_api.conf')
    
@lru_cache
def read_config():
    """Load the config into a ConfigParser, which can be queried with get(), items(), etc."""
    parser = ConfigParser()
    parser.read([config_path()])
    return parser
    