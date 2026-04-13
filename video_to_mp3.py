# Converts the videos to mp3 
import os 
import subprocess

files = os.listdir("videos") 
for file in files:
    if file.startswith("."):
        continue
    file_name_no_ext = os.path.splitext(file)[0]
    parts = file_name_no_ext.split(" ", 1)
    tutorial_number = parts[0]
    title = parts[1] if len(parts) > 1 else file_name_no_ext
    output_path = f"audios/{tutorial_number}_{title}.mp3"
    print(f"{tutorial_number} --> {title}")
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", output_path])

print("\nDone! All videos converted to MP3.")