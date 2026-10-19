# 2095. Contar los días que conserva una criba repetida

[Timus 2095](https://acm.timus.ru/problem.aspx?space=1&num=2095) · dificultad 277 · math

Problema original de Dmitry Ivankov, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los días se numeran 1, 2, 3, … Cada segundo día es de informe; de los
que quedan, cada tercero es de informe; de los que quedan, cada cuarto,
y así para siempre. Los días que nunca se quitan son tranquilos. Contar
los días tranquilos de [l; r]. Los límites son 1 segundo y 64 MB.

## Entrada

l y r, 1 ≤ l ≤ r ≤ 10⁹.

## Salida

El número de días tranquilos de l a r.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 10
```

Salida:

```
3
```

## Solución

Sea f(n) el número de días tranquilos entre los n primeros. Las
eliminaciones siempre toman posiciones de la lista de días restantes,
así que entre los c primeros días restantes el paso k quita exactamente
⌊c / k⌋, y los días restantes entre los n primeros siguen siendo un
prefijo de la lista. Por tanto f(n) se obtiene con c ← c − ⌊c / k⌋ para
k = 2, 3, … mientras c ≥ k; cuando c < k ningún paso posterior toca el
prefijo. El número c decrece más o menos como n / k, así que el bucle
acaba tras unos 2√(n/π) pasos, unos 3.6·10⁴ para 10⁹. La respuesta es
f(r) − f(l − 1).

En el ejemplo f(10): 10 → 5 → 4 → 3, y los días tranquilos son 1, 3
y 7.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2095_math.cpp](2095_math.cpp) | G++ 13.2 x64 | math | O(sqrt r) | AC | 0.015 s | 132 KB |
| [2095_math.go](2095_math.go) | Go 1.14 x64 | math | O(sqrt r) | AC | 0.031 s | 1076 KB |
| [2095_math.java](2095_math.java) | Java 1.8 | math | O(sqrt r) | AC | 0.125 s | 1584 KB |
| [2095_math.py](2095_math.py) | Python 3.12 x64 | math | O(sqrt r) | AC | 0.078 s | 368 KB |
| [2095_math.rs](2095_math.rs) | Rust 1.75 x64 | math | O(sqrt r) | AC | 0.015 s | 220 KB |
