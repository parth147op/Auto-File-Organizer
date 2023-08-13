import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure logging
logging.basicConfig(filename='file_organizer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def organize_files(directory):
    file_types = {
        'images': ['.jpg', '.png', '.jpeg', '.gif', '.bmp'],
        'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.xls', '.ppt', '.pptx'],
        'videos': ['.mp4', '.mkv', '.flv', '.mpeg', '.avi'],
        'apps': ['.exe', '.dmg', '.apk', '.jar'],
        'zips': ['.zip', '.rar', '.7z', '.tar.gz']
    }

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

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
                destination_path = os.path.join(folder_path, file)
                try:
                    shutil.move(file_path, destination_path)
                    logging.info(f"Moved {file_path} to {destination_path}")
                except Exception as e:
                    logging.error(f"Error moving {file_path} to {destination_path}. Error: {e}")


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
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
        logging.info("Observer stopped by user.")
        observer.stop()
    observer.join()
    logging.info("Observer thread has terminated.")
