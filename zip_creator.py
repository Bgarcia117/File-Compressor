import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    # This uses path lib to execute dest_dir + '/' compressed.zip
    with zipfile.ZipFile(dest_path, 'w') as archive:
        # zipfile.ZipFile is the library and a type that is used to make a zipfile and writes to the directory.     
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            # simplifies the file directories
            archive.write(filepath, arcname=filepath.name)
            # This writes the filepaths to the zipfile (archive is the zip) and arcname=filepath.name extracts the name of the file from the filepath.

if __name__ == "__main__":
    make_archive(filepaths=["example.py", "example2.py"], dest_dir="dest")
    # If this file is ran directly, the code will be executed. If it is imported, it will be ignored. 