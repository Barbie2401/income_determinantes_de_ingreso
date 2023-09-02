import matplotlib.pyplot as plt
import seaborn as sns
#Funciones creadas para aplicaar a la prueba:

#Fucnion para graficar histogramas
def histograma(dataframe):
    '''
    Función de histograma entregando Dataframe.
    
        Parameters: Dataframe.
        
        Returns: Histograma con información del dataframe y sus columnas.              
                       
    '''
    for col in dataframe.columns:
        plt.figure(figsize=(15,5))
        sns.histplot(dataframe[col])
        plt.title(f'Histograma de {col}')
        plt.xticks(rotation=55)
        plt.show()