import sys
from generation import generate_audio_from_script, strip_script, check_output_path, write_wav
from numpy import concatenate as np_concatenate
from bark import SAMPLE_RATE
# Usage: python generateScript.py <Script> <Output Name> <Output Path> 
# Example: python generateScript.py "Sun Tzu said: The art of war is of vital importance to the State." generations/TheArtOfWar/Chapter1

if len(sys.argv) != 4:
    print("Usage: python generateScript.py <Script> <Output Name> <Output Path>")
    sys.exit(1)

input = sys.argv[1]
name = sys.argv[2]
output_path = check_output_path(sys.argv[3])
script = strip_script(input)
pieces = generate_audio_from_script(script)
write_wav(f"{output_path}/audio/{name}.wav", SAMPLE_RATE, np_concatenate(pieces))