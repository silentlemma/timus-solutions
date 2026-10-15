# 1655. Piratas somalíes

[Timus 1655](https://acm.timus.ru/problem.aspx?space=1&num=1655) · dificultad 1846 · dp

Problema original de Denis Musin, del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cañón láser en un barco gira a lo sumo w vueltas por minuto y dispara
al instante, hundiendo lo que esté en su línea. n barcos piratas se
acercan en línea recta, el barco i desde el azimut bᵢ a distancia dᵢ con
velocidad vᵢ nudos. Ningún pirata puede acercarse a menos de una milla.
Con el cañón al principio en el azimut a, hay que hallar el menor tiempo
para hundirlos a todos y un orden de disparo, o decir que es imposible.

## Entrada

a, w y n (0 ≤ a < 360, 0.01 ≤ w ≤ 1, 1 ≤ n ≤ 500) y luego n líneas
bᵢ dᵢ vᵢ (0 ≤ bᵢ < 360, 1 ≤ dᵢ ≤ 1000, 0.01 ≤ vᵢ ≤ 100), con todos los
azimuts distintos.

## Salida

El menor tiempo en minutos con precisión 10⁻³ y el orden de los barcos,
un número por línea, o `Impossible`.

## Ejemplos

### Ejemplo 1

Entrada:

```
0.0 0.05 2
144.0 22.0 100.0
216.0 22.0 100.0
```

Salida:

```
12.000
2
1
```

### Ejemplo 2

Entrada:

```
0.0 0.05 2
144.0 20.0 100.0
216.0 20.0 100.0
```

Salida:

```
Impossible
```

## Solución

El barco i debe hundirse en (dᵢ − 1) / vᵢ · 60 minutos. Los azimuts se
miden en sentido horario desde la dirección inicial del cañón; los barcos
justo delante se hunden en el instante 0. Como el cañón dispara mientras
gira, cualquier barco por el que pase puede hundirse en ese momento, así
que en todo momento los barcos hundidos forman un arco alrededor del
inicio: unos tomados girando a la izquierda (antihorario) y otros a la
derecha.

El estado es entonces (i, j, extremo): se hundieron los i barcos más
cercanos al inicio por la izquierda y los j más cercanos por la derecha,
y el cañón apunta al extremo izquierdo o derecho de ese arco. El menor
tiempo de cada estado sale de los dos estados menores, siguiendo por el
mismo lado o volviendo a través del inicio desde el otro extremo, y un
paso solo vale si llega al barco nuevo antes de su plazo. La respuesta es
el mejor estado con i + j igual al número de barcos; las elecciones
guardadas dan el orden. `O(n²)` estados, unos 125 000 como mucho.

Detalles a tener en cuenta:

- pasar de un extremo al otro cruza el inicio, así que cuesta la suma de
  las dos distancias, no su diferencia;
- un barco que ya está a una milla solo se salva si está justo delante
  (prueba 03);
- cuando ambos sentidos son igual de rápidos (el primer ejemplo), el
  programa prefiere terminar por la izquierda, como una implementación
  aceptada independiente; un verificador acepta cualquier orden con el
  menor tiempo.

Las respuestas coinciden con una implementación aceptada independiente
en 60 pruebas aleatorias, orden incluido.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1655_dp.cpp](1655_dp.cpp) | G++ 13.2 x64 | dp | O(n²) | AC | 0.031 s | 4224 KB |
| [1655_dp.go](1655_dp.go) | Go 1.14 x64 | dp | O(n²) | AC | 0.046 s | 9508 KB |
| [1655_dp.java](1655_dp.java) | Java 1.8 | dp | O(n²) | AC | 0.187 s | 12828 KB |
| [1655_dp.py](1655_dp.py) | Python 3.12 x64 | dp | O(n²) | AC | 0.359 s | 15848 KB |
| [1655_dp.rs](1655_dp.rs) | Rust 1.75 x64 | dp | O(n²) | AC | 0.031 s | 7732 KB |
