# 1510. Orden

[Timus 1510](https://acm.timus.ru/problem.aspx?space=1&num=1510) · dificultad 87 · greedy

Problema original de Den Raskovalov, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N billetes (1 ≤ N ≤ 500000) de valores entre 0 y 10⁹, y más de la
mitad tienen el mismo valor. Hay que escribir ese valor.

Límite de tiempo: 1 segundo. Límite de memoria: 16 MB.

## Entrada

N y luego los N valores, uno por línea.

## Salida

El valor de la mayoría.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
3
3
2
2
3
```

Salida:

```
3
```

## Solución

Votación de Boyer–Moore: se guardan un candidato y un contador. Un
billete igual al candidato sube el contador, cualquier otro lo baja, y
cuando el contador vale cero el siguiente billete pasa a ser el
candidato. Cada bajada cancela un billete del candidato con otro
billete; la mayoría tiene más billetes que todos los demás juntos, así
que no puede cancelarse del todo y es el candidato al final. `O(N)` de
tiempo y `O(1)` de memoria.

Detalles a tener en cuenta:

- 16 MB es poco: guardar todos los billetes, y en Python incluso leer
  toda la entrada de golpe y partirla, ocupa unos 29 MB, así que todas
  las soluciones leen los billetes de uno en uno;
- la mayoría puede venir después de todos los demás billetes (prueba
  03, gen2) o alternarse con ellos (prueba 04);
- el valor de la mayoría puede ser 0 (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1510_greedy.cpp](1510_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.437 s | 136 KB |
| [1510_greedy.go](1510_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.093 s | 6024 KB |
| [1510_greedy.java](1510_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.265 s | 488 KB |
| [1510_greedy.py](1510_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.375 s | 444 KB |
| [1510_greedy.rs](1510_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.109 s | 232 KB |
