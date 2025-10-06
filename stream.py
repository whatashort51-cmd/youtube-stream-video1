import os
import time
import subprocess

# === 🔐 YouTube Stream Key (safe way: env var from Render) ===
# Render.com me Environment Variable add karo:
# Key: YOUTUBE_STREAM_KEY
# Value: cfuu-58e3-365k-em52-0ba6
STREAM_KEY = os.getenv("YOUTUBE_STREAM_KEY", "cfuu-58e3-365k-em52-0ba6")

# === 🎞️ Tumhare video file names (repo ke andar hone chahiye) ===
VIDEOS = [
    "Lofi Beats to Study, Relax & Sleep 🌙 _ MrCrazyAshu.mp4",
    "1YOUR_VIDEO_NAME.mp4",
    "YOUR_VIDEO_NAME.mp4"
]

# === 🌐 YouTube RTMP URL ===
YOUTUBE_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

# === ⚙️ FFmpeg streaming settings ===
FFMPEG_OPTIONS = [
    "-re",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-maxrate", "3000k",
    "-bufsize", "6000k",
    "-pix_fmt", "yuv420p",
    "-g", "50",
    "-c:a", "aac",
    "-b:a", "128k",
    "-ar", "44100",
    "-f", "flv"
]

def stream_video(video):
    """Stream a single video file to YouTube."""
    try:
        print(f"\n🚀 Now Streaming: {video}")
        command = [
            "ffmpeg",
            "-stream_loop", "-1",  # 🔁 repeat video forever
            "-i", video
        ] + FFMPEG_OPTIONS + [YOUTUBE_URL]

        subprocess.run(command, check=True)
        print(f"✅ Finished streaming: {video}")

    except subprocess.CalledProcessError as e:
        print(f"⚠️ FFmpeg error while streaming {video}: {e}")
        print("🔁 Restarting stream in 10 seconds...")
        time.sleep(10)
    except Exception as e:
        print(f"💥 Unexpected error: {e}")
        time.sleep(10)

def main():
    print("🎧 MrCrazyAshu 24×7 Lofi Stream Bot Starting...\n")
    while True:
        for video in VIDEOS:
            if os.path.exists(video):
                stream_video(video)
            else:
                print(f"❌ File not found: {video}")
                time.sleep(5)

if __name__ == "__main__":
    main()
