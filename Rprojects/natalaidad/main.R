library(readr)
library(dplyr)

# Leer el archivo CSV
datosnat <- read_csv("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natilidad2k18.csv")

# Calcular las medidas de tendencia central y dispersión para cada variable
variables <- c('ent_resid', 'ent_ocurr', 'sexo', 'edad_madn', 'edad_padn', 'ano_nac', 'mes_nac', 'escol_mad', 'escol_pad')
meduniv <- data.frame()

for (var in variables) {
  media <- mean(datosnat[[var]], na.rm = TRUE)
  moda <- as.numeric(names(which.max(table(datosnat[[var]]))))
  mediana <- median(datosnat[[var]], na.rm = TRUE)
  varianza <- var(datosnat[[var]], na.rm = TRUE)
  desviacionEstandar <- sd(datosnat[[var]], na.rm = TRUE)
  
  meduniv <- rbind(meduniv, data.frame(media, moda, mediana, varianza, desviacionEstandar))
}

rownames(meduniv) <- variables

# Guardar las medidas univariadas en un archivo CSV
write.csv(meduniv, "C:/Users/Csera/Documents/DinoDev_data/PyProjects/natilidad2k18_medidasUniv1.csv")

# Calcular la correlación y covarianza entre las variables
correlacion <- cor(c(datosnat[]), use = "complete.obs")
covarianza <- cov(as.numeric(datosnat[variables]), use = "complete.obs")

# Guardar la correlación y covarianza en archivos CSV
write.csv(correlacion, "C:/Users/Csera/Documents/DinoDev_data/PyProjects/natilidad2k18_correlacion1.csv")
write.csv(covarianza, "C:/Users/Csera/Documents/DinoDev_data/PyProjects/natilidad2k18_covarianza1.csv")
