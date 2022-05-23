import shutil

# Full path of
# the archive file
filename = "/home/dani/Descargas/Proyecto+Dia+9.zip"

# Target directory
extract_dir = "/home/dani/Documentos/python/Día 9/"

# Format of archive file
archive_format = "zip"

# Unpack the archive file
shutil.unpack_archive(filename, extract_dir, archive_format)
print("Archive file unpacked successfully.")
