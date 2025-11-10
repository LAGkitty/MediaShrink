import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select video file",
        filetypes=[("Video Files", "*.mp4 *.mov *.avi *.mkv")]
    )
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def get_duration(path):
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return float(result.stdout.strip())
    except:
        return 1.0

def compress_video_loop(input_file, output_file, target_mb, speed_quality):
    """
    speed_quality: -50 (speed) to 50 (quality), 0 = balanced
    Works for Linux, Windows, Mac as long as ffmpeg is installed and in PATH
    """
    duration = max(1, get_duration(input_file))
    target_bytes = target_mb * 1_000_000
    v_bitrate = int((target_mb * 8_000_000) / duration * 0.8)
    a_bitrate = int((target_mb * 8_000_000) / duration * 0.2)
    a_bitrate = max(32, min(a_bitrate, 128))

    attempt = 1
    last_output = None

    while True:
        temp_output = f"{output_file}_tmp_{attempt}.mp4"
        cmd = [
            "ffmpeg", "-y", "-i", input_file,
            "-b:v", f"{max(50, v_bitrate)}k",
            "-b:a", f"{max(32, a_bitrate)}k",
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-movflags", "+faststart",
            "-pix_fmt", "yuv420p",
            temp_output
        ]
        # Cross-platform: suppress output
        if sys.platform.startswith("win"):
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        else:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        size = os.path.getsize(temp_output)

        if size <= target_bytes:
            if last_output and os.path.exists(last_output):
                os.remove(last_output)
            final_output = output_file
            os.replace(temp_output, final_output)
            return final_output

        if last_output and os.path.exists(last_output):
            os.remove(last_output)
        last_output = temp_output

        # Adjust bitrates depending on slider
        factor = 1 - (speed_quality / 150)  # -50 → speed, 0 → balanced, 50 → quality
        v_bitrate = int(v_bitrate * factor)
        a_bitrate = int(a_bitrate * factor)
        attempt += 1

def start_compression():
    input_file = input_entry.get().strip()
    if not input_file:
        messagebox.showerror("Error", "Please select a video file.")
        return

    base, ext = os.path.splitext(input_file)
    output_file = base + "_compressed.mp4"

    try:
        target_mb = float(target_entry.get())
        speed_quality = slider.get()
        final = compress_video_loop(input_file, output_file, target_mb, speed_quality)
        messagebox.showinfo("Done", f"Compression finished!\nSaved as:\n{final}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Cross-Platform Video Compressor")
root.geometry("450x260")
root.resizable(False, False)

tk.Label(root, text="Select Video:").pack(pady=(10,0))
frame = tk.Frame(root)
frame.pack()
input_entry = tk.Entry(frame, width=35)
input_entry.pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Browse", command=browse_file).pack(side=tk.LEFT)

tk.Label(root, text="Target Size (MB):").pack(pady=(10,0))
target_entry = tk.Entry(root)
target_entry.insert(0,"10")
target_entry.pack()

tk.Label(root, text="Speed ↔ Quality:").pack(pady=(10,0))
slider = tk.Scale(root, from_=-50, to=50, orient=tk.HORIZONTAL)
slider.set(0)  # Middle = balanced
slider.pack(fill="x", padx=20)

tk.Button(root, text="Compress", bg="#2ecc71", fg="white", font=("Arial",11,"bold"),
          height=2, command=start_compression).pack(pady=15, fill="x", padx=20)

root.mainloop()
