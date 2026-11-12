# 1334. Damas

[Timus 1334](https://acm.timus.ru/problem.aspx?space=1&num=1334) · dificultad 541 · simulation

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos jugadores ponen por turnos fichas de su color en las casillas
oscuras de un tablero de ajedrez, empezando las blancas; hay 32
jugadas. Pierde quien hace la jugada tras la cual alguna ficha puede
ser capturada: una ficha A puede ser capturada por una ficha B del otro
color que esté junto a ella en diagonal, si la casilla justo detrás de A
en esa diagonal está libre. Hay que imprimir el número de la jugada
perdedora o `Draw`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

32 líneas con casillas en notación de ajedrez, como `a1`: las jugadas
de las blancas en las líneas impares y las de las negras en las pares.

## Salida

El número de la jugada perdedora o `Draw`.

## Ejemplos

### Ejemplo 1

Entrada:

```
a1
a3
a5
a7
b2
b4
b6
b8
c1
c3
c5
c7
d2
d4
d6
d8
e1
e3
e5
e7
f2
f4
f6
f8
g1
g3
g5
g7
h2
h4
h6
h8
```

Salida:

```
5
```

## Solución

Se colocan las fichas una a una. Tras cada jugada se mira cada ficha y
cada una de las cuatro diagonales: si la vecina de ahí es del otro color
y la casilla de detrás está en el tablero y libre, se puede capturar, y
la jugada recién hecha pierde. Cuenta la captura de cualquiera de los
dos, también la de quien acaba de jugar, y también hacia atrás. O(1): como
mucho 32 · 32 · 4 comprobaciones.

Detalles a tener en cuenta:

- un salto que caería fuera del tablero no es una captura, como con una
  ficha en una esquina (prueba 03);
- quien juega puede perder dándose a sí mismo la captura (prueba 05);
- la jugada 32 nunca pierde: para entonces todas las casillas oscuras
  están ocupadas y no hay donde caer, así que la 31 es la última que
  puede perder (prueba 07).

## Soluciones optimizadas

Go/Rust inspeccionan solo ternas afectadas por la ficha nueva. Antes de una jugada no terminal no existe captura; una terna intacta no cambia y la casilla recién ocupada no puede ser destino vacío. La nueva ficha es atacante o central capturada. Para cuatro diagonales d, exigir rival en cell+d y vacío en cell+2d (nuevo atacante) o cell−d (nuevo centro). Incluye oportunidades de ambos y direcciones hacia atrás. Marco de dos celdas da144 bytes para8×8, pared255 distinta de colores/vacío y accesos de dos pasos seguros. Alternar colores, aceptar letras mayúsculas/minúsculas, primer paso perdedor o Draw. M jugadas cuestan O(M), con espacio fijo. Go lee por los descriptores estándar en un búfer de 64 bytes y escribe la jugada desde un arreglo de tres bytes. Rust usa E/S de C. Se conservan escaneos sencillos; C++/Java/Python reutilizan admitidos.

El envío aceptado en Rust 1.75 x64 tarda 0.062 s frente a 0.046 s de la base y usa 60 KB frente a 208 KB.

El envío aceptado en Go 1.14 x64 tarda 0.031 s frente a 0.015 s de la base y usa 276 KB frente a 1036 KB.

Las implementaciones base aceptadas [1334_simulation.cpp](1334_simulation.cpp), [1334_simulation.java](1334_simulation.java), [1334_simulation.py](1334_simulation.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Los archivos originales revisan todo el tablero tras cada jugada. Go y Rust optimizados revisan cuatro direcciones diagonales desde la ficha nueva.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1334_simulation.cpp](1334_simulation.cpp) | G++ 13.2 x64 | simulation | O(1) | AC | 0.015 s | 132 KB | 11285022 |
| [1334_simulation.go](1334_simulation.go) | Go 1.14 x64 | simulation | O(1) | AC | 0.015 s | 1036 KB | 11285023 |
| [1334_simulation.java](1334_simulation.java) \* | Java 1.8 | simulation | O(1) | AC | 0.140 s | 1596 KB | 11285025 |
| [1334_simulation.py](1334_simulation.py) | Python 3.12 x64 | simulation | O(1) | AC | 0.078 s | 536 KB | 11285024 |
| [1334_simulation.rs](1334_simulation.rs) | Rust 1.75 x64 | simulation | O(1) | AC | 0.046 s | 208 KB | 11285026 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1334_simulation_optimized.rs](1334_simulation_optimized.rs) \* | Rust 1.75 x64 | simulation | O(M) | AC | 0.062 s | 60 KB | 11315739 |
| [1334_simulation_optimized.go](1334_simulation_optimized.go) \* | Go 1.14 x64 | simulation | O(M) | AC | 0.031 s | 276 KB | 11315915 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
