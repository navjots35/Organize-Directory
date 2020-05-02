import os
from pathlib import Path


# Created Category of file and extensions associated with it. Add as much as you want. 
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png'],
    "SOFTWARES": ['.exe', '.msi'],
    "ARCHIVES": ['.zip', '.rar', '.iso'],
    ".HTML FILES": ['.html'],
    "TORRENT FILES": ['.torrent']
}

# Function isolates the extension from the file and returns it, if can't find the extension based on the dictionary defined above then put it in a MISC
def take_my_extension(value):
    for category, extensions in SUBDIRECTORIES.items():
        for extension in extensions:
            if extension == value:
                return category
    return 'MISC'

# Just testing the above function
print(take_my_extension('.msi'))

# The main leader
def organize_it_baby():
    for item in os.scandir():
        if item.is_dir():       # If is directory the skip it
            continue
        itemPath = Path(item)                   #takes the file
        filetype = itemPath.suffix.lower()                  #isolates the extension from the file
        directory = take_my_extension(filetype)             # Passing the extension to the function 
        directoryPath = Path(directory)                     
        if directoryPath.is_dir() != True:                  # Creating Directory if does not exist
            directoryPath.mkdir()                           
        itemPath.rename(directoryPath.joinpath(itemPath))

organize_it_baby()                                  # calling it
