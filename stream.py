import os
import time
import subprocess
import threading
from flask import Flask

# === 🔑 Apna YouTube Stream Key yahan likho ===
STREAM_KEY = "cfuu-58e3-365k-em52-0ba6"

# === 🎥 Tumhare videos ke names (GitHub repo ke andar) ===
VIDEOS = [
    "Lofi Beats to Study, Relax & Sleep _ MrCrazyAshu.mp4",
    "1YOUR_VIDEO_NAME.mp4",
    "YOUR_VIDEO_NAME.mp4"
]

# === 🧠 YouTube RTMP URL ===
YOUTUBE_RTMP_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

# === ⚙️ Function: Ek video stream karne ke liye ===
def stream_video(video_path):
    print(f"🎬 Streaming video: {video_path}")
    command = [
        "ffmpeg",
        "-re", "-i", video_path,
        "-c:v", "libx264", "-preset", "veryfast", "-b:v", "4500k",
        "-maxrate", "4500k", "-bufsize", "9000k",
        "-pix_fmt", "yuv420p", "-g", "50",
        "-c:a", "aac", "-b:a", "160k",
        "-ar", "44100",
        "-f", "flv", YOUTUBE_RTMP_URL
    ]
    subprocess.run(command)
    print(f"✅ Finished streaming: {video_path}")

# === ♾️ Loop: sab videos ko ek ke baad ek stream karega ===
def start_stream_loop():
    while True:
        for video in VIDEOS:
            if os.path.exists(video):
                stream_video(video)
            else:
                print(f"⚠️ Video not found: {video}")
            time.sleep(5)  # 5 sec delay between videos

# === 🌐 Flask Web App (Render ke liye) ===
app = Flask(__name__)

@app.route('/')
def home():
    return "🎥 YouTube 24x7 Stream Bot is Running Successfully ✅"

# === 🚀 Flask + Stream ko parallel run karne ke liye ===
def run_flask():
    app.run(host='0.0.0.0', port=10000)

if __name__ == "__main__":
    print("🚀 Starting YouTube Stream Bot (Web + Stream Mode)...")
    threading.Thread(target=start_stream_loop, daemon=True).start()
    run_flask()
