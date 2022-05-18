import zipfile
import shutil



shutil.unpack_archive('Todo_comprimido.zip', 'Extraccion_terminada', 'zip')




#carpeta_origen = '/home/dani/Documentos/python/Día 9/Carpeta_compri'
#
#archivo_destino = 'Todo_comprimido'
#
#shutil.make_archive(archivo_destino, 'zip', carpeta_origen)









#zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')   #'r'= solo lectura
#zip_abierto.extractall()



#
#mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')    #'w'= escritura
#
#
#mi_zip.write('mi_texto1.txt')
#mi_zip.write('mi_texto2.txt')
#
#
#mi_zip.close()
