################################################################################
#                                                                              #
#                          GBIF2MaxEnt.R v0.1                                  #
#                                                                              #
# Comandos para la extracción de coordenadas de ocurrencia obtenidas de GBIF,  #
# procesados para ser utilizados (casi) de manera directa en MaxEnt            #
#                                                                              #
#                © Nicolás Pinel (CC BY-SA) - 2021-03-05                       #
#                                                                              #
################################################################################
#
# Lo primero que hay que hacer es cargar el archivo descargado de GBIF.
# Para hacer que todas las líneas a continuación fluyan sin problema,
# recomiendo cambiar el nombre del archivo descargado a datos.xlsx
# En caso de cargarlo a R con el nombre original, se debe ejecutar el comando:
#
# datos <- [NOMBRE DEL ARCHIVO ORIGINAL - SIN EXTENSION]
#
# reemplazando todo lo que se encuentra entre [] (incluyendo los corchetes) por
# el nombre del archivo (SIN extensión).

# Construímos el vector que utilizaremos como nombre de especie en cada fila.
species_name <- "Atelopus_spp"
species <- rep(species_name, length(datos$decimalLatitude))

# La siguiente línea construye el marco de datos que luego será
# guardada como un archivo
maxent <- data.frame("species" = species, "dd long" = datos$decimalLongitude, 
                     "dd lat" = datos$decimalLatitude)

# Asegurarse de darle un nombre al archivo que incluya la ruta completa a la 
# carpeta deseada. Si sólo se le asigna un nombre (sin ruta), este archivo 
# quedará guardado en la carpeta base del usuario (a menos que ya se haya hecho 
# algún cambio de directorio con el comando setwd() ).
out_file_name <- "data/samples/Atelopus_spp_occurences_gbif.csv"
write.csv(maxent, file=out_file_name, row.names=FALSE, quote=FALSE)

# Luego de guardar los datos como .csv, es importante modificar el nombre de 
# los encabezados de columna
# 
# dd.long -> dd long
# dd.lat  -> dd lat