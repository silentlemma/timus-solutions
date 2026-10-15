# 1670. Asterisco

[Timus 1670](https://acm.timus.ru/problem.aspx?space=1&num=1670) · dificultad 1904 · constructive

Problema original de Daniil Ayzenshteyn, del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La operación A * B escribe la secuencia A tras la secuencia B, y una
cadena de asteriscos se evalúa de izquierda a derecha. Una expresión es
una cadena de secuencias entre paréntesis unidas por asteriscos, y un
elemento de una secuencia es un número o una expresión entera, que se
aplana dentro de ella. Hay que escribir los números 1 … N en orden
creciente y añadir paréntesis, comas y asteriscos para que la expresión
valga la permutación dada, o imprimir `IMPOSSIBLE`. La expresión no debe
tener espacios y como mucho 100 000 caracteres.

## Entrada

N (1 ≤ N ≤ 10 000) y luego la permutación.

## Salida

La expresión o `IMPOSSIBLE`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3 4 2 1
```

Salida:

```
(1)*(2)*(3,4)
```

### Ejemplo 2

Entrada:

```
6
5 1 2 6 4 3
```

Salida:

```
IMPOSSIBLE
```

## Solución

Una secuencia conserva el orden de sus partes, y una cadena
s₁ * s₂ * … * s_k da s_k … s₂ s₁, sus partes al revés. Como los números
se escriben en orden creciente, cada parte de una expresión contiene un
tramo de valores consecutivos, y las partes salen o bien con valores
crecientes (una secuencia, unión directa) o decrecientes (una cadena de
asteriscos, unión inversa). Son exactamente las permutaciones
separables, las que se pueden cortar una y otra vez en bloques de
valores consecutivos ordenados hacia arriba o hacia abajo.

Los bloques se hallan en una pasada con una pila de bloques de
posiciones consecutivas con valores consecutivos. Cada número nuevo es
un bloque; mientras los dos bloques de arriba tengan rangos de valores
que se tocan, se unen: si va primero el rango menor, es una unión
directa; si va primero el mayor, inversa. La permutación es separable
exactamente cuando queda un solo bloque. Unir cualesquiera vecinos con
rangos que se tocan no hace daño: una ordenación separable sigue siéndolo
tras la unión, y una con el patrón 2 4 1 3 o 3 1 4 2 nunca se reduce a
un bloque.

Las uniones forman un árbol binario; una racha de uniones del mismo tipo
es un nodo con muchas partes, porque ambos tipos son asociativos. Un nodo
directo se escribe (parte,parte,…) y uno inverso parte*parte*…, con las
partes desde los valores menores, cada una entre paréntesis. Tanto la
pila como la escritura cuestan `O(N)`; la escritura usa su propia pila,
porque el árbol puede tener 10 000 niveles.

Detalles a tener en cuenta:

- un solo número arriba se escribe igualmente como (1) (prueba 03);
- la expresión queda corta: N − 1 separadores, dos paréntesis por
  secuencia y por número suelto en una cadena de asteriscos, es decir, a
  lo sumo unos 5N caracteres además de los 38 894 dígitos de
  1 … 10 000; el árbol alternado más profundo da unos 69 000 (gen4).

Un comprobador analiza la expresión, comprueba los números y la longitud
y la evalúa. Para todas las permutaciones de hasta 6 números la respuesta
es `IMPOSSIBLE` exactamente cuando contienen 2 4 1 3 o 3 1 4 2, y en
entradas mayores coinciden con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1670_constructive.cpp](1670_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.031 s | 616 KB |
| [1670_constructive.go](1670_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 6768 KB |
| [1670_constructive.java](1670_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 5520 KB |
| [1670_constructive.py](1670_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.140 s | 4172 KB |
| [1670_constructive.rs](1670_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 1792 KB |
