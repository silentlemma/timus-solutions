# 2159. La redacción más corta y menor que respeta reglas de orden de palabras

[Timus 2159](https://acm.timus.ru/problem.aspx?space=1&num=2159) · dificultad 1303 · graphs, greedy

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2021.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una redacción es una sucesión de palabras separadas por espacios
simples. Debe contener n palabras clave, y cada una de las k reglas
(a, b) dice que dondequiera que aparezca a, b debe aparecer más tarde.
Imprimir la redacción más corta que lo cumpla todo y, entre las más
cortas, la lexicográficamente menor, con el espacio menor que toda
letra; imprimir −1 si no existe. Los límites son 2 segundos y 256 MB.

## Entrada

n y k, 1 ≤ n, k ≤ 10⁵, las n palabras clave distintas y luego las k
reglas distintas; la longitud total de todas las palabras es a lo sumo
2 · 10⁶. Cada palabra es una secuencia no vacía de letras latinas
minúsculas.

## Salida

La redacción, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
atan
tan
atan ate
atan tabular
zzz atan
```

Salida:

```
atan ate tabular tan
```

### Ejemplo 2

Entrada:

```
1 3
a
a b
b c
c a
```

Salida:

```
-1
```

## Solución

Las palabras que deben aparecer son las clave y todo lo alcanzable desde
ellas por las reglas, halladas con una búsqueda. Si es posible, basta con
escribir cada una una vez, así que la redacción más corta tiene un
conjunto de palabras y una longitud fijos. Una palabra debe ir antes que
todas las palabras a las que apuntan sus reglas entre ellas; repetir una
palabra no ayuda, porque las reglas de su última copia siguen teniendo
que cumplirse después. Así que existe una redacción exactamente cuando
esas palabras no forman ciclo, y entonces es un orden topológico de
ellas.

Todos esos órdenes tienen la misma longitud, así que el menor se
construye de forma voraz: el algoritmo de Kahn con cola de prioridad
escribe siempre la menor palabra libre. Comparar palabras directamente
es correcto, porque una palabra seguida de un espacio es menor que
cualquier palabra más larga que empiece por ella, ya que el espacio es el
menor carácter.

Sean L la longitud total de las palabras de entrada, V el número de
palabras distintas de entrada y W la longitud máxima de una palabra.
Con el coste esperado de la tabla hash, el tiempo es
O(L + k + V W log(V + 1)) y el espacio es O(L + V + k). Cada operación
del montículo puede comparar O(log(V + 1)) pares de palabras, y cada
comparación puede recorrer O(W) caracteres.

Trampa: n cuenta solo las palabras clave; las reglas pueden introducir
más palabras obligatorias (prueba gen6, `heap 6`). Las comparaciones del
montículo pueden recorrer repetidamente prefijos comunes largos (prueba
gen10, `prefix 10`), por lo que su coste no puede contarse una sola vez
en L. En particular, dos palabras largas que esperan junto a una cadena
de palabras cortas pueden compararse en cada paso de la cadena, incluso
con solo tres palabras clave.

En el primer ejemplo "zzz" no tiene por qué aparecer, y las palabras
obligatorias atan, ate, tabular y tan salen en orden alfabético una vez
escrita atan.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2159_graphs_greedy.cpp](2159_graphs_greedy.cpp) | G++ 13.2 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.156 s | 19804 KB |
| [2159_graphs_greedy.go](2159_graphs_greedy.go) | Go 1.14 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.203 s | 28672 KB |
| [2159_graphs_greedy.java](2159_graphs_greedy.java) | Java 1.8 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.515 s | 31516 KB |
| [2159_graphs_greedy.py](2159_graphs_greedy.py) | Python 3.12 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.625 s | 53616 KB |
| [2159_graphs_greedy.rs](2159_graphs_greedy.rs) | Rust 1.75 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.140 s | 24824 KB |
