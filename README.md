# Advanced File Converter 🚀

This is a full-stack file converter application designed for live web hosting. It consists of:

1.  **Frontend:** A static HTML, CSS, and JavaScript site that handles most conversions directly in the browser.
2.  **Backend:** A Python Flask API for high-quality PDF to Word (DOCX) conversions, designed to be hosted as a web service.

This guide details how to deploy the entire application for free using GitHub and Render.

### **Prerequisites**
* A **[GitHub](https://github.com/)** account.
* A **[Render](https://render.com/)** account (you can sign up for free using your GitHub account).

---

## Deployment Instructions

We will deploy this project in two parts on Render: the Python **Web Service** (backend) and the **Static Site** (frontend).

### Step 1: Get the Code on GitHub

1.  **Create Files:** Create the four files (`index.html`, `app.py`, `requirements.txt`, `README.md`) in a folder on your computer.
2.  **Create Repository:** Go to GitHub and create a new, empty repository.
3.  **Upload Files:** Upload the four files to your new GitHub repository.

### Step 2: Deploy the Python Backend on Render

This will create the live server that performs the PDF to DOCX conversion.

1.  Log in to your **Render Dashboard**.
2.  Click **New +** and select **Web Service**.
3.  Connect the GitHub repository you just created.
4.  Fill in the service details:
    * **Name:** `file-converter-backend` (or any unique name).
    * **Region:** Choose a region near you (e.g., Singapore).
    * **Branch:** `main` (or your default branch).
    * **Runtime:** `Python 3`.
    * **Build Command:** `pip install -r requirements.txt`.
    * **Start Command:** `gunicorn app:app`.
    * **Instance Type:** Select `Free`.
5.  Click **Create Web Service**.
6.  Render will start building and deploying your backend. This may take a few minutes.
7.  Once it's live, **copy the URL** for your service. It will look something like `https://file-converter-backend.onrender.com`.

### Step 3: Connect the Frontend to Your Live Backend

Now we tell the website where to find its Python "brain".

1.  Go back to your code on your computer (or edit directly on GitHub).
2.  Open the `index.html` file.
3.  Find this line in the JavaScript section:
    ```javascript
    const backendUrl = '[https://your-backend-service-name.onrender.com/convert-pdf-to-docx](https://your-backend-service-name.onrender.com/convert-pdf-to-docx)';
    ```
4.  **Replace the placeholder URL** with the backend URL you copied from Render in the previous step. Make sure to keep the `/convert-pdf-to-docx` at the end.
5.  Save the changes to `index.html` and push them to your GitHub repository.

### Step 4: Deploy the Frontend on Render

This will publish your user-facing website.

1.  Go back to your **Render Dashboard**.
2.  Click **New +** and select **Static Site**.
3.  Select the **same GitHub repository** as before.
4.  Fill in the service details:
    * **Name:** `file-converter-frontend` (or any name you like).
    * **Branch:** `main`.
5.  The build settings can be left as default. Click **Create Static Site**.
6.  Render will deploy your `index.html` file. This is usually very fast.

### Step 5: You're Live!

Your static site will now have its own public URL (e.g., `https://file-converter-frontend.onrender.com`).

* **This is the main URL you share with people.**
* When a user visits this site and converts a PDF to DOCX, your frontend will correctly send the file to your live backend service for processing.

The entire application is now fully deployed and functional on the web.
