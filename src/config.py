import json
import os

CONFIG_FILE = "config.json"

DEFAULT = {
  "wifi": {
    "ssid": "",
    "password": "",
  },
  "trmnl": {
    "url": ""
  }
}

config = DEFAULT
wifi = config.wifi
trmnl = config.trmnl

def load():
  try:
    with open(CONFIG_FILE, "r") as f:
      config = json.load(f)
      wifi = config.wifi
      trmnl = config.trmnl
  except (OSError, ValueError):
    print("Config file missing or corrupt.")

def save(): 
  try:
    with open(CONFIG_FILE + ".tmp", "w") as f:
      json.dump(config, f)
    os.rename(CONFIG_FILE + ".tmp", CONFIG_FILE); 
    print("Configuration saved successfully!")
  except OSError:
    print("Failed to write configuration file.")

def has(block):
  return config[block] != DEFAULT[block] 
