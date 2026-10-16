# 1739. Fariukis

[Timus 1739](https://acm.timus.ru/problem.aspx?space=1&num=1739) · dificultad 1794 · bitmask

Problema original de Alex Samsonov, del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Estás dentro de una plantación y quieres sacar n frutas. Cada salida por
la puerta puede llevar cualquier conjunto de frutas, pero la alarma solo
calla si su aroma total es un múltiplo entero de 256. Las frutas pueden
volver a entrar libremente. Un desodorante baja un 25% el aroma de una
fruta y un perfume sube un 10% el aroma de una fruta; cada uno se puede
usar una vez en total, incluso los dos sobre la misma fruta, y el
efecto acaba cuando la fruta pasa la puerta. Sacar todas las frutas con
el menor número de salidas e imprimir el plan, o indicar que es
imposible.

## Entrada

n (1 ≤ n ≤ 12) y luego los n aromas, enteros de 1 a 1000.

## Salida

`IMPOSSIBLE`, o el número de acciones y luego las acciones:
`take k a1 … ak`, `return s b1 … bs`, `dearomatize p` y `aromatize q`,
a lo sumo 20 000. Se acepta cualquier plan con el menor número de
salidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
36 56 200
```

Salida:

```
4
take 2 2 3
return 1 3
aromatize 3
take 2 1 3
```

### Ejemplo 2

Entrada:

```
1
100
```

Salida:

```
IMPOSSIBLE
```

## Solución

Volver a entrar frutas no cuesta nada, así que una salida puede llevar
cualquier conjunto, esté ya fuera o no; solo importan las frutas que
siguen dentro, y un conjunto mayor nunca es peor. Para cada forma de
rociar (nada, el desodorante sobre la fruta i, el perfume sobre la
fruta j, o ambos) se listan los conjuntos cuyo aroma total pasa y se
conservan solo los que no están dentro de otro. Los aromas se
multiplican por 1000 para que 3/4, 11/10 y 33/40 de ellos sigan siendo
enteros. Las soluciones en Python, Java y Rust descartan además un
conjunto contenido en otro que necesita menos rociados, lo que deja
muchos menos movimientos.

Luego una programación dinámica sobre las frutas que siguen dentro y
los productos usados da el menor número de salidas: desde un estado,
una salida con un conjunto listado de un tipo de rociado no usado quita
el conjunto de las frutas de dentro. Reconstruir las elecciones da el
plan: volver a entrar las frutas necesarias que están fuera, rociar,
sacar. `O(4·2ⁿ·M)` para M conjuntos listados, más `O(n²·2ⁿ)` para
listarlos.

En el primer ejemplo salen primero 56 + 200 = 256; luego el 200 vuelve
a entrar, con el perfume pasa a 220 y sale con el 36: 36 + 220 = 256.

Trampas:

- un aroma rociado puede no ser entero: 0,75·100 y 1,1·36 son
  fracciones, y el total debe ser un múltiplo entero de 256;
- los dos productos pueden ir sobre una misma fruta, lo que da 33/40 de
  su aroma;
- una fruta sola pasa solo si su aroma ya es 256, 512 o 768: ningún
  rociado convierte otro aroma de 1 a 1000 en un múltiplo de 256.

El menor número de salidas coincide con una búsqueda en anchura sobre
todos los conjuntos y rociados con fracciones exactas en 200 casos
aleatorios de hasta 7 frutas, y con una implementación aceptada
independiente en las pruebas grandes; el comprobador reproduce cada
plan. La solución en Python corre en PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1739_bitmask.cpp](1739_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.203 s | 256 KB |
| [1739_bitmask.go](1739_bitmask.go) | Go 1.14 x64 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.218 s | 3188 KB |
| [1739_bitmask.java](1739_bitmask.java) | Java 1.8 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.203 s | 5132 KB |
| [1739_bitmask.py](1739_bitmask.py) | PyPy 3.10 x64 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.250 s | 7292 KB |
| [1739_bitmask.rs](1739_bitmask.rs) | Rust 1.75 x64 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.031 s | 960 KB |
