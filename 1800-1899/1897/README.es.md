# 1897. Alice, Bob y una cadena

[Timus 1897](https://acm.timus.ru/problem.aspx?space=1&num=1897) · dificultad 5381 · suffix_structures

Problema original de Oleksandr Kulkov, del Moscow IPT Contest en Petrozavodsk Summer 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una posición del juego es una subcadena t de una cadena fija s, quizá
vacía. Cada jugada añade una letra minúscula a la izquierda y otra a la
derecha, manteniendo el resultado como subcadena de s. Pierde quien no
puede jugar; ambas partes eligen óptimamente.

Entre las distintas posiciones iniciales ganadoras para quien juega,
hallar la k-ésima en orden lexicográfico. La cadena vacía va primero
y un prefijo propio precede a sus extensiones. Varias apariciones de
una misma subcadena cuentan una sola vez. Los límites son 1 segundo
y 256 MB.

## Entrada

La primera línea contiene s, solo con letras inglesas minúsculas,
con 1 ≤ |s| ≤ 100 000. La segunda contiene k, con 1 ≤ k ≤ 10¹⁰.

## Salida

Escribir la cadena solicitada, o `no solution` si hay menos de k
cadenas ganadoras. Si la respuesta es vacía, escribir `-`.

## Evaluación

Las salidas se comparan como secuencias de tokens.

## Ejemplos

### Ejemplo 1

Entrada:

```
abac
3
```

Salida:

```
b
```

### Ejemplo 2

Entrada:

```
rndstr
1
```

Salida:

```
-
```

### Ejemplo 3

Entrada:

```
abc
10
```

Salida:

```
no solution
```

## Solución

### Comprimir el juego por centros

Cada jugada añade dos letras y conserva el centro y la paridad de la
longitud de una aparición. Para longitud par, c es el hueco anterior
a la posición c; para longitud impar, es el carácter central. Con
paridad e de 0 o 1 y radio d, el inicio es c − d y la longitud 2d + e.

Desde cada centro, leer parejas de letras hacia fuera y formar un trie
de esas secuencias. Una raíz representa la cadena vacía; las raíces
impares se agrupan por carácter central. Prefijos iguales representan
subcadenas iguales y una jugada es un paso del trie. Marcar un terminal
cuando un centro llega al borde del texto.

Comprimir caminos conservando raíces, bifurcaciones y todos los
terminales, incluso con un solo hijo. Hay `O(n)` nodos porque hay
`O(n)` secuencias centrales. Una aparición terminal no añade una jugada
ni obliga a detenerse: otras apariciones pueden extenderse. Las marcas
registran exactamente dónde cambia el conjunto de apariciones.

Para construir los tries, preparar arrays de sufijos y consultas de
mínimo de LCP para s y su reverso. El prefijo común de dos secuencias
centrales es el mínimo de las coincidencias hacia la izquierda y hacia
la derecha, limitado por los radios disponibles. Si hace falta, comparar
las siguientes parejas. Estas comparaciones constantes permiten ordenar
centros y construir el trie comprimido con LCP adyacentes y una pila
de profundidades.

### Evaluar aristas comprimidas

Una posición gana si puede pasar a otra perdedora. Si una arista va
del radio L al R y el resultado del hijo es W(R), sus posiciones
internas solo tienen una continuación. Por tanto,
W(d) = W(R) XOR ((R − d) mod 2), para L < d ≤ R. Evaluar los nodos
explícitos de abajo arriba usando la primera posición de cada arista.

### Asignar cada cadena a un sufijo

Asignar cada subcadena a su aparición cuyo sufijo inicial tenga el
menor rango en el array de sufijos. En orden del array, estos dueños
forman los bloques habituales de prefijos nuevos: longitudes mayores
que el LCP con el sufijo anterior. Dentro de un bloque, aumentar la
longitud equivale al orden lexicográfico.

En una arista comprimida, los centros de las apariciones no cambian.
Cada incremento de radio antepone la misma letra a todas, conservando
el orden de sus sufijos. Un representante c es por tanto dueño de toda
la arista. Calcular representantes de abajo arriba: al radio del nodo,
comparar sus centros terminales y los representantes de sus hijos.

La arista L < d ≤ R aporta inicios p = c − d en
[c − R, c − L − 1]. Como el resultado alterna con d, las cadenas
ganadoras aportan 1 a uno de cada dos inicios del intervalo. Usar
arrays de diferencias separados para inicios pares e impares. Una raíz
impar ganadora aporta su carácter en el inicio representante; tratar
la raíz vacía aparte.

Las sumas de prefijos dan la cantidad ganadora de cada dueño. Recorrer
el array de sufijos hasta el bloque que contiene el rango k. Para su
inicio p, recorrer otra vez las aristas: cada una aporta como máximo
un radio d = c − p y una longitud 2d + e. Conservar los candidatos
ganadores, añadir su raíz de un carácter si corresponde, ordenar las
longitudes y elegir el rango restante.

Cada subcadena distinta tiene una sola posición de trie y un solo
dueño. La paridad de la arista calcula su resultado; las sumas la
cuentan una vez, y el orden de dueños y longitudes es lexicográfico.
Así se obtiene la cadena del rango solicitado.

La duplicación de sufijos con ordenación por conteo, la preparación de
LCP y la ordenación de caminos centrales cuestan `O(n log n)`. El juego
comprimido y las cuentas son lineales; ordenar las longitudes del dueño
elegido cuesta como máximo `O(n log n)`. El tiempo total y la memoria
de las tablas dispersas son `O(n log n)`.

En el primer ejemplo ganan la cadena vacía, `a`, `b` y `ba`; la tercera
es `b`. En el segundo, la posición vacía puede pasar a la terminal
`rn` y gana. En el tercero solo ganan la vacía y `b`, menos de diez.

Trampas:

- una jugada aumenta el radio en 1 y la longitud en 2;
- conservar todos los terminales al comprimir, incluso con un solo hijo;
- una aparición en el borde no impide extender otras apariciones;
- elegir dueños por rango de sufijo, no por primera posición en el texto;
- contar cadenas, no apariciones, y usar cuentas de 64 bits;
- una cadena vacía ganadora precede a toda candidata no vacía.

## Notas por lenguaje

Los prefijos centrales cortos se empaquetan en claves enteras para
reducir comparaciones. C++, Go, Java y Rust guardan las tablas LCP en
arrays de tipos primitivos.

La solución en Python corre en PyPy y sigue otro camino, a través de un
autómata de sufijos del reverso de s, cuyos enlaces de sufijo invertidos
forman el árbol de sufijos de s y dan así el orden lexicográfico. Una cadena que
aparece una sola vez solo puede crecer hasta que su aparición choca con
el extremo más cercano de s, así que su resultado sale de una paridad;
para las cadenas repetidas, los resultados de las longitudes de cada
estado del autómata se guardan en bitsets de tamaño total lineal, con
tramos compartidos para cadenas muy repetitivas. Después las cadenas
ganadoras se cuentan bajando por el árbol de sufijos hasta hallar la
k-ésima. Tarda 0,69 s de 1 s en el juez; versiones anteriores, con los
tries de centros y luego con un primer autómata, superaban el límite de
tiempo en las pruebas 73 y 107 del juez.

Las respuestas coinciden con una búsqueda completa del juego en 25 534
consultas de rango.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1897_suffix_structures.cpp](1897_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(n log n) | AC | 0.171 s | 28008 KB |
| [1897_suffix_structures.go](1897_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(n log n) | AC | 0.468 s | 92856 KB |
| [1897_suffix_structures.java](1897_suffix_structures.java) | Java 1.8 | suffix_structures | O(n log n) | AC | 0.468 s | 36316 KB |
| [1897_suffix_structures.py](1897_suffix_structures.py) | PyPy 3.10 x64 | suffix_structures | O(n log n) | AC | 0.687 s | 74404 KB |
| [1897_suffix_structures.rs](1897_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(n log n) | AC | 0.453 s | 45932 KB |
