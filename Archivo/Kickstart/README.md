Plot interactivo en Python con matplotlib haciendo un análisis de las rondas del
Kickstart de Google de los últimos dos años. Los datos sobre las rondas han sido
recogidos de los propios análisis de Google.

Para poder ejecutarlo hace falta tener instalado python con las bibliotecas numpy,
matplotlib y pyexcel_ods. No tiene opciones. Hace falta el archivo plot.py y plot.ods,
ya que ahí es donde están los datos que lee el script para hacer el plot.

Aquí hay una muestra de la interfaz junto al diagrama de barras de porcentajes de puntos
por ronda. Se clica en los algoritmos para saber cuál sería la puntuación media
y por rondas si supieras solo esos algoritmos. Está bien para ver cuánta importancia
tiene cada algoritmo o estructura de datos a la hora de competiciones de dificultad
similar al Kickstart.

![plot](plot_example)

Aclaraciones necesarias sobre el programa y los datos:

 - "Simplificación del problema" es cuando es necesario hacer observaciones clave
 que son muy dependientes del problema en cuestión. Hay que notar que esto tiene mucha
 importancia ya que muchos de los problemas complicados residen en este tipo de observaciones.
 No es un algoritmo ni una estructura de datos y es la única que no se puede estudiar
 o entrenar como tal.

 - Se ha subido en "archive.ods" toda la información que he recopilado de los análisis.
 Para cada ejercicio de cada ronda hay anotadas las puntuaciones, los algoritmos usados
 en los análisis y el link a dicho ejercicio. También hay una pequeña tabla donde
 se puede ver la aparición media de cada algoritmo, y cuántos puntos suele otorgar
 cuando aparece. Por ejemplo, fuerza bruta aparece muchas veces pero da muy poca puntuación.
 Por otro lado, los árboles de segmento o la búsqueda binaria aparecen mucho menos,
 pero cuando lo hacen dan bastante puntuación.

 - Tanto los datos como el plot son excesivamente no escalables. Si vas a usar esto
 de referencia, este es uno de los puntos en los que desde el principio habría que fijarse
 para hacerlo bien. Que hubiera rondas con diferente número de ejercicios a otras
 es una de las principales razones de que no sea escalable fácilmente.

TODO:

 - Arreglar el bug de que el algoritmo "Ordenar un vector" no se tuvo en cuenta a la hora del plot. Es
especialmente molesto porque actualmente es imposible obtener un 1 en todas las rondas.
