# 1251. Un cementerio que libera tumbas olvidadas

[Timus 1251](https://acm.timus.ru/problem.aspx?space=1&num=1251) · dificultad 1486 · simulation

Problema original de Stanislav Vasilyev, del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cementerio es una cuadrícula de N × M tumbas (1 ≤ N, M ≤ 100), vacía al
principio. Cada recién llegado ocupa la tumba libre de menor fila y luego
menor columna; si no hay ninguna libre, va al crematorio. De vez en
cuando los parientes visitan a los clientes. Una tumba queda libre el
primer día en que su cliente lleva más de 1000 días sin entierro ni
visita y ninguna de sus hasta 8 vecinas (incluidas las diagonales) ha
recibido visitas en los últimos 100 días. Dados hasta 15 000 eventos en
orden de tiempo (días de 0 a 7600, como mucho 10 000 llegadas), hay que contar los clientes
enviados al crematorio.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, y luego un evento por línea: `día d` para una llegada o
`día v k` para una visita al cliente k (los clientes se numeran por
orden de llegada).

## Salida

El número de clientes incinerados.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
1 d
1 d
1 d
1 d
300 d
500 v 2
1001 d
1002 d
1002 d
1003 v 3
1003 d
1003 d
1236 v 2
2032 v 2
2033 d
```

Salida:

```
3
```

## Solución

Para una tumba ocupada el día en que queda libre lo fijan dos números:
`max(touched + 1001, nearVisit + 101)`, donde `touched` es el último
entierro o visita de su cliente y `nearVisit` la última visita a una
vecina. Una visita sube el `touched` de su tumba y el `nearVisit` de las
vecinas, así que el día de liberación solo se retrasa.

El programa guarda el día de liberación de cada tumba ocupada en un
montículo de mínimos, con entradas nuevas tras entierros y visitas,
saltando las antiguas al sacarlas. Antes de los eventos de un día libera
todas las tumbas cuyo día ha llegado; luego atiende los eventos del día
en orden. Las tumbas libres están en un segundo montículo de mínimos con
clave `fila · M + columna`, así que una llegada toma la menor.
`O(NM + E log(NM + E))` con E ≤ 15 000.

Detalles a tener en cuenta:

- las tumbas se liberan al empezar el día, antes de las llegadas de ese
  día; el ejemplo lo necesita el día 1002;
- el día `touched + 1000` la tumba aún está ocupada y se libera al día
  siguiente (prueba 02);
- una visita a un cliente cuya tumba ya se liberó, o que fue incinerado,
  no cambia nada (prueba 04), y los clientes reciben número aunque los
  incineren;
- un entierro no retrasa a las vecinas.

Las respuestas se compararon con una simulación día a día en 200
cementerios pequeños aleatorios.

## Notas por lenguaje

- Go, C++ y Java empaquetan una liberación pendiente en un solo entero,
  `día · cells + tumba`; Python y Rust guardan un par.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1251_simulation.cpp](1251_simulation.cpp) | G++ 13.2 x64 | simulation | O(NM + E log(NM + E)) | AC | 0.031 s | 396 KB |
| [1251_simulation.go](1251_simulation.go) | Go 1.14 x64 | simulation | O(NM + E log(NM + E)) | AC | 0.062 s | 4676 KB |
| [1251_simulation.java](1251_simulation.java) | Java 1.8 | simulation | O(NM + E log(NM + E)) | AC | 0.125 s | 5108 KB |
| [1251_simulation.py](1251_simulation.py) | Python 3.12 x64 | simulation | O(NM + E log(NM + E)) | AC | 0.265 s | 8396 KB |
| [1251_simulation.rs](1251_simulation.rs) | Rust 1.75 x64 | simulation | O(NM + E log(NM + E)) | AC | 0.015 s | 1604 KB |
