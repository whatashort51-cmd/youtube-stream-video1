import os
import time
import subprocess

# --- CONFIGURATION ---
STREAM_KEY = "2gjx-pzxp-cums-d1vb-6w6g"
RTMP_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

# List of video files (loop order)
VIDEOS = [
    "1st video.mp4",
    "2nd video.mp4",
    "3rd video.mp4"
]

def stream_video(video_path):
    """Stream a single video using FFmpeg"""
    command = [
        "ffmpeg",
        "-re",
        "-stream_loop", "1",  # loop single file
        "-i", video_path,
        "-vcodec", "libx264",
        "-preset", "superfast",
        "-maxrate", "1800k",
        "-bufsize", "1800k",
        "-pix_fmt", "yuv420p",
        "-g", "60",
        "-acodec", "aac",
        "-b:a", "128k",
        "-ar", "44100",
        "-f", "flv",
        RTMP_URL
    ]
    print(f"📺 Now streaming: {video_path}")
    subprocess.call(command)

if __name__ == "__main__":
    while True:
        for video in VIDEOS:
            if os.path.exists(video):
                stream_video(video)
            else:
                print(f"⚠️ File not found: {video}")
                time.sleep(5)

# --- keep render port open (required for free web services) ---
from flask import Flask
import threading, os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ YouTube 24x7 Stream Bot is Running Successfully!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Flask ko background me chalao
threading.Thread(target=run_flask).start()
