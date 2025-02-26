import os
import time
import threading
from playsound import playsound

def play_sound():
    playsound("music/badapple.mp4")

def load_ascii_frames(ascii_folder):
    frames = []
    ascii_files = sorted(os.listdir(ascii_folder))

    for filename in ascii_files:
        if filename.endswith(".txt"):
            with open(os.path.join(ascii_folder, filename), 'r') as f:
                frames.append(f.read())
    return frames

def animate_ascii_art(frames, total_duration=219):
    num_frames = len(frames)
    frame_time = total_duration / num_frames  # More precise frame delay

    start_time = time.monotonic()  # Get a precise start time

    try:
        for i, frame in enumerate(frames):
            print(frame)
            print("\033[H\033[J", end="")  # Fast clear screen

            # Calculate when the next frame *should* be shown
            next_frame_time = start_time + (i + 1) * frame_time
            time.sleep(max(0, next_frame_time - time.monotonic()))  # Ensure correct timing

    except KeyboardInterrupt:
        print("\nThe animation was fucking shot")
        exit(0)

sound_thread = threading.Thread(target=play_sound, daemon=True)
sound_thread.start()

frames = load_ascii_frames('ASCIIframes')
animate_ascii_art(frames, total_duration=219)  # Total duration in seconds

