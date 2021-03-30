import pyaudio
import wave

# Constants #
SOUND_FILE_DIR = "audio_src/" # Root audio file directory


# Instance #
chunk = 1024
data = None

# Plays an audio file
# @param filename - Specify the file name
def play_audio(filename):
    if (filename != ""):
        try:
            wf = wave.open(SOUND_FILE_DIR + filename)
            p = pyaudio.PyAudio() # PyAudio Obj
            stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
            data = wf.readframes(chunk)
            # play stream (3)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(chunk)
            # stop stream (4)
            stream.stop_stream()
            stream.close()
            # close PyAudio (5)
            p.terminate()
        except:
            print('Error: File ' + filename + ' was not found!')
    else:
        print('Error: Filename not recognized!')

# is playing method
def isPlaying():
    if(data > 0):
        return data
    else:
        return data