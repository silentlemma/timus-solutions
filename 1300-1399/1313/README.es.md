# 1313. A propósito del deporte

[Timus 1313](https://acm.timus.ru/problem.aspx?space=1&num=1313) · dificultad 34 · implementation

Problema original con idea de Stanislav Vasiliev, preparado por Stanislav Vasiliev y Alexander Klepinin, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una imagen N × N (N ≤ 100), hay que imprimir sus píxeles por
diagonales: empezando en la esquina superior izquierda, una diagonal
tras otra, cada una desde su extremo inferior izquierdo hasta el
superior derecho. El ejemplo muestra el orden.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego N filas de N números naturales, cada uno a lo sumo 100.

## Salida

Los N² números en orden de diagonales, en una línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 3 6 10
2 5 9 13
4 8 12 15
7 11 14 16
```

Salida:

```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
```

## Solución

La diagonal s contiene las casillas cuya fila y columna suman s, para s
de 0 a 2N − 2. Recorrer una diagonal desde su casilla más baja hacia
arriba es tomar la fila i desde min(s, N − 1) hasta max(0, s − N + 1),
con columna s − i. `O(N²)`.

Detalles a tener en cuenta:

- las diagonales de la mitad inferior derecha son más cortas y terminan
  antes de la fila 0, de ahí la cota max(0, s − N + 1) (prueba 04);
- N = 1 es un solo píxel (prueba 02).

## Soluciones optimizadas

La solución optimizada en Java analiza los números a mano en lugar de
`StringTokenizer`, guarda la imagen en un solo arreglo plano de `byte`,
ya que cada número es a lo sumo 100, y escribe los números cifra a cifra
en un búfer de salida de 1 KB: 392 KB en lugar de 1176 KB, con el mismo
tiempo. El recorrido por las diagonales es el mismo.

La solución optimizada en Python guarda los colores, a lo sumo 100, en
un `bytearray`, prepara el texto de cada color una sola vez y construye
la respuesta como bytes: 484 KB en lugar de 1892 KB, con el mismo
tiempo.

## Notas por lenguaje

- Salvo en C++ y en las soluciones optimizadas en Java y Python, los
  números se copian como texto: nunca hacen falta como enteros.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1313_implementation.cpp](1313_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB | 11284904 |
| [1313_implementation.go](1313_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.046 s | 1352 KB | 11303290 |
| [1313_implementation.java](1313_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.078 s | 1176 KB | 11284908 |
| [1313_implementation.py](1313_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 1892 KB | 11284907 |
| [1313_implementation.rs](1313_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.031 s | 588 KB | 11284910 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1313_implementation_optimized.java](1313_implementation_optimized.java) | Java 1.8 | implementation | O(N^2) | AC | 0.093 s | 392 KB | 11303592 |
| [1313_implementation_optimized.py](1313_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.062 s | 484 KB | 11303739 |
