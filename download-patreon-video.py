import os
import subprocess
import re

def download_patreon_video(post_id):
    URL = f"import os
import subprocess
import re

def download_patreon_video(post_id):
    URL = f"https://www.patreon.com/posts/{post_id}"
    yt_dlp_command = ["yt-dlp", "--cookies-from-browser", "chrome", URL, "-F"]
    
    output = subprocess.check_output(yt_dlp_command).decode('utf-8')
    
    video_resolutions = re.findall(r"(\d+)\s+(mp4\s+\d+x\d+)", output)
    
    print("Available resolutions: ")
    for i, res in enumerate(video_resolutions, start=1):
        print(f"{i}. {res[1]}")
    
    choice = int(input("Select resolution: "))
    resolution_id = video_resolutions[choice-1][0]
    
    # Specify output directory and filename
    output_path = "~/patreon/%(title)s.%(ext)s"
    
    download_command = ["yt-dlp", "--cookies-from-browser", "chrome", URL, "-f", resolution_id, "-o", output_path]
    subprocess.run(download_command)

if __name__ == "__main__":
    post_id = input("Enter post id: ")
    download_patreon_video(post_id)
"
    yt_dlp_command = ["yt-dlp", "--cookies-from-browser", "chrome", URL, "-F"]
    
    output = subprocess.check_output(yt_dlp_command).decode('utf-8')
    
    video_resolutions = re.findall(r"(\d+)\s+(mp4\s+\d+x\d+)", output)
    
    print("Available resolutions: ")
    for i, res in enumerate(video_resolutions, start=1):
        print(f"{i}. {res[1]}")
    
    choice = int(input("Select resolution: "))
    resolution_id = video_resolutions[choice-1][0]
    
    # Specify output directory and filename
    output_path = "~/patreon/%(title)s.%(ext)s"
    
    download_command = ["yt-dlp", "--cookies-from-browser", "chrome", URL, "-f", resolution_id, "-o", output_path]
    subprocess.run(download_command)

if __name__ == "__main__":
    post_id = input("Enter post id: ")
    download_patreon_video(post_id)

