#Dependencies: ffmpeg, get by running ''choco install ffmpeg'' in cmd
#Usage: python jpgaudio2mp4.py <audio.mp3> <image.jpg> <output.mp4>


import subprocess
import sys

print("Creating video...")

if len(sys.argv) < 3:
    print('Usage: python jpgaudio2mp4.py <audio.mp3> <image.jpg> <output.mp4>')
    sys.exit(1)

def create_video(audio_path, image_path, output_path, fps=24):
  command = [
      "ffmpeg",
      "-loop", "1",
      "-i", image_path,
      "-i", audio_path,
      "-c:v", "libx264",
      "-tune", "stillimage",
      "-c:a", "aac",
      "-shortest", 
      output_path
  ]
  subprocess.run(command, check=True)

audio_path = sys.argv[1]
image_path = sys.argv[2]
output_path = sys.argv[3]

create_video(audio_path, image_path, output_path)

print("Video creation complete!")