from __future__ import print_function

from configurations import Config

import time


class Logger(object):

    def __init__(self, namespace = "COPUSH"):
        self.namespace = namespace

    def log(self, toLog, error = 0):
        if error == 0:
            first_color = Logger._n_color() 
        elif error == 1:
            first_color = Logger._r_color() + "(ERROR) -> "
        elif error == 2:
            first_color = Logger._y_color() + "(WARNING) -> "
        else:
            first_color = Logger._g_color() + "(SUCCESS) -> "

        second_color = Logger._n_color()
        
        print("[%s]|%s%s%s|: %s%s%s" % (
            Logger._get_current_date_time(), 
            Logger._b_color(), 
            self.namespace, 
            Logger._n_color(), 
            first_color,
            str(toLog),
            second_color))

    def logerr(self, toLog):
        self.log(toLog, 1)

    def logwarn(self, toLog):
        self.log(toLog, 2)

    def loggood(self, toLog):
        self.log(toLog, 3)
    
    @staticmethod
    def _n_color():
        return "\033[0m"

    @staticmethod
    def _r_color():
        return "\033[0;31m"

    @staticmethod
    def _g_color():
        return "\033[0;32m"

    @staticmethod
    def _b_color():
        return "\033[0;34m"

    @staticmethod
    def _y_color():
        return "\033[1;33m"

    @staticmethod
    def _get_current_date_time():
        return time.strftime("%c")
