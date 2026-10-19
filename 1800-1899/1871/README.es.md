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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1871_dijkstra.cpp](1871_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(n^2 log n) | AC | 0.015 s | 684 KB |
| [1871_dijkstra.go](1871_dijkstra.go) | Go 1.14 x64 | dijkstra | O(n^2) | AC | 0.031 s | 1556 KB |
| [1871_dijkstra.java](1871_dijkstra.java) | Java 1.8 | dijkstra | O(n^2) | AC | 0.125 s | 1616 KB |
| [1871_dijkstra.py](1871_dijkstra.py) | Python 3.12 x64 | dijkstra | O(n^2) | AC | 0.078 s | 1228 KB |
| [1871_dijkstra.rs](1871_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(n^2) | AC | 0.046 s | 564 KB |
