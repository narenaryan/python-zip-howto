from zipfile import ZipFile

with ZipFile('config.zip') as zip_archive:
  for item in zip_archive.filelist:
    print(item)
  print(f'\nThere are {len(zip_archive.filelist)} ZipInfo objects present in archive')
