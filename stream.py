import os
import time
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# === 🔑 Apna YouTube Stream Key yahan likho ===
STREAM_KEY = "cfuu-58e3-365k-em52-0ba6"

# === 🎵 Tumhare videos ke names (GitHub repo ke andar) ===
VIDEOS = [
    "Lofi Beats to Study, Relax & Sleep 🌙 _ MrCrazyAshu.mp4",
    "1YOUR_VIDEO_NAME.mp4",
    "YOUR_VIDEO_NAME.mp4"
]

# === 📡 YouTube RTMP Server URL ===
YOUTUBE_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

def stream_video(video):
    """Ek single video ko YouTube par stream karta hai"""
    try:
        print(f"\n🚀 Starting stream: {video}")
        command = [
            "ffmpeg",
            "-re",
            "-i", video,
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
            YOUTUBE_URL
        ]
        subprocess.run(command)
    except Exception as e:
        print(f"❌ Error streaming {video}: {e}")

def start_stream_loop():
    """Ye function videos ko continuous loop me stream karta rahega"""
    while True:
        for video in VIDEOS:
            if os.path.exists(video):
                stream_video(video)
            else:
                print(f"⚠️ File not found: {video}")
            time.sleep(5)

# === 🌐 Fake HTTP server to keep Render service alive ===
class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Server is alive and streaming!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("", port), KeepAliveHandler)
    print(f"🌍 Keep-alive server running on port {port}")
    server.serve_forever()

if __name__ == "__main__":
    # Start fake HTTP server in background thread
    threading.Thread(target=run_server, daemon=True).start()
    # Start YouTube stream loop
    start_stream_loop()
