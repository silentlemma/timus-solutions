# 2010. Casillas Atacadas en un Tablero Vacío

[Timus 2010](https://acm.timus.ru/problem.aspx?space=1&num=2010) · dificultad 133 · math

Problema popular, del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Coloca una pieza en `(x,y)` de un tablero vacío de `n×n`. Calcula por
separado cuántas casillas ataca en un movimiento un rey, caballo, alfil,
torre y dama. Las coordenadas van de 1 a `n`. No se cuenta la casilla
inicial y no existen otras piezas que bloqueen las líneas. El caballo
salta de la manera habitual.

## Entrada

La primera línea contiene `n`, `1 ≤ n ≤ 100 000 000`; la siguiente
contiene `x y`, `1 ≤ x,y ≤ n`. Límite de tiempo 0,5 segundos y memoria
64 MB.

## Salida

Escribe exactamente cinco líneas, en orden: `King: cantidad`, `Knight:
cantidad`, `Bishop: cantidad`, `Rook: cantidad`, `Queen: cantidad`. Las
etiquetas distinguen mayúsculas. Las etiquetas y los enteros únicos se
comparan por tokens.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
8
5 2
```

```
King: 8
Knight: 6
Bishop: 9
Rook: 14
Queen: 23
```

Existen las ocho casillas vecinas. Seis destinos del caballo quedan
dentro. Los cuatro rayos del alfil miden 1, 4, 1 y 3, en total 9. La
torre ataca otras 7 casillas de su fila y otras 7 de su columna: 14. La
dama alcanza `9+14=23`.

## Solución

Solo hacen falta distancias a los bordes; no se construye ni recorre el tablero.

Para el rey, la primera coordenada puede ser `x` o cualquiera de los
vecinos existentes `x−1,x+1`. Hay `a=1+[x>1]+[x<n]` opciones, donde los
corchetes valen 1 si la condición se cumple y 0 en otro caso.
Análogamente hay `b=1+[y>1]+[y<n]` segundas coordenadas. Cada pareja
está como máximo a un paso; `a·b−1` elimina la casilla inicial. También
da cero para `n=1`.

Para el caballo se prueban los ocho desplazamientos distintos `(±1,±2)`
y `(±2,±1)`. Se cuenta cada destino solo si ambas coordenadas están en
`1..n`. No hay repeticiones ni desplazamiento al origen.

Un rayo del alfil termina al alcanzar el más cercano de sus dos bordes.
Sus cuatro longitudes son `min(x−1,y−1)`, `min(x−1,n−y)`, `min(n−x,y−1)`
y `min(n−x,n−y)`. La suma cuenta exactamente una vez cada destino
diagonal: todos pertenecen a uno de los rayos, y estos solo se cruzan en
el origen excluido.

La torre ataca todas las otras casillas de su fila y columna: `n−1` en
cada una. Su única intersección es el origen ya excluido, de modo que
son `2(n−1)`. La dama une los ataques del alfil y la torre, disjuntos
fuera del origen; basta sumarlos sin restar nada más. Así se incluyen
todos los destinos legales y ninguno ilegal, demostrando las cinco
respuestas.

Hay un número fijo de operaciones y ocho comprobaciones del caballo:
tiempo `O(1)` y espacio adicional `O(1)`. Ninguna respuesta supera
`4(n−1) ≤ 399 999 996`; los programas usan enteros de 64 bits o enteros
de Python. Las coordenadas con signo permiten rechazar destinos
negativos del caballo. Como alternativa, se pueden intersectar las dos
diagonales completas con el tablero y quitar el origen de cada una.

## Notas por lenguaje

No cuentes el origen, un segundo movimiento ni saltos fuera del tablero.
El resultado de la torre no depende de la posición; el del alfil sí. No
vuelvas a restar el origen al sumar los ataques de la dama. Las mismas
fórmulas cubren `n=1`. Go 1.14 requiere una función de mínimo; Java 8 y
Rust usan coordenadas amplias con signo. Python almacena una cantidad
constante de valores y se ejecuta en CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2010_math.cpp](2010_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 400 KB |
| [2010_math.go](2010_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1120 KB |
| [2010_math.java](2010_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 412 KB |
| [2010_math.py](2010_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 552 KB |
| [2010_math.rs](2010_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 236 KB |
