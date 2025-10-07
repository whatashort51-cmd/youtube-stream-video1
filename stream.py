import os
import subprocess
import threading
import time
from flask import Flask

app = Flask(__name__)

# ====== CONFIGURATION ======
# Choose one of your video options here 👇
# Uncomment (remove #) from the video you want to stream

# VIDEO_FILE = "1YOUR_VIDEO_NAME.mp4"
# VIDEO_FILE = "Lofi Beats to Study, Relax & Sleep 🌙 _ MrCrazyAshu.mp4"
VIDEO_FILE = "YOUR_VIDEO_NAME.mp4"   # ← current active video

YOUTUBE_KEY = "cfuu-58e3-365k-em52-0ba6"  # your YouTube stream key
YOUTUBE_RTMP_URL = f"rtmp://a.rtmp.youtube.com/live2/{YOUTUBE_KEY}"

# ====== STREAM FUNCTION ======
def start_stream():
    while True:
        try:
            print(f"🔴 Starting YouTube Live Stream with: {VIDEO_FILE}")
            command = [
                "ffmpeg",
                "-re",
                "-stream_loop", "-1",
                "-i", VIDEO_FILE,
                "-vcodec", "libx264",
                "-preset", "veryfast",
                "-maxrate", "3000k",
                "-bufsize", "6000k",
                "-pix_fmt", "yuv420p",
                "-g", "50",
                "-acodec", "aac",
                "-b:a", "128k",
                "-ar", "44100",
                "-f", "flv",
                YOUTUBE_RTMP_URL
            ]
            subprocess.run(command)
            print("⚠️ Stream ended or failed, retrying in 10 seconds...")
            time.sleep(10)
        except Exception as e:
            print("❌ Error:", e)
            time.sleep(10)

# ====== KEEP SERVER ALIVE ======
@app.route('/')
def home():
    return f"✅ YouTube 24x7 Stream Bot is Running Successfully!<br>Now Streaming: {VIDEO_FILE}"

def keep_alive():
    app.run(host='0.0.0.0', port=10000)

# ====== MAIN EXECUTION ======
if __name__ == "__main__":
    threading.Thread(target=keep_alive).start()
    time.sleep(3)
    start_stream()
