# -*- coding: utf-8 -*-  

from pyvirtualdisplay import Display

display = Display(visible=0, size=(1280, 960))
class DisplayLib(object):
    """docstring for Display"""
    def __init__(self):
        pass

    ## open virtual dispaly
    def start_display(self):
        display.start()
      
    ## close virtual dispaly
    def stop_dispaly(self):
        display.stop()
