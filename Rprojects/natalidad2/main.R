#<3J
library(dplyr)
library(ggplot2)
library(data.table)
library(reshape2)

#un verdadero hombre no habla mal de lopez obrador
data <- fread("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18.csv")
data2 <- data[, c("ent_resid", "ent_ocurr", "sexo", "edad_madn", "edad_padn", "ano_nac", "mes_nac", "escol_mad", "escol_pad")]
#1
media1 <- mean(data2$ent_resid, na.rm = TRUE)
mediana1 <- median(data2$ent_resid, na.rm = TRUE)
moda1 <- as.numeric(names(which.max(table(data2$ent_resid))))
std1 <- sd(data2$ent_resid, na.rm = TRUE)
png("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_hist1.png")
hist(data2$ent_resid, main = "Entidad residencia", xlab = "")

abline(v = media1, col = "blue", lwd = 2)
abline(v = mediana1, col = "red", lwd = 2)
abline(v = mediana1+std1, col = "red", lwd = 2)
abline(v = mediana1-std1, col = "red", lwd = 2)
abline(v = moda1, col = "purple", lwd = 2)
legend("topright", legend = c("Promedio", "Moda", "Mediana y desviación"), fill = c("blue", "purple", "red"))

dev.off()
#2
media2 <- mean(data2$ent_ocurr, na.rm = TRUE)
mediana2 <- median(data2$ent_ocurr, na.rm = TRUE)
moda2 <- as.numeric(names(which.max(table(data2$ent_ocurr))))
std2 <- sd(data2$ent_ocurr, na.rm = TRUE)
png("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_hist2.png")
hist(data2$ent_ocurr, main = "Entidad ocurrencia", xlab = "")

abline(v = media2, col = "blue", lwd = 2)
abline(v = mediana2, col = "red", lwd = 2)
abline(v = mediana2+std2, col = "red", lwd = 2)
abline(v = mediana2-std2, col = "red", lwd = 2)
abline(v = moda2, col = "purple", lwd = 2)
legend("topright", legend = c("Promedio", "Moda", "Mediana y desviación"), fill = c("blue", "purple", "red"))

dev.off()
#3
media3 <- mean(data2$sexo, na.rm = TRUE)
mediana3 <- median(data2$sexo, na.rm = TRUE)
moda3 <- as.numeric(names(which.max(table(data2$sexo))))
std3 <- sd(data2$sexo, na.rm = TRUE)
png("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_hist3.png")
hist(data2$sexo, main = "Sexo", xlab = "", xlim = c(0, 3))

abline(v = media3, col = "blue", lwd = 2)
abline(v = mediana3, col = "red", lwd = 2)
abline(v = mediana3+std3, col = "red", lwd = 2)
abline(v = mediana3-std3, col = "red", lwd = 2)
abline(v = moda3, col = "purple", lwd = 2)
legend("topright", legend = c("Promedio", "Moda", "Mediana y desviación"), fill = c("blue", "purple", "red"))

dev.off()
#4
media4 <- mean(data2$edad_madn, na.rm = TRUE)
mediana4 <- median(data2$edad_madn, na.rm = TRUE)
moda4 <- as.numeric(names(which.max(table(data2$edad_madn))))
std4 <- sd(data2$edad_madn, na.rm = TRUE)
png("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_hist4.png")
hist(data2$edad_madn, main = "Edad madre", xlab = "")

abline(v = media4, col = "blue", lwd = 2)
abline(v = mediana4, col = "red", lwd = 2)
abline(v = mediana4+std4, col = "red", lwd = 2)
abline(v = mediana4-std4, col = "red", lwd = 2)
abline(v = moda4, col = "purple", lwd = 2)
legend("topright", legend = c("Promedio", "Moda", "Mediana y desviación"), fill = c("blue", "purple", "red"))

dev.off()
#5
media5 <- mean(data2$edad_padn, na.rm = TRUE)
mediana5 <- median(data2$edad_padn, na.rm = TRUE)
moda5 <- as.numeric(names(which.max(table(data2$edad_padn))))
std5 <- sd(data2$edad_padn, na.rm = TRUE)
png("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_hist5.png")
hist(data2$edad_padn, main = "Edad padre", xlab = "")

abline(v = media5, col = "blue", lwd = 2)
abline(v = mediana5, col = "red", lwd = 2)
abline(v = mediana5+std5, col = "red", lwd = 2)
abline(v = mediana5-std5, col = "red", lwd = 2)
abline(v = moda5, col = "purple", lwd = 2)
legend("topright", legend = c("Promedio", "Moda", "Mediana y desviación"), fill = c("blue", "purple", "red"))

dev.off()
#6
media6 <- mean(data2$ano_nac, na.rm = TRUE)
mediana6 <- median(data2$ano_nac, na.rm = TRUE)
moda6 <- as.numeric(names(which.max(table(data2$ano_nac))))
std6 <- sd(data2$ano_nac, na.rm = TRUE)
png("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_hist6.png")
hist(data2$ano_nac, main = "Ano nacimiento", xlab = "", breaks = 1000, xlim = c(2000, 2025))

abline(v = media6, col = "blue", lwd = 2)
abline(v = mediana6, col = "red", lwd = 2)
abline(v = mediana6+std6, col = "red", lwd = 2)
abline(v = mediana6-std6, col = "red", lwd = 2)
abline(v = moda6, col = "purple", lwd = 2)
legend("topright", legend = c("Promedio", "Moda", "Mediana y desviación"), fill = c("blue", "purple", "red"))

dev.off()
#7
media7 <- mean(data2$mes_nac, na.rm = TRUE)
mediana7 <- median(data2$mes_nac, na.rm = TRUE)
moda7 <- as.numeric(names(which.max(table(data2$mes_nac))))
std7 <- sd(data2$mes_nac, na.rm = TRUE)
png("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_hist7.png")
hist(data2$mes_nac, main = "Mes nacimiento", xlab = "", breaks = 100, xlim = c(1,12))

abline(v = media7, col = "blue", lwd = 2)
abline(v = mediana7, col = "red", lwd = 2)
abline(v = mediana7+std7, col = "red", lwd = 2)
abline(v = mediana7-std7, col = "red", lwd = 2)
abline(v = moda7, col = "purple", lwd = 2)
legend("topright", legend = c("Promedio", "Moda", "Mediana y desviación"), fill = c("blue", "purple", "red"))

dev.off()
#8
media8 <- mean(data2$escol_mad, na.rm = TRUE)
mediana8 <- median(data2$escol_mad, na.rm = TRUE)
moda8 <- as.numeric(names(which.max(table(data2$escol_mad))))
std8 <- sd(data2$escol_mad, na.rm = TRUE)
png("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_hist8.png")
hist(data2$escol_mad, main = "Escolaridad Madre", xlab = "")

abline(v = media8, col = "blue", lwd = 2)
abline(v = mediana8, col = "red", lwd = 2)
abline(v = mediana8+std8, col = "red", lwd = 2)
abline(v = mediana8-std8, col = "red", lwd = 2)
abline(v = moda8, col = "purple", lwd = 2)
legend("topright", legend = c("Promedio", "Moda", "Mediana y desviación"), fill = c("blue", "purple", "red"))

dev.off()
#9
media9 <- mean(data2$escol_pad, na.rm = TRUE)
mediana9 <- median(data2$escol_pad, na.rm = TRUE)
moda9 <- as.numeric(names(which.max(table(data2$escol_pad))))
std9 <- sd(data2$escol_pad, na.rm = TRUE)
png("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_hist9.png")
hist(data2$escol_pad, main = "Escolaridad Padre", xlab = "")

abline(v = media9, col = "blue", lwd = 2)
abline(v = mediana9, col = "red", lwd = 2)
abline(v = mediana9+std9, col = "red", lwd = 2)
abline(v = mediana9-std9, col = "red", lwd = 2)
abline(v = moda9, col = "purple", lwd = 2)
legend("topright", legend = c("Promedio", "Moda", "Mediana y desviación"), fill = c("blue", "purple", "red"))

dev.off()

#Covarianza y correlacion
covarianza <- cov(data2)
correlacion <- cor(data2)
df_covarianza <- melt(covarianza)
df_correlacion <- melt(correlacion)

g1 <- ggplot(df_covarianza, aes(x=Var1, y=Var2, fill=value)) + 
  geom_tile() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Matriz de Covarianza", x = "Variable", y = "Variable")

g2 <- ggplot(df_correlacion, aes(x=Var1, y=Var2, fill=value)) + 
  geom_tile() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Matriz de Correlación", x = "Variable", y = "Variable")

ggsave("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_cov.png", g1)
ggsave("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18_cor.png", g2)
