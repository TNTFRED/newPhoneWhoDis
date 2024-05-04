# A Program to automatically back up a folder

import os
import shutil
import datetime
import schedule
import time

sourceDirectory = "C:/Users/Sam/codingProjects/PythonProjects"
destinationDirectory = "C:/Users/Sam/Documents/Backups"

def copyFolderToDirectory(source, dest):
  today = datetime.date.today()
  destDir = os.path.join(dest, str(today))

  try:
    shutil.copytree(source, destDir)
    print(f"Folder Copied to: {destDir}")
  except FileExistsError:
    print(f"Folder already exists in: {dest}")

schedule.every().weeks.do(lambda: copyFolderToDirectory(sourceDirectory, destinationDirectory))

while True:
  schedule.run_pending()
  time.sleep(300)