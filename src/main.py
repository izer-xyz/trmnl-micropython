import json
import network
import urequests
import machine 

print('[config] load')

FW_VERSION = '0.0.1'
CONFIG_FILE = 'config.json'
config = json.load(open(CONFIG_FILE, 'r'))

print(config)

print('[wifi] connect')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config['wifi']['ssid'), config['wifi']['password'])

headers = {
  "ID":  ubinascii.hexlify(machine.unique_id(), ':').decode().upper(),
  "Access-Token": config['display']['api_key'],
  "Battery-Voltage": '0',
  "FW-Version": FW_VERSION,
  "RSSI": str(wlan.status('rssi')),
}

print('[api] display')

api_display = urequests.get(config['trmnl']['base_url']) + '/api/display', headers=headers)
config['display'] = api_display.json()
api_display.close()

json.dump(config, open(CONFIG_FILE + ".tmp", "w"))

image_url = config['display']['image_url']

print('[api] image')

api_img = urequests.get(image_url)
open(dest_path, "wb").write(api_img.content)
api_img.close()

// todo display image 

machine.deepsleep(config['device']['refresh_rate'], 5 * 1000))
machine.reset()
