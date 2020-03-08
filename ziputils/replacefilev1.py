from zipfile import ZipFile

with ZipFile('config.zip', 'a') as zip_archive:
	zip_archive.writestr(
		'docker/docker-compose.yaml', # File to replace
    b'docker-compose-file-content-new'   # Data
  )
