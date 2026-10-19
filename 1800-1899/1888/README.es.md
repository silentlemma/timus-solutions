# 1888. Experiencia de los pilotos

[Timus 1888](https://acm.timus.ru/problem.aspx?space=1&num=1888) · dificultad 463 · bfs

Problema original de Magaz Asanov, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n vuelos llevó a dos de p pilotos, y la experiencia de uno
era exactamente un año mayor que la del otro; no se sabe cuál. Cada
experiencia es un número entero de años de 1 a 50. Hay que hallar la
mayor diferencia posible entre el piloto más y el menos experimentado y
unas experiencias que la den, o escribir −1 si los datos se
contradicen.

## Entrada

n y p (2 ≤ n ≤ 1000, 2 ≤ p ≤ 50) y luego n vuelos, cada uno con dos
números de piloto distintos.

## Salida

La mayor diferencia y después las p experiencias, o −1. Se acepta
cualquier asignación válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
1 2
3 1
2 4
3 4
```

Salida:

```
2
1 2 2 3
```

### Ejemplo 2

Entrada:

```
3 3
1 2
2 3
1 3
```

Salida:

```
-1
```

## Solución

Los pilotos de un vuelo difieren en uno, así que sus experiencias
tienen distinta paridad. Por tanto un grupo conexo de pilotos debe ser
bipartito; un ciclo impar significa −1.

Dentro de un grupo, dos pilotos a distancia k difieren como mucho en k,
así que la diferencia es como mucho el diámetro. Y se alcanza: la
experiencia 1 + (distancia a un extremo de un diámetro) cambia
exactamente en uno a lo largo de cada vuelo, porque en un grafo
bipartito las distancias de vecinos difieren en uno. Con p ≤ 50 el
diámetro es como mucho 49, así que los valores quedan en 1 … 50.

Grupos distintos se desplazan por separado, así que con dos o más la
respuesta es el 49 completo: un grupo alterna 1 y 2 según la paridad y
los demás alternan 49 y 50. Un BFS desde cada piloto cuesta
`O(p·(p + n))`.

En el primer ejemplo los pilotos forman el ciclo 1–2–4–3 de longitud
cuatro, cuyo diámetro es 2: desde el piloto 1 las distancias son 0, 1,
1, 2.

Trampas:

- varios grupos dan 49 enseguida, por pequeños que sean;
- un grupo no puede superar su diámetro, aunque sea largo y estrecho;
- la misma pareja puede volar varias veces, lo que no cambia nada.

Las respuestas coinciden con una implementación aceptada independiente,
y las experiencias pasan un comprobador, en 200 conjuntos aleatorios de
vuelos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1888_bfs.cpp](1888_bfs.cpp) | G++ 13.2 x64 | bfs | O(p (p + n)) | AC | 0.015 s | 204 KB |
| [1888_bfs.go](1888_bfs.go) | Go 1.14 x64 | bfs | O(p (p + n)) | AC | 0.062 s | 1196 KB |
| [1888_bfs.java](1888_bfs.java) | Java 1.8 | bfs | O(p (p + n)) | AC | 0.109 s | 716 KB |
| [1888_bfs.py](1888_bfs.py) | Python 3.12 x64 | bfs | O(p (p + n)) | AC | 0.109 s | 760 KB |
| [1888_bfs.rs](1888_bfs.rs) | Rust 1.75 x64 | bfs | O(p (p + n)) | AC | 0.062 s | 256 KB |
