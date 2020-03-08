from zipfile import ZipFile
from io import BytesIO

def create_zip_v1():
    """
    returns: zip archive
    """
    archive = BytesIO()

    with ZipFile(archive, 'w') as zip_archive:
        # Create three files on zip archive
        with zip_archive.open('docker/docker-compose.yaml', 'w') as file1:
            file1.write(b'compose-file-content...')
        
        with zip_archive.open('app/app-config.json', 'w') as file2:
            file2.write(b'app-config-content...')

        with zip_archive.open('root-config.json', 'w') as file3:
            file3.write(b'root-config-content...')


    return archive

archive = create_zip_v1()

# Flush archive stream to a file on disk
with open('config.zip', 'wb') as f:
    f.write(archive.getbuffer())

archive.close()