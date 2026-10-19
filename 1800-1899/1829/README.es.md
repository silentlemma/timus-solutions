# 1829. Tablas de enrutamiento

[Timus 1829](https://acm.timus.ru/problem.aspx?space=1&num=1829) · dificultad 2969 · sorting

Problema original de Igor Andrianov, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una fila de una tabla de enrutamiento contiene una red d, una máscara m
(unos y luego ceros) y una pasarela g. Un paquete a la dirección a va a
la pasarela de la fila coincidente (d and m = a and m) con la máscara
más larga; para cada dirección hay como mucho una coincidencia más
larga. Dos tablas son equivalentes si con ambas cada dirección va a la
misma pasarela, o a ninguna. Decidir si dos tablas dadas son
equivalentes.

## Entrada

El número de filas de la primera tabla, sus filas "d m g" con
direcciones con puntos, y luego la segunda tabla de la misma forma.
Como mucho 65536 filas en total.

## Salida

"YES" si las tablas son equivalentes y "NO" si no.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
192.168.0.0 255.255.255.0 192.168.14.1
192.168.1.0 255.255.255.0 192.168.14.1
192.168.2.0 255.255.255.0 192.168.14.2
192.168.3.0 255.255.255.0 192.168.14.2
2
192.168.0.0 255.255.252.0 192.168.14.1
192.168.2.0 255.255.254.0 192.168.14.2
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
1
192.168.0.0 255.255.255.0 192.168.14.1
2
192.168.0.0 255.255.255.0 192.168.14.1
172.16.0.0 255.255.0.0 172.16.0.1
```

Salida:

```
NO
```

## Solución

Una fila cubre el bloque alineado de direcciones de d and m a
(d and m) or not m, y dos bloques cualesquiera están anidados o
separados. Así, una tabla es una familia laminar de intervalos sobre la
recta 0 … 2³² − 1, y una dirección se enruta por el bloque más interior
que la contiene.

Cada tabla se convierte en su función de enrutamiento escrita a trozos:
se ordenan los bloques por inicio, el mayor primero en caso de empate,
y se barre con una pila de bloques abiertos. Antes de que se abra un
bloque, el tramo desde el último corte pertenece al bloque de la cima;
cuando el barrido pasa el final del bloque de la cima, se emite su
tramo restante y se desapila. Un trozo se funde con el anterior si se
tocan y comparten pasarela, y las direcciones fuera de todo bloque
simplemente se omiten. Dos tablas son equivalentes exactamente cuando
estas listas canónicas son iguales. Domina la ordenación:
`O(n log n)`.

En el primer ejemplo ambas tablas dan los trozos 192.168.0.0 …
192.168.1.255 hacia .14.1 y 192.168.2.0 … 192.168.3.255 hacia .14.2;
en el segundo, el trozo extra 172.16.0.0/16 las distingue.

Trampas:

- la dirección de red escrita puede tener bits fuera de la máscara;
  solo cuenta d and m;
- una fila puede repetir la pasarela que daría su bloque envolvente,
  así que hay que comparar tras fundir, no fila a fila;
- una ruta por defecto 0.0.0.0 0.0.0.0 cubre las 2³² direcciones, así
  que los extremos necesitan enteros de 64 bits.

Las respuestas coinciden con una comprobación directa de la
coincidencia más larga en cada borde de bloque en unos cientos de
tablas pequeñas y con una implementación aceptada independiente en las
grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1829_sorting.cpp](1829_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.171 s | 2632 KB |
| [1829_sorting.go](1829_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.156 s | 7464 KB |
| [1829_sorting.java](1829_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.250 s | 9296 KB |
| [1829_sorting.py](1829_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.515 s | 23092 KB |
| [1829_sorting.rs](1829_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.046 s | 6584 KB |
