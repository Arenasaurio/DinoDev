#TRABAJO REALIZADO POR ARENAS S. CESAR E.,CUAHUTLE S. LUIS A., FELIX P. RODRIGO

unzip('wine.zip')

datos <- read.table("wine.data", header = TRUE, sep = ",")
colnames(datos)[2]<-"Alcohol"
colnames(datos)[3]<-"Malic acid"
colnames(datos)[4]<-"Ash"
colnames(datos)[5]<-"Alcalinity of ash"
colnames(datos)[6]<-"Magnesium"
colnames(datos)[7]<-"Total phenols"
colnames(datos)[8]<-"Flavanoids"
colnames(datos)[9]<-"Nonflavanoid phenols"
colnames(datos)[10]<-"Proanthocyanins"
colnames(datos)[11]<-"Color intensity"
colnames(datos)[12]<-"Hue"
colnames(datos)[13]<-"OD280/OD315 of diluted wines"
colnames(datos)[14]<-"Proline"
datos <- datos[ , -c(1)]

mean(datos[ , c(1)])
mean(datos[ , c(2)])
mean(datos[ , c(3)])
mean(datos[ , c(4)])
mean(datos[ , c(5)])
mean(datos[ , c(6)])
mean(datos[ , c(7)])
mean(datos[ , c(8)])
mean(datos[ , c(9)])
mean(datos[ , c(10)])
mean(datos[ , c(11)])
mean(datos[ , c(12)])
mean(datos[ , c(13)])
summary(datos)
resultados<-c()
for(i in 1:13) {
  for(j in i:13) {
    r <- cor(datos[,i], datos[,j])
    resultados <- c(resultados, r)
    
  }
}

# Imprime los resultados
print('Correlaciones')
print(resultados)
