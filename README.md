# PruebaIntern

Dentro del desarrollo del ejercicio se planteó un problema donde se debe ajustar un número dado por el usuario para convertirlo a un número palíndromo, donde se debe ajustar de tal forma que, dentro de los números que no cumplan esta condición debe dejarse el número mayor. De igual forma, al no exceder el número de intentos y el número ya ser un palíndromo, debe reemplazarse los números por un '9' sin que esto cambie su estructura de número palíndromo. Este ejercicio se escogió por la complejidad y el reto que representa respecto al uso de lógica, pues puede llegar a demostrar cómo se pueden aplicar los conocimientos ya adquiridos dentro de un ejercicio que implica bastante lógica, independientemente de qué lenguaje se use.

Para el desarrollo de este problema, se planteó primeramente usar lenguaje python.

Se analizaron las restricciones del ejercicio y las necesidades del mismo, donde se indica que:

- n debe ser un número positivo y menor o igual a 100.000.

- k debe ser un número positivo o igual a 0 e igual o menor a 100.000.

- i debe ser un dígito.

Para resolverlo, se usa el concepto de listas por cuanto se indica que "i" debe ser un dígito, así, es más sencillo poder buscar la manera de comparar posiciones dentro de sí misma. Por ende, se comparan las posiciones última y primera por medio de un ciclo for indicando que, al ser diferentes los números ubicados en las posiciones correspondientes, compare qué número es mayor e iguale en ambas posiciones con este valor. Al finalizar, se imprime en pantalla los valores de k, n y s, así como el resultado de la operación.

Para ejecutar el código:

1. Descargue el archivo "Desarrollo_ejercicio_1"
2. Copie la dirección donde se encuentra ubicado el archivo descargado anteriormente (ej: C:\Users\PAOLA\Documents)
3. Entrar a CMD en windows y ubicarse en esa dirección (ej: cd C:\Users\PAOLA\Documents)
4. Ya ubicado en la carpeta donde almacenó el archivo por medio de CMD, ejecutar con el comando python el archivo descargado de la siguiente forma:

python Desarrollo_ejercicio_1.py

5. Seguir las instrucciones dadas en el programa.