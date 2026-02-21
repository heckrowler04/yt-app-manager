🎬 YouTube Video Manager (CLI App)
==================================

A simple **Python command-line application** to manage your saved YouTube videos.

This project allows you to:

-   📄 List stored videos

-   ➕ Add a new video

-   ✏️ Update video details

-   ❌ Delete a video

-   💾 Persist data using a JSON file

All video data is stored locally inside a `youtube.txt` file in JSON format.

* * * * *

🚀 Features
-----------

-   Stores video data as **JSON** (JavaScript Object Notation --- a lightweight structured data format)

-   Uses Python file handling

-   Simple CLI menu-driven interface

-   Uses `match-case` (Python 3.10+ feature)

-   Automatically saves updates after every modification

* * * * *

🛠️ Tech Stack
--------------

-   **Python 3.10+**

-   Built-in `json` module

-   File handling

* * * * *

📂 Project Structure
--------------------

youtube-manager/\
│\
├── main.py\
├── youtube.txt   (auto-created when you add videos)\
└── README.md

* * * * *

⚙️ How It Works
---------------

### 1️⃣ Load Data

-   Reads video data from `youtube.txt`

-   If the file does not exist, it initializes an empty list

* * * * *

### 2️⃣ Add Video

-   Takes video name and duration as input

-   Appends data as a dictionary:

{"Name": "Video Title", "Time": "10:05"}

* * * * *

### 3️⃣ Update Video

-   Displays all videos

-   User selects index

-   Replaces selected video with new details

* * * * *

### 4️⃣ Delete Video

-   Displays all videos

-   User selects index

-   Deletes the selected entry

* * * * *

▶️ How To Run
-------------

### Step 1 --- Clone the repository

git clone https://github.com/your-username/youtube-manager.git\
cd youtube-manager

* * * * *

### Step 2 --- Run the script

python main.py

Make sure you are using **Python 3.10 or above** (required for `match-case`).

* * * * *

🧠 Learning Concepts Covered
----------------------------

This project helps you understand:

-   File handling in Python

-   JSON data storage

-   Lists and dictionaries

-   Functions and modular programming

-   Error handling using `try-except`

-   CLI application design

* * * * *

### 📊 Why This Project Is Useful for Data Engineering

-   JSON is widely used in APIs and data pipelines

-   File-based storage simulates basic data ingestion workflows

-   CRUD operations (Create, Read, Update, Delete) are foundational for data systems

* * * * *

📌 Future Improvements
----------------------

Possible enhancements:

-   Input validation (prevent crashes from invalid input)

-   Exception handling for invalid index

-   Use `.json` file instead of `.txt`

-   Add timestamps

-   Convert into a Flask web app

-   Store data in SQLite instead of file system

-   Add search functionality

* * * * *

🖥️ Sample Output
-----------------

---Youtube manager app---

1\. List all the yt vids you've stored\
2\. Add a yt video\
3\. Update a yt video details\
4\. Delete a yt video\
5\. Exit the app

* * * * *

📜 License
----------

This project is open-source and free to use.
