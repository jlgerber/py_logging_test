#!/usr/bin/env python2
"""
example
"""
from optparse import OptionParser
import logging,logging.config
import pprint
pp = pprint.PrettyPrinter(indent=4)

from logging_eg import customfilter
from logging_eg import constants
from logging_eg import update
from logging_eg import predicates

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

def main():
    parser = OptionParser(usage="usage: %prog [options]",
                          version="%prog 1.0")
    parser.add_option("-f", "--farm",
                      action="store_true",
                      dest="on_farm",
                      default=False,
                      help="Pretend we are running on the farm")
    parser.add_option("-v", "--verbose",
                      action="store_true",
                      dest="verbose",
                      default=False,
                      help="Print out internal state")

    (options, args) = parser.parse_args()

    if options.on_farm == True:
        doit("FARM1", options.verbose)
    else:
        doit(None, options.verbose)


def doit(farm=None, verbose=False):
    os.environ[constants.AD_SHOW] = "SRGTBILKO"
    os.environ[constants.AD_USER] = "clu"
    os.environ[constants.AD_OS] = "cent7_64"

    farm_str = "LOCAL"
    if not farm is None:
        os.environ[constants.AD_FARM] = farm
        farm_str = farm
    config = update.config(predicates.on_farm, LOGGING, FARM)
    if verbose:
        print "------------------------"
        print "CONFIGURATION DICTIONARY"
        print "------------------------"
        pp.pprint(config)
        print ""
        print "------------------------"
        print "    OUTPUT ({})".format(farm_str)
        print "------------------------"
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
    main()