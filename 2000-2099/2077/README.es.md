# 2077. Abreviaturas únicas más cortas con punto o guion

[Timus 2077](https://acm.timus.ru/problem.aspx?space=1&num=2077) · dificultad 6156 · strings, sorting

Problema original de Mikhail Rubinchik, preparado por Egor Shchelkonogov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada palabra de un conjunto se escribe entera, como un prefijo seguido
de un punto, o como un prefijo y un sufijo unidos por un guion. Una
palabra encaja en una reducción si al cambiar el punto o el guion por
alguna cadena (quizá vacía) se obtiene la palabra. Cada reducción debe
encajar solo con su propia palabra. Minimizar la longitud total; después
dejar enteras tantas palabras como se pueda; después usar los menos
guiones posibles; después maximizar la longitud total de los prefijos
antes de los guiones. Se garantiza que la respuesta es única. Los
límites son 0.5 segundos y 32 MB.

## Entrada

n, 1 ≤ n ≤ 10⁶, y después n palabras distintas de letras minúsculas en
orden lexicográfico, de longitud total a lo sumo 10⁶.

## Salida

Las reducciones, una por línea, en el orden de entrada.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
aba
abaca
add
dd
```

Salida:

```
aba
a-ca
add
dd
```

### Ejemplo 2

Entrada:

```
2
aa
aaaaa
```

Salida:

```
aa
aaa.
```

### Ejemplo 3

Entrada:

```
2
abc
abcdabc
```

Salida:

```
abc
abcd.
```

## Solución

Que otra palabra encaje en una reducción no depende de las demás
reducciones, así que cada criterio se reparte en una elección por
palabra: la reducción más corta, la palabra entera en caso de empate,
luego un punto antes que un guion, luego el prefijo más largo. Los
prefijos y sufijos no son vacíos (así lee el juez el enunciado). Una
palabra w de longitud m cuesta m entera, a + 1 con un prefijo de
longitud a y un punto, y a + b + 1 con un guion entre un prefijo de
longitud a y un sufijo de longitud b, a + b ≤ m.

Punto. Como las palabras están ordenadas, las que comparten un prefijo
con w forman un tramo contiguo alrededor de w, y el prefijo más corto
que ninguna otra palabra tiene, si existe, mide uno más que el mayor
prefijo común de w con sus dos vecinas.

Guion. Otra palabra v encaja en w[..a]-w[m−b..] si empieza con las
primeras a letras de w, termina con sus últimas b letras y mide al
menos a + b. Las palabras con ese prefijo forman un tramo [lo, hi] del
orden de entrada. Para los sufijos, las palabras invertidas se ordenan y
se recorren con una pila, que numera los nodos del trie de palabras
invertidas y da el nodo de cada par (palabra, b); cada nodo guarda la lista de sus
palabras por número creciente, M entradas en total para una longitud
total M. Así el par (a, b) es único cuando, en la lista del nodo de
(w, b), las palabras con número en [lo, hi] distintas de w son todas
más cortas que a + b. Una búsqueda binaria halla esa parte de la lista
y un máximo en rango de las longitudes (bloques de 32 con una tabla
dispersa sobre los bloques) la comprueba.

Si (a, b) no es único, tampoco lo es (a − 1, b): el tramo del prefijo
solo crece y la cota de longitud solo baja. Así que a va de m − 1 a 1
mientras b solo crece, a lo sumo 2m comprobaciones por palabra, cada una
en O(log n). Los tramos [lo, hi] de todos los prefijos salen de dos
pasadas con pilas sobre las palabras ordenadas: una guarda la última
palabra de cada tramo y la otra mantiene la primera mientras se forman
las respuestas. Recorrer a hacia abajo también hace que el primer guion
de un coste dado tenga el prefijo más largo, así que solo uno
estrictamente más barato lo reemplaza. Todo cuesta O(M log M) y los
arrays ocupan unos 25 MB.

En el primer ejemplo "a-a" también encajaría con "aba", así que
"abaca" queda "a-ca", más corto que la palabra entera o "abac.". En el
segundo ejemplo "a-aa" es único para "aaaaa", porque "aa" es demasiado
corta para contener ambas partes, pero "aaa." mide lo mismo y un punto
gana a un guion.

## Notas por lenguaje

El enunciado solo admite C, C++ y Pascal, pero el formulario de envío
de Timus ofrece además Rust 1.75, así que hay soluciones en C++ y Rust;
Go, Python y Java no se pueden enviar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2077_strings_sorting.cpp](2077_strings_sorting.cpp) | G++ 13.2 x64 | strings, sorting | O(M log M) | AC | 0.234 s | 22020 KB |
| [2077_strings_sorting.rs](2077_strings_sorting.rs) | Rust 1.75 x64 | strings, sorting | O(M log M) | AC | 0.250 s | 22312 KB |
