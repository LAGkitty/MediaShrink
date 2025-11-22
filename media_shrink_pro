# Universal Media Shrink Pro - Videos + Audio + Images (Pure Tkinter)
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import threading
import time

# === Safe RGB to Hex (Never crashes!) ===
def rgb_to_hex(r, g, b):
    return f"#{max(0, min(255, int(r))):02x}{max(0, min(255, int(g))):02x}{max(0, min(255, int(b))):02x}"

# === Animated Gradient Background (Smoother Transitions, No Gaps) ===
class GradientBackground(tk.Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, highlightthickness=0, bg="black", **kwargs)
        self.colors = [
            (120, 0, 255), (0, 200, 255), (255, 0, 200),
            (80, 255, 150), (255, 100, 0), (120, 0, 255)  # Loop back for smooth wrap
        ]
        self.angle = 0
        self.animate()

    def animate(self):
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w <= 1 or h <= 1:  # Wait until sized
            self.after(100, self.animate)
            return
        step_size = 2  # Dense spacing
        strip_width = 20  # Wide strips for overlap/no gaps
        num_strips = int((w + 800) / step_size) + 50  # Extra strips for full coverage
        for i in range(num_strips):
            t = (i + self.angle * 0.5) / num_strips
            idx = int(t * (len(self.colors) - 1)) % (len(self.colors) - 1)
            r1, g1, b1 = self.colors[idx]
            r2, g2, b2 = self.colors[idx + 1]
            ratio = (t * (len(self.colors) - 1)) % 1
            r = r1 + (r2 - r1) * ratio
            g = g1 + (g2 - g1) * ratio
            b = b1 + (b2 - b1) * ratio
            color = rgb_to_hex(r, g, b)
            x = (self.angle * 2 + i * step_size) % (w + 800) - 400  # Wide coverage
            self.create_rectangle(x, -50, x + strip_width, h + 50, fill=color, outline="")
        self.angle = (self.angle + 1) % num_strips
        self.after(60, self.animate)  # Smooth animation

# === Main Window ===
root = tk.Tk()
root.title("Media Shrink Pro")
root.geometry("640x700")  # Increased height to ensure button visibility
root.configure(bg="black")
root.resizable(False, False)

# Background
bg = GradientBackground(root)
bg.place(x=0, y=0, relwidth=1, relheight=1)

# Card
card = tk.Frame(root, bg="#0a001a", highlightbackground="#ff00ff", highlightthickness=3)
card.place(relx=0.5, rely=0.5, anchor="center", width=540, height=600)  # Increased height

# Title (pulsing)
def pulse_title():
    import math, time
    hue = (time.time() * 0.3) % 1.0
    r = int(255 * abs(math.sin(hue * 6)))
    g = int(255 * abs(math.sin((hue + 0.33) * 6)))
    b = int(255 * abs(math.sin((hue + 0.66) * 6)))
    title.config(fg=rgb_to_hex(r*1.2, g*0.8, b*1.5))
    root.after(50, pulse_title)

title = tk.Label(card, text="MEDIA SHRINK PRO", font=("Impact", 28, "bold"), bg="#0a001a")
title.pack(pady=(20, 5))
pulse_title()

tk.Label(card, text="Compress Videos • Audio • Images", font=("Segoe UI", 10), fg="#cccccc", bg="#0a001a").pack(pady=5)

# File input
tk.Label(card, text="Input File", fg="#00ffff", bg="#0a001a", font=("bold", 10)).pack(anchor="w", padx=50, pady=(10,3))
input_frame = tk.Frame(card, bg="#0a001a")
input_frame.pack(fill="x", padx=50, pady=3)
input_entry = tk.Entry(input_frame, font=("Consolas", 11), bg="#1a0033", fg="#00ffcc", relief="flat", bd=6, insertbackground="#00ffcc")
input_entry.pack(side="left", expand=True, fill="x")
tk.Button(input_frame, text="Browse", bg="#00cc99", fg="white", font=("bold", 9), relief="flat", padx=12,
          command=lambda: input_entry.delete(0, tk.END) or input_entry.insert(0, filedialog.askopenfilename(
              filetypes=[("All Media", "*.mp4 *.mov *.avi *.mkv *.webm *.mp3 *.wav *.flac *.aac *.jpg *.jpeg *.png *.webp *.gif *.bmp *.tiff")]))
).pack(side="right")

# Output
tk.Label(card, text="Output File", fg="#ff00ff", bg="#0a001a", font=("bold", 10)).pack(anchor="w", padx=50, pady=(10,3))
output_frame = tk.Frame(card, bg="#0a001a")
output_frame.pack(fill="x", padx=50, pady=3)
output_entry = tk.Entry(output_frame, font=("Consolas", 11), bg="#1a0033", fg="#00ffcc", relief="flat", bd=6)
output_entry.pack(side="left", expand=True, fill="x")
tk.Button(output_frame, text="Save As", bg="#0066ff", fg="white", font=("bold", 9), relief="flat", padx=12,
          command=lambda: output_entry.delete(0, tk.END) or output_entry.insert(0, filedialog.asksaveasfilename(
              defaultextension=".mp4", filetypes=[("MP4 Video", "*.mp4"), ("MP3 Audio", "*.mp3"), ("WebP Image", "*.webp"), ("JPEG", "*.jpg")]))
).pack(side="right")

# Target size
tk.Label(card, text="Target Size (MB)", fg="#ffff00", bg="#0a001a").pack(pady=(10,3))
target_entry = tk.Entry(card, width=10, font=("Consolas", 14, "bold"), bg="#330022", fg="#ffff00", relief="flat", bd=6)
target_entry.insert(0, "10")
target_entry.pack()

# Speed-Quality Slider
tk.Label(card, text="Speed ↔ Quality", fg="#00ffaa", bg="#0a001a").pack(pady=(10,3))
slider = tk.Scale(card, from_=-50, to=50, orient="horizontal", bg="#0a001a", fg="#00ffff", troughcolor="#330066", highlightthickness=0, length=400)
slider.set(0)
slider.pack(pady=3)

# Progress
progress_var = tk.DoubleVar()
progress = ttk.Progressbar(card, variable=progress_var, maximum=100, length=420)
style = ttk.Style()
style.configure("TProgressbar", background="#00ffaa", troughcolor="#220033", thickness=20)
progress.pack(pady=10)

status = tk.Label(card, text="Ready — supports video, audio & images", fg="#00ffcc", bg="#0a001a", font=("Consolas", 11))
status.pack(pady=5)

# Glowing button
glow = 0
def animate_button():
    global glow
    intensity = 0.8 + 0.2 * __import__("math").sin(glow * 0.2)
    color = rgb_to_hex(255 * intensity, 50 * intensity, 200 * intensity)
    compress_btn.config(bg=color)
    glow += 1
    root.after(70, animate_button)

compress_btn = tk.Button(card, text="Compress", font=("Impact", 20, "bold"), fg="white", relief="flat", bd=0, padx=50, pady=15)
compress_btn.pack(pady=20)  # Increased pady for visibility
animate_button()

# === Universal Compression (With Real-Time Progress & Auto-Output) ===
def shrink_media():
    in_file = input_entry.get().strip()
    out_file = output_entry.get().strip()
    if not in_file or not os.path.exists(in_file):
        return messagebox.showerror("Error", "Select a valid file")
    if not out_file:
        base, ext = os.path.splitext(in_file)
        out_file = base + "_compressed" + ext
        output_entry.delete(0, tk.END)
        output_entry.insert(0, out_file)
    try:
        target_mb = float(target_entry.get())
        if target_mb <= 0: raise ValueError
    except:
        return messagebox.showerror("Error", "Invalid size")
    speed_quality = slider.get()

    compress_btn.config(state="disabled", text="WORKING...")
    progress_var.set(0)
    status.config(text="Processing...")

    def update_progress(perc):
        root.after(0, lambda: progress_var.set(perc))

    def run():
        try:
            ext = os.path.splitext(in_file)[1].lower()
            size_bytes = target_mb * 1_000_000

            if ext in {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".gif"}:
                # Image: Simulate progress (fast operation)
                for p in range(0, 101, 5):
                    update_progress(p)
                    time.sleep(0.05)
                base_quality = max(10, min(100, int(100 - (os.path.getsize(in_file) / size_bytes) * 50)))
                quality = max(5, min(100, base_quality + int(speed_quality * 0.5)))
                cmd = ["ffmpeg", "-y", "-i", in_file]
                if out_file.lower().endswith(".webp"):
                    cmd += ["-q:v", str(quality), out_file]
                else:
                    cmd += ["-q:v", str(max(1, 31 - quality//3)), out_file]
                subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            elif ext in {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"}:
                # Audio: Simulate progress
                for p in range(0, 101, 5):
                    update_progress(p)
                    time.sleep(0.1)
                base_bitrate = max(32, min(320, int((size_bytes * 8) / (get_duration(in_file) or 60) / 1000)))
                bitrate = max(32, min(320, int(base_bitrate * (1 + speed_quality / 100))))
                subprocess.run([
                    "ffmpeg", "-y", "-i", in_file,
                    "-b:a", f"{bitrate}k", "-ac", "2", out_file
                ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            else:
                # Video: Real progress
                duration = get_duration(in_file)
                v_bitrate = max(50, int((size_bytes * 8 * 0.9) / duration / 1000))
                a_bitrate = min(192, int((size_bytes * 8 * 0.1) / duration / 1000))
                presets = ['ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow']
                preset_index = 4 + int(speed_quality / 12.5)
                preset = presets[max(0, min(8, preset_index))]
                null = "NUL" if os.name == "nt" else "/dev/null"

                # Pass 1: 0-50%
                status.config(text="Pass 1/2: Analyzing...")
                subprocess.run(["ffmpeg", "-y", "-i", in_file, "-c:v", "libx264", "-preset", preset, "-b:v", f"{v_bitrate}k", "-pass", "1", "-an", "-f", "null", null], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                update_progress(50)

                # Pass 2: 50-100% with real progress
                status.config(text="Pass 2/2: Encoding...")
                cmd = [
                    "ffmpeg", "-y", "-i", in_file, "-c:v", "libx264", "-preset", preset,
                    "-b:v", f"{v_bitrate}k", "-pass", "2", "-c:a", "aac", "-b:a", f"{a_bitrate}k",
                    "-movflags", "+faststart", "-progress", "pipe:1", out_file
                ]
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True, stderr=subprocess.STDOUT)
                for line in proc.stdout:
                    if line.startswith("out_time_ms="):
                        try:
                            ms = int(line.split("=")[1])
                            percent = min(100.0, (ms / 1000000.0) / duration * 100)
                            overall = 50 + (percent / 2)
                            update_progress(overall)
                        except: pass
                proc.wait()
                if proc.returncode != 0:
                    raise Exception("FFmpeg failed")
                for f in ["ffmpeg2pass-0.log", "ffmpeg2pass-0.log.mbtree"]: 
                    if os.path.exists(f): os.remove(f)

            root.after(0, lambda: messagebox.showinfo("Done!", f"Success!\nSaved: {out_file}"))
            root.after(0, lambda: status.config(text="Complete!"))
        except Exception as e:
            root.after(0, lambda: messagebox.showerror("Error", str(e)))
            root.after(0, lambda: status.config(text="Error occurred"))
        finally:
            root.after(0, lambda: compress_btn.config(state="normal", text="Compress"))
            root.after(0, lambda: progress_var.set(0))

    threading.Thread(target=run, daemon=True).start()

def get_duration(path):
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True)
        return float(r.stdout.strip()) if r.stdout.strip() else 60
    except:
        return 60

compress_btn.config(command=shrink_media)

# Auto output suggestion (only if empty)
def suggest_output(*args):
    if not output_entry.get().strip():
        path = input_entry.get().strip()
        if path and os.path.exists(path):
            base, ext = os.path.splitext(path)
            output_entry.delete(0, tk.END)
            output_entry.insert(0, base + "_compressed" + ext)

input_entry.bind("<FocusOut>", suggest_output)
input_entry.bind("<KeyRelease>", suggest_output)

root.mainloop()
