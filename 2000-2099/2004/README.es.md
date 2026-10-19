# 2004. Una cadena mínima con todas las palabras binarias

[Timus 2004](https://acm.timus.ru/problem.aspx?space=1&num=2004) · dificultad 762 · graphs, greedy

Problema original de Ilya Kuchumov, del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada entero de 0 a `2^n−1`, tomar su representación de exactamente
`n` bits, con ceros iniciales. Separarla en un bloque superior de
`ceil(n/2)` bits y otro inferior de `floor(n/2)` bits. Mover el inferior
delante del superior, manteniendo el orden interno. Hallar una cadena
binaria mínima que contenga todas las palabras resultantes como
subcadenas contiguas. Se admite cualquier óptimo.

## Entrada

Un entero `n`, `1 ≤ n ≤ 20`. Tiempo 0,5 segundos, memoria 64 MB.

## Salida

Una cadena binaria de longitud mínima. Los ceros iniciales son significativos.

## Evaluación

Un comprobador verifica que la respuesta es una cadena binaria de
longitud 2ⁿ + n − 1 que contiene todas las palabras de longitud n; se
acepta cualquier cadena así.

## Ejemplos

```
1
```

```
10
```

Para `n=1` deben aparecer 0 y 1. Tanto el ejemplo `10` como la salida
del programa `01` son mínimos.

## Solución

Intercambiar dos bloques fijos es invertible: separar el resultado tras
sus primeros `floor(n/2)` bits y volver a intercambiarlos. Por ello, con
`n` par o impar las palabras resultantes son exactamente las `2^n`
palabras binarias. No hace falta evaluar la función.

Una cadena de longitud `L` tiene solo `L−n+1` ventanas de longitud `n`.
Cubrir `2^n` palabras distintas exige `L≥2^n+n−1`. Construiremos una
cadena que alcance esta cota.

Los vértices de un grafo dirigido son las palabras de `n−1` bits. Cada
palabra de `n` bits es una arista de su prefijo a su sufijo, etiquetada
con el último bit. Cada vértice tiene dos entradas y dos salidas. Para
`n=1` hay un solo vértice, la palabra vacía, y dos bucles. Un recorrido
euleriano escribe todas las palabras una vez mediante solapamientos.

Empezamos con `n` ceros, usando el bucle completamente nulo en el
vértice cero. Después añadimos 1 si la palabra de `n` bits resultante no
se usó; en caso contrario añadimos 0. Un arreglo de bytes marca palabras
usadas y un desplazamiento con máscara mantiene la ventana. Añadimos
exactamente `2^n−1` caracteres más.

¿Por qué este recorrido voraz termina todas las aristas sin retroceder?
Fuera del inicio no puede atascarse: las entradas usadas superan a las
salidas usadas en una, y ambos grados totales son iguales. Una parada
prematura cerraría entonces un recorrido en cero. Las aristas restantes
estarían equilibradas en cada vértice. Si un vértice no nulo conserva
alguna salida, su arista cero sigue disponible, pues se prefiere la
arista uno. Por equilibrio, el destino de esa arista cero también
conserva una salida. Añadir ceros repetidamente alcanza el vértice cero
en no más de `n−1` pasos, contradiciendo la parada allí. El bucle cero
inicial es la única excepción al orden de preferencia y está
precisamente en el inicio. Así se usan todas las aristas, las ventanas
son distintas y se alcanza la cota inferior.

Tiempo `O(2^n+n)` y memoria `O(2^n+n)`, incluyendo salida y marcas. La
salida máxima tiene 1 048 595 bits. No se guarda la lista de palabras
transformadas ni una pila recursiva.

La salida es lineal: el ciclo de `2^n` aristas requiere `n−1` caracteres
adicionales de solapamiento. Marcar la palabra cero antes del bucle.
Mantener solo los últimos `n` bits con máscara `2^n−1`. Resolver `n=1`
con el mismo código. No comparar respuestas válidas con una única cadena
esperada.

## Notas por lenguaje

C++ reserva una cadena, Go usa `strings.Builder`, Java llena un arreglo
de caracteres, Rust llena un vector de bytes y Python añade a un arreglo
de bytes y lo escribe directamente. Los índices y desplazamientos caben
en enteros con signo de 32 bits para `n≤20`. Se miden los recursos de
cada programa completo con la entrada máxima.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2004_graphs_greedy.cpp](2004_graphs_greedy.cpp) | G++ 13.2 x64 | graphs, greedy | O(2^n + n) | AC | 0.015 s | 1964 KB |
| [2004_graphs_greedy.go](2004_graphs_greedy.go) | Go 1.14 x64 | graphs, greedy | O(2^n + n) | AC | 0.031 s | 4352 KB |
| [2004_graphs_greedy.java](2004_graphs_greedy.java) | Java 1.8 | graphs, greedy | O(2^n + n) | AC | 0.109 s | 6180 KB |
| [2004_graphs_greedy.py](2004_graphs_greedy.py) | Python 3.12 x64 | graphs, greedy | O(2^n + n) | AC | 0.375 s | 5736 KB |
| [2004_graphs_greedy.rs](2004_graphs_greedy.rs) | Rust 1.75 x64 | graphs, greedy | O(2^n + n) | AC | 0.031 s | 2096 KB |
