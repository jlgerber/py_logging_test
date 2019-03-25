#!/usr/bin/env python2
"""
example
"""
from optparse import OptionParser
import logging,logging.config
import pprint
pp = pprint.PrettyPrinter(indent=4)
from itertools import izip

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

def fake_lib_mod():
    """
    fake a library module, which would be logging to a non-dd log
    """
    root_log = logging.getLogger("3ps")
    root_log.debug("a root debug message")
    yield 1
    root_log.info("a root info message")
    yield 1
    root_log.warn("a root warn message")
    yield 1

def fake_ad_mod():
    """
    fake root ad module
    """
    ad_log = logging.getLogger("ad."+ __name__)

    ad_log.debug("an ad debug message")
    yield 1
    ad_log.info("an ad info message")
    yield 1
    ad_log.warn("an ad warn message")
    yield 1

def fake_adfoo_mod():
    """
    fake ad.foo module
    """
    ad_foo_log = logging.getLogger("ad.foo")

    ad_foo_log.debug("an ad.foo debug message")
    yield 1
    ad_foo_log.info("an ad.foo info message")
    yield 1
    ad_foo_log.warn("an ad.foo warn message")
    yield 1

def doit(farm=None, verbose=False):
    # fake the setup of the environment
    os.environ[constants.AD_SHOW] = "SRGTBILKO"
    os.environ[constants.AD_OS] = "cent7_64"

    # setup farm
    farm_str = "LOCAL"
    if not farm is None:
        os.environ[constants.AD_FARM] = farm
        farm_str = farm

    # update config dict
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

    # Setup logging
    logging.config.dictConfig(config)

    for _,_,_ in izip(
        fake_lib_mod(),
        fake_ad_mod(),
        fake_adfoo_mod()
    ):
        pass

if __name__ == "__main__":
    main()