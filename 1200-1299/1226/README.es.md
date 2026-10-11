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

Se lee toda la entrada de una vez y se recorre: cada vez que empieza una
secuencia de letras, se busca dónde acaba y se invierte en su sitio. Las
cifras, la puntuación, los espacios y los saltos de línea no se tocan,
así que el texto conserva su disposición exacta. `O(L)` para `L`
caracteres.

Detalles a tener en cuenta:

- las líneas pueden acabar en espacios, y deben quedarse, así que el
  texto no se parte en palabras para volver a unirlas;
- una palabra acaba en cualquier carácter que no sea letra, incluidas las
  cifras y el guion bajo: `abc123` se convierte en `cba123`;
- la última línea puede no tener salto de línea, y no hay que añadirlo.

La salida se comparó carácter a carácter con el texto esperado en todas
las pruebas, incluidas 1000 líneas de caracteres imprimibles aleatorios.

## Notas por lenguaje

- Python invierte cada coincidencia de una expresión regular sobre los
  bytes en bruto; los demás lenguajes recorren los bytes a mano.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1226_strings.cpp](1226_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 156 KB |
| [1226_strings.go](1226_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 916 KB |
| [1226_strings.java](1226_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 444 KB |
| [1226_strings.py](1226_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 568 KB |
| [1226_strings.rs](1226_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 224 KB |
