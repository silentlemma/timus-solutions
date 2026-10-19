# 1839. El Mentaculus

[Timus 1839](https://acm.timus.ru/problem.aspx?space=1&num=1839) · dificultad 2461 · geometry

Problema original de Alexey Samsonov (preparado por Victor Kamashev), del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arco PQR y dos puntos A, B forman una cara cuando A y B están al
otro lado de la recta PR que Q, los ángulos APR, ARP, BPR, BRP son
agudos, A y B están más cerca de la recta PR que el doble de la
longitud de PR, y la recta AB no tiene puntos comunes con el segmento
PR. Dados n arcos y m puntos, contar las caras.

## Entrada

n y m (1 ≤ n ≤ 100, 1 ≤ m ≤ 10⁴), luego n arcos como tres puntos en
orden a lo largo del arco, cada uno de como mucho media circunferencia,
y luego m puntos. Todas las coordenadas son enteras de valor absoluto
hasta 10⁴.

## Salida

El número de caras.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 7
-2 2 0 0 2 2
-2 -2 0 0 2 -2
-1 3
1 3
0 5
0 3
-1 -3
1 -3
2 -3
```

Salida:

```
4
```

## Solución

Cada arco se trata por separado. Las tres primeras condiciones afectan
a un punto cada vez y son pruebas enteras exactas: el lado de PR por un
producto vectorial, los ángulos de la base agudos por dos productos
escalares, y la distancia por |cross| < 2·|PR|². Los puntos que pasan
son los ojos; sus proyecciones sobre PR quedan estrictamente dentro del
segmento.

Para dos ojos A y B, la recta AB no toca el segmento PR exactamente
cuando P y R quedan estrictamente del mismo lado de ella. La
orientación de P, A, B dice si B se ve desde P con un ángulo mayor que
A, y la de R, A, B si B se ve desde R con un ángulo menor. Así que la
recta no toca PR exactamente cuando los dos ojos quedan en órdenes
opuestos por el ángulo en P y por el ángulo en R, y los ángulos
iguales, que ponen P o R sobre la recta, nunca cuentan. Se ordenan los
ojos por el ángulo en P, los iguales por el ángulo en R, y se cuentan
las inversiones estrictas de los ángulos en R con un árbol de Fenwick.

Los ángulos se comparan por sus tangentes height/near, con productos de
números menores que 2³¹, así que todo es exacto. `O(n·m log m)`.

En el ejemplo el arco superior tiene los ojos (−1, 3), (1, 3), (0, 3) y
(0, 5): los tres de y = 3 se emparejan con rectas paralelas, mientras
que toda recta por (0, 5) y otro ojo corta PR. El arco inferior tiene
(−1, −3) y (1, −3); desde (2, −3) R se ve en ángulo recto. Son 3 + 1
caras.

Trampas:

- una recta por P o R toca el segmento, así que los ojos alineados con
  P o con R nunca forman pareja;
- se excluyen los ángulos rectos en P o R y los puntos de la recta PR;
- la respuesta puede superar 2³¹;
- la solución en Python ordena primero por tangentes en coma flotante y
  luego corrige el orden con productos exactos, y corre en PyPy.

Las respuestas coinciden con una comprobación de todos los pares de
puntos en cientos de páginas pequeñas aleatorias y con una
implementación aceptada independiente en las grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1839_geometry.cpp](1839_geometry.cpp) | G++ 13.2 x64 | geometry | O(n m log m) | AC | 0.234 s | 528 KB |
| [1839_geometry.go](1839_geometry.go) | Go 1.14 x64 | geometry | O(n m log m) | AC | 0.484 s | 7344 KB |
| [1839_geometry.java](1839_geometry.java) | Java 1.8 | geometry | O(n m log m) | AC | 0.515 s | 6980 KB |
| [1839_geometry.py](1839_geometry.py) | PyPy 3.10 x64 | geometry | O(n m log m) | AC | 2.078 s | 12808 KB |
| [1839_geometry.rs](1839_geometry.rs) | Rust 1.75 x64 | geometry | O(n m log m) | AC | 0.234 s | 1296 KB |
