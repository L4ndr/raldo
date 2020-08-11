from watchdog.observers import Observer
from time import sleep
from watchdog.events import FileSystemEventHandler
import os

downloads = f"{os.expanduser("~")}/Downloads"
os.chdir(downloads)

image_extensions = ["jpg", "png", "jpeg", "gif"]
video_extensions = ["mp4", "avi", "mov", "flv"]
document_extensions = ["docx", "pdf", "doc", "txt", "odt"]
compressed_extensions = ["zip", "tar", "rar", "7z"]

folders = {
    "img":f"{downloads}/Pictures/",
    "vid":f"{downloads}/Videos/",
    "doc":f"{downloads}/Documents/",
    "zip":f"{downloads}/Compressed"
}

def extension_handler(filename):
    count = filename.count(".")
    extension = filename.split(".")[-count:]
    if extension in image_extensions: return "img"
    elif extension in video_extensions: return "vid"
    elif extension in document_extensions: return "doc"
    elif extension in compressed_extensions: return "zip"
    else: raise Exception("Unknown extension.")


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir():
            try:
                extension_type = extension_handler(filename)
                os.system(f"mv {downloads}/{filename} {folders[extension_type]}")
            except:
                pass

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, f"{downloads}/", recursive=True)
observer.start()

try:
    while True:
        sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
