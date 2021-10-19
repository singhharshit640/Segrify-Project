import os
import shutil
from pathlib import Path

# from win10toast import ToastNotifier


compressed = ["zip", "rar", "bz2", "7z", "arj", "gz", "z", "tar"]
documents = ["pdf", "doc", "docx", "txt", "tex", "wpd", "pptx", "odt", "odp", "ppt", "rtf", "ods", "xls", "xlsm",
             "xlsx",
             "pps"]
images = ["jpg", "jpeg", "png", "ico", "ai", "bmp", "gif", "ps", "psd", "svg", "tif", "tiff"]
music = ["mp3", "m3u8", "aif", "cda", "mid", "midi", "mp3", "mpa", "ogg", "wav", "wma", "wpl"]
programming = ["c", "cpp", "class", "cs", "h", "java", "pl", "sh", "swift", "vb"]
setup = ["exe", "msi", "bat", "bin", "deb", "pkg", "rpm", "wsf"]
videos = ["mp4", "mkv", "3g2", "3gp", "flv", "h264", "m4v", "mov", "mpg", "mpeg", "rm", "swf", "vob", "wmv"]

iso = ["iso", "dmg", "toast", "vcd"]
keys = ["pem", "ppk"]
shortcuts = ["lnk"]
torrent = ["torrent"]
fonts = ["fnt", "fon", "otf", "ttf"]
data_and_database_files = ["csv", "dat", "db", "dbf", "log", "mdb", "sql", "xml"]

# toaster = ToastNotifier()

structure = {
    "Compressed": compressed,
    "Data and DataBase Files": data_and_database_files,
    "Documents": documents,
    "Fonts": fonts,
    "Images": images,
    "Iso's (Disc or Media Files)": iso,
    "Music": music,
    "Programming": programming,
    "Setups (Installers)": setup,
    "Shortcuts": shortcuts,
    "Torrents": torrent,
    "Videos": videos,
}


def create_structure_txt(srcpath):
    structure_text_path = os.path.join(os.getcwd(), "structure.txt")
    shutil.copy(structure_text_path, srcpath)


def folder_name(extension):
    """Utility Function to Find the folder name in which the file is to be put"""

    # items() function returns the key and value
    for key, value in structure.items():
        if extension in value:
            return key

    # if extension not found return Others as folder name
    return "Others"


def create_path(srcpath, foldername):
    return Path(os.path.join(srcpath, foldername)).mkdir(exist_ok=True)


def movefiles(srcpath, file, foldername):
    """Utility Function to move files"""
    print(srcpath, file, foldername)

    # Make Sure the path exists
    create_path(srcpath, foldername)

    move_from = os.path.join(srcpath, file)
    move_to = os.path.join(srcpath, foldername)
    return shutil.move(move_from, move_to)


def segragete(srcpath):
    """Specify the path to be segregated"""
    print(srcpath)
    try:
        # Copying structure.txt file to the srcpath
        create_structure_txt(srcpath)
        for file in os.listdir(srcpath):
            if os.path.isfile(os.path.join(srcpath, file)):

                # Skip if filename is structure.txt
                if file == "structure.txt":
                    continue
                # Reversing File String to get last .
                fileReverse = file[::-1].split(".")[0]

                # Reversing the extension back to correct
                fileReverse = fileReverse[::-1].lower()

                # Get the Folder Name
                foldername = folder_name(fileReverse)
                movefiles(srcpath, file, foldername)

        # Return True when no Error
        return True
    except Exception as e:
        print("Failed: ", e)

        # Return False upon Error
        return False
        # toaster.show_toast("Status", "Segregation failed")
    # finally:
    # print("Segregation Comlete")
    # toaster.show_toast("Status", "Segregation completed successfully")
