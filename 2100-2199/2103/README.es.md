# 2103. La nota más rápida con correo gratis a los múltiplos

[Timus 2103](https://acm.timus.ru/problem.aspx?space=1&num=2103) · dificultad 1200 · math, number_theory

Problema original de Alexey Danilyuk, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los empleados se numeran 1, 2, 3, … y se sientan en despachos en ese
orden. El empleado x puede enviar una nota gratis a cualquier múltiplo
de x mayor que x, o llevarla a cualquier otro empleado con un coste igual
a la distancia entre sus números. Hallar la forma más barata de que un
miembro de la junta s ≤ 7 haga llegar una nota al empleado t, e imprimir
la ruta. Se acepta cualquier ruta óptima. Los límites son 1 segundo y
64 MB.

## Entrada

s y t, 1 ≤ s ≤ 7, 1 ≤ t ≤ 10⁹.

## Salida

El coste, el número de empleados de la ruta y la ruta.

## Evaluación

Un comprobador compara el coste y reproduce la ruta impresa.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 7
```

Salida:

```
2
2
5 7
```

### Ejemplo 2

Entrada:

```
3 30
```

Salida:

```
0
2
3 30
```

### Ejemplo 3

Entrada:

```
6 1000000
```

Salida:

```
1
3
6 5 1000000
```

## Solución

El correo gratis solo sube, así que llegar a t ≤ s cuesta s − t pasos
andando, y bajar andando es la ruta. Para t > s:

- Coste 0 exactamente cuando t es múltiplo de s: el correo gratis solo
  llega a múltiplos del remitente.
- Coste 1 significa correo gratis a un múltiplo m de s, un paso a m ± 1
  y correo gratis hasta t, así que m ± 1 debe dividir a t. Se prueban
  todos los divisores r de t en O(√t), buscando un múltiplo de s (al
  menos s) junto a r.
- Si no, el coste es 2, y siempre hay ruta. Para s ≤ 5, por correo al
  múltiplo de s más cercano a t, a lo sumo a 2. Para s = 6 o 7, se
  escribe t = 2ᵃ 3ᵇ r con r coprimo con 6. Si r > 1, entonces r ± 1 es
  múltiplo de 6: andar hasta 6 (a lo sumo un paso), correo a r ± 1, un
  paso a r y correo a t. Si t es potencia de 2, es múltiplo de 8, a dos
  pasos de 6 y a uno de 7; si es potencia de 3, es múltiplo de 9,
  alcanzado como 7 → 9 o 6 → 5 → 10 → 9; y los múltiplos de 6 ya costaban
  1 o 0.

En el tercer ejemplo 1 000 000 = 5 · 200 000 y 5 está un paso por debajo
de 6, así que el coste es 1: 6, 5, 1 000 000.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2103_math_number_theory.cpp](2103_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(sqrt t) | AC | 0.015 s | 432 KB |
| [2103_math_number_theory.go](2103_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(sqrt t) | AC | 0.031 s | 1116 KB |
| [2103_math_number_theory.java](2103_math_number_theory.java) | Java 1.8 | math, number_theory | O(sqrt t) | AC | 0.140 s | 468 KB |
| [2103_math_number_theory.py](2103_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(sqrt t) | AC | 0.109 s | 756 KB |
| [2103_math_number_theory.rs](2103_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(sqrt t) | AC | 0.046 s | 232 KB |
