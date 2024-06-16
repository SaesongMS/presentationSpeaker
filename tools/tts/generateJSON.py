import sys
from generation import generate_chapter, generate_audio_from_script, strip_script, check_output_path
import json
from bark import SAMPLE_RATE
from numpy import concatenate as np_concatenate
from scipy.io.wavfile import write as write_wav
# Usage: python generateJSON.py <json_path>

with open(sys.argv[1]) as f:
    data = json.load(f)

print(data)

title = list(data.keys())[0]
print(title)
chapters = data[title]

output_path = check_output_path(f"generations/{title}")

title = strip_script(title)
title_audio = generate_audio_from_script(title)
write_wav(f"{output_path}/audio/title.wav", SAMPLE_RATE, np_concatenate(title_audio))

counter = 1
for chapter in chapters:
    chapter_title = chapter
    chapter_text = chapters[chapter_title]
    chapter_title = str(''.join(e for e in chapter_title if e.isalnum()))
    generate_chapter(chapter_title, counter, chapter_text, output_path)
    print(f"Chapter {chapter_title} generated and saved")
    counter += 1


print("Done")
