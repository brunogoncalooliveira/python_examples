import os
import sys
from pynput import keyboard

class KeyEvents:
    """
    #
    # use it like this to detect keypresses and keyreleases
    #
    import keyevents

    def kpress(k):
        print('press ' + str(k))

    def krelease(k):
        print('release ' + str(k)) 

    a = keyevents.KeyEvents(kpress, krelease)
    """
    def __init__(self, keypress, keyrelease):
        print('init')
        self.keypress = keypress
        self.keyrelease = keyrelease
        self.tecla = None
        self.main()

    def on_press(self, key):
        if self.tecla == None:
            try:
                self.tecla = key.vk
            except AttributeError:
                self.tecla = key.value.vk
            self.keypress(self.tecla)


    def on_release(self, key):
        self.keyrelease(self.tecla)
        self.tecla = None
        if key == keyboard.Key.esc:
            # Stop listener
            return False


    def main(self):
        try:
            with keyboard.Listener( on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()

        finally:
            #ser.close()
            print('fim do programa')
