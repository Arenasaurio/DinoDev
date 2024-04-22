library(ggplot2)

# Descomprime el archivo 'wine.zip'
unzip('wine.zip')

# Lee los datos desde el archivo "wine.data"
datos <- read.table("wine.data", header = TRUE, sep = ",")
colnames(datos)[2:14] <- c("Alcohol", "Malic_acid", "Ash", "Alcalinity_of_ash", "Magnesium",
                           "Total_phenols", "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins",
                           "Color_intensity", "Hue", "OD280sOD315_of_diluted_wines", "Proline")

# Elimina la primera columna (no necesaria)
datos <- datos[, -1]

# Guarda los datos en un archivo CSV llamado "wine_dataset.csv"
write.csv(datos, file = "wine_dataset.csv", row.names = FALSE)

# Calcula las medias de las variables
means <- sapply(datos, mean)
write.csv(means, "promedios.csv")

# Calcula las varianzas de las variables
vars <- sapply(datos, var)

# Calcula las covarianzas entre las variables
cov_matrix <- cov(datos)

# Calcula las correlaciones entre las variables
cor_matrix <- cor(datos)

# Imprime las medias y varianzas
print("Medias:")
print(means)
print("Varianzas:")
print(vars)

# Imprime las matrices de covarianza y correlación
print("Matriz de Covarianza:")
print(cov_matrix)
write.csv(cov_matrix, "matCov.csv")
print("Matriz de Correlación:")
print(cor_matrix)

# Convertir la matriz en un marco de datos para ggplot
cov_df <- as.data.frame(cov_matrix)
cov_df$row <- rownames(cov_df)
cov_df <- tidyr::gather(cov_df, col, value, -row)

cor_df <- as.data.frame(cor_matrix)
cor_df$row <- rownames(cor_df)
cor_df <- tidyr::gather(cor_df, col, value, -row)

# Gráficas de covarianzas y correlaciones
# Matriz de colores para la covarianza
mi_paleta <- colorRampPalette(c("turquoise4", "turquoise1", "white"))
mi_paleta2 <- colorRampPalette(c("turquoise4", "turquoise1", "blue"))
print(colnames(datos))

# Crea el gráfico de dispersión con la paleta de colores
variable_color <- "Flavanoids"
a <- ggplot(datos, aes(x = Flavanoids, y = Total_phenols, color = get(variable_color))) +
  geom_point() +
  scale_color_gradientn(colours = mi_paleta2(100)) +
  theme_minimal() +
  labs(title = "Gráfico de Covarianza entre Flavanoids y Total phenols",
       x = "Flavanoids",
       y = "Total phenols")
ggsave(filename = "covarianzaFlavTotPh.png", plot = a)


b <- ggplot(data = cor_df, aes(x = row, y = col, fill = value)) +
  geom_tile() +
  geom_text(aes(label = round(value, 2)), size = 3) + 
  scale_fill_gradientn(colours = mi_paleta(100), name = "Correlation") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  labs(title = "Matriz de Correlación")
ggsave(filename = "correlacion.png", plot = b)





# Gráficas relacionadas con los datos
# Histograma del Alcohol
c <- ggplot(datos, aes(x = Alcohol)) +
  geom_histogram(aes(y=..density..), binwidth = 1, fill = "turquoise4", color = "black") +
  geom_density(alpha=.2, fill="turquoise1") +
  theme_minimal() +
  labs(title = "Distribución del Alcohol", x = "Alcohol", y = "Densidad")
ggsave(filename = "historgramaAlc.png", plot = c)


d <-ggplot(datos, aes(x = Flavanoids, y = OD280sOD315_of_diluted_wines, color = get(variable_color))) +
  geom_point() +
  scale_color_gradientn(colours = mi_paleta2(100)) +
  theme_minimal() +
  labs(title = "Gráfico de Covarianza entre Flavanoids y la turbidez de un vino",
       x = "Flavanoids",
       y = "OD280sOD315_of_diluted_wines")
ggsave(filename = "covarianzaFlavTurb.png", plot = d)

e <- ggplot(data = cov_df, aes(x = row, y = col, fill = value)) +
  geom_tile() +
  geom_text(aes(label = round(value, 2)), size = 2) + 
  scale_fill_gradientn(colours = mi_paleta(100), name = "Covarianza") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  labs(title = "Matriz de Covarianza")
ggsave(filename = "covari.png", plot = e)
