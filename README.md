# SimpleVideoShrink-Python

VideoShrink is a **cross-platform video compressor** that automatically compresses videos to a target file size while keeping audio.  
It works on **Linux, Mac, and Windows** as long as `ffmpeg` is installed.

---

## Features

- Compress videos until they fit under a **target file size** (MB).  
- Preserves audio.  
- **Speed ↔ Quality slider**: adjust compression aggressiveness.  
  - Middle = balanced  
  - Left = faster compression, lower quality  
  - Right = slower compression, higher quality  
- Automatically deletes temporary files and keeps only the final compressed video.  
- Simple and intuitive **Tkinter GUI**.

---

## Supported Platforms

- Linux  
- macOS  
- Windows  

> Note: Make sure `ffmpeg` is installed and available in your system PATH.

---

## Supported Formats

- Input: `.mp4`, `.mov`, `.avi`, `.mkv`  
- Output: `.mp4`

---

## Installation

1. Make sure you have **Python 3** installed.  
2. Install **Tkinter** (if not already installed):
   ```bash
   # Linux (Debian/Ubuntu)
   sudo apt install python3-tk

   # macOS (usually included with Python)
   brew install python-tk   # optional

   # Windows (included with Python installer)
