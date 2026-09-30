import json
import network
import urequests
import machine 

FW_VERSION = 'trmnl-mp 0.0.1'

print(f'Hello v{FW_VERSION}')

# Default refresh rate
refresh_rate = 5 * 1000; 
CONFIG_FILE = 'config.json'

try: 
  # load config
  print(f'[config] load {CONFIG_FILE}')
  config = json.load(open(CONFIG_FILE, 'r'))
  print(config)
  
  # connect to wifi
  ssid = config['wifi']['ssid']
  password = config['wifi']['password']
  print(f'[wifi] connect to {ssid}')
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect(ssid, password)
  
  # connect to api
  headers = {
    "ID":  ubinascii.hexlify(machine.unique_id(), ':').decode().upper(),
    "Access-Token": config['display']['api_key'],
    "Battery-Voltage": '0',
    "FW-Version": FW_VERSION,
    "RSSI": str(wlan.status('rssi')),
  }
  base_url = config['trmnl']['base_url']

  # TODO call log API with error.log content if not empty and delete the file on success
  
  # call display API
  print(f'[api] display {base_url}')
  api_display = urequests.get(base_url + '/api/display', headers=headers)
  config['display'] = api_display.json()
  api_display.close()
  
  # update config
  json.dump(config, open(CONFIG_FILE + ".tmp", "w"))

  # override default refresh 
  refresh_rate = config['device']['refresh_rate']
  
  # download image
  image_url = config['display']['image_url']
  print(f'[api] image {image_url}')
  api_img = urequests.get(image_url)
  open(dest_path, "wb").write(api_img.content)
  api_img.close()
  
  # display image 
except Exception as e:
  print('[error]') 
  print(e)
  # TODO save to error.log

print(f'[machine] sleep {refresh_rate}')
machine.deepsleep(refresh_rate)
# reset just in case deepsleep doesn't reset
machine.reset()
