YouTube Subscriptions Retriever
===============================

This project retrieves your YouTube subscriptions—sorted from the oldest to the newest—and saves the information in a text file named "subscriptions.txt".

Features
--------
- OAuth 2.0 Authentication: Securely authenticate your Google account.
- Data Retrieval: Fetches your YouTube subscriptions using the YouTube Data API v3.
- Sorting: Sorts subscriptions by the date you subscribed (oldest first).
- Output File: Saves the results to a text file for easy review.

Installation
------------
1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/YouTube-Subscriptions-Retriever.git
   cd YouTube-Subscriptions-Retriever

2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate   # For Windows use: venv\Scripts\activate

3. Install the dependencies:
   pip install -r requirements.txt

Configuration
-------------
1. Set Up Google API Credentials:
   - Go to the Google Cloud Console: https://console.developers.google.com/
   - Enable the YouTube Data API v3 for your project.
   - Create an OAuth client ID for a desktop application.
   - Download the JSON file and place it in the repository root.
   - Rename the file to "client_secret.json" (or update the filename in the code accordingly).

2. Note:
   - Do not share your "client_secret.json" file publicly, as it contains sensitive information.

Usage
-----
Simply run the script from the repository root:
   python script.py

Follow the authentication prompt in your browser. After authorization, the script will generate a file named "subscriptions.txt" in the same directory containing your subscription details.

Files Included
--------------
- script.py: The main script that retrieves and processes your YouTube subscriptions.
- requirements.txt: Lists the required Python libraries.
- README.txt: This documentation file.

Contributing
------------
Contributions are welcome! Please feel free to open an issue or submit a pull request with improvements or bug fixes.
