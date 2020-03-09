#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Multiprocess with mqtt example


@author: jev
"""

import multiprocessing
import time
import paho.mqtt.client as mqtt
import asyncio


class Process():
    """ process to run separately """
    
    running = True
    counter = 0
    
    def __init__(self,name):
        
        self.name = name
        self.client = mqtt.Client()
        self.client.connect('localhost')
        self.client.subscribe(name+'/cmd')
        self.client.on_message = self.on_message
      
    
    def on_message(self,client,userdata,msg):
        
        txt = msg.payload.decode("utf-8")
        print(msg.topic+" "+ txt)
        if txt == 'stop':
            self.running = False
            print('stopping...')
    
    def main(self):
        
        while self.running:
            #print(f'[{self.name}] counter: {self.counter}')
            self.counter += 1
            self.client.publish(self.name + '/counter',str(self.counter))
            self.client.loop()
            time.sleep(0.5)
            
        print('Process is done.')
        
        
def main():
    """ main function """
    
    p = Process('Fry')
    proc = multiprocessing.Process(target=p.main,daemon=True)
    proc.start()
    
    
    print('Running, press Ctrl-C to stop')
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('Stopping')
        proc.terminate()
        
    
    print('Done.')
    
if __name__=="__main__":
    main()