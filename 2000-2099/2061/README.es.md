# 2061. Contar palabras binarias ricas

[Timus 2061](https://acm.timus.ru/problem.aspx?space=1&num=2061) · dificultad 3176 · strings, bruteforce

Problema original de Mikhail Rubinchik, del Concurso Palindrómico del 11 de julio de 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una palabra de longitud n es rica si contiene exactamente n palíndromos
no vacíos distintos como subcadenas. Para cada longitud i de 1 a n,
contar las palabras ricas de longitud i sobre un alfabeto de dos
letras. Los límites son 1 segundo y 64 MB.

## Entrada

Un entero n, 1 ≤ n ≤ 61.

## Salida

n líneas: la cantidad de palabras binarias ricas de longitud 1, 2, …, n.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
2
4
8
16
```

## Solución

La entrada solo tiene 61 valores posibles y las respuestas crecen hasta
unos 3·10¹², demasiadas palabras para enumerarlas en un segundo. Por eso
las respuestas se calculan una vez, de antemano, y los programas
imprimen las n primeras de una tabla. Lo interesante es cómo se calcula
la tabla.

Añadir una letra a una palabra agrega como mucho un palíndromo distinto
nuevo: todo palíndromo nuevo es un sufijo, y si dos sufijos `U` y `V`,
`|U| > |V|`, fueran nuevos, `V`, sufijo palindrómico del palíndromo `U`,
sería también su prefijo y ya habría aparecido antes. Así, una palabra
de longitud L tiene a lo sumo L palíndromos distintos, y tiene
exactamente L solo si cada letra añadió uno nuevo. Por tanto todo
prefijo de una palabra rica es rico, y las palabras ricas forman un
árbol en el que cada palabra es una palabra rica más una letra.

Una búsqueda en profundidad recorre ese árbol. Mantiene un árbol
palindrómico de la palabra actual: un nodo por palíndromo distinto, un
enlace de sufijo a su mayor sufijo palindrómico propio y transiciones
`c: P → cPc`. Para probar una letra c, se siguen los enlaces de sufijo
desde el mayor sufijo palindrómico hasta que la letra anterior sea c;
ese palíndromo con c a ambos lados es el nuevo mayor sufijo
palindrómico. Si ese nodo ya existe, la palabra con c no es rica y la
rama se corta; si no, se crea el nodo, la búsqueda baja un nivel y al
volver se quitan el nodo y la transición. Cada paso cuesta como mucho
O(L), la profundidad es a lo sumo 61 y la memoria es mínima.

Intercambiar las dos letras lleva palabras ricas a palabras ricas, así
que la búsqueda empieza por la letra 0 y duplica cada cantidad. Las
palabras de longitud 20 que empiezan por 0 dividen el trabajo en partes
independientes para varios hilos. La búsqueda completa recorre unas
10¹³ palabras y tarda alrededor de una hora y media con 22 hilos. Sus resultados
coinciden con la sucesión A216264 de la OEIS para todas las longitudes
hasta 60.
[2061_strings_bruteforce_table.py](2061_strings_bruteforce_table.py) es la
misma búsqueda en Python: demasiado lenta para las 61 longitudes, comprueba
las primeras en segundos.

En el ejemplo las 16 palabras de longitud 4 son ricas; las primeras
palabras no ricas aparecen con longitud 8, por ejemplo 00101100.

## Notas por lenguaje

La mayor cantidad, 2 966 632 985 826, necesita enteros de 64 bits. Cada
programa guarda la tabla como constante e imprime sus n primeros
elementos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2061_strings_bruteforce.cpp](2061_strings_bruteforce.cpp) | G++ 13.2 x64 | strings, bruteforce | O(n) | AC | 0.001 s | 132 KB |
| [2061_strings_bruteforce.go](2061_strings_bruteforce.go) | Go 1.14 x64 | strings, bruteforce | O(n) | AC | 0.001 s | 1048 KB |
| [2061_strings_bruteforce.java](2061_strings_bruteforce.java) | Java 1.8 | strings, bruteforce | O(n) | AC | 0.046 s | 1524 KB |
| [2061_strings_bruteforce.py](2061_strings_bruteforce.py) | Python 3.12 x64 | strings, bruteforce | O(n) | AC | 0.046 s | 400 KB |
| [2061_strings_bruteforce.rs](2061_strings_bruteforce.rs) | Rust 1.75 x64 | strings, bruteforce | O(n) | AC | 0.015 s | 208 KB |
