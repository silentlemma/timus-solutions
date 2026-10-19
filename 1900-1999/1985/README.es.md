# 1985. Una columna rica en primos en una numeración hamiltoniana

[Timus 1985](https://acm.timus.ru/problem.aspx?space=1&num=1985) · dificultad 1970 · constructive

Problema original de Mikhail Rubinchik, con agradecimiento especial a Alexander Ipatov, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Rellenar una cuadrícula `n×n` con los enteros de 1 a `n²`, cada uno una
vez. Las celdas con valores consecutivos deben compartir un lado. La
puntuación de una columna es su número de primos. Maximizar la mayor
puntuación de columna y mostrar cualquier cuadrícula óptima. `1≤n≤256`.
Límites: 1 segundo y 64 MB.

## Entrada

Un entero `n`.

## Salida

Una cuadrícula óptima: `n` filas de `n` enteros.

## Evaluación

Un comprobador verifica la permutación, que los números consecutivos
comparten lado y que la mejor columna tiene la cantidad óptima de
primos; se acepta cualquier tabla óptima.

## Ejemplos

Entrada:

```
4
```

Salida:

```
2 1 12 11
3 16 13 10
4 15 14 9
5 6 7 8
```

## Solución

Interpretar las etiquetas como el orden de un recorrido hamiltoniano.
Cada visita escribe el siguiente entero. Todas las coordenadas
siguientes empiezan en cero.

### Puntuación óptima

Los colores de ajedrez alternan durante el recorrido. Todas las
etiquetas impares tienen el mismo color y todo primo salvo 2 es impar.
Una columna contiene como máximo `ceil(n/2)` primos impares y quizá 2:
cota `ceil(n/2)+1`.

Para `n=1` el óptimo es cero y para `n=3`, dos. En el segundo caso el
recorrido empieza en el color mayoritario, de modo que la columna
central solo tiene una etiqueta impar. Tres primos en una columna
exterior exigirían 2 en su celda central, 1 en el vecino horizontal y 3
en un vecino vertical. Desde esa esquina, las etiquetas 4 a 9 quedan
forzadas a recorrer el perímetro restante; el otro extremo de la columna
recibe el compuesto 9. Las reflexiones cubren las demás posiciones. Una
serpiente por filas alcanza dos. Usar esa serpiente para los dos tamaños
impares pequeños; para los demás se alcanza la cota general.

### Preparación y desvíos

Cribar los primos hasta `n²` y construir `next[x]`, el primo más pequeño
estrictamente mayor que `x`, o cero si no existe. Una diferencia de
primos impares `g` es par. Con ancho `t=(g−2)/2`, caminar
horizontalmente `t` pasos, uno vertical, volver `t` pasos y avanzar otro
vertical aumenta la etiqueta en `g` y cambia la fila en dos. Guardar los
anchos para rellenar los huecos después.

### Tamaño par

Escribir 1 en `(0,1)`, 2 en `(0,0)` y 3 en `(1,0)`. Los desvíos
derecha/abajo/izquierda/abajo colocan los siguientes primos impares en
la columna 0 y filas `1,3,…,n−1`. Cada desvío ocupa prefijos izquierdos
iguales de dos filas. Exigir `t<n−1` deja al menos una columna libre a
la derecha.

Desde el primo inferior, recorrer hacia la derecha el resto de la última
fila. Rellenar los pares de filas restantes de abajo arriba: la fila
inferior de derecha a izquierda hasta su primera celda libre, y la
superior de esa columna hacia la derecha. Finalmente rellenar la primera
fila desde la derecha hasta la columna 2. Se visita cada celda una vez.
La columna 0 contiene `n/2` primos impares y 2, alcanzando `n/2+1`.

### Tamaño impar de al menos cinco

Usar la columna 2, con una franja de ancho dos a la izquierda y `w=n−3`
a la derecha. Buscar `0≤a≤w`, salvo `w−1`, tal que `p=3+2a` y `q=p+2n`
sean primos. Desde `q`, comprobar también las siguientes `(n−3)/2`
diferencias entre primos: sus anchos deben satisfacer `0≤t<w` y cada
primo debe ser como máximo `n²`. Descartar el candidato si falla alguna
condición.

1. Escribir 1 en `(1,1)` y 2 en `(1,2)`. Ir `a` celdas a la derecha en
   la fila 1, subir a la fila 0 y volver `a` celdas a la izquierda. La
   etiqueta en `(0,2)` es el primo `p`.
2. Rellenar toda la franja izquierda excepto el 1: visitar
   `(0,1),(0,0),(1,0),(2,0),(2,1)` y luego, para filas impares
   `r=3,5,…,n−2`, visitar `(r,1),(r,0),(r+1,0),(r+1,1)`. Entrar en
   `(n−1,2)` con etiqueta `q=p+2n`.
3. Ascender por la columna objetivo con desvíos
   derecha/arriba/izquierda/arriba. Las filas pares `n−3,n−5,…,2`
   reciben los siguientes primos. Cada pareja de filas de la franja
   derecha conserva sufijos libres iguales.
4. Sea `L=3+a`. Si `L=n`, las dos franjas superiores ya están llenas:
   recorrer la fila 2 a la derecha. En otro caso `m=n−L≥2`: recorrer la
   fila 2 hasta `L`, visitar `(1,L)` y `(0,L)`, cruzar la fila 0 hasta
   el borde derecho, volver por la fila 1 hasta `L+1` y cruzar la fila 2
   desde `L+1` al borde derecho. Así se llena el rectángulo superior
   derecho restante. Excluir `a=w−1` evita la versión imposible de una
   sola columna.
5. Rellenar hacia abajo los pares inferiores de la franja derecha,
   desde las filas 3 y 4: fila superior de derecha a izquierda hasta su
   límite libre, e inferior de ese límite hacia la derecha. Usar los
   anchos guardados.

La franja izquierda y los sufijos derechos son disjuntos, y todos los
enlaces entre tramos unen celdas vecinas. El recorrido es hamiltoniano.
Cada fila par de la columna 2 contiene un primo impar, y la fila 1
contiene 2: puntuación `(n+1)/2+1`.

### Condiciones finitas y complejidad

Las condiciones de ancho se verifican en todo el dominio permitido, sin
asumir un teorema no demostrado sobre los primos. Una comprobación
independiente por división de prueba cubre los 128 tamaños pares y los
126 impares de al menos cinco. Todos los impares tienen un prefijo
admisible. Los mayores anchos observados son 8 para desvíos pares, 14
para el prefijo impar elegido y 16 para los desvíos ascendentes; también
se cumplen las desigualdades de espacio libre específicas de cada
tamaño. Ejecutar la búsqueda descrita para cada tamaño permitido
reproduce el certificado. Además se comprueban las 256 construcciones
completas: permutación, adyacencia y optimalidad.

En el ejemplo, la primera columna es `2,3,4,5` y contiene tres primos,
igual a la cota para `n=4`.

La criba tarda `O(n² log log n)`. La tabla de sucesores, el recorrido y
los candidatos requieren `O(n²)`: `O(n)` candidatos con `O(n)`
transiciones de coste constante. La memoria es `O(n²)` y la propia
salida contiene `n²` entradas.

Trampas:

- 1 no es primo y 2 es el único primo par.
- Para `n=3` el óptimo es dos, no tres.
- Un recorrido hamiltoniano válido puede tener una puntuación subóptima.
- El siguiente primo debe ser estrictamente mayor que la etiqueta actual.
- Conservar los anchos para rellenar las franjas restantes.
- El certificado finito se refiere a `n≤256`, no a todos los tamaños mayores.

## Notas por lenguaje

Los cinco programas usan la misma construcción, criba y consultas
constantes del siguiente primo. Python guarda la primalidad en un
arreglo de bytes. C++, Go y Java usan etiquetas enteras; Rust usa
índices `usize`. La mayor etiqueta es 65 536. La salida se almacena en
memoria o se escribe con búfer.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1985_constructive.cpp](1985_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2 log log n) | AC | 0.031 s | 568 KB |
| [1985_constructive.go](1985_constructive.go) | Go 1.14 x64 | constructive | O(n^2 log log n) | AC | 0.031 s | 2796 KB |
| [1985_constructive.java](1985_constructive.java) | Java 1.8 | constructive | O(n^2 log log n) | AC | 0.140 s | 6440 KB |
| [1985_constructive.py](1985_constructive.py) | Python 3.12 x64 | constructive | O(n^2 log log n) | AC | 0.109 s | 4260 KB |
| [1985_constructive.rs](1985_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2 log log n) | AC | 0.031 s | 1212 KB |
