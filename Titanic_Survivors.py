#!/usr/bin/env python
# coding: utf-8

# # Introducción
El análisis de datos es una técnica fundamental en el mundo de la tecnología y los negocios. Es una herramienta que permite a las empresas y a los científicos obtener información valiosa a partir de grandes conjuntos de datos. En este proyecto, utilizaremos Python para analizar un conjunto de datos de Titanic y obtener información relevante para entender la supervivencia de los pasajeros.
# In[20]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Carga y exploración de los datos

# In[3]:


titanic_data = pd.read_csv('train.csv')


# In[19]:


titanic_data.head(10)


# In[5]:


titanic_data.info()



# In[6]:


titanic_data.describe()


# # Limpieza y preparación de los datos
En este paso, vamos a realizar algunas tareas de limpieza y preparación de los datos para poder analizarlos y visualizarlos mejor.

Primero, eliminamos las columnas que no necesitamos, como PassengerId, Name, Ticket y Cabin.
# In[7]:


titanic_data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

Luego, eliminamos cualquier fila que tenga valores faltantes en alguna de sus columnas:
# In[8]:


titanic_data.dropna(inplace=True)

También podemos crear una nueva columna AgeGroup que agrupe a los pasajeros en diferentes grupos de edad:

# In[9]:


bins = [0, 18, 25, 40, 60, np.inf]
labels = ['0-18', '19-25', '26-40', '41-60', '60+']
titanic_data['AgeGroup'] = pd.cut(titanic_data['Age'], bins=bins, labels=labels)

Por último, podemos crear una columna FamilySize que combine las columnas SibSp y Parch para obtener el tamaño de la familia de cada pasajero:
# In[10]:


titanic_data['FamilySize'] = titanic_data['SibSp'] + titanic_data['Parch'] + 1


# # Análisis exploratorio de datos
Ahora que hemos preparado nuestros datos, podemos comenzar a analizarlos y visualizarlos para obtener algunas ideas y patrones interesantes.

Por ejemplo, podemos utilizar un gráfico de barras para ver la distribución de los pasajeros según su género:
# In[11]:


sns.countplot(x='Sex', data=titanic_data)
plt.show()

También podemos utilizar un gráfico de barras para ver la distribución de los pasajeros según su clase:
# In[13]:


sns.countplot(x='Pclass', data=titanic_data)
plt.show()

Podemos usar un gráfico de barras apiladas para ver la distribución de los pasajeros según su género y su clase:
# In[14]:


sns.countplot(x='Pclass', hue='Sex', data=titanic_data)
plt.show()

También podemos utilizar un gráfico de barras agrupadas para ver la tasa de supervivencia según la clase y el género:
# In[15]:


sns.barplot(x='Pclass', y='Survived', hue='Sex', data=titanic_data)
plt.show()

Podemos utilizar un gráfico de densidad para ver la distribución de la edad de los pasajeros:
# In[16]:


sns.kdeplot(x='Age', data=titanic_data)
plt.show()

podemos utilizar un gráfico de barras para ver la distribución de los pasajeros según su grupo de edad:
# In[17]:


sns.countplot(x='AgeGroup', data=titanic_data)
plt.show()

Podemos utilizar un gráfico de barras agrupadas para ver la tasa de supervivencia según el tamaño de la familia:
# In[18]:


sns.barplot(x='FamilySize', y='Survived', data=titanic_data)
plt.show()


# # Resumen ejecutivo
En este proyecto de análisis de datos, utilizamos Python para analizar un conjunto de datos de Titanic. El conjunto de datos contenía información sobre los pasajeros, incluyendo su edad, género, clase, tasa de supervivencia y otros detalles. Utilizamos técnicas de visualización y análisis estadístico para entender mejor la distribución de los pasajeros y las relaciones entre las diferentes variables.

Nuestro análisis reveló que la mayoría de los pasajeros eran hombres y que la mayoría de ellos viajaban en tercera clase. También observamos que la tasa de supervivencia fue más alta para las mujeres que para los hombres, y que la tasa de supervivencia fue más alta para los pasajeros de primera clase que para los pasajeros de segunda y tercera clase. Además, descubrimos que la mayoría de los pasajeros tenían entre 26 y 40 años y que las familias más grandes tenían menos probabilidades de sobrevivir que las familias más pequeñas.


# # Conclusiones
Finalmente, podemos sacar algunas conclusiones interesantes de nuestros análisis y visualizaciones. Por ejemplo, podemos observar que la mayoría de los pasajeros eran hombres y que la mayoría de los pasajeros viajaban en tercera clase. También podemos ver que la tasa de supervivencia fue más alta para las mujeres que para los hombres, y que la tasa de supervivencia fue más alta para los pasajeros de primera clase que para los pasajeros de segunda y tercera clase. También podemos ver que la mayoría de los pasajeros tenían entre 26 y 40 años y que las familias más grandes tuvieron menos probabilidades de sobrevivir que las familias más pequeñas.

