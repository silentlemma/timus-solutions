# 1170. El paseo recto de longitud L más rápido a través de zonas de distinta velocidad

[Timus 1170](https://acm.timus.ru/problem.aspx?space=1&num=1170) · dificultad 1479 · geometry

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Desde el origen hay que caminar `L` metros en línea recta hasta un punto
de coordenadas positivas. `N ≤ 500` rectángulos de lados paralelos a los
ejes en el primer cuadrante tienen coeficientes de retraso: un tramo de
longitud `d` dentro de uno cuesta `d·c`, y fuera de ellos el desierto
cuesta `d·c0`. Todos los números son enteros positivos de hasta 32000, y
`L` llega más allá de todos los rectángulos. Hay que hallar el menor
tiempo total y un punto que lo alcance.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, luego `N` líneas `x1 y1 x2 y2 c`, y luego `c0` y `L`.

## Salida

El menor tiempo y después el punto final, todo con seis decimales.

## Evaluación

Se acepta cualquier punto final a distancia `L` del origen, con
coordenadas positivas y que dé el menor tiempo; el comprobador recalcula
el tiempo a lo largo de su dirección rectángulo por rectángulo.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
1 1 2 2 1
2 3
```

Salida:

```
4.585786
2.121320 2.121320
```

## Solución

Caminando con ángulo `t`, la recta `x = a` se alcanza tras `a / cos t` y
la recta `y = b` tras `b / sin t`. Se entra en un rectángulo en el mayor
de `x1 / cos t` e `y1 / sin t`, y se sale en el menor de `x2 / cos t` e
`y2 / sin t`. Así que el tiempo es `c0·L` más `(c − c0)` por la cuerda de
cada rectángulo, y el lado por el que se pasa solo cambia en las
direcciones de las cuatro esquinas.

Entre dos direcciones de esquina vecinas el tiempo tiene entonces la forma
`c0·L + p / cos t + q / sin t` con enteros fijos `p` y `q`. Si `p, q > 0`,
está por encima de `c0·L` en todo el tramo. Si no, es monótono (cuando `p`
y `q` tienen signos distintos) o cóncavo (ambos negativos), así que su
menor valor está en un extremo del tramo. Las direcciones por debajo de la
esquina más baja no tocan ningún rectángulo y cuestan exactamente `c0·L`.
Por tanto la respuesta es el mejor entre `c0·L` y los tiempos en las
direcciones de las esquinas.

Cada rectángulo aporta cuatro términos, cada uno activado y desactivado
en dos direcciones de esquina, así que un barrido por las direcciones
ordenadas por pendiente mantiene `p` y `q` al día. Las pendientes se
comparan como fracciones, así que las esquinas sobre el mismo rayo
comparten un evento. `O(N log N)`.

Detalles a tener en cuenta:

- el tiempo es continuo en la dirección, así que evaluar una esquina con
  los `p` y `q` del tramo justo anterior es exacto;
- dos esquinas sobre un mismo rayo deben fusionarse exactamente, o un
  tramo falso diminuto entre ellas podría mostrar un tiempo que ninguna
  dirección tiene;
- el punto final debe tener coordenadas positivas, así que la dirección
  vacía se toma a mitad de camino por debajo de la esquina más baja, no a
  lo largo del eje.

Las respuestas se compararon con un barrido denso de 20 000 direcciones
en 400 conjuntos aleatorios de rectángulos, incluidas zonas rápidas tras
franjas lentas, y con una solución escrita aparte en todas las pruebas.

## Notas por lenguaje

- C++ y Java guardan los eventos en un mapa ordenado cuyo comparador
  compara pendientes como fracciones; Python, Go y Rust reducen cada
  dirección por el mcd y ordenan.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1170_geometry.cpp](1170_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 340 KB |
| [1170_geometry.go](1170_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.015 s | 1560 KB |
| [1170_geometry.java](1170_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.171 s | 3856 KB |
| [1170_geometry.py](1170_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 1592 KB |
| [1170_geometry.rs](1170_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.015 s | 540 KB |
