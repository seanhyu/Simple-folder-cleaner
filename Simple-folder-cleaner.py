import os
from os.path import exists, join
from shutil import move

PPTS = r"C:\Users\Sean Yu\Documents\PPTS"
XLSXS = r"C:\Users\Sean Yu\Documents\Excels"
PDFS = r"C:\Users\Sean Yu\Documents\PDFS"
DOCXS = r"C:\Users\Sean Yu\Documents\Docs"
PICS = r"C:\Users\Sean Yu\Pictures"
PROGRAMS = r"C:\Users\Sean Yu\AppData\Local\Programs\Downloaded"
VIDEOS = r"C:\Users\Sean Yu\Videos"
APPS = r"C:\Users\Sean Yu\Apps"


def uniqueName(oldName):
    name = oldName
    counter = 1
    while exists(name):
        name = f"{name} ({str(counter)})"
        counter += 1
    return name
def moveFile (dest,entry,name):
    if exists(f"{dest}\\{name}"):
        oldName = f"{dest}\\{name}"
        newName = uniqueName(oldName)
        os.rename(oldName,newName)
    move(entry,dest)

class fileMover():
    def moveHandler(self):
        with os.scandir(r"C:\Users\Sean Yu\Downloads") as directory:
            for entry in directory:
                name = entry.name
                if name.endswith(".pptx"):
                    moveFile(PPTS,entry,name)
                elif name.endswith(".pdf"):
                    moveFile(PDFS,entry,name)
                elif name.endswith(".jpg") or name.endswith(".png") or name.endswith(".jpeg") or name.endswith(".PNG"):
                    moveFile(PICS,entry,name)
                elif name.endswith(".py") or name.endswith(".cpp") or name.endswith(".java"):
                    moveFile(PROGRAMS,entry,name)
                elif name.endswith(".xlsx"):
                    moveFile(XLSXS,entry,name)
                elif name.endswith(".docx"):
                    moveFile(DOCXS,entry,name)
                else:
                    continue
