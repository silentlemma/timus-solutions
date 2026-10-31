# 1226. Cada palabra escrita al revés

[Timus 1226](https://acm.timus.ru/problem.aspx?space=1&num=1226) · dificultad 114 · strings

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El enunciado deja que el lector adivine la transformación por el
ejemplo: un texto de hasta 1000 líneas de hasta 255 caracteres
imprimibles debe reproducirse con las letras de cada palabra en orden
inverso. Una palabra es una secuencia máxima de letras latinas,
mayúsculas o minúsculas; cualquier otro carácter se queda donde está.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El texto.

## Salida

El texto con cada palabra al revés.

## Ejemplos

### Ejemplo 1

Entrada:

```
This is an example of a simple test. If you did not 
understand the ciphering algorithm yet, then write the 
letters of each word in the reverse order. By the way, 
"reversing" the text twice restores the original text.
```

Salida:

```
sihT si na elpmaxe fo a elpmis tset. fI uoy did ton 
dnatsrednu eht gnirehpic mhtirogla tey, neht etirw eht 
srettel fo hcae drow ni eht esrever redro. yB eht yaw, 
"gnisrever" eht txet eciwt serotser eht lanigiro txet.
```

## Solución

Se recorre el texto: cada vez que empieza una secuencia de letras, se
busca dónde acaba y se invierte. Las cifras, la puntuación, los espacios
y los saltos de línea no se tocan, así que el texto conserva su
disposición exacta. `O(L)` para `L` caracteres.

Detalles a tener en cuenta:

- las líneas pueden acabar en espacios, y deben quedarse, así que el
  texto no se parte en palabras para volver a unirlas;
- una palabra acaba en cualquier carácter que no sea letra, incluidas las
  cifras y el guion bajo: `abc123` se convierte en `cba123`;
- la última línea puede no tener salto de línea, y no hay que añadirlo.

La salida se comparó carácter a carácter con el texto esperado en todas
las pruebas, incluidas 1000 líneas de caracteres imprimibles aleatorios.

## Soluciones optimizadas

La solución optimizada en C++ lee el texto con `getchar` y guarda solo
la palabra actual en un búfer de 255 bytes, que basta porque una palabra
no cruza de una línea a otra y una línea tiene como mucho 255
caracteres; imprime la palabra al revés en cuanto la termina algo que no
es letra, en lugar de reunir todo el texto en un `std::string`:
{1226_strings_optimized.cpp}.

La solución optimizada en Java lee toda la entrada como bytes en bloques
de 64 KB e invierte las secuencias de letras en su sitio dentro de ese
arreglo de bytes, en lugar de decodificar caracteres con un reader y un
writer y crear una cadena por palabra: {1226_strings_optimized.java}.

La solución optimizada en Python procesa una línea cada vez en un
`bytearray` e invierte las secuencias de letras con rebanadas, en lugar
de importar el módulo de expresiones regulares y sustituir sobre todo el
texto; una palabra no cruza de una línea a otra, así que es seguro.
Ahorra memoria, pero el bucle sobre cada carácter corre en Python y
cuesta tiempo: {1226_strings_optimized.py}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1226_strings_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +46.15%; base: `1226_strings.cpp`.

- `1226_strings_optimized.java`: reducción de tiempo +0.00%; reducción
  de memoria +35.00%; base: `1226_strings.java`.

- `1226_strings_optimized.py`: reducción de tiempo +0.00%; reducción de
  memoria +33.10%; base: `1226_strings.py`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1226_strings.rs](1226_strings.rs).

- Python invierte cada coincidencia de una expresión regular sobre los
  bytes en bruto; C++, Go y Rust leen toda la entrada e invierten las
  secuencias de letras en su sitio; Java lee el texto carácter a
  carácter en Latin-1, que conserva cada byte tal cual, e imprime cada
  palabra invertida cuando la termina algo que no es letra.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1226_strings.cpp](1226_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 156 KB | 11283715 |
| [1226_strings.go](1226_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 916 KB | 11283716 |
| [1226_strings.java](1226_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 720 KB | 11304343 |
| [1226_strings.py](1226_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 568 KB | 11283717 |
| [1226_strings.rs](1226_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 224 KB | 11283719 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1226_strings_optimized.cpp](1226_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 84 KB | 11304344 |
| [1226_strings_optimized.java](1226_strings_optimized.java) \* | Java 1.8 | strings | O(L) | AC | 0.093 s | 468 KB | 11304346 |
| [1226_strings_optimized.py](1226_strings_optimized.py) \* | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 380 KB | 11304345 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
