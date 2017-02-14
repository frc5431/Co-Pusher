from __future__ import print_function

from jsonmerge import merge

import os
import platform
import json
class Config(object):

    def __init__(self):
        self._upload_config = json.load(Config._get_upload_config())
        self._advanced_config = json.load(Config._get_advanced_config())
        self._merged_config = merge(self._upload_config, self._advanced_config)

    @staticmethod
    def _get_current_dir():
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def _get_config_dir():
        return Config._get_current_dir() + "/config"

    @staticmethod
    def _get_upload_config():
        return open(Config._get_config_dir() + "/upload.json", 'r')

    @staticmethod
    def _get_advanced_config():
        return open(Config._get_config_dir() + "/advanced.json", 'r')

    def __getitem__(self, key):
        try:
            return self._merged_config.__getitem__(key)
        except KeyError as err:
            print("CONFIGURATION ERROR... The configuration key %s doesn't exist!" % err.message)
            exit(1)
            return None
    
    @staticmethod
    def get_system_type():
        system_type = str(platform.system())
        if "win" in system_type.lower():
            return "win"
        else:
            return "nix"
