# 1777. Anindilyakwa

[Timus 1777](https://acm.timus.ru/problem.aspx?space=1&num=1777) · dificultad 126 · simulation

Problema original de Ivan Burmistrov, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un claro hay tres montones de piedras de tamaños distintos. Cada
persona, por turno, encuentra los dos montones cuyos tamaños difieren
menos y trae un montón nuevo de exactamente esa diferencia; todos los
montones se quedan. Las preguntas terminan con la persona que encuentra
dos montones iguales. ¿A cuántas personas se pregunta?

## Entrada

Los tres tamaños distintos x₁, x₂, x₃ (1 ≤ xᵢ ≤ 10¹⁸).

## Salida

El número de personas preguntadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
11 5 9
```

Salida:

```
3
```

## Solución

El proceso se simula tal cual: ordenar los montones, tomar la menor
diferencia entre vecinos, parar si es 0 y, si no, añadir un montón de
ese tamaño. La menor diferencia se encoge de forma parecida a los
números en el algoritmo de Euclides, así que el proceso es corto: el
más largo encontrado, con tres números de Fibonacci consecutivos cerca
de 10¹⁸, pregunta a 85 personas, y tamaños al azar a una docena o así.
`O(s² log s)` para s pasos.

En el ejemplo las diferencias son 2, 4 y 6: la primera persona trae un
montón de 2, la segunda vuelve a ver 9 y 11 y trae otro de 2, y la
tercera señala los dos montones de 2.

Trampas:

- la persona que encuentra montones iguales también cuenta;
- el montón nuevo puede repetir un tamaño viejo, lo que acaba con la
  persona siguiente;
- tamaños de hasta 10¹⁸ necesitan números de 64 bits.

Las respuestas coinciden con una implementación aceptada independiente
en 90 tríos aleatorios, incluidos tríos de números de Fibonacci.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1777_simulation.cpp](1777_simulation.cpp) | G++ 13.2 x64 | simulation | O(s^2 log s) for s steps | AC | 0.015 s | 192 KB |
| [1777_simulation.go](1777_simulation.go) | Go 1.14 x64 | simulation | O(s^2 log s) for s steps | AC | 0.031 s | 1124 KB |
| [1777_simulation.java](1777_simulation.java) | Java 1.8 | simulation | O(s^2 log s) for s steps | AC | 0.125 s | 1712 KB |
| [1777_simulation.py](1777_simulation.py) | Python 3.12 x64 | simulation | O(s^2 log s) for s steps | AC | 0.093 s | 436 KB |
| [1777_simulation.rs](1777_simulation.rs) | Rust 1.75 x64 | simulation | O(s^2 log s) for s steps | AC | 0.062 s | 248 KB |
