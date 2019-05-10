#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

"""
Package DxLogging
"""

import logging

VERSION = 'v.0.1.005'

def logging_est(logfile_path, debug=False):
    """
    Establish Logging

    logfile_path: path to the logfile. Default: current directory.
    debug: Set debug mode on (True) or off (False). Default: False
    """

    logging.basicConfig(filename=logfile_path,
                        format='%(levelname)s:%(asctime)s:%(message)s',
                        level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger()

    if debug is True:
        logger.setLevel(10)
        print_info('Debug Logging is enabled.')


def print_debug(print_obj, debug=False):
    """
    Call this function with a log message to prefix the message with DEBUG

    print_obj: Object to print to logfile and stdout
    debug: Flag to enable debug logging. Default: False
    :rtype: None
    """
    try:
        if debug is True:
            print 'DEBUG: {}'.format(str(print_obj))
            logging.debug(str(print_obj))
    except:
        pass


def print_info(print_obj):
    """
    Call this function with a log message to prefix the message with INFO
    """
    print 'INFO: {}'.format(str(print_obj))
    logging.info(str(print_obj))

def print_warning(print_obj):
    """
    Call this function with a log message to prefix the message with INFO
    """
    print 'WARN: %s' % (str(print_obj))
    logging.warn(str(print_obj))

def print_exception(print_obj):
    """
    Call this function with a log message to prefix the message with EXCEPTION
    """
    print str(print_obj)
    logging.exception('EXCEPTION: {}'.format(str(print_obj)))