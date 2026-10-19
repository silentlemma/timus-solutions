# 1947. Buscar un meandro

[Timus 1947](https://acm.timus.ru/problem.aspx?space=1&num=1947) · difficulty 1730 · bruteforce

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero de 5×5 contiene doce fichas `/`, doce `\` y un hueco `*`.
Cada ficha tiene dos arcos separados entre puntos medios de sus lados.
T, R, B y L indican arriba, derecha, abajo e izquierda:

| Ficha | Primer arco | Segundo arco |
|---|---|---|
| `/` | T↔L | R↔B |
| `\` | T↔R | B↔L |

Los extremos de fichas vecinas se unen por el borde común; los dos arcos
de una ficha no se unen. Se gana con una curva continua entre dos lados
exteriores distintos que recorra al menos tres fichas diferentes. Valen
lados adyacentes. El hueco interrumpe la curva.

Un movimiento desplaza un bloque recto de 1..4 fichas una casilla hacia
el hueco, dejándolo en el otro extremo. No se giran fichas. Determinar
si ya se gana o se puede ganar en un movimiento. Límites: 1 s y 64 MB.

## Entrada

Cinco líneas de cinco símbolos: doce `/`, doce `\` y un único `*`.

## Salida

Si el tablero ya gana, imprimir `WIN`. En otro caso, cualquier movimiento
ganador: `L`, `R`, `U` o `D`, seguido del número de fichas, 1..4. La letra
describe las fichas; el hueco va en sentido contrario. Si no existe tal
movimiento, imprimir `FAIL`. Un tablero ya ganador exige `WIN`.

## Evaluación

Un comprobador acepta cualquier movimiento ganador: lo aplica, sigue las
curvas y verifica que una de ellas une dos lados distintos pasando por
al menos tres fichas. `WIN` se imprime si el tablero ya gana, y `FAIL`
solo si ningún movimiento sirve.

## Ejemplos

```
*/\//
\/\\\
\////
/\\\\
\//\/
```

```
WIN
```

```
\/\/\
\/\//
//\/*
\\\/\
\//\/
```

```
D2
```

## Solución

Comprobar primero el tablero inicial. Para evaluar un tablero, empezar en
cada uno de los veinte puntos medios exteriores. El puerto de entrada
determina el único puerto de salida en la ficha; se pasa al puerto opuesto
de la celda vecina. Parar ante hueco, borde exterior o estado repetido
(celda, puerto de entrada). Marcar celdas distintas: ambos arcos de una
ficha pueden aparecer en la curva. Una salida gana si pertenece a otro
lado exterior y se han visitado al menos tres fichas diferentes.

Si no gana, enumerar cuatro direcciones y longitudes 1..4, descartando
destinos del hueco fuera del tablero. En una copia, intercambiar el hueco
con su vecino repetidamente. Para L/R/U/D el hueco avanza a derecha,
izquierda, abajo y arriba. Devolver el primer movimiento ganador o `FAIL`.
Siempre hay ocho movimientos legales: los cuatro destinos de su fila y
los cuatro de su columna.

Corrección: los puertos interiores tienen grado dos, con extremos solo
en el exterior o junto al hueco. Toda curva ganadora es un camino entre
extremos exteriores y se recorre por completo desde uno de los veinte
inicios. A la inversa, un recorrido exitoso certifica la conexión y las
tres fichas distintas. Los intercambios desplazan cada ficha del bloque
una casilla y realizan el movimiento exigido. La enumeración cubre todos
los resultados de un movimiento: el hallado es válido y el fracaso total
prueba `FAIL`. La comprobación inicial garantiza la prioridad de `WIN`.

O(1) tiempo y espacio para el tablero fijo de 5×5. Como máximo se prueban
nueve tableros con veinte recorridos cada uno. Hay 48 arcos y 100 estados
de entrada; las marcas de estados garantizan la terminación.

No unir los cuatro puertos ni interpretar el símbolo como una diagonal.
Un arco corto de esquina, una curva al mismo lado o un ciclo interior
no ganan. Contar fichas diferentes, no arcos, y respetar la dirección
de las fichas. Cada ficha del bloque se desplaza una sola casilla.

## Notas por lenguaje

C++, Go, Java y Rust marcan estados y fichas mediante arreglos booleanos;
Python usa conjuntos y una máscara de 25 bits. Se copia el tablero para
cada candidato. Solo se necesita la biblioteca estándar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1947_bruteforce.cpp](1947_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 360 KB |
| [1947_bruteforce.go](1947_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.015 s | 1080 KB |
| [1947_bruteforce.java](1947_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.109 s | 500 KB |
| [1947_bruteforce.py](1947_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.109 s | 704 KB |
| [1947_bruteforce.rs](1947_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.046 s | 248 KB |
