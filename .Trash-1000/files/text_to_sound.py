# -*- coding: utf-8 -*-
import os

def t_to_s():
    os.system('sh /home/pi/man_machine_interaction/bin/tts.sh')
    print('\n*************转换成功*************\n')
    os.system('mplayer /home/pi/man_machine_interaction/bin/turing.wav')
if __name__ == '__main__':
    t_to_s()
