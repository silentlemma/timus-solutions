# 1193. ¿Cuánto antes debe empezar un examen oral para que todos terminen a tiempo?

[Timus 1193](https://acm.timus.ru/problem.aspx?space=1&num=1193) · dificultad 181 · greedy

Problema original de Anatoly Uglov, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 40` estudiantes reciben sus preguntas al empezar un examen oral. El
estudiante `i` se prepara `T1` minutos (todos distintos) y luego responde
durante `T2` minutos, de uno en uno, en el orden en que terminan de
prepararse; quien termina mientras otro responde espera en una cola. Cada
estudiante debe terminar como mucho `T3` minutos después del inicio
previsto. Hay que hallar el menor número de minutos que hay que adelantar
el examen para que todos terminen a tiempo.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `T1 T2 T3` para cada estudiante.

## Salida

El número de minutos, 0 si no hace falta adelantar.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
100 10 120
70 40 150
99 15 400
```

Salida:

```
15
```

### Ejemplo 2

Entrada:

```
2
100 10 110
80 15 100
```

Salida:

```
0
```

## Solución

Empezar `s` minutos antes lo desplaza todo en `s`: el orden de la cola y
cada espera siguen iguales, y solo los plazos quedan `s` minutos más tarde
respecto al inicio. Así que se simula el examen una vez, en orden de
`T1`: cada respuesta empieza cuando el estudiante está listo o cuando
termina la anterior, lo que sea más tarde. La respuesta es el mayor
retraso, el final menos `T3`, o 0 si nadie se retrasa. `O(N log N)` por la
ordenación.

Detalles a tener en cuenta:

- la cola va por el fin de la preparación, no por el orden de entrada;
- un estudiante listo cuando nadie responde empieza enseguida, así que
  puede haber ratos sin nadie respondiendo;
- el adelanto no puede ser negativo: si todos van sobrados, la respuesta
  es 0.

Las respuestas se compararon con una solución escrita aparte, que busca
el adelanto por bisección, en 300 exámenes aleatorios y en todas las
pruebas.

## Notas por lenguaje

- Todos los lenguajes ordenan a los estudiantes por tiempo de preparación
  y hacen el mismo bucle.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1193_greedy.cpp](1193_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 192 KB |
| [1193_greedy.go](1193_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1116 KB |
| [1193_greedy.java](1193_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 3776 KB |
| [1193_greedy.py](1193_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 380 KB |
| [1193_greedy.rs](1193_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 236 KB |
