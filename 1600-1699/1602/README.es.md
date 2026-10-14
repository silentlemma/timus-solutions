# 1602. El ascensor

[Timus 1602](https://acm.timus.ru/problem.aspx?space=1&num=1602) · dificultad 454 · implementation

Problema original de Vladimir Yakovlev, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Petya está en la planta más alta, la n, de un rascacielos y quiere
llegar a la primera. El ascensor está en la planta k bajando a la
primera; allí se detiene 15 segundos antes de poder subir. Recorre una
planta en v segundos, Petya baja una planta corriendo en u segundos
(0,1 < v < u < 100, con como mucho dos decimales), y subir al ascensor
lleva 5 segundos. ¿Hasta qué planta debe bajar Petya a pie para llegar
cuanto antes a la primera? Entre plantas igual de buenas se elige la de
menos camino a pie.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

n, k, u y v.

## Salida

La planta.

## Ejemplos

### Ejemplo 1

Entrada:

```
50 49 4.8 0.2
```

Salida:

```
45
```

## Solución

Se prueba cada planta f. Bajar a pie hasta abajo (f = 1) cuesta
(n − 1)·u. Si no, Petya llama al ascensor al llegar a la planta f, en el
instante (n − f)·u. El ascensor puede salir de la primera planta en
(k − 1)·v + 15, así que empieza a subir en el más tardío de los dos
momentos, sube f − 1 plantas, espera 5 segundos a que se suba y baja de
nuevo f − 1 plantas. Gana el menor total, y a igualdad la planta más
alta, que supone menos camino a pie: `O(n)`.

El ejemplo fija la lectura: el ascensor solo empieza a subir cuando se
le llama desde la planta f. Si pudiera subir justo tras su parada, en el
ejemplo la planta 44 sería mejor que la 45.

Los resultados se compararon con una implementación independiente en
3500 entradas aleatorias y propensas a empates.

Detalles a tener en cuenta:

- u y v tienen dos decimales, y hay empates exactos (prueba 09, plantas
  3 y 4); en centésimas de segundo todos los tiempos son enteros
  exactos, así que no hace falta comparar números reales;
- bajar a pie todo el camino también es una opción, y en edificios bajos
  suele ser la mejor (prueba 02);
- a igualdad gana la planta más alta, así que la comparación se queda
  con las plantas posteriores cuando los totales coinciden.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1602_implementation.cpp](1602_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 416 KB |
| [1602_implementation.go](1602_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1096 KB |
| [1602_implementation.java](1602_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1680 KB |
| [1602_implementation.py](1602_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 464 KB |
| [1602_implementation.rs](1602_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.062 s | 236 KB |
