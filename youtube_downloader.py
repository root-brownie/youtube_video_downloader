import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube

def browse_directory():
    directory = filedialog.askdirectory()
    download_path.set(directory)

def download_video():
    try:
        url = url_entry.get()
        resolution = resolution_combobox.get()
        download_folder = download_path.get()
        
        yt = YouTube(url)
        
        # Filter streams to get the selected resolution stream
        stream = yt.streams.filter(progressive=True, file_extension="mp4", resolution=resolution).first()
        
        if stream is None:
            raise Exception(f"No {resolution} stream available for this video.")
        
        stream.download(output_path=download_folder)
        messagebox.showinfo("Download Complete", "Video downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
app = tk.Tk()
app.title("YouTube Video Downloader (HD)")
app.geometry("400x200")

# Set the dark background
app.configure(bg="black")

# Create the input field for the YouTube URL
url_label = tk.Label(app, text="Enter YouTube URL:", fg="white", bg="black")
url_label.pack(pady=10)
url_entry = tk.Entry(app, width=40)
url_entry.pack()

# Create the combobox to select the resolution
resolutions = ["1080p", "720p", "480p", "360p"]
resolution_combobox = ttk.Combobox(app, values=resolutions, state="readonly")
resolution_combobox.set("720p")
resolution_combobox.pack(pady=10)

# Create the button to browse and select the download directory
download_path = tk.StringVar()
download_path.set("C:/Downloads")  # Default download directory
browse_button = tk.Button(app, text="Browse", command=browse_directory, fg="white", bg="gray")
browse_button.pack(pady=5)
directory_label = tk.Label(app, textvariable=download_path, fg="white", bg="black")
directory_label.pack()

# Create the download button
download_button = tk.Button(app, text="Download", command=download_video, fg="white", bg="gray")
download_button.pack(pady=20)

# Start the application
app.mainloop()
