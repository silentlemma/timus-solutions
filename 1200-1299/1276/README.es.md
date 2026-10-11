# 1276. Tren

[Timus 1276](https://acm.timus.ru/problem.aspx?space=1&num=1276) · dificultad 731 · combinatorics

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N ≤ 40 vagones, cada uno con un enganche de tipo A o B en su
extremo izquierdo y derecho (AA, AB, BA o BB), y una locomotora con
enganches así. Nada se puede girar. Un tren de K vagones debe tener
enganches iguales entre vecinos, y sus extremos deben encajar con la
locomotora: el tren empieza con el enganche que encaja con el derecho
de la locomotora y termina con el que encaja con el izquierdo, de modo
que la locomotora puede ir en cualquier extremo. Hay que contar los
trenes distintos, comparados como cadenas de enganches; si no hay
ninguno, se imprime NO.

Límite de tiempo: 1 segundo. Límite de memoria: 4 MB.

## Entrada

N y K, la locomotora y luego los N vagones.

## Salida

`NO`, o `YES` y el número de trenes.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
AB
AA
AB
BA
BA
```

Salida:

```
YES
2
```

### Ejemplo 2

Entrada:

```
4 4
BA
AA
AB
BA
BA
```

Salida:

```
NO
```

## Solución

Se lee el tren como un camino entre dos estados, A y B. Un vagón AA se
queda en A, uno BB en B, uno AB pasa de A a B y uno BA vuelve. Así que
los vagones de cambio se alternan, empezando por el que sale del estado
inicial. Su número s fija cuántos AB y BA se usan y el estado final.
Además divide el camino en s + 1 tramos, alternando A y B.

Los vagones de un mismo tipo son iguales, así que un tren queda fijado
por cuántos AA van a cada tramo A y cuántos BB a cada tramo B. Para cada
s con el estado final correcto y cada reparto de los K − s vagones
restantes en a de tipo AA y b de tipo BB dentro de las existencias, se
suma

```text
C(a + rA − 1, rA − 1) · C(b + rB − 1, rB − 1)
```

donde rA y rB son los números de tramos A y B (si un estado no tiene
tramos, solo caben cero vagones de su tipo). Ningún binomial pasa de 41
arriba, y el total queda muy por debajo de 2⁶³. `O(N + K²)`.

Detalles a tener en cuenta:

- el primer enganche del tren debe encajar con el derecho de la
  locomotora y el último con el izquierdo; al invertirlos el segundo
  ejemplo da `YES`;
- los vagones de un tipo son intercambiables: cuarenta vagones AA forman
  un solo tren (prueba 05);
- un tipo que no puede seguirse a sí mismo, como AB, no da trenes de más
  de un vagón (prueba 08).

Los números se compararon con listar todos los trenes distintos en 300
casos aleatorios de hasta siete vagones.

## Notas por lenguaje

- Todos suman sobre el número de cambios; Python usa `math.comb` y
  los demás una tabla de binomiales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1276_combinatorics.cpp](1276_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N + K²) | AC | 0.015 s | 164 KB |
| [1276_combinatorics.go](1276_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N + K²) | AC | 0.015 s | 1120 KB |
| [1276_combinatorics.java](1276_combinatorics.java) | Java 1.8 | combinatorics | O(N + K²) | AC | 0.125 s | 504 KB |
| [1276_combinatorics.py](1276_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N + K²) | AC | 0.109 s | 624 KB |
| [1276_combinatorics.rs](1276_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N + K²) | AC | 0.015 s | 268 KB |
