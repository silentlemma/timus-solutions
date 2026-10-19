# 2081. Tiempos decrecientes tras un visor averiado

[Timus 2081](https://acm.timus.ru/problem.aspx?space=1&num=2081) · dificultad 721 · greedy

Problema original de Pavel Egorov, preparado por Ivan Burmistrov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un temporizador muestra MM:SS en un visor de siete segmentos dibujado
con `_`, `|` y `.`, pero algunos segmentos encendidos pueden no verse
(un segmento visible siempre es correcto). Dadas n lecturas, recuperar
tiempos de 00:00 a 59:59, estrictamente decrecientes y coherentes con
cada lectura. Se acepta cualquier respuesta válida. Los límites son
2 segundos y 256 MB.

## Entrada

n ≤ 100 y después tres líneas de 17 caracteres por lectura: los cuatro
dígitos ocupan las columnas 1–3, 5–7, 11–13 y 15–17.

## Salida

n líneas MM:SS.

## Evaluación

Un comprobador verifica el formato, el decrecimiento estricto y que
cada segmento visible pertenezca al dígito elegido.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
._..._........._.
|...._|.*...|.._|
|_|.._..*...|.|..
....._....._..._.
|.|...|.*.|.|.._.
|.|.|_..*.|_|.._.
```

Salida:

```
03:12
00:05
```

## Solución

Un dígito encaja en una celda si cada carácter visible coincide con el
del dígito en ese lugar. Para cada lectura las cuatro celdas dan una
tabla de dígitos que encajan. Recorriendo las lecturas en orden, se toma
el mayor tiempo que encaja y queda por debajo de la respuesta anterior,
bajando desde ella.

Esto nunca falla si existe alguna respuesta: por inducción el valor
voraz de cada lectura es al menos el de esa respuesta, porque el valor
de la respuesta encaja y está por debajo de su valor anterior, que es a
lo sumo el valor voraz anterior. El recorrido cuesta a lo sumo 3600
pasos por lectura.

En el ejemplo la primera lectura encaja tanto con 09:48 como con 03:12,
así que la salida puede diferir del ejemplo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2081_greedy.cpp](2081_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 392 KB |
| [2081_greedy.go](2081_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 1272 KB |
| [2081_greedy.java](2081_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.187 s | 2448 KB |
| [2081_greedy.py](2081_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 564 KB |
| [2081_greedy.rs](2081_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.031 s | 256 KB |
