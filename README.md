# Advanced File Converter 🚀

This is a web-based file converter with a powerful two-part design.

* **⚡️ Live Demo (Client-Side):** The main interface runs directly in your browser. It uses JavaScript for fast and private conversions like Image-to-PDF, PDF-to-Image, and text manipulation. You can try it out right now!
* **🧠 Full Power (Server-Side):** For high-quality PDF to Word (DOCX) conversion that preserves layout, tables, and images, this project uses a Python backend. To unlock this feature, you need to run the backend on your computer.

## Live Demo

**[👉 Click here to try the live demo 👈](https://johnrey1819.github.io/templates/)**

*(Note: In the live demo, only the JavaScript-based conversions will work. PDF to DOCX requires the local setup below.)*

---

## Get Full Functionality: Local Setup Guide

To use the powerful PDF-to-DOCX converter and run the complete application, follow these steps on your own computer.

### 1. Get the Code

Clone this repository to your machine using Git:
```bash
git clone [https://johnrey1819.github.io/templates/](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git)
cd YOUR-REPOSITORY-NAME
```
(Or use the "Download ZIP" option on GitHub).

### 2. Set Up the Python Backend

You'll need your terminal or command prompt for these steps.

**a. Create and Activate a Virtual Environment**

This creates a safe sandbox for the Python tools.
```bash
# On macOS or Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```
*(You will see `(venv)` next to your command prompt if it worked.)*

**b. Install the Required Tools**

This project uses a few Python libraries. Install them easily with this command:
```bash
pip install -r requirements.txt
```

### 3. Run the Full Application

**a. Start the Python Server**

In your terminal (with `(venv)` active), start the server:
```bash
python app.py
```
Keep this terminal window open! It's now running the "brain" of the converter.

**b. Open the Website**

Go to the project folder on your computer and double-click the `index.html` file.

**✅ Success!** The website is now open, and because the Python server is running in the background, **all features, including PDF to DOCX, will work perfectly.**

---

## Troubleshooting

* **PDF to DOCX Fails:** If you get a "Could not connect" error, it's because the Python server (`app.py`) is not running. Make sure the terminal from Step 3a is still open and running the script.
* **Command Not Found (`python` or `pip`):** You may need to [install Python](https://www.python.org/downloads/) or use `python3` and `pip3` on macOS/Linux.
