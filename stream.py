import os
import time
import subprocess

# === 🔐 Apna YouTube Stream Key yahan likho ===
STREAM_KEY = "cfuu-58e3-365k-em52-0ba6"

# === 🎬 Tumhare videos ke names (GitHub repo ke andar) ===
VIDEOS = [
    "1YOUR_VIDEO_NAME.mp4",
    "YOUR_VIDEO_NAME.mp4",
    "Lofi Beats to Study, Relax & Sleep 🌙 _ MrCrazyAshu.mp4"
]

# === ⚙️ YouTube RTMP Server URL ===
YOUTUBE_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

def stream_video(video):
    """Ek single video ko YouTube par stream karta hai"""
    try:
        print(f"\n🚀 Starting stream: {video}")
        command = [
            "ffmpeg",
            "-re",
            "-i", video,
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-maxrate", "3000k",
            "-bufsize", "6000k",
            "-pix_fmt", "yuv420p",
            "-g", "50",
            "-c:a", "aac",
            "-b:a", "128k",
            "-ar", "44100",
            "-f", "flv",
            YOUTUBE_URL
        ]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Error while streaming {video}: {e}")
        print("🔁 Restarting stream in 5 seconds...")
        time.sleep(5)

# === 🔁 Continuous Streaming Loop with Auto-Restart ===
while True:
    for video in VIDEOS:
        try:
            stream_video(video)
        except Exception as e:
            print(f"💥 Unexpected error: {e}")
            print("🔄 Restarting main loop in 10 seconds...")
            time.sleep(10)
