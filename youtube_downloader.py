#vasantharaj_n
import yt_dlp
import os
import shutil

def download_video_with_audio(video_url):
    # Check if ffmpeg is installed
    if not shutil.which("ffmpeg"):
        print("Error: FFmpeg is not installed or not in PATH.")
        return

    # Get available formats and video title
    ydl_opts_info = {"quiet": True, "extract_flat": True}
    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        info = ydl.extract_info(video_url, download=False)
        title = info.get("title", "output").replace(" ", "_")
        formats = info.get("formats", [])
    
    # Display available formats
    print(f"\nAvailable formats for: {title}")
    for f in formats:
        if f.get("vcodec") != "none" or f.get("acodec") != "none":
            fmt_id = f["format_id"]
            resolution = f.get("resolution", "audio only")
            ext = f["ext"]
            print(f"{fmt_id}: {resolution} ({ext})")

    # Ask user for format code
    format_code = input("Enter the format code to download (e.g., 137+251 for video+audio): ").strip()

    # Set download options
    ydl_opts = {
        "quiet": False,
        "merge_output_format": "mp4",
        "outtmpl": f"{title}.%(ext)s",
        "format": format_code,
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
    }

    # Download video with audio
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Download complete: {title}.mp4")
    except Exception as e:
        print(f"Error during download: {e}")

def main():
    while True:
        video_url = input("\nEnter the YouTube video link (or 'exit' to quit): ").strip()
        if video_url.lower() == "exit":
            print("Exiting...")
            break
        download_video_with_audio(video_url)

if __name__ == "__main__":
    main()
