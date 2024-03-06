import pyautogui
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import subprocess
import time
import os
import threading
import tkinter as tk


class ScreenRecorder:
    def __init__(self):
        self.duration = 0
        self.video_filename = "screen_capture.mp4"
        self.audio_filename = "audio_capture.wav"
        self.recording = False

    def start_recording(self, duration):
        self.duration = duration
        self.recording = True
        self.record_audio_thread = threading.Thread(target=self.record_audio)
        self.record_audio_thread.start()
        self.record_screen_with_audio()

    def stop_recording(self):
        self.recording = False

    def record_audio(self):
        fs = 44100  # Sample rate
        seconds = self.duration

        print("Recording audio...")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished

        print("Saving audio to", self.audio_filename)
        write(self.audio_filename, fs, myrecording)

    def record_screen_with_audio(self):
        # Get screen resolution
        screen_width, screen_height = pyautogui.size()

        # Set up subprocess to call ffmpeg command
        command = [
            'ffmpeg',
            '-y',
            '-f', 'gdigrab',
            '-framerate', '30',
            '-video_size', f'{screen_width}x{screen_height}',
            '-i', 'desktop',
            '-f', 'pulse',
            '-i', 'default',
            '-t', str(self.duration),
            '-c:v', 'libx264',
            '-preset', 'ultrafast',
            '-crf', '0',
            '-c:a', 'aac',
            '-strict', 'experimental',
            '-b:a', '256k',
            '-pix_fmt', 'yuv420p',
            '-threads', '0',
            self.video_filename
        ]

        print("Recording screen with audio...")
        self.ffmpeg_process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
        while self.recording:
            time.sleep(0.1)
        self.ffmpeg_process.kill()


class App:
    def __init__(self, master):
        self.master = master
        self.screen_recorder = ScreenRecorder()

        self.label = tk.Label(master, text="Screen Recorder")
        self.label.pack()

        self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack()

    def start_recording(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        duration = 10  # Duration of recording in seconds
        self.screen_recorder.start_recording(duration)

    def stop_recording(self):
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.screen_recorder.stop_recording()


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()

