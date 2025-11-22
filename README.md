# Media Shrink Pro

A sleek, cross-platform GUI tool built with pure Python (Tkinter) for compressing videos, audio files, and images to a specific target size using FFmpeg. Features an animated cyberpunk-inspired interface with glowing effects, real-time progress, and automatic output suggestions. No external dependencies beyond Python and FFmpeg—perfect for quick media optimization!

## Features
- **Multi-Format Support**: Compress videos (MP4, MOV, AVI, MKV, etc.), audio (MP3, WAV, FLAC, AAC, etc.), and images (JPG, PNG, WEBP, etc.).
- **Target Size Compression**: Specify a desired file size in MB, and the tool adjusts bitrate/quality accordingly.
- **Speed-Quality Slider**: Balance between fast compression and high quality.
- **Real-Time Progress**: Smooth progress bar updates during compression.
- **Auto Output Naming**: If no output specified, defaults to `input_compressed.ext` in the same directory.
- **Beautiful UI**: Animated gradient background, pulsing title, glowing button—no extra installs needed.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Requirements
- **Python 3.8+**: Comes pre-installed on most systems (Tkinter is included).
- **FFmpeg**: Must be installed and added to your system PATH.
  - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html), extract, and add `bin` folder to PATH.
  - **macOS**: Install via Homebrew: `brew install ffmpeg`.
  - **Linux (Ubuntu/Debian)**: `sudo apt update && sudo apt install ffmpeg`.
  - **Linux (Fedora)**: `sudo dnf install ffmpeg`.
  - **Linux (Arch)**: `sudo pacman -S ffmpeg`.

Verify FFmpeg: Open a terminal and run `ffmpeg -version`. If not found, check your PATH.

## Installation
1. Clone or download the repository:
   ```
   git clone https://github.com/yourusername/media-shrink-pro.git
   cd media-shrink-pro
   ```
2. No pip installs needed—just ensure FFmpeg is set up.

## Usage
1. Run the script:
   ```
   python media_shrink_pro.py
   ```
   (Replace with your script filename, e.g., `VideoShrink.py` or `media_shrink_pro.py`.)

2. In the GUI:
   - **Input File**: Browse or paste the path to your media file.
   - **Output File**: Browse to choose a save location, or leave blank for automatic naming (`input_compressed.ext` in the same folder).
   - **Target Size (MB)**: Enter the desired output size (e.g., 10 for 10MB).
   - **Speed ↔ Quality Slider**: Slide left for faster compression (lower quality), right for better quality (slower).
   - Click **Compress** to start.

3. Watch the progress bar and status updates. A success message will appear when done!

## Troubleshooting
- **FFmpeg Not Found**: Ensure it's installed and in PATH. Restart your terminal/IDE after installation.
- **No Progress for Images/Audio**: These are fast operations; progress simulates smoothly.
- **Video Compression Fails**: Check if input video is valid. For large files, use a higher quality setting or larger target size.
- **UI Issues**: On some Linux distros, Tkinter themes might vary—ensure `python3-tk` is installed.

## Contributing
Fork the repo, make changes, and submit a pull request. Suggestions for features like batch processing or more formats welcome!

## License
MIT License—free to use, modify, and distribute.

---

Built with ❤️ using Python and FFmpeg. If you like it, star the repo!
