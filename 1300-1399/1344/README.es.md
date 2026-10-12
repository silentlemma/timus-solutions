# 1344. Nabo gigante

[Timus 1344](https://acm.timus.ru/problem.aspx?space=1&num=1344) · dificultad 4147 · dsu

Problema original de Pavel Egorov, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 32 poleas sin peso están unidas por cuerdas sin peso. Cada polea
tiene una cuerda pasada por encima y otra atada a su eje. En una polea
del primer tipo la cuerda del eje sube y los dos extremos de la otra
cuerda bajan; en el segundo tipo es al revés. Cada extremo de cuerda
lleva a otra polea, al techo, a un nabo de 1 kg o, en exactamente un
extremo, a ninguna parte: ahí hay que colgar una carga. Todas las
cuerdas son verticales, y las poleas unidas por una cuerda están a
distinta altura. Hay que hallar la masa de la carga que deja el sistema
en equilibrio, con cuatro cifras tras el punto, o imprimir
`No solution` si no existe y `Any` si sirve cualquier masa.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego, para cada polea, su tipo T, adónde llevan los dos extremos
de la cuerda pasada por ella (X1 y X2) y adónde lleva la cuerda de su
eje (Y). 0 es el techo, −1 el nabo y −2 el extremo libre.

## Salida

La masa, `No solution` o `Any`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 -1 2 0
2 1 0 -2
```

Salida:

```
2.0000
```

### Ejemplo 2

Entrada:

```
4
1 3 2 0
2 1 0 4
1 -1 4 1
2 3 2 -2
```

Salida:

```
No solution
```

### Ejemplo 3

Entrada:

```
4
1 2 2 0
2 1 1 -2
1 4 4 0
2 3 3 -1
```

Salida:

```
Any
```

## Solución

Se miden las fuerzas en kilogramos. Una cuerda sobre una polea sin peso
tiene la misma tensión t en sus dos extremos, y la polea está en
equilibrio cuando la cuerda del eje sostiene ambos extremos: la tensión
del eje es a = 2t. Una cuerda entre dos poleas tiene una sola tensión.
El extremo del nabo tiene tensión 1, el extremo libre la masa
desconocida m, y el techo da lo que haga falta.

A qué parte de la otra polea llega una cuerda se deduce de las
direcciones: una cuerda que sale de la polea i hacia abajo llega a la
polea j desde arriba. En j es su eje o los extremos pasados por ella,
según qué lado mire hacia arriba. Así cada cuerda dice «esta tensión es
igual a aquella», y cada polea dice «a = 2t».

Todas estas relaciones multiplican por potencias de dos. Una unión de
conjuntos disjuntos sobre las tensiones guarda, para cada tensión, el
exponente de dos que la relaciona con la raíz de su grupo. Cuando una relación
cierra un ciclo y las potencias no cuadran, como t = 2t, todas las
tensiones de ese grupo deben ser 0. Entonces:

- si el grupo del nabo debe ser 0, el nabo no puede colgar:
  `No solution`;
- si el nabo y el extremo libre están en un grupo, m es la potencia de
  dos entre ellos;
- si el grupo del extremo libre debe ser 0, m = 0;
- si no, el extremo libre no depende del nabo: `Any`.

`O(N log N)`.

Detalles a tener en cuenta:

- una cuerda que llega a una polea se encuentra con su eje o con la
  cuerda pasada por ella, y solo las direcciones dicen con cuál;
- las relaciones de tensión contradictorias impiden el equilibrio
  solo si su grupo contiene el nabo (prueba 02);
- el extremo libre puede colgar de un sistema sin relación con el nabo
  (pruebas 03 y 06);
- una cadena de 31 poleas móviles da 2³¹, más de lo que cabe en enteros
  de 32 bits con signo.

La unión de conjuntos se comparó con una eliminación de Gauss exacta
sobre las mismas ecuaciones en unos 3000 sistemas aleatorios de hasta 5
poleas.

## Notas por lenguaje

- Las cinco soluciones guardan los exponentes de dos como enteros y solo
  construyen la masa al final.
- **Java**: la masa se redondea con `BigDecimal` y `HALF_EVEN`
  (empates al par).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1344_dsu.cpp](1344_dsu.cpp) | G++ 13.2 x64 | dsu | O(N log N) | AC | 0.015 s | 224 KB |
| [1344_dsu.go](1344_dsu.go) | Go 1.14 x64 | dsu | O(N log N) | AC | 0.031 s | 1104 KB |
| [1344_dsu.java](1344_dsu.java) | Java 1.8 | dsu | O(N log N) | AC | 0.109 s | 1928 KB |
| [1344_dsu.py](1344_dsu.py) | Python 3.12 x64 | dsu | O(N log N) | AC | 0.062 s | 784 KB |
| [1344_dsu.rs](1344_dsu.rs) | Rust 1.75 x64 | dsu | O(N log N) | AC | 0.015 s | 260 KB |
