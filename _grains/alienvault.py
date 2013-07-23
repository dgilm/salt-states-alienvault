import os
import StringIO
import ConfigParser


def _profile():
    '''
    Return the host profile for Alienvault minions
    '''
    alienvault_config = '/etc/ossim/ossim_setup.conf'
    if not os.path.isfile(alienvault_config):
        return {}

    # default ossim_setup file comes with no main header!
    # append [root] as main header to be able to use ParserConfig
    config_str = '[root]\n' + open(alienvault_config, 'r').read()
    config_fp = StringIO.StringIO(config_str)

    config = ConfigParser.RawConfigParser()
    config.readfp(config_fp)
    profile = config.get('root', 'profile')

    return profile


def alienvault_is_allinone():
    '''
    Check if minion is an AV all-in-one
    '''
    return {'alienvault_is_allinone':
            'Server' and 'Framework' and 'Sensor' and 'Database' in _profile()}


def alienvault_is_server():
    '''
    Check if minion is an AV Server
    '''
    return {'alienvault_is_server': 'Server' in _profile()}


def alienvault_is_framework():
    '''
    Check if minion is an AV Framework
    '''
    return {'alienvault_is_framework': 'Framework' in _profile()}


def alienvault_is_sensor():
    '''
    Check if minion is an AV Sensor
    '''
    return {'alienvault_is_sensor': 'Sensor' in _profile()}


def alienvault_is_database():
    '''
    Check if minion is an AV Database
    '''
    return {'alienvault_is_server': 'Database' in _profile()}
