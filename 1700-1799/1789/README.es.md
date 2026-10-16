# 1789. En busca del Dodecaedro

[Timus 1789](https://acm.timus.ru/problem.aspx?space=1&num=1789) · dificultad 220 · constructive

Problema original de Mikhail Rubinchik, del Concurso Regional por Equipos de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un artefacto está sobre uno de n pedestales en fila, y en los demás hay
copias. En cada turno se toca un pedestal. Si el artefacto está allí,
se encuentra; si no, el artefacto pasa a un pedestal vecino, izquierdo
o derecho, a su elección. Imprimir una secuencia de a lo sumo 1000
toques que encuentre el artefacto dondequiera que empiece y como sea
que se mueva.

## Entrada

n (2 ≤ n ≤ 100).

## Salida

El número de toques y luego los pedestales tocados en orden.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
2
2 2
```

## Solución

Tras cada toque fallido el artefacto se mueve, así que la paridad de su
pedestal cambia en cada turno. Se tocan 2, 3, …, n − 1. Si en el primer
toque el artefacto está en un pedestal par, en cada turno tiene la
misma paridad que el tocado y no está a su izquierda, así que no puede
saltarlo y queda atrapado en n − 1 a más tardar. Si no, tras esos
n − 2 toques tiene la paridad de n − 1, y tocar n − 1, n − 2, …, 2 lo
barre igual desde la derecha. Para n > 2, los pedestales 1 y n
nunca se tocan: un artefacto allí tiene que moverse hacia dentro. Eso
da 2(n − 2) toques. Con n = 2 no hay parte central, y basta tocar el
pedestal 1 dos veces. `O(n)`.

En el ejemplo ambas pasadas son el único toque del pedestal 2: un
artefacto en 2 se atrapa enseguida, y uno en 1 o 3 tiene que ir al 2.

Trampas:

- la pasada desde la izquierda sola pierde el artefacto que empieza con
  la otra paridad, que simplemente se cuela;
- con n > 2, tocar los extremos es inútil, el artefacto no puede
  quedarse en ellos;
- n = 2 necesita su propia respuesta, ya que la fórmula da cero toques.

El verificador sigue el conjunto de pedestales donde el artefacto aún
puede estar y exige que se vacíe. Todo n de 2 a 100 pasa, y una
búsqueda completa sobre esos conjuntos para n hasta 12 confirma que no
existe una secuencia más corta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1789_constructive.cpp](1789_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 400 KB |
| [1789_constructive.go](1789_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1108 KB |
| [1789_constructive.java](1789_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.109 s | 1644 KB |
| [1789_constructive.py](1789_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.062 s | 396 KB |
| [1789_constructive.rs](1789_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 204 KB |
