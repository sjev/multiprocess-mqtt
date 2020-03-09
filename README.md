# multiprocess-mqtt
example prototype of a framework running multiple processes with mqtt messaging 


## MQTT server

for this example a local mqtt server is required. We'll use mosquitto

`mosquitto -p 1883 -v`   - start server

`mosquitto_sub -h localhost -t "#" -v` - listen to events


## MQTT python client

`conda install -c conda-forge paho-mqtt`  ( or install with pip)


## Useful examples

[Sonoff Micropython](https://github.com/havnfun/micropython-sonoff-basic/blob/master/control.py)