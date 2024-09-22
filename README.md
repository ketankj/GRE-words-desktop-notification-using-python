# GRE_Words_Desktop_Notification using python

GRE Vocabulary Notification Script
This script randomly selects GRE vocabulary words from a JSON file and sends desktop notifications at regular intervals. It's perfect for those preparing for the GRE or anyone who wants to build their vocabulary by receiving regular reminders.

Features:
Sends notifications with a randomly selected GRE word and its meaning.
Notifies users every 30 minutes by default.
Uses plyer to create desktop notifications.
Customizable notification icon for a personalized experience.
Requirements:
Python 3.x
plyer library for notifications
JSON file containing the vocabulary words and their meanings
(Optional) Custom icon for the notification
Installation:
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/GRE_Vocab_Notifier.git
cd GRE_Vocab_Notifier
Install the required Python library:

bash
Copy code
pip install plyer
Place your GRE words in a JSON file named GRE_Words.json in the same directory. The JSON format should look like this:

json
Copy code
{
  "word1": "definition1",
  "word2": "definition2",
  ...
}
(Optional) Customize the notification icon by placing your .ico file in the directory and updating the file path in the script.

Usage:
Ensure the JSON file with words and meanings is present in the same folder.

Run the Python script:

bash
Copy code
python gre_vocab_notifier.py
The script will send you a desktop notification with a new GRE word and its definition every 30 minutes.

Customization:
To change the interval between notifications, modify the time.sleep(60*30) line in the script to your preferred time in seconds (e.g., 60 seconds = 1 minute).
You can replace the default icon by updating the path in the app_icon parameter in the script.
