# YoutubeVideos-HighQuality-Downloader
"Download any YouTube video in the quality of your choice."
YouTube Video Downloader
========================

This script allows you to download YouTube videos in your preferred quality using `yt-dlp`.

### Requirements
1. Python installed on your system.
2. Install `yt-dlp` and `ffmpeg` if not already installed:
   
   ```sh
   pip install yt-dlp
   ```
   
   Install FFmpeg:
   - **Windows:**
     1. Download the latest version from https://ffmpeg.org/download.html.
     2. Extract the downloaded ZIP file.
     3. Move the extracted folder to `C:\Program Files\FFmpeg`.
     4. Add `C:\Program Files\FFmpeg\bin` to your system's PATH variable.
     5. Verify installation by running `ffmpeg -version` in the command prompt.
   
   - **Linux/macOS:**
     - Install via package manager:
       ```sh
       sudo apt install ffmpeg  # Ubuntu/Debian
       sudo dnf install ffmpeg  # Fedora
       brew install ffmpeg      # macOS (using Homebrew)
       ```
     - Verify installation by running `ffmpeg -version` in the terminal.

### How to Run
1. Save the script as `youtube_downloader.py`.
2. Open a terminal or command prompt and navigate to the script directory.
3. Run the script using:
   
   ```sh
   python youtube_downloader.py
   ```
4. Enter the YouTube video URL when prompted.
5. Select the format code from the displayed list.
6. The video will be downloaded and saved as an MP4 file in the current directory.

### Exit
To exit the script, type `exit` when prompted for a YouTube video link.

Enjoy downloading!

