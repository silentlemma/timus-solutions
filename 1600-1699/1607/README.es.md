# 1607. Taxi

[Timus 1607](https://acm.timus.ru/problem.aspx?space=1&num=1607) · dificultad 46 · implementation

Problema original de Denis Musin, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Petya regatea con un taxista. Petya empieza en a y sube la oferta en b
cada vez; el taxista empieza en c y baja el precio en d cada vez;
hablan por turnos, primero Petya. Ninguno nombra un precio que pase el
del otro: el taxista acepta la oferta de Petya en vez de pedir menos, y
Petya acepta el precio del taxista en vez de ofrecer más. ¿Cuánto paga
Petya? Todos los números van de 1 a 10000.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

a, b, c y d.

## Salida

El precio del viaje.

## Ejemplos

### Ejemplo 1

Entrada:

```
150 50 1000 100
```

Salida:

```
450
```

## Solución

Se simula el regateo. Si a ya es al menos c, el taxista lo acepta. Si
no, Petya sube b; si eso alcanza el precio del taxista, Petya acepta ese
precio. Luego el taxista baja d; si eso alcanza la oferta de Petya, el
taxista la acepta. La distancia se reduce al menos en 2 por ronda, así
que hay como mucho unas 5000 rondas: `O(c − a)`. Los resultados se
compararon con una implementación independiente en 800 entradas
aleatorias.

Detalles a tener en cuenta:

- el lado que pasaría el precio del otro cede al precio del otro, así
  que la respuesta siempre es un precio que se llegó a nombrar (pruebas
  04 y 05);
- Petya puede empezar por encima del precio del taxista; entonces no hay
  regateo y Petya paga a (prueba 02).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1607_implementation.cpp](1607_implementation.cpp) | G++ 13.2 x64 | implementation | O(c - a) | AC | 0.015 s | 132 KB |
| [1607_implementation.go](1607_implementation.go) | Go 1.14 x64 | implementation | O(c - a) | AC | 0.015 s | 1112 KB |
| [1607_implementation.java](1607_implementation.java) | Java 1.8 | implementation | O(c - a) | AC | 0.140 s | 1600 KB |
| [1607_implementation.py](1607_implementation.py) | Python 3.12 x64 | implementation | O(c - a) | AC | 0.093 s | 416 KB |
| [1607_implementation.rs](1607_implementation.rs) | Rust 1.75 x64 | implementation | O(c - a) | AC | 0.031 s | 224 KB |
