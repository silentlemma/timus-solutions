# 1401. Jugadores

[Timus 1401](https://acm.timus.ru/problem.aspx?space=1&num=1401) · dificultad 159 · constructive

Problema original de Alex Samsonov, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que cubrir un tablero de 2ⁿ × 2ⁿ, 1 ≤ n ≤ 9, al que le falta una
casilla, con piezas en forma de L de tres casillas. Se imprime el
tablero con 0 en la casilla quitada y el número de la pieza en cada una
de las demás, con las piezas numeradas de 1 a (4ⁿ − 1) / 3, o -1 si no
hay forma de cubrirlo.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

n y luego las coordenadas x (fila) e y (columna) de la casilla
quitada, con 1 ≤ x, y ≤ 2ⁿ; la casilla superior izquierda es (1, 1).

## Salida

2ⁿ líneas de 2ⁿ números. Se acepta cualquier recubrimiento.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 1
```

Salida:

```
0 1 3 3
1 1 4 3
2 4 4 5
2 2 5 5
```

## Solución

Siempre se puede, partiendo por la mitad. Se divide el tablero en cuatro
cuartos; la casilla quitada está en uno de ellos. Se coloca una pieza en
las tres casillas junto al centro del tablero que pertenecen a los otros
tres cuartos. Ahora cada cuarto es un tablero de 2ⁿ⁻¹ × 2ⁿ⁻¹ con
exactamente una casilla ocupada, que es la misma tarea, y un tablero de
1 × 1 no necesita nada. Las soluciones guardan los cuadrados pendientes
en una pila en lugar de usar recursión, cada uno con su casilla ocupada,
y numeran las piezas en el orden en que se colocan. `O(4ⁿ)`.

Detalles a tener en cuenta:

- la respuesta nunca es -1;
- un tablero de 512 × 512 imprime 262 144 números, así que la salida se
  almacena en búfer (pruebas generadas).

Las pruebas se juzgan con un verificador que exige 0 solo en la casilla
quitada y cada número de 1 a (4ⁿ − 1) / 3 en tres casillas que formen
una L dentro de un cuadrado de 2 × 2.

## Soluciones optimizadas

La solución optimizada en C++ rellena un arreglo global de `int` de
512 × 512 en lugar de un `vector` de `vector` y usa recursión en lugar
de una pila de cuadrados: cada llamada coloca la pieza de un cuadrado y
baja a sus cuartos, con a lo sumo n ≤ 9 llamadas anidadas. Los cuartos
se recorren en orden inverso, así que las piezas reciben los mismos
números que con la pila. Las casillas se imprimen una a una con `printf`
en lugar de juntar antes todo el tablero como texto en un `string`:
{1401_constructive_optimized.cpp}.

La solución optimizada en Go guarda el tablero en casillas `int32` en
lugar de `int` de 64 bits, ya que los números de las piezas no pasan de
(4⁹ − 1) / 3 = 87 381, lo que reduce el tablero a la mitad, y formatea
cada número con `strconv.AppendInt` en un mismo slice de bytes
reutilizado en lugar de crear una cadena por casilla:
{1401_constructive_optimized.go}.

La solución optimizada en Java usa recursión en lugar de apilar un
objeto `Square` por cada cuadrado: cada llamada coloca la pieza de un
cuadrado y baja a sus cuartos, con a lo sumo n ≤ 9 llamadas anidadas, y
los cuartos se recorren en orden inverso, así que las piezas reciben los
mismos números que con la pila. Lee la entrada con `StreamTokenizer` en
lugar de `Scanner` y escribe el tablero fila a fila mediante un
`BufferedWriter`, reutilizando el mismo `StringBuilder` para cada fila,
en lugar de construir antes toda la salida:
{1401_constructive_optimized.java}.

La solución optimizada en Python guarda cada fila en un `array("I")` de
casillas sin signo de 4 bytes, donde caben los números de pieza hasta
(4⁹ − 1) / 3 = 87 381, en lugar de una lista de objetos enteros. Baja
recursivamente a los cuartos, con a lo sumo n ≤ 9 llamadas anidadas, en
lugar de mantener una pila de tuplas, los recorre en orden inverso para
que las piezas reciban los mismos números y escribe el tablero fila a
fila en lugar de unirlo en una sola cadena:
{1401_constructive_optimized.py}.

La solución optimizada en Rust construye el tablero igual, pero escribe
los números directamente en un `BufWriter` en lugar de formatear antes
todo el tablero en un `String` de hasta 1.5 MB aproximadamente:
{1401_constructive_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1401_constructive_optimized.cpp`: reducción de tiempo -200.00%;
  reducción de memoria +70.00%; base: `1401_constructive.cpp`.

- `1401_constructive_optimized.go`: reducción de tiempo +0.00%;
  reducción de memoria +54.86%; base: `1401_constructive.go`.

- `1401_constructive_optimized.java`: reducción de tiempo +38.42%;
  reducción de memoria +57.07%; base: `1401_constructive.java`.

- `1401_constructive_optimized.py`: reducción de tiempo +16.80%;
  reducción de memoria +83.59%; base: `1401_constructive.py`.

- `1401_constructive_optimized.rs`: reducción de tiempo -48.39%;
  reducción de memoria +72.59%; base: `1401_constructive.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1401_constructive.cpp](1401_constructive.cpp) | G++ 13.2 x64 | constructive | O(4^n) | AC | 0.031 s | 3760 KB | 11286021 |
| [1401_constructive.go](1401_constructive.go) | Go 1.14 x64 | constructive | O(4^n) | AC | 0.031 s | 4732 KB | 11286022 |
| [1401_constructive.java](1401_constructive.java) | Java 1.8 | constructive | O(4^n) | AC | 0.203 s | 13044 KB | 11286024 |
| [1401_constructive.py](1401_constructive.py) | Python 3.12 x64 | constructive | O(4^n) | AC | 0.375 s | 10628 KB | 11286023 |
| [1401_constructive.rs](1401_constructive.rs) | Rust 1.75 x64 | constructive | O(4^n) | AC | 0.031 s | 4276 KB | 11286025 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1401_constructive_optimized.cpp](1401_constructive_optimized.cpp) \* | G++ 13.2 x64 | constructive | O(4^n) | AC | 0.093 s | 1128 KB | 11305930 |
| [1401_constructive_optimized.go](1401_constructive_optimized.go) | Go 1.14 x64 | constructive | O(4^n) | AC | 0.031 s | 2136 KB | 11305934 |
| [1401_constructive_optimized.java](1401_constructive_optimized.java) \* | Java 1.8 | constructive | O(4^n) | AC | 0.125 s | 5600 KB | 11305935 |
| [1401_constructive_optimized.py](1401_constructive_optimized.py) \* | Python 3.12 x64 | constructive | O(4^n) | AC | 0.312 s | 1744 KB | 11307190 |
| [1401_constructive_optimized.rs](1401_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(4^n) | AC | 0.046 s | 1172 KB | 11307191 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
