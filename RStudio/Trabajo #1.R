#vector: Variable string / todo lo que empiece por c:
variable<- "Hola mundo" 
#Lista
materias<- c("Biología","Química", "Física")
notas_materias<- matrix(c(4.3, 4.5, 5.0, 4.0, 3.0, 2.5, 4.6, 4.0, 5.0), nrow=3, ncol=3, byrow= TRUE)
#Tipo arreglo
#Similar a una matrix y a una lista
arreglo <- array(c('perros', 'gatos'), dim = c(3,4,2))
arreglo <- array(c('perros', 'gatos', "loros"), dim = c(3,4,2))
arreglo <- array(c('perros', 'gatos', "loros"), dim = c(3,4,1))
arreglo <- array(c('perros', 'gatos', "loros"), dim = c(3,4,3))

suma <- function(var1, var2) {
  resultado = var1 + var2
  return(resultado)
}

