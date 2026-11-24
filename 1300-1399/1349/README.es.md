# 1349. Granja

[Timus 1349](https://acm.timus.ru/problem.aspx?space=1&num=1349) · dificultad 51 · math

Problema original atribuido a Pierre Fermat, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado n, 0 ≤ n ≤ 100, hay que hallar tres enteros distintos a, b, c de 1
a 100 con aⁿ + bⁿ = cⁿ, el de menor a, luego menor b y luego menor c, o
imprimir −1 si no hay ninguno.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

a, b y c, o −1.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
0
```

Salida:

```
-1
```

### Ejemplo 2

Entrada:

```
1
```

Salida:

```
1 2 3
```

## Solución

- n = 0: toda potencia vale 1, y 1 + 1 nunca es 1, así que no hay
  respuesta.
- n = 1: a + b = c, y la menor elección con tres números distintos es
  1 2 3.
- n = 2: la menor terna pitagórica, 3 4 5, es la primera en el orden
  pedido.
- n ≥ 3: por el último teorema de Fermat, aⁿ + bⁿ = cⁿ no tiene solución
  en enteros positivos.

`O(1)`.

Detalles a tener en cuenta:

- n = 0 no tiene respuesta aunque todas las potencias sean iguales
  (prueba 01);
- los números deben ser distintos, lo que descarta respuestas como
  1 1 2 para n = 1.

Una búsqueda sobre todas las ternas hasta 100 para n de 0 a 5 dio las
mismas respuestas.

## Soluciones optimizadas

`1349_math_optimized.py`. Conserva casos completos: solo potencias uno/dos admiten testigos positivos mínimos 1,2,3 y 3,4,5; cero y mayores que dos no tienen solución. Normaliza token decimal quitando blancos exteriores, signo más opcional y ceros iniciales; compara bytes 1/2 sin int ni diccionario. Escribe respuesta completa antes de os._exit(0). O(I) análisis de I bytes, trabajo matemático constante, sin tabla arbitraria. CPython nuevo 0.062 s/644 KB frente a PyPy viejo 0.109 s/172 KB: memoria mayor explícita, base intacta.

Fuente exacto: Python 3.12 x64 Accepted #11327873: 0.062 s / 644 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 5/130; 98/130. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Conserva asterisco por la meta propia de primer puesto en ambas. La variante anterior conservada tiene su par propio #11325067 (PyPy 3.10 x64): 0.109 s / 172 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1349_math_optimized.py`: 0.062 s / 644 KB; base didáctica conservada `1349_math.py`: 0.093 s / 336 KB.

Las soluciones optimizadas imprimen las mismas tres respuestas. Java
analiza el exponente a mano con `System.in.read` en lugar de `Scanner`:
0.062 s en lugar de 0.125 s y 316 KB en lugar de 1612 KB. Rust escribe
la respuesta como una cadena de bytes con `write_all` en lugar de
`println!`: 0.031 s en lugar de 0.062 s y 212 KB en lugar de 232 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1349_math.cpp](1349_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11285147 |
| [1349_math.go](1349_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1064 KB | 11285150 |
| [1349_math.java](1349_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB | 11285153 |
| [1349_math.py](1349_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 336 KB | 11285152 |
| [1349_math.rs](1349_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.062 s | 232 KB | 11285154 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1349_math_optimized.java](1349_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.062 s | 316 KB | 11303601 |
| [1349_math_optimized.rs](1349_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 212 KB | 11303602 |
| [1349_math_optimized.py](1349_math_optimized.py) | Python 3.12 x64 | math | O(I) token input; O(1) mathematical cases | AC | 0.062 s | 644 KB | 11327873 |
