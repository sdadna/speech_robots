cd /home/pi/man_machine_interaction/samples/iat_sample/
chmod 777 32bit_make.sh
make
#设置libmsc.so库搜索路径
export LD_LIBRARY_PATH=$(pwd)/../../libs/RaspberryPi/
cd /home/pi/man_machine_interaction/samples/tts_sample/
chmod 777 32bit_make.sh
make
#设置libmsc.so库搜索路径
export LD_LIBRARY_PATH=$(pwd)/../../libs/RaspberryPi/
cd /home/pi/man_machine_interaction/samples/asr_sample/
chmod 777 32bit_make.sh
make
#设置libmsc.so库搜索路径
export LD_LIBRARY_PATH=$(pwd)/../../libs/RaspberryPi/

cd /home/pi/man_machine_interaction/bin/
python2 interface.py
