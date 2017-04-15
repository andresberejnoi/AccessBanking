#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:50:49 2017
"""

import json
import base64
import requests

def get_api_key():
    with open("key.txt","r") as f:
        key = f.readline().rstrip()
    return key
#API url
if __name__=='__main__':
    #audio file
    audio_file = "man_audio.flac"
    # encoding audio file with Base64 (~200KB, 15 secs)
    with open(audio_file, 'rb') as speech:
        speech_content = base64.b64encode(speech.read())
    
    api_func = "syncrecognize?key=" + get_api_key()
    api_url = "https://speech.googleapis.com/v1beta1/speech:" + api_func
    print(api_url)
    
    #define json file
    recognize = {"congig":{"encoding":"FLAC",
                           "sample_rate":16000,
                           "language_code":"en-US"},
                 "audio":{"content":speech_content.decode('UTF-8')}
                 }
    
    audio_data = json.dumps(recognize)
    req = requests.post(api_url, data=audio_data)

