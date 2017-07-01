#!/bin/bash
#

CUR_PATH=$(pwd)
IAT_PATH=$CUR_PATH/voice/samples/iat_sample
TTS_PATH=$CUR_PATH/voice/samples/tts_sample

cd $IAT_PATH
source 32bit_make.sh

cd $TTS_PATH
source 32bit_make.sh

#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUR_PATH/voice/libs/RaspberryPi
