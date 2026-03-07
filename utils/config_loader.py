import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# __file__ = utils/config_loader.py
# dirname once = utils/
# dirname twice = project root

with open(os.path.join(BASE_DIR, "data", "config.json")) as f:
    config = json.load(f)
