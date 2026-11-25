# 1871. Ondas sísmicas

[Timus 1871](https://acm.timus.ru/problem.aspx?space=1&num=1871) · dificultad 623 · dijkstra

Problema original de Dmitry Ivankov, del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada usuario de Twitter tiene una lista de seguidores, que ven todos
sus tuits. Un seguidor puede retuitear: delante del mensaje se pone la
cadena "RT @nick: ", donde nick es el usuario cuyo tuit o retuit se
repite. Un mensaje de más de 140 caracteres nunca se envía. El primer
usuario tuitea sobre un terremoto; ¿quién se entera?

## Entrada

n (2 ≤ n ≤ 100), luego n líneas "nombre k seguidor₁ … seguidorₖ" con
nombres distintos de 1 a 30 letras latinas, y por último el tuit: una
línea no vacía de como mucho 140 caracteres con códigos ASCII de 32 a
127.

## Salida

El número de usuarios que se enteran del terremoto y luego sus nombres
en cualquier orden, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
Miyako 1 Sae
Yuno 2 Miyako Sae
Nazuna 1 Nori
Sae 1 Yuno
Nori 1 Nazuna
Hidamari is going to collapse!!!
```

Salida:

```
3
Miyako
Sae
Yuno
```

## Solución

Un usuario que envía un mensaje de como mucho 140 caracteres se lo
muestra a todos sus seguidores. Un retuit del mensaje del usuario u es
6 + |u| caracteres más largo: el prefijo "RT @: " y el nombre. Más
corto siempre es mejor, así que buscamos el mensaje más corto que cada
usuario podría enviar. Es un camino mínimo desde el primer usuario,
que empieza con la longitud del tuit, con peso 6 + |u| en cada arista
que sale de u. El algoritmo de Dijkstra sobre n ≤ 100 usuarios lo
encuentra, y los usuarios cuyo mensaje más corto pasa de 140 no pueden
enviarlo. La respuesta son los usuarios que pueden enviarlo junto con todos sus
seguidores: un seguidor ve el mensaje aunque su propio retuit fuera
demasiado largo. `O(n²)`, o `O(n² log n)` en C++ por las consultas a `map`.

En el ejemplo el tuit de Miyako tiene 32 caracteres. Sae lo ve y lo
retuitea con 44 caracteres, Yuno ve eso y retuitea 53 caracteres, que
vuelven a llegar a Miyako y Sae. Nazuna y Nori nunca se enteran.

Trampas:

- menos retuits no significa un mensaje más corto: un nombre largo en
  un camino corto puede perder ante varios nombres cortos;
- el tuit puede empezar o acabar con espacios, que cuentan, así que la
  línea debe leerse entera;
- un mensaje de exactamente 140 caracteres todavía se envía;
- los usuarios que no pueden retuitear se enteran igualmente si alguien
  a quien siguen envía el mensaje.

Los usuarios coinciden con una implementación aceptada independiente en
180 redes aleatorias, incluidas algunas donde el camino con menos
retuits da el mensaje más largo.

## Soluciones optimizadas

Go guarda los seguidores en máscaras de bits y agrupa los remitentes por longitud del mensaje. Cada remitente se procesa en su longitud mínima. El envío 11317173 tardó 0,031 s y usó 1024 KB frente a 0,031 s y 1524 KB en la base.

Rust asigna identificadores enteros a los nombres y usa máscaras de 128 bits para seguidores y grupos por longitud del mensaje. Rust 1.75 x64, envío 11323125. Tiempo 0,031 → 0,031 s, memoria 552 → 204 KB.

Python solo lee las listas de seguidores de los usuarios que pueden reenviar el mensaje y termina el recorrido cuando todos lo han recibido. El envío 11322813 tardó 0,078 s y usó 628 KB. La versión sencilla tardó 0,093 s y usó 1096 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321936 · Go 1.14 x64 №11322073 · Java 1.8 №11321776 · Python 3.12 x64 №11321779 · Rust 1.75 x64 №11322074.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1871_dijkstra.cpp](1871_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(n^2 log n) | AC | 0.015 s | 672 KB | 11321936 |
| [1871_dijkstra.go](1871_dijkstra.go) | Go 1.14 x64 | dijkstra | O(n^2) | AC | 0.031 s | 1524 KB | 11322073 |
| [1871_dijkstra.java](1871_dijkstra.java) | Java 1.8 | dijkstra | O(n^2) | AC | 0.109 s | 1600 KB | 11321776 |
| [1871_dijkstra.py](1871_dijkstra.py) | Python 3.12 x64 | dijkstra | O(n^2) | AC | 0.093 s | 1096 KB | 11321779 |
| [1871_dijkstra.rs](1871_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(n^2) | AC | 0.031 s | 552 KB | 11322074 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1871_dijkstra_optimized.go](1871_dijkstra_optimized.go) | Go 1.14 x64 | dijkstra | O(E + (n + L) ceil(n / 64)) | AC | 0.031 s | 1024 KB | 11317173 |
| [1871_dijkstra_optimized.rs](1871_dijkstra_optimized.rs) \* | Rust 1.75 x64 | dijkstra | O(E + n + L) | AC | 0.031 s | 204 KB | 11323125 |
| [1871_dijkstra_optimized.py](1871_dijkstra_optimized.py) | Python 3.12 x64 | dijkstra | O(E + n + L) | AC | 0.078 s | 628 KB | 11322813 |

\* El corte de clasificación no contiene envíos comparables en Go de otros autores. El corte de clasificación tampoco contiene envíos comparables en Rust de otros autores.
