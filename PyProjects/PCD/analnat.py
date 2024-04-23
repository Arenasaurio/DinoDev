import pandas as pd
import numpy as np

datosnat = pd.read_csv("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natilidad2k18.csv")
media1=datosnat['ent_resid'].mean()
moda1=datosnat['ent_resid'].mode()
mediana1=datosnat['ent_resid'].median()
varian1=datosnat['ent_resid'].var()
desvia1=datosnat['ent_resid'].std()

media2=datosnat['ent_ocurr'].mean()
moda2=datosnat['ent_ocurr'].mode()
mediana2=datosnat['ent_ocurr'].median()
varian2=datosnat['ent_ocurr'].var()
desvia2=datosnat['ent_ocurr'].std()

media3=datosnat['sexo'].mean()
moda3=datosnat['sexo'].mode()
mediana3=datosnat['sexo'].median()
varian3=datosnat['sexo'].var()
desvia3=datosnat['sexo'].std()

media4=datosnat['edad_madn'].mean()
moda4=datosnat['edad_madn'].mode()
mediana4=datosnat['edad_madn'].median()
varian4=datosnat['edad_madn'].var()
desvia4=datosnat['edad_madn'].std()

media5=datosnat['edad_padn'].mean()
moda5=datosnat['edad_padn'].mode()
mediana5=datosnat['edad_padn'].median()
varian5=datosnat['edad_padn'].var()
desvia5=datosnat['edad_padn'].std()

media6=datosnat['ano_nac'].mean()
moda6=datosnat['ano_nac'].mode()
mediana6=datosnat['ano_nac'].median()
varian6=datosnat['ano_nac'].var()
desvia6=datosnat['ano_nac'].std()

media7=datosnat['mes_nac'].mean()
moda7=datosnat['mes_nac'].mode()
mediana7=datosnat['mes_nac'].median()
varian7=datosnat['mes_nac'].var()
desvia7=datosnat['mes_nac'].std()

media8=datosnat['escol_mad'].mean()
moda8=datosnat['escol_mad'].mode()
mediana8=datosnat['escol_mad'].median()
varian8=datosnat['escol_mad'].var()
desvia8=datosnat['escol_mad'].std()

media9=datosnat['escol_pad'].mean()
moda9=datosnat['escol_pad'].mode()
mediana9=datosnat['escol_pad'].median()
varian9=datosnat['ent_resid'].var()
desvia9=datosnat['ent_resid'].std()

meduniv = {
    'media' : [media1, media2, media3, media4, media5, media6, media7, media8, media9],
    'moda' : [moda1[0], moda2[0], moda3[0], moda4[0], moda5[0], moda6[0], moda7[0], moda8[0], moda9[0]],
    'mediana' : [mediana1, mediana2, mediana3, mediana4, mediana5, mediana6, mediana7, mediana8, mediana9],
    'varianza' : [varian1, varian2, varian3, varian4, varian5, varian6, varian7, varian8, varian9],
    'desviacionEstandar' : [desvia1, desvia2, desvia3, desvia4, desvia5, desvia6, desvia7, desvia8, desvia9]
}

df1 = pd.DataFrame(meduniv, index=['ent_resid', 'ent_ocurr', 'sexo', 'edad_madn', 'edad_padn', 'ano_nac', 'mes_nac', 'escol_mad', 'escol_pad'])
df1.to_csv("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natilidad2k18_medidasUniv.csv")

variables = ['ent_resid', 'ent_ocurr', 'sexo', 'edad_madn', 'edad_padn', 'ano_nac', 'mes_nac', 'escol_mad', 'escol_pad']
correlacion = datosnat[variables].corr()
covarianza = datosnat[variables].cov()
correlacion.to_csv("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natilidad2k18_correlacion.csv")
covarianza.to_csv("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natilidad2k18_covarianza.csv")

#pega tus graficos luis , no se registro ala mejor por eso no se ve

#luis comio pito aqui
#ya se me