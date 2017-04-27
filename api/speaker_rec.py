"""References:

https://www.slideshare.net/mchua/sigproc-selfstudy-17323823

"""

import tensorflow as tf
import numpy as np
import scipy
from scipy.io import wavfile        #works with 16 and 32 bit audio files, but not 24
import pyaudio as pa
import sys
#from scipy.io.wavfile import read   #reads wavfiles

def readSoundData(filename):
    data = wavfile.read(filename)[1] #read function returns rate and data. Here we are just taking the data
    return data

def writeSoundData(outname,samplerate,data):
    wavfile.write(outname,samplerate,data)

#Create network model (LSTM seems like a good choice)
def LSTM_net(data):
    """Placeholder function for now. 
    
    """
    inputs = tf.placeholder(dtype=tf.int16)
    hidden_1 = tf.Variable()
    hidden_1 = tf.Variable(tf.random_uniform(shape=[]))
    

if __name__ == '__main__':
    try:
        #provide outfile for sound to be saved to. It has to be .wav for now
        outfile = sys.argv[1]
    except IndexError:
        #if no output filename is proided, use default:
        outfile = "test.wav"
        
    
    #some testing variables
    RATE = 16000
    CHUNKSIZE = 1024
    RECORD_SECONDS = 2.5
    
    #Initializing a PyAudio object
    audio = pa.PyAudio()
    stream = audio.open(format=pa.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)
    
    """
    for i in range(10):
        data = stream.read(CHUNKSIZE)
        numpydata = np.fromstring(data, dtype=np.int16)
        pa.play
    """
    
    #the following for loop is taken from http://stackoverflow.com/questions/24974032/reading-realtime-audio-data-into-numpy-array
    frames = []
    for _ in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
        data = stream.read(CHUNKSIZE)
        frames.append(np.fromstring(data, dtype=np.int16))
    
    #print(numpydata)
    numpydata = np.hstack(frames)
    
    # close stream
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    #write to file
    writeSoundData(outfile,RATE,numpydata)
    
    
    
    
    
    