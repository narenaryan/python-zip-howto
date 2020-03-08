from zipfile import ZipFile, ZipInfo
from io import BytesIO


def delete(path):
    """
    Param: path -> file in archive
    Param: data -> data to be updated
    
    Returns a new zip file after deleting path
    """
    new_zip = BytesIO()

    with ZipFile('config.zip', 'r') as old_archive:
        with ZipFile(new_zip, 'w') as new_archive:
            for item in old_archive.filelist:
                if item.filename != path:
                    # Copy everything other than path to be inserted
                    new_archive.writestr(item, old_archive.read(item.filename))

    return new_zip

new_zip = delete('docker/docker-compose.yaml')

# Flush new zip to disk
with open('config.zip', 'wb') as f:
    f.write(new_zip.getbuffer())

new_zip.close()
