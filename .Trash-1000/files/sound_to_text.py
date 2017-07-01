import os
def s_to_t():
    os.system('sudo arecord -D "plughw:1,0" -d 3 -r 16000 -f S16_LE > /home/pi/man_machine_interaction/bin/man.wav')
    os.system('sh /home/pi/man_machine_interaction/bin/iat.sh')
if __name__ == '__main__':
    s_to_t()
