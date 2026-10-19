# 1929. Un trío distinguido y equipos restantes factibles

[Timus 1929](https://acm.timus.ru/problem.aspx?space=1&num=1929) · difficulty 385 · combinatorics

Original problem from Ural Regional School Programming Contest 2012 | by Olga Soboleva (prepared by Kirill Devyatkin).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

De n personas, m son especiales. Cada equipo debe tener tres personas
y al menos una especial. Contar los equipos sin orden que contienen
a la persona 1 y permiten dividir a TODAS las demás en equipos válidos.
Cada equipo elegido cuenta una vez, sin importar cuántas particiones
restantes existan. Límites: 1 segundo, 64 MB.

## Entrada

Primera línea: n,m, con 6≤n≤999, n divisible por 3 y 1≤m≤n.
La segunda enumera los m identificadores especiales distintos, entre
1 y n, en cualquier orden. La persona 1 puede ser especial o no.

## Salida

Un entero: número de equipos factibles que contienen a la persona 1.

## Evaluación

Comparación exacta de un token entero.

## Ejemplos

```
6 4
2 3 4 6
```

```
10
```

## Solución

Sea h=1 si la persona 1 es especial, y h=0 en caso contrario. Entre
posibles acompañantes hay S=m−h especiales y U=n−m−(1−h) ordinarios.
Enumerar r=0,1,2, el número de acompañantes especiales. Se retiran
h+r especiales y el equipo elegido exige h+r≥1. Quedan t=n/3−1
equipos, que pueden formarse exactamente cuando m−h−r≥t.

La condición es necesaria porque cada equipo restante necesita una
persona especial distinta. Para suficiencia, asignar una distinta a
cada equipo. Quedan exactamente 2t personas para 2t plazas vacías;
llenarlas arbitrariamente, incluso con especiales adicionales.
No existen otras restricciones.

Un r factible contribuye C(S,r)·C(U,2−r). Las selecciones imposibles
aportan cero; C(a,0)=1, C(a,1)=a, C(a,2)=a(a−1)/2. Los tres casos
son disjuntos y cubren cada pareja sin orden exactamente una vez.
Su suma es, por tanto, la cantidad solicitada.

O(m) tiempo de lectura y O(1) cálculo. C++, Go y Java leen en flujo
con O(1) espacio auxiliar; Python y Rust almacenan O(m) de entrada.

El equipo seleccionado también necesita alguien especial. Restar a la
persona 1 de la categoría correcta; no contar orden ni asignaciones de
roles. Los equipos restantes necesitan al menos una especial, no
exactamente una. Si m<n/3, el resultado es cero; con m=n/3 cada equipo
tiene exactamente una, ya cubierto por la fórmula. C(0,0)=1.
Leer todos los identificadores aunque ya se haya encontrado el 1.

## Notas por lenguaje

Bastan enteros con signo de 32 bits: respuesta ≤C(998,2)=497503 y
producto intermedio a(a−1) inferior a un millón. Go usa int, Rust i32
para cantidades y Python enteros. Comprobar disponibilidad antes de
multiplicar: puede no haber acompañantes ordinarios. No hacen falta
factoriales, módulos, coma flotante ni enteros grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1929_combinatorics.cpp](1929_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(m) | AC | 0.015 s | 392 KB |
| [1929_combinatorics.go](1929_combinatorics.go) | Go 1.14 x64 | combinatorics | O(m) | AC | 0.031 s | 1100 KB |
| [1929_combinatorics.java](1929_combinatorics.java) | Java 1.8 | combinatorics | O(m) | AC | 0.125 s | 2404 KB |
| [1929_combinatorics.py](1929_combinatorics.py) | Python 3.12 x64 | combinatorics | O(m) | AC | 0.078 s | 492 KB |
| [1929_combinatorics.rs](1929_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(m) | AC | 0.046 s | 240 KB |
