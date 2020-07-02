from flask import Flask
app = Flask(__name__)

import netifaces

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/network')
def network():
    plant_network = netifaces.ifaddresses('eth1')
    plant_network = plant_network[netifaces.AF_INET][0]['addr']

    PLC_network = netifaces.ifaddresses('eth0')
    PLC_network = PLC_network[netifaces.AF_INET][0]['addr']

    return 'Plant:' + plant_network + ' PLC:' + PLC_network

if __name__ == '__main__':
    print('starting....')
    app.run(host='0.0.0.0', port=8080)
