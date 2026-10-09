# 1102. Partir una línea en las palabras de un diálogo extraño

[Timus 1102](https://acm.timus.ru/problem.aspx?space=1&num=1102) · dificultad 176 · strings

Problema original de Katya Ovechkina, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un diálogo es cualquier secuencia de las palabras `out`, `output`,
`puton`, `in`, `input` y `one`, escrita sin espacios. Para cada una de
`N` líneas (`N ≤ 1000`, letras minúsculas, `4 · 10^6` letras en total)
imprime `YES` si es un diálogo y `NO` si no.

Límite de tiempo: 1 segundo. Límite de memoria: 16 MB.

## Entrada

`N` y luego `N` líneas.

## Salida

`YES` o `NO` para cada línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
puton
inonputin
oneputonininputoutoutput
oneininputwooutoutput
outpu
utput
```

Salida:

```
YES
NO
YES
NO
NO
NO
```

## Solución

Leídas hacia delante, las palabras se solapan mal: `out` empieza
`output`, `in` empieza `input`, y `output` + `one` se lee como `out` +
`puton` + `e`. Leídas hacia atrás se convierten en `tuo`, `tuptuo`,
`notup`, `ni`, `tupni` y `eno`, y ninguna es el principio de otra. Así
que en cada punto termina como mucho una palabra, y cortar la línea de
forma voraz desde el final, palabra a palabra, o bien consume toda la
línea o bien demuestra que no hay partición. `O(L)` para `L` letras.

Detalles a tener en cuenta:

- un voraz hacia delante que toma siempre la palabra más larga falla:
  `outputon` es `out` + `puton`, pero tomar primero `output` deja `on`;
- las líneas son largas y el límite de memoria es de solo 16 MB, así que
  hay que evitar copias de toda la entrada.

Las respuestas se comprobaron con una programación dinámica hacia
delante sobre los prefijos, en todos los diálogos de hasta tres palabras,
en casi diálogos y en líneas aleatorias estropeadas.

## Notas por lenguaje

- Python compara la línea invertida con la expresión regular
  `(?:tuo|tuptuo|notup|ni|tupni|eno)*+`; el `*+` posesivo no guarda
  estados a los que volver, lo que es seguro porque la partición es
  única.
- Java lee la entrada byte a byte y guarda solo las seis últimas letras
  con una programación dinámica hacia delante sobre ellas, ya que una
  línea de cuatro millones de letras como `String` no cabría en 16 MB.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1102_strings.cpp](1102_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.156 s | 5768 KB |
| [1102_strings.go](1102_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.078 s | 11448 KB |
| [1102_strings.java](1102_strings.java) | Java 1.8 | strings | O(L) | AC | 0.421 s | 476 KB |
| [1102_strings.py](1102_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.140 s | 8328 KB |
| [1102_strings.rs](1102_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 7760 KB |
