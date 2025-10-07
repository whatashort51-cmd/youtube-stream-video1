from flask import Flask
import os
import threading
import time

app = Flask(__name__)

VIDEO_FILES = [
    "1YOUR_VIDEO_NAME.mp4",
    "Lofi Beats to Study, Relax & Sleep 🌙 _ MrCrazyAshu.mp4",
    "YOUR_VIDEO_NAME.mp4"
]

def keep_alive():
    """Keep alive ping every 4 minutes."""
    while True:
        os.system('curl -Is https://youtube-stream-video1.onrender.com > /dev/null')
        time.sleep(240)  # 4 minutes

@app.route('/')
def home():
    return "✅ YouTube 24x7 Stream Bot is Running Successfully!<br>Now Streaming: " + VIDEO_FILES[0]

def stream_videos():
    """Simulated loop for streaming."""
    while True:
        for video in VIDEO_FILES:
            print(f"Now streaming {video} ...")
            time.sleep(10)  # simulate streaming

if __name__ == "__main__":
    # Start self-ping thread
    threading.Thread(target=keep_alive, daemon=True).start()
    # Start stream loop
    threading.Thread(target=stream_videos, daemon=True).start()
    # Start web server
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
