import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def organize_files(directory):
    # List all file types you want to sort
    file_types = {
        'images': ['.jpg', '.png', '.jpeg', '.gif', '.bmp'],
        'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.xls', '.ppt', '.pptx'],
        'videos': ['.mp4', '.mkv', '.flv', '.mpeg', '.avi'],
        'apps': ['.exe', '.dmg', '.apk', '.jar'],  # Applications
        'zips': ['.zip', '.rar', '.7z', '.tar.gz'],  # Zip files
        # You can add more file types as you need
    }

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # Make sure we're not creating folders for folders
        if not os.path.isfile(file_path):
            continue

        for folder, extensions in file_types.items():
            _, extension = os.path.splitext(file)

            if extension.lower() in extensions:
                folder_path = os.path.join(directory, folder)

                # Create folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the file
                shutil.move(file_path, os.path.join(folder_path, file))

# Run the function on a directory


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Here we'll call the function to re-organize the files
        organize_files("C:/Users/parth/Downloads")

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path="C:/Users/parth/Downloads", recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
