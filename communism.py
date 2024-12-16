from pyaudio import paInt16, PyAudio
import wave
import keyboard
import time
import understanding


CHUNK = 1024
FORMAT = paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

#p = pyaudio.PyAudio()
recording = False
'''stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
frames = []'''


def on_press_a(e):
    global frames, recording, stream, p
    if not recording:
        recording = True
        p = PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        frames = []
        print('Recording...')


def on_release_a(e):
    global frames, stream, recording, p
    if recording:
        print("Finished")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        recording = False
        understanding.STT("output.wav")


#keyboard.on_press_key("a", on_press_a)
#keyboard.on_release_key("a", on_release_a)
print(f"{understanding.name} is ready!")
while True:
    try:
        if keyboard.is_pressed('ctrl+alt+a'):
            on_press_a(1)
            while keyboard.is_pressed('ctrl+alt+a'):
                data = stream.read(CHUNK, exception_on_overflow=False)
                frames.append(data)
            on_release_a(1)
        else:
            time.sleep(0.1)
        #data = stream.read(CHUNK, exception_on_overflow=False)
        #frames.append(data)
    except OSError:
        pass

