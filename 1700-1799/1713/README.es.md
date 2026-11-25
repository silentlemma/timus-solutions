# 1713. Subcadenas clave

[Timus 1713](https://acm.timus.ru/problem.aspx?space=1&num=1713) · dificultad 633 · strings

Problema original de Dmitry Ivankov (idea de Alexander Mironenko), de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una clave de un comando es una subcadena suya que no es subcadena de
ningún otro comando. Para cada uno de los n comandos, hallar una clave
más corta.

## Entrada

n (2 ≤ n ≤ 1000) y luego n comandos: de 1 a 100 letras latinas
minúsculas. Ningún comando es subcadena de otro.

## Salida

Una clave más corta de cada comando, en el orden de entrada. Se acepta
cualquier clave más corta.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
abcm
acm
bcd
```

Salida:

```
ab
ac
d
```

## Solución

Una subcadena que empieza en la posición p de un comando está en otro
comando justo cuando es prefijo de algún sufijo de ese otro comando.
Así que en p la clave más corta tiene una letra más que el prefijo
común más largo con algún sufijo de otro comando, si cabe antes del
final del comando.

Se ordenan todos los sufijos de todos los comandos, a lo sumo 10⁵. En
el orden, el prefijo común de dos sufijos es el mínimo de los prefijos
comunes de los vecinos entre ellos. Por eso el mayor prefijo común con
un sufijo de otro comando se alcanza en el sufijo así más cercano por
arriba o por abajo. Dos barridos lo hallan. Al bajar, el valor en curso
vuelve a empezar en el prefijo común con el vecino cuando este es de
otro comando, y si no toma el mínimo con él. Al subir es igual. El
mejor inicio de cada comando da su clave. `O(L log L · ℓ)` para L
letras en total y comandos de longitud ℓ.

Trampas:

- el comando entero siempre es una clave, pues ningún comando está
  dentro de otro, así que cada comando tiene respuesta;
- una subcadena que se repite dentro de su propio comando puede seguir siendo
  clave: solo cuentan los otros comandos;
- se acepta cualquier clave más corta, así que las pruebas usan un
  comprobador.

El comprobador verifica que cada clave esté en su comando, en ningún
otro, y tenga la longitud mínima. Las longitudes coinciden con una
implementación aceptada independiente en 200 conjuntos pequeños
aleatorios y en otros grandes.

## Soluciones optimizadas

Go almacena cada posición de sufijo en 32 bits y guarda las longitudes de los prefijos comunes en arreglos de bytes. El envío 11317316 usó 1728 KB frente a 10568 KB de la versión sencilla.

Rust almacena cada posición de sufijo en 32 bits y guarda las longitudes de los prefijos comunes en arreglos de bytes. El envío 11317319 usó 800 KB frente a 5644 KB de la versión sencilla.

Java almacena cada posición de sufijo en 32 bits y guarda las longitudes de los prefijos comunes en arreglos de bytes. El envío 11317320 usó 2000 KB frente a 20308 KB de la versión sencilla.

Python empaqueta cada sufijo y su posición en un entero. Cada letra minúscula ocupa cinco bits. El relleno con ceros coloca primero el sufijo más corto cuando es prefijo de otro. Al descartar los bits de posición, el bit distinto de mayor peso señala la primera letra diferente. Python 3.12 x64, envío 11319668. Tiempo 0,546 → 0,328 s, memoria 20160 → 12324 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321951 · Python 3.12 x64 №11321948 · Rust 1.75 x64 №11321950 · Go 1.14 x64 №11322285 · Java 1.8 №11322286.

C++ guarda las posiciones de los sufijos en enteros de 32 bits y las longitudes de prefijo en bytes. G++ 13.2 x64, envío 11322344. Tiempo 0,062 → 0,062 s, memoria 1908 → 676 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1713_strings.cpp](1713_strings.cpp) | G++ 13.2 x64 | strings | O(L log L · ℓ) | AC | 0.062 s | 1908 KB | 11321951 |
| [1713_strings.go](1713_strings.go) | Go 1.14 x64 | strings | O(L log L · ℓ) | AC | 0.14 s | 10568 KB | 11322285 |
| [1713_strings.java](1713_strings.java) | Java 1.8 | strings | O(L log L · ℓ) | AC | 0.296 s | 20308 KB | 11322286 |
| [1713_strings.py](1713_strings.py) | Python 3.12 x64 | strings | O(L log L · ℓ) | AC | 0.546 s | 20160 KB | 11321948 |
| [1713_strings.rs](1713_strings.rs) | Rust 1.75 x64 | strings | O(L log L · ℓ) | AC | 0.078 s | 5644 KB | 11321950 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1713_strings_optimized.go](1713_strings_optimized.go) \* | Go 1.14 x64 | strings | O(L log L · ℓ) | AC | 0.078 s | 1728 KB | 11317316 |
| [1713_strings_optimized.rs](1713_strings_optimized.rs) | Rust 1.75 x64 | strings | O(L log L · ℓ) | AC | 0.046 s | 800 KB | 11317319 |
| [1713_strings_optimized.java](1713_strings_optimized.java) | Java 1.8 | strings | O(L log L · ℓ) | AC | 0.281 s | 2000 KB | 11317320 |
| [1713_strings_optimized.py](1713_strings_optimized.py) \* | Python 3.12 x64 | strings | O(L log L · ℓ) | AC | 0.328 s | 12324 KB | 11319668 |
| [1713_strings_optimized.cpp](1713_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(L log L · ℓ) | AC | 0.062 s | 676 KB | 11322344 |

\* El objetivo de clasificación de Go sigue pendiente. El objetivo de clasificación de Rust sigue pendiente. La clasificación guardada de Python no tiene envíos comparables de otros autores.
