# 1892. Mañana en Koltsovo

[Timus 1892](https://acm.timus.ru/problem.aspx?space=1&num=1892) · dificultad 886 · simulation

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Programar dos colas FIFO para una sola pista: despegues y aterrizajes.
Se conoce cuándo entra cada vuelo en su cola y cada operación empieza
en cuanto se permite. Los intervalos mínimos se miden entre inicios:

| Inicio anterior | Inicio posterior | Intervalo mínimo |
| --- | --- | --- |
| despegue | despegue | t₁ |
| despegue | aterrizaje | t₂ |
| aterrizaje | despegue | t₃ |
| aterrizaje | aterrizaje | t₄ |

No se permite despegar mientras haya vuelos esperando para aterrizar,
aunque un aterrizaje todavía deba esperar por seguridad. Si un vuelo
entra en la cola de aterrizajes justo cuando podría empezar un despegue,
también tiene prioridad. Hallar el inicio de cada operación.

Los límites son 1 segundo y 64 MB.

## Entrada

La primera línea contiene t₁, t₂, t₃ y t₄ en segundos, con
30 ≤ tᵢ ≤ 500 y max(t₁, t₄) ≤ min(t₂, t₃).

Después se indica n, el número de despegues, con 1 ≤ n ≤ 50, seguido
de sus n horas de llegada a la cola. A continuación se indica m, el
número de aterrizajes, con 1 ≤ m ≤ 50, seguido de sus m horas de llegada.

Cada hora tiene formato `hh:mm:ss` y está entre `06:00:00` y `10:00:00`,
inclusive. Cada lista es estrictamente creciente; las horas de las dos
listas distintas pueden coincidir.

## Salida

Escribir los n inicios de despegue y después los m inicios de aterrizaje,
conservando el orden de entrada dentro de cada grupo. Usar `hh:mm:ss`,
con dos dígitos por campo. Los inicios pueden ser posteriores a `10:00:00`.

## Evaluación

Las salidas se comparan como secuencias de tokens.

## Ejemplos

### Ejemplo 1

Entrada:

```
60 60 60 60
2
07:01:00
07:01:30
2
07:00:00
07:02:10
```

Salida:

```
07:01:00
07:02:00
07:00:00
07:03:00
```

## Solución

Convertir las horas a segundos. Mantener un puntero al primer vuelo
sin procesar de cada cola, además del último inicio de despegue D y
de aterrizaje A. Una operación anterior inexistente no impone restricciones.

Para el siguiente despegue, calcular el inicio más temprano que respeta
la seguridad: d = max(su hora de llegada, D + t₁, A + t₃). Comparar d
con la hora a de llegada del siguiente aterrizaje a su cola, no con su
inicio factible. Si a ≤ d, procesar primero ese aterrizaje en
max(a, D + t₂, A + t₄) y actualizar A. En otro caso, procesar el despegue
en d y actualizar D. Si una cola se agota, continuar con la otra usando
las mismas restricciones de seguridad.

La elección es obligatoria. El siguiente despegue no puede empezar
antes de d. Si a ≤ d, ya hay un vuelo esperando para aterrizar cuando
el despegue sería posible, y lo bloquea aunque su propia espera de
seguridad termine más tarde. Si a > d, no hay aterrizajes en cola en d,
por lo que el despegue empieza entonces. Elegida la cola, su primer
vuelo empieza en el máximo de su llegada y los límites de seguridad.
Solo importa el último inicio de cada clase: cualquier inicio anterior
de la misma clase da una cota inferior más débil. Repetir este paso
produce el horario requerido.

Cada paso procesa un vuelo, así que el tiempo es `O(n + m)`. Las listas
de entrada y las respuestas agrupadas ocupan `O(n + m)` memoria.

En el ejemplo, el primer aterrizaje empieza a las `07:00:00`. Los
despegues empiezan a las `07:01:00` y `07:02:00`: el segundo aterrizaje
aún no ha llegado. Entra en su cola a las `07:02:10`, pero el último
despegue retrasa su inicio hasta las `07:03:00`. La salida agrupa los
despegues antes que los aterrizajes, en vez de ordenar las cuatro
operaciones cronológicamente.

Trampas:

- comparar con d la llegada del siguiente aterrizaje, incluida la igualdad;
- un aterrizaje en cola bloquea despegues antes de su propio inicio factible;
- mantener por separado los últimos inicios de despegue y aterrizaje;
- medir los intervalos desde los inicios, no desde las finalizaciones;
- mantener el orden FIFO y escribir los dos grupos en orden de entrada.

Las respuestas coinciden con una simulación segundo a segundo en 179
casos, con una búsqueda exhaustiva en 700 casos pequeños y con una
implementación aceptada independiente en 56 casos generados.

## Notas por lenguaje

Las cinco versiones usan la misma simulación con segundos enteros. C++,
Java y Rust guardan los tiempos en enteros con signo de 32 bits; Go usa
`int` y Python su tipo entero. Bastan para un máximo de 100 operaciones
con intervalos de hasta 500 segundos. El centinela negativo inicial
requiere un tipo con signo.

Python lee tokens de bytes y Java usa entrada por líneas con búfer.
Todas las versiones rellenan los campos del reloj con ceros iniciales y
conservan horas posteriores a la última llegada permitida, sin recortar
la respuesta en `10:00:00`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1892_simulation.cpp](1892_simulation.cpp) | G++ 13.2 x64 | simulation | O(n + m) | AC | 0.015 s | 444 KB |
| [1892_simulation.go](1892_simulation.go) | Go 1.14 x64 | simulation | O(n + m) | AC | 0.031 s | 1148 KB |
| [1892_simulation.java](1892_simulation.java) | Java 1.8 | simulation | O(n + m) | AC | 0.140 s | 540 KB |
| [1892_simulation.py](1892_simulation.py) | Python 3.12 x64 | simulation | O(n + m) | AC | 0.078 s | 612 KB |
| [1892_simulation.rs](1892_simulation.rs) | Rust 1.75 x64 | simulation | O(n + m) | AC | 0.015 s | 248 KB |
