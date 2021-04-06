VERSION = (1, 0, 0, 'dev6')
__version__ = '.'.join(map(str, VERSION))

from .events import config_inited, embed_analytics_code


def setup(app):
    app.add_config_value('analytics', None, True)
    app.connect('config-inited', config_inited)
    app.connect('builder-inited', embed_analytics_code)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
