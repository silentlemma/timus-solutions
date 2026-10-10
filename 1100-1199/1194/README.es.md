# 1194. Cuántos apretones de manos cuando una fiesta se dispersa de vuelta a casa

[Timus 1194](https://acm.timus.ru/problem.aspx?space=1&num=1194) · dificultad 83 · math

Problema original de Leonid Volkov, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 20000` hobbits, `K` de ellos matrimonios, salen juntos de una
fiesta. En cada cruce un grupo se divide en grupos menores, y cada uno da
la mano a todos aquellos de los que se separa. Los grupos se siguen
dividiendo hasta que cada uno es un hobbit solo o un matrimonio. Se dan
las divisiones; hay que contar todos los apretones de manos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `K`, y luego, para cada división, el número del grupo, el número de
grupos nuevos y el número y tamaño de cada uno.

## Salida

El número de apretones de manos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 0
1 2 2 2 3 1
2 2 4 1 5 1
```

Salida:

```
3
```

## Solución

Dos hobbits cualesquiera se dan la mano exactamente una vez: en la
división en la que acaban por primera vez en grupos distintos. Los únicos
pares que nunca se separan son los matrimonios, que vuelven juntos a
casa. Así que la respuesta es `N·(N − 1)/2 − K`, y la descripción de las
divisiones no importa. `O(1)`, aparte de leer la primera línea.

Detalles a tener en cuenta:

- las líneas de las divisiones pueden ignorarse por completo, pero una
  solución que suma los pares separados en cada división obtiene el mismo
  número;
- `N·(N − 1)/2` llega a unos `2·10⁸`, que aún cabe en 32 bits, aunque la
  aritmética de 64 bits no cuesta nada aquí.

Las respuestas se compararon con una solución escrita aparte, que suma
los apretones división a división, en 200 fiestas aleatorias y en todas
las pruebas.

## Notas por lenguaje

- Todos los lenguajes leen solo `N` y `K`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1194_math.cpp](1194_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB |
| [1194_math.go](1194_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1064 KB |
| [1194_math.java](1194_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1552 KB |
| [1194_math.py](1194_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 328 KB |
| [1194_math.rs](1194_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 208 KB |
