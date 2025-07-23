# file_organizer
🗂️ File Organizer (Python Script)
A simple yet effective Python script to organize files locally into categorized folders such as Images, Videos, Documents, Music, and more. This script helps clean up messy download folders or desktops in seconds.

📌 Features
🔍 Automatically identifies file types based on extensions

🗃 Groups similar files into subfolders (e.g., JPGs and PNGs into Images)

🪄 Customizable folder structure

🧹 Works on any local directory

💻 Cross-platform: Windows, macOS, and Linux

📂 Example
Before:

text
Downloads/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── script.py
├── video.mp4
├── archive.zip
After:

text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Music/
│   └── song.mp3
├── Scripts/
│   └── script.py
├── Videos/
│   └── video.mp4
├── Archives/
│   └── archive.zip
🚀 Getting Started
✅ Prerequisites
Python 3.x installed

📦 Install Required Libraries (if any)
This script uses only built-in Python libraries like os, shutil, and pathlib, so no external dependencies are needed.

🛠️ Usage
Clone the repository or download the script:

bash
git clone https://github.com/your-username/fileorganizer.git
cd fileorganizer
Run the organizer script:

bash
python file_organizer.py
When prompted, enter the path of the folder to organize (or set it inside the script).

🧠 How It Works
Scans a directory for files

Classifies them by extension:

.jpg, .png → Images

.pdf, .docx, .txt → Documents

.mp3, .wav → Music

.mp4, .avi → Videos

.zip, .rar → Archives

.py, .js, .cpp → Code

Moves each file to its respective folder

✏️ Customize Categories
You can edit the script to modify or add custom categories. Look for a dictionary like:

python
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    ...
}
Just add or change extensions as needed.

📁 File Structure
text
fileorganizer/
├── README.md
├── file_organizer.py
💡 Tip
Automate the script to run on a schedule using:

Windows: Task Scheduler

macOS/Linux: cron jobs

📜 License
This project is licensed under the MIT License.

🤝 Contributing
Pull requests, issues, and suggestions are welcome!
Feel free to fork the repo and make improvements.
