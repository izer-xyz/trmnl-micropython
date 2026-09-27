import network
import socket
import uasyncio as asyncio

def connect(config):
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  print(f"Connecting to network: {config.wifi.ssid}...")
  wlan.connect(config.wifi.ssid, config.wifi.password)
  retry = 10
  while not wlan.isconnected() and retry > 0:
    time.sleep(1)
    retry -= 1
  if wlan.isconnected():
    print("IP Configuration:", wlan.ifconfig()) # (IP, Subnet, Gateway, DNS)
    return True
  else:
    print("Connection failed.")
    return False

def ap(config):
  ap = network.WLAN(network.AP_IF)
  ap.active(True)
  ap.config(
    essid = config.wifi.ssid, 
    authmode = network.AUTH_OPEN
  )
  ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1'))
  asyncio.create_task(dummy_dns())

async def dummy_dns():
    udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udps.setblocking(False)
    udps.bind(('0.0.0.0', 53))
    while True:
        try:
            data, addr = udps.recvfrom(512)
            if len(data) >= 12:
                # Craft a bare-minimum DNS answer pointing to our IP
                response = data[:2] + b'\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00' + data[12:] + b'\xc0\x0c\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04' + IP_BYTES
                udps.sendto(response, addr)
        except OSError:
            pass  # No data waiting to be read
        await asyncio.sleep_ms(10)
