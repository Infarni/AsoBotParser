# AsoBotParser

# Create virtual enviroment
python -m venv venv

# Install requirements
pip install -r requirements.txt

# Settings
To log in to your account, you need to enter your mobile phone number in the constant in the settings.py file

# Launch
After launching, you need to enter the code that will be sent to you by Telegram and then the password for your account
If you need to change your account, delete the <your phone number>.session file and change the PHONE constant to a new number

To parse categories, run categories.py. The file is saved in data/categories.csv (Note: the file is not canceled when you collect new data. It must be deleted before running it again, otherwise new data will be added to the end of the file)
To parsing applications, you need to place a manually formatted file with application id in data/format_apps.csv and then run apps.py (Note: the file is not canceled when you collect new data. It must be deleted before running it again, otherwise new data will be added to the end of the file)