# 1089. Corregir erratas de una letra con un diccionario

[Timus 1089](https://acm.timus.ru/problem.aspx?space=1&num=1089) · dificultad 840 · strings

Problema original de Anton Botov, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un diccionario de hasta 100 palabras en minúsculas (hasta 8 letras cada
una) termina con una línea `#`; después viene un texto de hasta 1000
palabras. Una palabra es una secuencia máxima de letras `a`–`z`. Cada
palabra del texto que no está en el diccionario pero difiere de una
palabra del diccionario en exactamente una letra (misma longitud, una
posición) debe sustituirse por esa palabra del diccionario; el
diccionario es tal que hay como mucho una opción. Imprime el texto
corregido, dejando todo lo demás exactamente igual, y luego el número de
correcciones.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

El diccionario, una palabra por línea, la línea `#` y luego el texto.

## Salida

El texto corregido y luego el número de correcciones en su propia línea.

## Evaluación

La salida debe ser igual al texto esperado; solo se ignoran los espacios
en blanco del final.

## Ejemplos

### Ejemplo 1

Entrada:

```
country
occupies
surface
covers
russia
largest
europe
part
about
world
#
the rushia is the larjest cauntry in the vorld.
it ockupies abaut one-seventh of the earth's surfase.
it kovers the eastern park of yurope and the northern park of asia.
```

Salida:

```
the russia is the largest country in the world.
it occupies about one-seventh of the earth's surface.
it covers the eastern part of europe and the northern part of asia.
11
```

## Solución

Se recorre el texto carácter a carácter. Todo lo que no es letra se copia
tal cual; una secuencia de letras es una palabra. Una palabra que está en
el diccionario se deja. Si no, se compara con cada palabra del diccionario
de la misma longitud, y si una difiere en exactamente una posición, se
escribe esa palabra en su lugar y se cuenta una corrección.
`O(T · W · L)` para `T` palabras del texto, `W` palabras del diccionario y
longitud `L ≤ 8`.

Detalles a tener en cuenta:

- solo una letra cambiada es una errata corregible: una letra que falta o
  que sobra no, así que `aple` y `appple` se quedan como están;
- una palabra que ya está en el diccionario es correcta aunque otra
  palabra del diccionario esté a una letra de ella;
- las cifras, los apóstrofos y los guiones separan palabras:
  `one-seventh` son dos palabras;
- los espacios, la puntuación y las líneas vacías deben conservarse tal
  cual.

Las respuestas se comprobaron con una sustitución por expresión regular
sobre las secuencias de letras que verifica que cada corrección es única.

## Notas por lenguaje

- Python usa `re.sub` con una función que lleva la cuenta.
- C++ y Java leen el texto línea a línea; Go, Python y Rust lo leen entero
  y lo parten por los saltos de línea, quitando los retornos de carro.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1089_strings.cpp](1089_strings.cpp) | G++ 13.2 x64 | strings | O(T · W · L) | AC | 0.015 s | 416 KB |
| [1089_strings.go](1089_strings.go) | Go 1.14 x64 | strings | O(T · W · L) | AC | 0.015 s | 1244 KB |
| [1089_strings.java](1089_strings.java) | Java 1.8 | strings | O(T · W · L) | AC | 0.125 s | 700 KB |
| [1089_strings.py](1089_strings.py) | Python 3.12 x64 | strings | O(T · W · L) | AC | 0.109 s | 496 KB |
| [1089_strings.rs](1089_strings.rs) | Rust 1.75 x64 | strings | O(T · W · L) | AC | 0.031 s | 464 KB |
