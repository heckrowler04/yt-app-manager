🎬 YouTube Video Manager CLI
============================

> A minimal, fast, and interactive **command-line video tracker** built with Python.\
> Store, manage, and organize your saved YouTube videos locally --- no database required.

* * * * *

✨ Overview
----------

This project is a lightweight **CLI-based video manager** that lets you maintain a personal collection of videos with simple commands. It demonstrates core programming concepts, clean logic design, and real-world data handling patterns.

* * * * *

⚡ Features
----------

✔ List saved videos\
✔ Add new videos\
✔ Update existing entries\
✔ Delete videos\
✔ Automatic data persistence\
✔ Clean menu-driven interface

All data is stored locally inside:

youtube.txt

in structured **JSON format**\
(JSON = a standard text format used for storing structured data)

* * * * *

🧰 Tech Stack
-------------

| Technology | Purpose |
| --- | --- |
| Python 3.10+ | Core programming language |
| JSON Module | Data storage |
| File Handling | Persistent storage |
| Match-Case | Menu navigation logic |

* * * * *

📁 Project Structure
--------------------

youtube-manager/\
│\
├── main.py\
├── youtube.txt     # auto-generated storage file\
└── README.md

* * * * *

⚙️ How It Works
---------------

### Data Loading

-   Reads stored videos from file

-   Initializes empty list if file doesn't exist

### Add Operation

Stores videos in dictionary format:

{"Name": "Video Title", "Time": "10:05"}

### Update Operation

-   Displays list

-   User selects index

-   Replaces selected record

### Delete Operation

-   Displays list

-   Removes chosen entry

* * * * *

▶️ Running the App
------------------

### 1️⃣ Clone Repository

git clone https://github.com/your-username/youtube-manager.git\
cd youtube-manager

### 2️⃣ Run Program

python main.py

Requirement:

Python ≥ 3.10

* * * * *

🧠 Concepts Demonstrated
------------------------

-   File I/O operations

-   JSON data handling

-   Lists & dictionaries

-   Functions and modular design

-   Error handling (`try-except`)

-   CLI interaction logic

* * * * *

📊 Why This Project Matters (For Developers)
--------------------------------------------

This project mirrors real engineering fundamentals:

| Concept | Real-World Equivalent |
| --- | --- |
| Local JSON Storage | API responses |
| CRUD Operations | Database systems |
| File Persistence | Data pipelines |
| Input Handling | User-facing tools |

* * * * *

🚀 Future Improvements
----------------------

Potential upgrades:

-   Input validation system

-   Search functionality

-   SQLite database backend

-   Timestamp logging

-   Web interface (Flask / FastAPI)

-   Export to CSV / JSON

-   Sorting & filtering

* * * * *

🖥 Example Interface
--------------------

--- Youtube Manager App ---

1\. List Videos\
2\. Add Video\
3\. Update Video\
4\. Delete Video\
5\. Exit

* * * * *

📜 License
----------

Open-source and free to use.

* * * * *

⭐ Developer Note
----------------

This project is intentionally simple but structured like a real system.\
It's designed to showcase clean logic, modular thinking, and data handling --- all core skills of strong software engineers.
