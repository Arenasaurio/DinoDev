
library(tidydice)
library(dplyr)
library(explore)

library(readxl)

datos<-read_excel("datos.xlsx")
head(datos)
datos <- datos[, -which(names(datos) %in% c("Marca Temporal", "Nombre completo:"))]
a<- unlist(datos)
S<-0:10
frecuencia<-numeric(length(S))
for(numero in S){
  frecuencia[numero]<-sum(a==numero)
  print(frecuencia[numero])
}

for(i in seq_along(S)){
  cat("Numero", S[i], ":", frecuencia[i], "\n")
  probabilidad<-frecuencia[i]/length(a)
  cat("Probabilidad de ", S[i], ":", probabilidad[i], "\n")
}