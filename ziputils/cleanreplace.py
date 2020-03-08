from zipfile import ZipFile, ZipInfo
from io import BytesIO


def update_or_insert(path, data):
    """
    Param: path -> file in archive
    Param: data -> data to be updated
    
    Returns a new zip file with the updated content
    for the given path
    """
    new_zip = BytesIO()

    with ZipFile('config.zip', 'r') as old_archive:
        with ZipFile(new_zip, 'w') as new_archive:
            for item in old_archive.filelist:
                if item.filename != path:
                    # Copy everything other than path to be inserted
                    new_archive.writestr(item, old_archive.read(item.filename))
                else:
                    # For path to insert, create a new object
                    zip_inf = ZipInfo(path)
                    new_archive.writestr(zip_inf, data)
    return new_zip

new_zip = update_or_insert(
    'docker/docker-compose.yaml',
    b'docker-compose-file-content-new'
)

# Flush new zip to disk
with open('config.zip', 'wb') as f:
    f.write(new_zip.getbuffer())

new_zip.close()
