# 1111. Ordenar cuadrados por su distancia a un punto

[Timus 1111](https://acm.timus.ru/problem.aspx?space=1&num=1111) · dificultad 383 · geometry

Problema original de Timus; no se indican autor ni fuente.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `n` cuadrados rellenos (`1 ≤ n ≤ 50`), cada uno dado por dos
vértices opuestos con coordenadas enteras en `(−9999, 9999)`; los
cuadrados pueden estar girados en cualquier ángulo, y un cuadrado puede
reducirse a un punto. La distancia de un punto `P` a un cuadrado es la
longitud del segmento más corto de `P` a un punto del cuadrado, así que
es 0 cuando `P` está dentro. Imprime los números de los cuadrados
ordenados por distancia, primero el menor número en caso de empate.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`n`, luego `n` líneas `x1 y1 x2 y2` con dos vértices opuestos, y luego la
línea `x y` de `P`.

## Salida

Los números de los cuadrados (desde 1) en orden, separados por espacios.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0 1 1
0 3 1 4
0 0
```

Salida:

```
1 2
```

## Solución

Se mira cada cuadrado desde su centro `C`, con `D = (x2 − x1, y2 − y1)`
la diagonal. Sus lados van en la dirección de `D` girada `±45°`, es decir
de `D ± D⊥`, donde `D⊥` es `D` girada `90°`. Con el desplazamiento
doblado `q = 2P − (x1 + x2, y1 + y2)`, todo entero, las proyecciones de
`q` en las dos direcciones de los lados son `s1 = |q · (D + D⊥)|` y
`s2 = |q · (D − D⊥)|`, y `P` está dentro exactamente cuando ambas valen
como mucho `h = |D|²`. Fuera, los excesos `a = max(0, s1 − h)` y
`b = max(0, s2 − h)` dan la distancia al cuadrado `(a² + b²) / (8h)`, y un
cuadrado reducido a un punto da `|q|² / 4`.

Así cada distancia al cuadrado es una fracción exacta de enteros, y dos
se comparan multiplicando en cruz, usando el índice original en los
empates. Se lee `P` y se calcula toda expresión que lo contiene con
enteros de precisión arbitraria; solo las coordenadas acotadas de los
vértices y los denominadores usan enteros de ancho fijo. Hay
`O(n log n)` comparaciones. Si `L` es la máxima longitud decimal de una
coordenada de `P` (al menos 1), con multiplicación escolar la cota es
`O(n L² + n log n L)` de tiempo y `O(n L)` de memoria de trabajo.
El tamaño de los denominadores está acotado.

Detalles a tener en cuenta:

- los empates son frecuentes, por cuadrados simétricos y por `P` dentro
  de varios, así que la comparación debe ser exacta: en coma flotante dos
  distancias iguales pueden quedar en cualquier orden;
- la cota de los vértices no limita `P`. En la prueba `09` las dos
  distancias son iguales, pero el numerador del cuadrado es `2^64`:
  ampliar solo la comparación final llega demasiado tarde. Ni siquiera
  128 bits cubren todo `P` válido; la lectura, las proyecciones, los
  cuadrados y las comparaciones requieren precisión arbitraria;
- los vértices dados son opuestos, no contiguos, y cualquiera de las dos
  diagonales en cualquier sentido describe el mismo cuadrado.

Las respuestas se comprobaron con un cálculo exacto aparte con
fracciones: se construyen los cuatro vértices, la pertenencia se prueba
con productos cruzados y la distancia es la menor a los cuatro lados
como segmentos. Cientos de conjuntos aleatorios, muchos con empates,
coincidieron.

## Notas por lenguaje

- C++ y Rust incluyen pequeñas implementaciones de enteros largos con
  signo; Go usa `math/big.Int`, Java usa `BigInteger` y Python sus propios
  enteros, desactivando el límite de dígitos decimales de entrada. Todos
  usan la misma fórmula de proyecciones y comparan fracciones exactas,
  seguidas de los índices originales.
- Go usa `sort.Slice` con desempate explícito por índice para evitar
  los intercambios adicionales de `sort.SliceStable`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1111_geometry.cpp](1111_geometry.cpp) | G++ 13.2 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 444 KB |
| [1111_geometry.go](1111_geometry.go) | Go 1.14 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 1288 KB |
| [1111_geometry.java](1111_geometry.java) | Java 1.8 | geometry | O(n L² + n log n L) | AC | 0.156 s | 3956 KB |
| [1111_geometry.py](1111_geometry.py) | Python 3.12 x64 | geometry | O(n L² + n log n L) | AC | 0.078 s | 624 KB |
| [1111_geometry.rs](1111_geometry.rs) | Rust 1.75 x64 | geometry | O(n L² + n log n L) | AC | 0.031 s | 240 KB |
