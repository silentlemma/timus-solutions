# 1906. Recuperar una recurrencia modular

[Timus 1906](https://acm.timus.ru/problem.aspx?space=1&num=1906) · difficulty 6173 · number_theory

Problema original de Denis Dublennykh, Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dadas n observaciones a₀,…,aₙ₋₁, encuentra el prefijo más largo generado
por un mismo multiplicador entero k y un mismo módulo entero positivo P:
aᵢ₊₁=k·aᵢ mod P. Cada observación conservada debe ser un resto, aᵢ<P.
Límites: 1 segundo y 64 MB.

## Entrada

Primero n, 1≤n≤10 000, y después n enteros 0≤aᵢ≤10⁹.
Los espacios y los saltos de línea son separadores equivalentes.

## Salida

Imprime L, P y k: la longitud máxima y cualquier par de parámetros
que produzca ese prefijo. Se exige 1≤P≤2·10¹⁸ y 0≤k≤2·10¹⁸.
No es obligatorio que k<P.

## Evaluación

El comprobador constructivo compara L con el óptimo guardado,
verifica los límites, aᵢ<P y cada transición con enteros exactos.
Se admite cualquier par válido, incluso un multiplicador no reducido.

## Ejemplos

```
5
1 2 4 8 0
```

```
5 16 2
```

```
3
4 2 1
```

```
3 5 3
```

## Solución

Cada par adyacente aporta aᵢ·k≡aᵢ₊₁ (mod P). Mantén un sistema
equivalente: P divide G y d·k≡e (mod P), con d>0. G=0 no restringe
el módulo. Inicialmente d=a₀,e=a₁,G=0.

Para añadir la fila (a,b), calcula g=gcd(d,a) y coeficientes xd+ya=g.
Sustituye ambas filas por (g,xe+yb) y (0,(d/g)b−(a/g)e).
La matriz entera de esta transformación tiene determinante uno:
es reversible para cualquier módulo. Actualiza G mediante el máximo
común divisor con la segunda fila, d=g y e=xe+yb; reduce e módulo G
cuando G>0. Si d divide a, basta x=1,y=0. La fila (0,0) no aporta
nada; una fila (0,b), b>0, es imposible porque P debe superar b.

Con G>0, un divisor P de G es válido exactamente si gcd(d,P) divide e.
Si gcd(d,G) divide e, el mayor módulo es G. En otro caso, define
U=gcd(G,e), Q=G/U y D=d/gcd(d,e). Divide repetidamente Q por gcd(Q,D)
hasta que ese gcd sea uno. El mayor módulo admisible es UQ.

La prueba examina los exponentes de cada primo p. Si su exponente
en e es al menos el de d, se permite toda la potencia de G y D no
contiene p. En otro caso, P puede retener como máximo el exponente
de e: U ya contiene esa parte y el bucle elimina todo exceso de Q.
Por tanto UQ es admisible y todos los otros módulos válidos lo dividen.

El prefijo es posible si y solo si el mayor módulo supera todas sus
observaciones. Si G=0, elige P=d·10⁹+1, que es suficientemente grande
y coprimo con d. Incorpora las filas una a una y, al primer fallo,
devuelve el estado anterior. Ningún prefijo mayor puede ser válido,
pues contendría el prefijo que ya resultó imposible.

Para reconstruir k, toma h=gcd(d,P), q=P/h. Si q=1 usa k=0; de lo
contrario, k=(e/h)·inverse(d/h mod q) mod q. Esto satisface el pivote
y, por equivalencia, todas las filas originales. Si a₀=0, la respuesta
es la racha inicial de ceros, con P=1,k=0. Una única observación
positiva admite P=a₀+1,k=0.

Mientras G=0, las filas son proporcionales y 0≤e≤10⁹. El primer G
no nulo no supera 10¹⁸, y luego solo disminuye mediante gcd. Por eso
P≤10¹⁸+1 y k<P cumplen los límites. Por ejemplo, 12,2,9 produce
G=52,d=2,e=9; eliminar potencias excesivas da P=13,k=11.

Basta una pasada. Una cota conservadora de operaciones euclidianas
es O(n log² B), B=2·10¹⁸. Se usan O(n) posiciones para la entrada
y O(1) de estado adicional. No hace falta factorizar ni buscar
binariamente la longitud óptima.

## Notas por lenguaje

Los valores guardados caben en enteros con signo de 64 bits, pero
los determinantes intermedios pueden acercarse a 10²⁷ y el producto
al reconstruir k a 10³⁶. C++ y Rust usan 128 bits con signo; Go usa
math/big, Java 8 BigInteger y Python 3.12 enteros exactos. Normaliza
los restos negativos. Hay que admitir módulos compuestos y secuencias
decrecientes.

Las respuestas coinciden con una búsqueda exhaustiva sobre módulos
pequeños y con la enumeración de divisores de los primeros menores 2 × 2
en 6441 casos; otros 10 000 casos comprueban por separado el paso de
divisores. El comprobador acepta cuatro salidas válidas y rechaza 15
inválidas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1906_number_theory.cpp](1906_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log^2 B) | AC | 0.015 s | 524 KB |
| [1906_number_theory.go](1906_number_theory.go) | Go 1.14 x64 | number_theory | O(n log^2 B) | AC | 0.046 s | 4044 KB |
| [1906_number_theory.java](1906_number_theory.java) | Java 1.8 | number_theory | O(n log^2 B) | AC | 0.109 s | 5296 KB |
| [1906_number_theory.py](1906_number_theory.py) | Python 3.12 x64 | number_theory | O(n log^2 B) | AC | 0.093 s | 1888 KB |
| [1906_number_theory.rs](1906_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log^2 B) | AC | 0.046 s | 628 KB |
