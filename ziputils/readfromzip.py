from zipfile import ZipFile

docker_compose_config = None

with ZipFile('config.zip') as zip_archive:
  docker_compose_config = zip_archive.read('config/docker/docker-compose.yaml')

print(docker_compose_config)