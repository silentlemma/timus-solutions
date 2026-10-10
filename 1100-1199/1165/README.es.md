# 1165. Dónde aparece por primera vez una cadena de dígitos en 123456789101112…

[Timus 1165](https://acm.timus.ru/problem.aspx?space=1&num=1165) · dificultad 930 · strings

Problema original de Nikita Shamgunov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`S` es la cadena infinita de todos los enteros positivos escritos uno tras
otro: `1234567891011121314…`, indexada desde 1. Dada una cadena `A` de a
lo sumo 200 dígitos, hay que hallar el menor `k` tal que `A` aparece en
`S` empezando en la posición `k`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La cadena `A`.

## Salida

El número `k`. Puede tener unos 200 dígitos.

## Ejemplos

### Ejemplo 1

Entrada:

```
101
```

Salida:

```
10
```

## Solución

El primer dígito de un número `x` de `d` dígitos está en la posición
`d·x + 1 − R(d)`, donde `R(d)` es el repituno `11…1` de `d` unos: los
números más cortos ocupan `(d − 1)·10^(d−1) − R(d − 1)` dígitos, y
`10^(d−1) + R(d − 1) = R(d)`.

Una aparición de `A` cubre una racha de números consecutivos. Hay tres
tipos:

1. Algún número `x` está entero dentro de `A`. Entonces `x` es una
   subcadena de `A` sin cero inicial y fija todo lo demás: se escriben
   `x + 1`, `x + 2`, … a la derecha y `x − 1`, `x − 2`, … a la izquierda y
   se compara con `A`. Hay `O(n²)` subcadenas así.
2. `A` es el final de `y − 1` seguido del comienzo de `y`, ninguno
   completo, con la frontera en `i`. El comienzo de `y` es `A[i..]`. Sus
   últimos `i` dígitos son los últimos `i` de `y − 1` más uno, es decir,
   `A[..i] + 1` recortado a `i` dígitos, incluso cuando un acarreo
   convierte `99…9` en `100…0`. El `y` más corto superpone esas dos partes
   conocidas lo más posible, así que se prueba cada superposición y se
   comprueba como en el caso 1.
3. `A` está dentro de un solo número pero no al principio. El número más
   corto así es `1A`, de modo que `k` es la posición de `1A` más uno.

La respuesta es la menor posición entre todos los candidatos que pasan la
comprobación. `O(n³)` operaciones con dígitos, `n ≤ 200`.

Detalles a tener en cuenta:

- `A` puede empezar con ceros o ser solo ceros: `0` aparece por primera
  vez dentro de `10`, en la posición 11;
- la respuesta supera con mucho los 64 bits, así que las posiciones
  necesitan números grandes;
- el número anterior a una potencia de diez tiene un dígito menos;
- el recorrido hacia la izquierda debe fallar si llega a cero.

Las respuestas se compararon con una búsqueda directa en `S` en todas las
cadenas de hasta tres dígitos y en otras aleatorias de hasta cinco, 1 708
cadenas en total, y en 400 cadenas generadas de hasta 200 dígitos con una
solución escrita aparte.

## Notas por lenguaje

- Python usa sus propios enteros grandes en todo momento.
- Go y Java recorren los vecinos como cadenas decimales y calculan las
  posiciones con `big.Int` y `BigInteger`.
- C++ y Rust lo hacen todo con cadenas decimales, con pequeñas funciones
  para sumar uno, restar uno, multiplicar por la longitud y restar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1165_strings.cpp](1165_strings.cpp) | G++ 13.2 x64 | strings | O(n³) | AC | 0.015 s | 420 KB |
| [1165_strings.go](1165_strings.go) | Go 1.14 x64 | strings | O(n³) | AC | 0.031 s | 4540 KB |
| [1165_strings.java](1165_strings.java) | Java 1.8 | strings | O(n³) | AC | 0.156 s | 6188 KB |
| [1165_strings.py](1165_strings.py) | Python 3.12 x64 | strings | O(n³) | AC | 0.093 s | 680 KB |
| [1165_strings.rs](1165_strings.rs) | Rust 1.75 x64 | strings | O(n³) | AC | 0.031 s | 260 KB |
