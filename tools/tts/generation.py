import sys, os
import os
import sys
print(os.path.dirname(sys.executable))
import torch

if(torch.cuda.is_available()):
    print("CUDA is available")
else:
    print("CUDA is not available")

from bark import SAMPLE_RATE, generate_audio, preload_models
from bark.generation import (
    generate_text_semantic,
    preload_models,
)
from bark.api import semantic_to_waveform
from scipy.io.wavfile import write as write_wav
import nltk
import numpy as np
import sys
nltk.download('punkt')

print("Preloading models...")
preload_models()

def strip_script(script):
    return script.replace("\n", "").strip()

def generate_audio_from_script(script, SPEAKER="v2/en_speaker_6"):
    
    sentences = nltk.sent_tokenize(script)
    GEN_TEMP = 0.6
    silence = np.zeros(int(0.25 * SAMPLE_RATE))  # quarter second of silence

    pieces = []
    for sentence in sentences:
        semantic_tokens = generate_text_semantic(
            sentence,
            history_prompt=SPEAKER,
            temp=GEN_TEMP,
            min_eos_p=0.05,  # this controls how likely the generation is to end
        )

        audio_array = semantic_to_waveform(semantic_tokens, history_prompt=SPEAKER,)
        pieces += [audio_array, silence.copy()]

    return pieces

def check_output_path(output_path):
    print(f"before: {output_path}")
    if not os.path.exists(output_path):
        os.makedirs(f"{output_path}/audio")
    #check if folder exists with the title and if yes add a number to the title
    elif os.path.exists(output_path):
        i = 1
        while os.path.exists(output_path + str(i)):
            i += 1
        output_path = output_path + str(i)
        os.makedirs(f"{output_path}/audio")
    print(f"after: {output_path}")
    return output_path

def generate_chapter(title, chapter_number, chapter_text, output_path="generations"):
    title_str = strip_script(title)
    title_pieces = generate_audio_from_script(title_str)
    script = strip_script(chapter_text)
    script_pieces = generate_audio_from_script(script)
    write_wav(f"{output_path}/audio/{chapter_number}_{title}.wav", SAMPLE_RATE, np.concatenate(title_pieces + script_pieces))