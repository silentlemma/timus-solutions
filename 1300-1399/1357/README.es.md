# 1357. Tetera 1.0 para torpes

[Timus 1357](https://acm.timus.ru/problem.aspx?space=1&num=1357) · dificultad 1187 · simulation

Problema original de Vladimir Yakovlev, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 500 estudiantes se despiertan en momentos distintos de un mismo día
y comparten una tetera sobre un hornillo de 400 W. Quien encuentra el
hornillo libre vierte 200 ml de agua a 20 °C y empieza a calentarla.
Quien encuentra la tetera al fuego añade 200 ml a 20 °C, y las
temperaturas se mezclan en proporción a las masas. La tetera admite 1
litro, cinco porciones; si está llena, los que llegan esperan a que
quede libre. En cuanto el agua llega a 100 °C, todos los de la tetera
reciben su café y la tetera puede usarse de nuevo al instante. El agua
de masa m se calienta P·Δt / (C·m) grados en Δt segundos, con
C = 4190 J/(kg·K). Para cada estudiante hay que imprimir el momento del
café.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N horas de despertar `HH:MM:SS` en orden creciente.

## Salida

N líneas con las horas del café en el mismo formato.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
07:00:00
07:02:00
07:05:30
12:00:00
```

Salida:

```
07:08:23
07:08:23
07:08:23
12:02:48
```

## Solución

Se cuenta el calor que aún falta para hervir:
Q = C · Σ mᵢ · (100 − Tᵢ). La mezcla no cambia Q, porque es lineal en
las masas, y el hornillo lo reduce en P cada segundo. Cada porción
añade C · 0,2 kg · 80 K = 67 040 J, que el hornillo aporta en
exactamente 167,6 s. Así, una tetera puesta en el momento s con k
porciones hierve en s + 167,6 · k, sin importar cuándo se añadieron las
demás porciones.

La simulación guarda los estudiantes de la tetera, una cola de espera y
el momento de hervor. Quien llega antes de ese momento se une a la
tetera y retrasa el hervor 167,6 s, o se pone en la cola si la tetera
está llena. En el momento de hervor, los de la tetera reciben su café,
y hasta cinco de la cola forman la tetera siguiente, que se pone al
fuego enseguida. Todos los tiempos se guardan en milisegundos enteros,
donde 167,6 s son exactamente 167 600, así que no hay ningún error de
redondeo. `O(N)`.

El enunciado deja tres cosas abiertas; las pruebas del juez siguen estas
convenciones, según se cuenta en el foro del problema:

- la respuesta se redondea hacia arriba al segundo: 10:00:00 y 10:00:01
  comparten una tetera que hierve a las 10:05:35,2, y se imprime
  `10:05:36` (prueba 05);
- un estudiante que se despierta justo cuando el agua hierve no se une a
  esa tetera y pone una nueva (prueba 03);
- las horas pasada la medianoche siguen desde `00:00:00` (prueba 04).

Las respuestas se compararon con una simulación que sigue las
temperaturas y las masas con fracciones exactas, como en el enunciado,
en 400 casos aleatorios.

## Notas por lenguaje

- Las cinco soluciones usan la misma simulación entera en milisegundos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1357_simulation.cpp](1357_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.015 s | 208 KB |
| [1357_simulation.go](1357_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.015 s | 1224 KB |
| [1357_simulation.java](1357_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.171 s | 2236 KB |
| [1357_simulation.py](1357_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.078 s | 664 KB |
| [1357_simulation.rs](1357_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 248 KB |
