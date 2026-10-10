# 1121. Los tipos de las sucursales más cercanas en una cuadrícula de calles

[Timus 1121](https://acm.timus.ru/problem.aspx?space=1&num=1121) · dificultad 352 · bruteforce

Problema original de Leonid Volkov y Alexander Somov, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula de `H × W` cruces (`1 ≤ H, W ≤ 150`) guarda en cada cruce
una máscara de bits con los tipos de sucursales que hay allí (los tipos
son potencias de dos, como mucho 11; 0 significa ninguna sucursal). La
distancia es el número de tramos de calle recorridos, es decir, la
distancia Manhattan. Para cada cruce con sucursales imprime `-1`; para
cada cruce vacío imprime la unión bit a bit de los tipos de sus sucursales
más cercanas, o `0` si no hay ninguna a distancia 5 o menos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`H W` y luego `H` líneas de `W` máscaras.

## Salida

`H` líneas de `W` números.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 5
0 0 2 0 2
0 0 0 0 0
0 0 0 0 0
0 0 0 5 0
1 0 0 4 0
```

Salida:

```
2 2 -1 2 -1
3 2 2 7 2
1 7 7 5 7
1 5 5 -1 5
-1 1 4 -1 4
```

## Solución

Solo importan las distancias de 1 a 5, así que para cada cruce vacío se
miran los cruces a distancia 1, luego 2, y así sucesivamente: el anillo a
distancia `d` tiene `4d` celdas, 60 hasta la distancia 5. En la primera
distancia donde aparece alguna sucursal, la respuesta es el «o» bit a bit
de las máscaras de ese anillo; ahí se para. Los desplazamientos de cada
anillo se listan una vez de antemano. `O(H · W · 60)`, unos 1,4 millones
de comprobaciones.

Detalles a tener en cuenta:

- los tipos se combinan con «o», no se suman: dos sucursales del mismo
  tipo a la distancia mínima cuentan una vez (en `3 0 6` el centro recibe
  `7`, no `9`);
- solo cuenta la distancia mínima, aunque sucursales más lejanas añadirían
  tipos;
- las sucursales a seis calles o más dan `0`, no sus tipos.

Las respuestas se comprobaron con una búsqueda en anchura desde todas las
sucursales a la vez hasta la distancia 5, donde los tipos más cercanos de
un cruce son la unión de los de sus vecinos una capa más cerca, en todas
las pruebas y 40 mapas aleatorios.

## Notas por lenguaje

- Todos los lenguajes recorren los mismos anillos precalculados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1121_bruteforce.cpp](1121_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(H·W·60) | AC | 0.031 s | 256 KB |
| [1121_bruteforce.go](1121_bruteforce.go) | Go 1.14 x64 | bruteforce | O(H·W·60) | AC | 0.031 s | 1376 KB |
| [1121_bruteforce.java](1121_bruteforce.java) | Java 1.8 | bruteforce | O(H·W·60) | AC | 0.109 s | 3664 KB |
| [1121_bruteforce.py](1121_bruteforce.py) | Python 3.12 x64 | bruteforce | O(H·W·60) | AC | 0.406 s | 2512 KB |
| [1121_bruteforce.rs](1121_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(H·W·60) | AC | 0.015 s | 628 KB |
