from zipfile import ZipFile, ZipInfo
from io import BytesIO

def create_zip_v2():
    """
    returns: zip archive
    """
    archive = BytesIO()

    with ZipFile(archive, 'w') as zip_archive:
        # Create three files on zip archive

        file1 = ZipInfo('docker/docker-compose.yaml')
        zip_archive.writestr(file1, b'compose-file-content...')

        file2 = ZipInfo('app/app-config.json')
        zip_archive.writestr(file2, b'app-config-content...')

        file3 = ZipInfo('root-config.json')
        zip_archive.writestr(file3, b'root-config-content...')

    return archive

archive = create_zip_v2()

# Flush archive stream to a file on disk
with open('config.zip', 'wb') as f:
    f.write(archive.getbuffer())

archive.close()