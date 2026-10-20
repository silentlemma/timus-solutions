# 2222. El mayor número de caballos en un tablero 3 × N cuyo grafo de ataques es un árbol

[Timus 2222](https://acm.timus.ru/problem.aspx?space=1&num=2222) · dificultad 1127 · dp

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Colocar tantos caballos como sea posible en un tablero 3 × N de modo
que el grafo de caballos que se atacan sea un árbol: conexo y sin
ciclos. Imprimir cualquier colocación óptima. Los límites son 1 segundo
y 256 MB.

## Entrada

N, 1 ≤ N ≤ 10⁵.

## Salida

Tres filas de N ceros y unos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
0 1 1
1 0 1
1 1 1
```

### Ejemplo 2

Entrada:

```
2
```

Salida:

```
1 0
0 0
0 1
```

## Solución

Un caballo ataca como mucho a dos columnas de distancia, así que el
tablero se llena columna a columna con una DP de perfil sobre las dos
últimas columnas. Un estado guarda cuáles de esas seis casillas tienen
caballo y cuáles ya están conectadas entre sí a través de caballos
anteriores, renumeradas en un orden canónico. Añadir una columna con una
máscara de caballos une cada caballo nuevo con los que ataca en las dos
columnas anteriores; una unión dentro de una misma componente cerraría
un ciclo y está prohibida, y una componente que sale del perfil sin
tocar la nueva columna solo se permite si es todo el árbol terminado,
que pasa a un estado terminado especial que solo acepta columnas
vacías. Todos los estados alcanzables así se generan una vez como un
autómata pequeño.

La DP guarda el mayor número de caballos de cada estado, columna a
columna. Tras unas pocas columnas el vector de puntuaciones se desplaza
exactamente en 2 en todos los estados alcanzables en cada paso, y desde
entonces cada paso es la misma actualización max-plus, así que la DP se
detiene y se reutilizan las mismas elecciones para todas las columnas
restantes. La respuesta es el mejor estado cuyo perfil es una sola
componente, y la colocación se reconstruye hacia atrás con las
elecciones guardadas.

El primer ejemplo pone 7 caballos en el tablero 3 × 3: el centro no
ataca nada y queda vacío, y las ocho casillas exteriores forman un solo
ciclo de saltos de caballo, así que se deja fuera una de ellas.

Trampa (pruebas 05, 08 y 09): N=5 ya alcanza 2N+3 caballos, pero
el óptimo para N=8 es solo 18; para N=9 vuelve a ser 21. Reutilizar
elecciones solo cuando todo el vector de puntuaciones aumente por igual.

El autómata tiene tamaño fijo, así que esto cuesta O(N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2222_dp.cpp](2222_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 924 KB |
| [2222_dp.go](2222_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 2080 KB |
| [2222_dp.java](2222_dp.java) | Java 1.8 | dp | O(N) | AC | 0.171 s | 4124 KB |
| [2222_dp.py](2222_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.203 s | 8336 KB |
| [2222_dp.rs](2222_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 1656 KB |
