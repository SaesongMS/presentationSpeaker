# Usage: python slides2mp4.py <generations path>
# Example: python slides2mp4.py generations/The Art of War
# generations path should be an generations/{Article Title}, where the images and audio are stored in subdirectories imgs and audio respectively

import os
import sys
import subprocess

if len(sys.argv) != 2:
    print("Usage: python slides2mp4.py <generations path>")
    exit()

generations_path = sys.argv[1]

if not os.path.exists(f"{generations_path}/imgs"):
    print(f"Error: {generations_path}/imgs does not exist")
    exit()
else:
    images = os.listdir(f"{generations_path}/imgs")
    if(len(images) == 0):
        print(f"Error: {generations_path}/imgs is empty")
        exit()

if not os.path.exists(f"{generations_path}/audio"):
    print(f"Error: {generations_path}/audio does not exist")
    exit()
else:
    audio = os.listdir(f"{generations_path}/audio")
    if(len(audio) == 0):
        print(f"Error: {generations_path}/audio is empty")
        exit()

if(len(images) != len(audio)):
    print(f"Error: Number of images and audio files do not match")
    exit()

def create_video(audio_path, image_path, output_path):
    command = [
        "python",
        "tools/slides2mp4/jpgaudio2mp4.py",
        audio_path,
        image_path,
        output_path
    ]
    subprocess.run(command, check=True)


def merge_videos(input_file, output_path):
    with open('temp.txt', 'w') as f:
        for path in input_file:
            f.write(f"file '{path}'\n")

    command = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", "temp.txt",
        "-c", "copy",
        output_path
    ]
    subprocess.run(command, check=True)

    # Delete the temporary file
    os.remove('temp.txt')

videos = []
#merge title with first slide
create_video(f"{generations_path}/audio/title.wav", f"{generations_path}/imgs/0.jpg", f"{generations_path}/0.mp4")
videos.append(f"{generations_path}/0.mp4")

#audio files names start with a number, e.g. 1_Introduction.wav, 2_The Art of War.wav
# so we can sort them and iterate over them
# we skip the audio file named title.wav
# we skip the image file named 0.jpg

for i in range(1, len(images)):
    #search for the audio file
    audio_file = None
    for a in audio:
        if a.startswith(f"{i}_"):
            audio_file = a
            break
    if audio_file is None:
        print(f"Error: Could not find audio file for slide {i}")
        exit()
    
    create_video(f"{generations_path}/audio/{audio_file}", f"{generations_path}/imgs/{i}.jpg", f"{generations_path}/{i}.mp4")
    videos.append(f"{generations_path}/{i}.mp4")


#merge videos
merge_videos(videos, f"{generations_path}/output.mp4")

for v in videos:
    os.remove(v)

print(f"Video saved to {generations_path}/output.mp4")




