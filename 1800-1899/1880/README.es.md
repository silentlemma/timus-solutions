# 1880. Los autovalores de Psych Up

[Timus 1880](https://acm.timus.ru/problem.aspx?space=1&num=1880) · dificultad 30 · two_pointers, hashing

Problema original de Denis Mukhametianov, del Concurso Regional Escolar de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los tres jugadores de un equipo tiene una lista de números
"propios". Un número es propio del equipo si está en las tres listas.
¿Cuántos hay?

## Entrada

Tres bloques: la longitud n de una lista (1 ≤ n ≤ 4000) y luego sus n
números positivos distintos hasta 10⁹ en orden creciente.

## Salida

La cantidad de números que están en las tres listas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
13 20 22 43 146
4
13 22 43 146
5
13 43 67 89 146
```

Salida:

```
3
```

## Solución

Las listas están ordenadas, así que se recorren a la vez con un puntero
en cada una. Si los tres números actuales son iguales, se cuenta uno.
Después se avanzan todos los punteros que están en el menor de ellos;
cuando una lista se acaba, se para. La solución en Python intersecta
tres conjuntos. `O(n)`.

En el ejemplo 13, 43 y 146 están en las tres listas, mientras que 20,
22, 67 y 89 faltan en al menos una.

Trampas:

- un número que solo está en dos listas no cuenta;
- tras una coincidencia avanzan los tres punteros, y si no, solo los
  que están en el mínimo, o el recorrido puede saltarse un número
  común;
- el recorrido para en cuanto se agota una lista.

Los recuentos coinciden con una implementación aceptada independiente
en 50 equipos aleatorios.

## Soluciones optimizadas

`1880_hashing_optimized.py`. Mantiene la intersección de conjuntos con lector entero de 8192 bytes e iteradores islice, evitando listas completas adicionales. Construye el primer conjunto e intersecta in situ. intersection_update puede parar al encontrar todos los candidatos: agota explícitamente el segundo iterador antes de leer la tercera longitud; si queda vacío, no necesita la tercera entrada. Trabajo hash esperado lineal en la entrada consumida, estado O(tamaño del primer conjunto) más búferes acotados; no es garantía hash del peor caso. main escribe el conteo y llama os._exit(0).

Accepted exacto Python 3.12 x64 #11327481: 0.078 s / 1164 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 4/499, memoria 3/499. Con 1024 KB o más la admisión estricta exige tiempo y memoria: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11301859 (Python 3.12 x64) era 0.093 s / 1400 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1880_hashing_optimized.py`: 0.078 s / 1164 KB; base didáctica conservada `1880_hashing.py`: 0.078 s / 1860 KB.

Las soluciones optimizadas (C++, Rust) guardan una sola lista. Guardan
la primera lista y luego la intersecan con cada lista siguiente mientras
la leen, moviendo un puntero por los números guardados; los números
comunes se escriben sobre el principio del mismo arreglo, y la escritura
nunca adelanta al puntero. Los números se analizan a mano, con `getchar`
en C++ y desde un búfer de 1 KB en Rust. Con el mismo tiempo, C++ ocupa
108 KB en lugar de 240 KB y Rust 228 KB en lugar de 500 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1880_hashing.py](1880_hashing.py) | Python 3.12 x64 | hashing | O(n) | AC | 0.078 s | 1860 KB | 11291026 |
| [1880_two_pointers.cpp](1880_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.015 s | 240 KB | 11303522 |
| [1880_two_pointers.go](1880_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n) | AC | 0.046 s | 1364 KB | 11291024 |
| [1880_two_pointers.java](1880_two_pointers.java) | Java 1.8 | two_pointers | O(n) | AC | 0.093 s | 536 KB | 11303524 |
| [1880_two_pointers.rs](1880_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.046 s | 500 KB | 11303525 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1880_two_pointers_optimized.cpp](1880_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.015 s | 108 KB | 11303644 |
| [1880_two_pointers_optimized.rs](1880_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.031 s | 228 KB | 11303645 |
| [1880_hashing_optimized.py](1880_hashing_optimized.py) | Python 3.12 x64 | hashing | O(I) expected time; O(first set + bounded buffers) storage | AC | 0.078 s | 1164 KB | 11327481 |
