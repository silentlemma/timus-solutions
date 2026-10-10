# 1192. Cuánto avanza una pelota que rebota en un sueño

[Timus 1192](https://acm.timus.ru/problem.aspx?space=1&num=1192) · dificultad 109 · math

Problema original de Igor Goldberg, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Desde un suelo plano infinito se lanza una pelota con un ángulo de `a`
grados sobre la horizontal y velocidad `V` m/s, con gravedad `10` m/s² y
sin aire. Rebota con el mismo ángulo, perdiendo energía cinética por un
factor `K > 1` en cada rebote, y pi se toma como `3.1415926535`. Hay que
hallar hasta qué distancia del punto de lanzamiento puede llegar la
pelota, con dos decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`V` (hasta 500000), `a` (de 0 a 90) y `K`.

## Salida

La distancia en metros, redondeada a dos decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 15 2.50
```

Salida:

```
2.08
```

## Solución

Un vuelo a velocidad `v` y ángulo `a` recorre `v²·sin(2a)/g`. Un rebote
mantiene el ángulo y divide la energía cinética, es decir `v²`, entre `K`.
Los vuelos forman una serie geométrica de razón `1/K`, cuya suma es el
primer vuelo por `K/(K − 1)`. `O(1)`.

Detalles a tener en cuenta:

- pi debe ser el `3.1415926535` dado: con él, un lanzamiento en vertical a
  la mayor velocidad aún se desplaza unos metros, y las respuestas
  esperadas lo incluyen;
- el resultado puede llegar a unos `2.5·10¹⁴` cuando `K` es cercano a 1,
  aún dentro de la precisión de un double para dos decimales;
- `V = 0` o `a = 0` dan `0.00`.

Las respuestas se compararon con una solución escrita aparte en todas las
pruebas.

## Notas por lenguaje

- Java imprime con la configuración regional de EE. UU. para que el
  separador decimal sea un punto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1192_math.cpp](1192_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 152 KB |
| [1192_math.go](1192_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1096 KB |
| [1192_math.java](1192_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1920 KB |
| [1192_math.py](1192_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 416 KB |
| [1192_math.rs](1192_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 248 KB |
