# Auto File Organizer

Organize your files automatically based on their file types. This script watches a specified directory and moves files to subdirectories based on their extensions. It is particularly useful for directories like Downloads or Desktop where files can accumulate over time.


## Features

- Automatic file categorization based on extensions.
- Uses watchdog to monitor the directory for changes, ensuring quick response to file additions.
- Configuration-based setup to easily specify which file types belong to which category.
- Comprehensive logging for tracking file movements and potential errors.

## Installation

1. Ensure you have Python installed.
2. Clone this repository
3. Navigate to the cloned directory and install required packages: `pip install watchdog`

## Configuration

Before you run the script, configure your desired settings:

1. Open config.json in a text editor.
2. Modify watch_directory to the directory you want to monitor and organize.
3. Adjust the file_types object to organize the file extensions as you see fit.

## Running the Script

1. In the terminal, navigate to the directory containing run.py
2. Run the script: `python run.py`
- The script will start monitoring the directory specified in config.json. Files will be moved to their respective subdirectories based on their extensions.
- To stop the script, simply press `CTRL+C`.

## Logs

Check the file_organizer.log file for detailed logs about file movements and any encountered issues.

## How It Works

The script monitors the specified directory and automatically moves newly added files to the corresponding categorized folder. If the folder doesn't exist, the script creates one. Currently, the script can organize the following file types:

- Images: `.jpg`, `.png`, `.jpeg`, `.gif`, `.bmp`
- Documents: `.doc`, `.docx`, `.txt`, `.pdf`, `.xlsx`, `.xls`, `.ppt`, `.pptx`
- Videos: `.mp4`, `.mkv`, `.flv`, `.mpeg`, `.avi`
- Applications: `.exe`, `.dmg`, `.apk`, `.jar`
- Zip files: `.zip`, `.rar`, `.7z`, `.tar.gz`


## Customization

To customize the file types and categories, modify the `file_types` dictionary in the `organize_files` function.

## Future Enhancements

- Implement a delay or file size check to ensure downloads are complete before moving files.
- Optimize for large directories by checking only newly modified files.

## Contributing

Feel free to fork this repository and make enhancements. Pull requests are welcome!

## Run on Startup

To run this script on startup, refer to the startup guide based on your operating system in the following [link](https://stackoverflow.com/questions/7284527/how-to-run-a-script-during-boot-as-root).

