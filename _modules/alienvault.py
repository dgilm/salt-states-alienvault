'''
Alienvault module for Salt execution

:maintainer:    David Gil <dgil@a3sec.com>
:maturity:      new
:depends:       python-mysqldb, ossim-cd-tools
:platform:      all
'''
import logging

import salt.utils

log = logging.getLogger(__name__)


# Check before loading the module
def __virtual__():
    return 'alienvault' \
        if __grains__['kernel'] == 'Linux' and __grains__['os'] == 'Debian' \
        else False


def __config_read():
    '''
    Read alienvault global configuration file
    '''

    import StringIO
    import ConfigParser
    import os

    alienvault_config = '/etc/ossim/ossim_setup.conf'
    if not os.path.isfile(alienvault_config):
        return None

    # default ossim_setup file comes with no main header!
    # append [root] as main header to be able to use ParserConfig
    config_str = '[root]\n' + open(alienvault_config, 'r').read()
    config_fp = StringIO.StringIO(config_str)

    config = ConfigParser.RawConfigParser()
    config.readfp(config_fp)

    return config


def profile():
    '''
    Return the host profile for Alienvault minions

    CLI Example::

        salt '*' alienvault.profile
    '''
    profile = "Not an AV host"
    config = __config_read()
    if config:
        profile = config.get('root', 'profile')
    return profile


def update():
    '''
    Update the Alienvault minion

    CLI Example::

        salt '*' alienvault.update
    '''
    cmd = 'alienvault-update -c -q'
    out = __salt__['cmd.run_stdout'](cmd)
    return out


def update_feed():
    '''
    Update the Alienvault minion feed

    CLI Example::

        salt '*' alienvault.update_feed
    '''
    cmd = 'alienvault-update -c -q --feed'
    out = __salt__['cmd.run_stdout'](cmd)
    return out


def versions():
    '''
    Return versions of alienvault packages installed

    CLI Example::

        salt '*' alienvault.versions
    '''

    versions = {}

    # alienvault specific packages
    av_pkg_list = (
        'alienvault-directives-pro',
        'ossim-server',
        'alienvault-logger',
        'ossim-agent',
        'ossim-framework',
        'snort-rules-default',
    )

    all_pkgs = __salt__['pkg.list_pkgs']()

    for p in av_pkg_list:
        if all_pkgs.has_key(p):
            versions[p] = all_pkgs[p]

    return versions


def query(dbname, query):
    '''
    Query to the Alienvault database.

    CLI Example::

        salt '*' alienvault.query alienvault 'select hostname from host'
    '''
    import MySQLdb

    conn = None
    result = {}
    config = __config_read()

    if not config:
        return None

    try:
        conn = MySQLdb.connect(config.get('database', 'db_ip'),
                               config.get('database', 'user'),
                               config.get('database', 'pass'),
                               dbname)
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()

    except MySQLdb.Error, e:
        log.error('Error executing query: {0}'.format(e.args[1]))
        return {}

    finally:
        if conn:
            conn.close()

    return result


def count_db(dbname, table):
    '''
    Get number of items in a database table

    CLI Example::

        salt '*' alienvault.count_db alienvault_siem acid_event
    '''
    count = 0
    q = "SELECT count(*) FROM {0}".format(table)
    result = query(dbname, q)
    if result:
        return result[0][0]
    return count


def logger_total_logs():
    '''
    Get the total number of logs stored in Alienvault Logger

    CLI Example::
        salt '*' alienvault.logger_total_logs
    '''

    import os

    LOGS_DIR = '/var/ossim/logs'
    numlogs = 0

    if not os.path.exists(LOGS_DIR):
        return numlogs

    for root, dirs, files in os.walk(LOGS_DIR):
        if 'count.total' in files:
            with open(os.path.join(root, 'count.total')) as count_total:
                numlogs += int(count_total.read())

    return numlogs


if __name__ == "__main__":
    print profile()
    print query('alienvault', 'select count(*) from host')
    print count_db('alienvault_siem', 'acid_event')
