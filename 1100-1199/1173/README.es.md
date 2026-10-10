# 1173. Un recorrido cerrado por todos los puntos sin segmentos que se crucen

[Timus 1173](https://acm.timus.ru/problem.aspx?space=1&num=1173) · dificultad 1050 · geometry

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La casa de Wally y las de `N ≤ 1000` amigos son puntos del plano, sin
tres en una misma recta, con coordenadas de a lo sumo tres decimales.
Hay que hallar un orden en el que Wally sale de casa, visita a cada amigo
una vez por segmentos rectos y vuelve, sin que dos segmentos se crucen
salvo los consecutivos en su extremo común. Si no existe, se imprime
`-1`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las coordenadas de Wally, `N`, y luego `N` líneas con las coordenadas y
el identificador de 1 a `N` de un amigo.

## Salida

`0`, los identificadores de los amigos en orden de visita y otra vez `0`,
uno por línea.

## Evaluación

Se acepta cualquier orden que visite a cada amigo una vez y en el que dos
lados no vecinos del recorrido cerrado nunca se toquen; el comprobador
prueba cada par de lados de forma exacta. Como siempre existe un
recorrido, `-1` nunca es correcto.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0
3
3 3 1
6 0 2
6 2 3
```

Salida:

```
0
1
3
2
0
```

## Solución

Se ordenan los amigos por ángulo alrededor de la casa. Dos amigos vecinos
en ese orden abarcan una cuña vista desde la casa, y el segmento entre
ellos queda dentro de la cuña mientras esta sea más estrecha que media
vuelta. Las cuñas de pares distintos no se solapan, así que esos
segmentos nunca se cruzan entre sí ni con los dos segmentos desde la
casa, que van por bordes de cuñas.

El recorrido va de la casa a algún amigo, sigue el orden angular y
vuelve. Se salta exactamente una cuña, la que hay entre el último y el
primer amigo. Como mucho una cuña puede ser más ancha que media vuelta,
así que, si la hay, el recorrido empieza justo después de ella; si no,
puede empezar en cualquier parte. Por tanto la respuesta nunca es `-1`.
`O(N log N)`.

Detalles a tener en cuenta:

- las coordenadas tienen tres decimales, así que se pasan a enteros en
  milésimas y el orden angular usa productos vectoriales exactos, que
  caben en 64 bits;
- la casa puede estar dentro del grupo de amigos, donde un inicio
  descuidado pondría un segmento a través de la cuña de más de media
  vuelta;
- con dos amigos solo hay dos cuñas, y exactamente una es más ancha que
  media vuelta.

Cada salida se comprobó probando todos los pares de lados en todas las
pruebas, incluidas mil casas de amigos alrededor, al lado y lejos de la
casa.

## Notas por lenguaje

- Todos los lenguajes ordenan con la misma comparación exacta: primero el
  semiplano de la dirección y luego el signo del producto vectorial.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1173_geometry.cpp](1173_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 244 KB |
| [1173_geometry.go](1173_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1212 KB |
| [1173_geometry.java](1173_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.156 s | 3388 KB |
| [1173_geometry.py](1173_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.109 s | 1036 KB |
| [1173_geometry.rs](1173_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.015 s | 364 KB |
