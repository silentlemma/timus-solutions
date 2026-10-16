# 1790. En busca de la Verdad

[Timus 1790](https://acm.timus.ru/problem.aspx?space=1&num=1790) · dificultad 1335 · simulation

Problema original de Mikhail Rubinchik, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un artefacto está sobre uno de n pedestales en fila. En cada turno se
toca un pedestal: si el artefacto está allí se encuentra; si no, pasa a
un pedestal vecino a su elección. Dada una secuencia de m toques,
decidir si siempre encuentra el artefacto, sea cual sea su inicio y sus
movimientos.

## Entrada

n y m (2 ≤ n, m ≤ 100000), luego m números de pedestal de 1 a n.

## Salida

"YES" si la secuencia siempre encuentra el artefacto; si no, "NO".

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
2 2
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
3 3
1 2 3
```

Salida:

```
NO
```

## Solución

Se sigue el conjunto de pedestales donde aún puede estar el artefacto.
Cada movimiento cambia la paridad de su pedestal, así que el conjunto
se divide en una parte par y una impar, y cada parte es siempre un
tramo lo, lo + 2, …, hi de una paridad sin huecos. Tocar un extremo de
un tramo lo acorta en un lugar. Tocar dentro de un tramo deja un hueco,
pero tras el movimiento los dos vecinos del hueco se alcanzan desde los
lugares a dos pasos, así que nada cambia. Un movimiento convierte el
tramo lo…hi en lo − 1…hi + 1 de la otra paridad, salvo que un tramo que
toca la pared en 1 o n se empuja hacia dentro: 1 pasa a 2 y n a n − 1.
La respuesta es YES cuando ambos tramos están vacíos al final.
`O(n + m)`.

En el segundo ejemplo un artefacto que empieza en 2 se escapa: el
toque de 1 falla y va a 3; el toque de 2 falla y vuelve a 2; el toque
de 3 falla de nuevo.

Trampas:

- un conjunto de hasta 100000 pedestales durante 100000 turnos es
  demasiado lento de seguir lugar por lugar, de ahí los dos tramos;
- un toque estrictamente dentro de un tramo se desperdicia, no deja un
  hueco permanente;
- en una pared el tramo no crece más allá de ella, sino que retrocede
  hacia dentro.

Las respuestas coinciden con una simulación directa de todo el conjunto
en 400 secuencias cortas aleatorias sobre pocos pedestales, y con una
implementación aceptada independiente en barridos largos, barridos
estropeados y secuencias aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1790_simulation.cpp](1790_simulation.cpp) | G++ 13.2 x64 | simulation | O(n + m) | AC | 0.062 s | 128 KB |
| [1790_simulation.go](1790_simulation.go) | Go 1.14 x64 | simulation | O(n + m) | AC | 0.031 s | 1544 KB |
| [1790_simulation.java](1790_simulation.java) | Java 1.8 | simulation | O(n + m) | AC | 0.125 s | 4592 KB |
| [1790_simulation.py](1790_simulation.py) | Python 3.12 x64 | simulation | O(n + m) | AC | 0.140 s | 7036 KB |
| [1790_simulation.rs](1790_simulation.rs) | Rust 1.75 x64 | simulation | O(n + m) | AC | 0.031 s | 2128 KB |
