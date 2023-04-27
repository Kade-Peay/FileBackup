import logging
import shutil
import os
from datetime import datetime

# Set up logging configuration
logging.basicConfig(filename="backup.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# What to backup where kinda thing
local_backup = "C:/Users/Kade/Desktop/Film"
server_backup = "//10.66.45.171/nas/Film"

# Folder is organized as follows
# Film/datedFolder/
# inside the dated folder are pictures


# Loop through all my folders
for folder in os.listdir(local_backup):
    local_folder = os.path.join(local_backup, folder)
    server_folder = os.path.join(server_backup, folder)
    if not os.path.exists(server_folder):
        shutil.copytree(local_folder, server_folder)

        # Log the backup operation
        now = datetime.now()
        date_string = now.strftime("%Y-%m-%d %H:%M:%S")
        message = f"Backup completed on {date_string} - Local folder: {str(folder)}"
        logging.info(message)
    else:
        # Log that the backup was skipped
        now = datetime.now()
        date_string = now.strftime("%Y-%m-%d %H:%M:%S")
        message = f"Backup skipped on {date_string} - Local folder already exists: {str(folder)}"
        logging.info(message)

# Print the date string
print(f"Backup Succesful on {date_string}")
