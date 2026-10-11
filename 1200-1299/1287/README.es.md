# 1287. Canales en Marte

[Timus 1287](https://acm.timus.ru/problem.aspx?space=1&num=1287) · dificultad 381 · dp

Problema original de Alexander Mironenko (preparado por Igor Goldberg), del Concurso Individual de la Universidad Estatal de los Urales 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un campo de N × N (N ≤ 1400) está sembrado con dos clases de grano,
`s` y `S`, una por celda. Hay que hallar la racha recta más larga de
celdas iguales por fila, columna o cualquiera de las diagonales. Se
imprime la letra cuya racha más larga es mayor, o `?` si son iguales, y
luego esa longitud.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N líneas de N letras.

## Salida

La letra ganadora o `?`, y luego la racha más larga.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
SsS
sSs
SsS
```

Salida:

```
S
3
```

### Ejemplo 2

Entrada:

```
2
sS
Ss
```

Salida:

```
?
2
```

## Solución

Se recorre el campo fila a fila. Para cada celda se guarda la longitud
de la racha que termina en ella en cada una de las cuatro direcciones:
desde la izquierda, desde arriba, desde arriba a la izquierda y desde
arriba a la derecha. Cada una es la racha del vecino más uno si el
vecino tiene la misma letra, y 1 si no. Solo hace falta la fila
anterior, y la racha más larga de cada letra se guarda por el camino.
`O(N²)` de tiempo y `O(N)` de memoria.

Detalles a tener en cuenta:

- la diagonal desde arriba a la derecha es fácil de olvidar (prueba 06);
- con rachas más largas iguales se imprime `?` (prueba 02);
- el campo tiene casi dos millones de celdas, así que la lectura debe
  ser rápida.

Las respuestas se compararon con recorrer cada racha desde cada celda
en 300 campos aleatorios de hasta nueve celdas de lado.

## Notas por lenguaje

- C++, Go, Java y Rust guardan los cuatro arreglos de rachas de dos
  filas.
- Python sería demasiado lento celda a celda. Construye las filas, las
  columnas y las dos diagonales como cadenas de bytes: las diagonales
  son las columnas de las filas desplazadas un paso cada una, y `zip`
  hace la trasposición. Después una búsqueda binaria sobre k pregunta si
  aparecen k copias seguidas de una letra en el texto, con `bytes.find`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1287_dp.cpp](1287_dp.cpp) | G++ 13.2 x64 | dp | O(N²) | AC | 0.093 s | 232 KB |
| [1287_dp.go](1287_dp.go) | Go 1.14 x64 | dp | O(N²) | AC | 0.109 s | 6276 KB |
| [1287_dp.java](1287_dp.java) | Java 1.8 | dp | O(N²) | AC | 0.171 s | 4624 KB |
| [1287_dp.py](1287_dp.py) | Python 3.12 x64 | dp | O(N²) | AC | 0.406 s | 25392 KB |
| [1287_dp.rs](1287_dp.rs) | Rust 1.75 x64 | dp | O(N²) | AC | 0.046 s | 3160 KB |
