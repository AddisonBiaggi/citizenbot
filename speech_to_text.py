# to run this, you'll need to do:
# pip install openai-whisper
# pip install pydub
# pip install tensorflow

# You'll also need an audio file in m4a or mp3 format to transcribe.
# I ran this in google colab. I haven't tested running it locally.

import whisper
import os
import tensorflow as tf
from pydub import AudioSegment
tenMinutes = 1000 * 60 * 10
sound = AudioSegment.from_file("drive/MyDrive/colab data/audio.m4a")

numChunks = len(sound)//tenMinutes
interval = tenMinutes
progress = 0
for i in range(numChunks):
    if progress + interval > len(sound):
        chunk = sound[progress:]
    else:
        chunk = sound[progress:progress + interval]

    # writing mp3 files is a one liner
    chunk.export("drive/MyDrive/colab data/audio_chunk" + str(i) + ".mp3", format="mp3")
    progress += interval

model = whisper.load_model("base")
allText = ""
textChunks = []
for i in range(numChunks):
    result = model.transcribe("drive/MyDrive/colab data/audio_chunk" + str(i) + ".mp3")
    print(result["text"])
    allText += result["text"]
    textChunks.append(result["text"])

print(allText)

print(textChunks[3])