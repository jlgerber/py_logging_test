import logging,logging.config
import pprint
pp = pprint.PrettyPrinter(indent=4)

from logging_eg import customfilter
from logging_eg import constants
from logging_eg import update
import os

LOGGING = {
        'version': 1,
        'filters': {
            'adfilter': {
                '()': customfilter.AdFilter,
            }
        },
        'formatters': {
            'detailed': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
            },
            'ad': {
                'class': 'logging.Formatter',
                'format': constants.AD_FORMAT
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'WARN',
                'formatter': 'ad',
                'filters': ['adfilter']
            },
            'adconsole': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'ad',
                'filters': ['adfilter']
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'mplog.log',
                'mode': 'w',
                'formatter': 'detailed',
            },
            'adfile': {
                'class': 'logging.FileHandler',
                'filename': 'mplog.log',
                'mode': 'w',
                'formatter': 'ad',
                'filters': ['adfilter']
            },
            'errors': {
                'class': 'logging.FileHandler',
                'filename': 'mplog-errors.log',
                'mode': 'w',
                'level': 'ERROR',
                'formatter': 'detailed',
            },
        },
        'loggers': {
            # the level is set in the handlers
            'ad': {
                'level': 'DEBUG',
                # propagate is false so that we can handle logging
                # separately for AD and Root level logging. This
                # does force us to register separate console handlers for
                # the root
                'propagate': False,
                'handlers': ['adfile', 'adconsole']
            }
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
    }

FARM = {
        'handlers': {
            'adconsole': {
                'level': 'DEBUG'
            },
            'console': {
                'level': 'DEBUG',
            },
        }
    }


def doit(farm=None):
    os.environ[constants.AD_SHOW] = "SRGTBILKO"
    os.environ[constants.AD_USER] = "clu"
    os.environ[constants.AD_OS] = "cent7_64"

    if not farm is None:
        os.environ[constants.AD_FARM] = farm
    config = update.config(update.on_farm_predicate, LOGGING, FARM)
    pp.pprint(config)

    logging.config.dictConfig(config)

    root_log = logging.getLogger()
    ad_log = logging.getLogger("ad."+ __name__)

    root_log.debug("a root debug message")
    ad_log.debug("an ad debug message")

    root_log.info("a root info message")
    ad_log.info("an ad info message")

    root_log.warn("a root warn message")
    ad_log.warn("an ad warn message")


if __name__ == "__main__":
    import sys
    farm = sys.argv[1] if len(sys.argv)>1 else None
    doit(farm)