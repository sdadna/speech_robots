#!/usr/bin/python
#coding:utf-8

import requests
import json
import wave
import pyaudio
import os
from pydub import AudioSegment

def trans_rate(intput_file):
    sound = AudioSegment.from_file(intput_file)
    s = sound.set_frame_rate(16000)
    s.export(intput_file, format="wav")

def record_sound(wave_file):
	CHUNK = 4096
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = wave_file

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()


	trans_rate(WAVE_OUTPUT_FILENAME)

def sound_to_text(wave_input, intput_file):
	current_path = os.getcwd()
	print current_path
	os.chdir(r"voice/bin")

	wavefile = wave_input.split('/').pop()
	textfile = intput_file.split('/').pop()
	commands = "./iat_sample" + " " + wavefile + " " + textfile
	print commands
	os.system(commands)

	os.chdir(current_path)
	current_path = os.getcwd()
	print current_path

def text_to_sound(wave_input,intput_file):
	current_path = os.getcwd()
	print current_path
	os.chdir(r"voice/bin")

	wavefile = wave_input.split('/').pop()
	textfile = intput_file.split('/').pop()
	commands = "./tts_sample" + " " + wavefile + " " + textfile
	print commands
	os.system(commands)

	os.chdir(current_path)
	current_path = os.getcwd()
	print current_path

def play_sound(wave_file):
	commands = "aplay " + wave_file 
	print commands
	os.system(commands)

def get_response(intput_file, output_file):
    KEY = 'd8a55e7b5b06450d927e3c5132fffb0d'    
    url = 'http://www.tuling123.com/openapi/api'
    #从write_text.txt中获取用户输入文本
    t = open(intput_file,'r')
    req_info = t.readline()
    print(req_info)
    t.close()
    #图灵接口
    query = {'key': KEY, 'info': req_info}
    headers = {'Content-type': 'text/html', 'charset': 'utf-8'}
    response = requests.get(url, params=query, headers=headers)
    res = response.text
    res_text = (json.loads(res).get('text').replace('<br>', '\n'))
    #向read_text.txt中写入图灵反馈文本
    f = open(output_file,'w')
    f.write(res_text.encode('utf-8'))
    print(res_text)
    f.close()

def start():
	intput_file="voice/bin/write_text.txt"
	output_file="voice/bin/read_text.txt"
	wave_input="voice/bin/input.wav"
	wave_output="voice/bin/output.wav"
	#while True:
	record_sound(wave_input)
	sound_to_text(wave_input,intput_file)
	get_response(intput_file, output_file)
	text_to_sound(wave_output,output_file)
	play_sound(wave_output)
	

if __name__ == "__main__":
	start()
