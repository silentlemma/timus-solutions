# 2020. Vaciar Dos Colas de Tráfico Opuestas

[Timus 2020](https://acm.timus.ru/problem.aspx?space=1&num=2020) · dificultad 162 · simulation

Problema original de Denis Dublennykh, preparado por Nick Burlakov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos colas llegan a un cruce desde direcciones opuestas, sur y norte.
Cada coche sigue recto (`F`), gira a la izquierda (`L`) o a la derecha
(`R`). Las colas se dan del coche más cercano al más lejano, sin
adelantamientos; cada cruce tarda un segundo. Un giro a la izquierda
cede al primer coche contrario si sigue recto o gira a la derecha. Dos
giros a la izquierda pueden pasar juntos, al igual que dos maniobras sin
giro a la izquierda. En cada segundo pasan todos los primeros coches
autorizados; sus sucesores actúan desde el segundo siguiente. No llegan
más coches. Determine cuándo se vacían ambas colas.

Cada cola inicial tiene entre 1 y 1 000 coches. Límites: 1 segundo y 64 MB.

## Entrada

La primera línea describe la cola del sur; la segunda, la del norte.
Ambas usan solo `F`, `L`, `R` y empiezan por el coche más próximo.

## Salida

Imprima el tiempo total en segundos hasta que hayan pasado todos los coches.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
RLF
FF
```

```
4
```

```
L
L
```

```
1
```

## Solución

Mantenga índices `i`, `j` de los primeros coches pendientes y un contador.
Mientras ambas colas tengan coches, lea **ambas cabezas antiguas** `a`, `b`.
El coche sur avanza si `a != L` o `b == L`; el norte avanza si `b != L` o
`a == L`. Calcule las dos condiciones antes de cambiar cualquier índice.
Avance los autorizados y añada un segundo.

| Cabeza sur | Cabeza norte | Quién cruza |
| --- | --- | --- |
| `L` | `F` o `R` | solo norte |
| `F` o `R` | `L` | solo sur |
| `L` | `L` | ambos |
| `F` o `R` | `F` o `R` | ambos |

Al vaciarse una cola, no quedan oponentes que bloqueen la otra. Cada coche
restante tarda un segundo; añada el número total de coches pendientes.

El invariante afirma que tras `t` segundos simulados los índices son
exactamente los coches que ya pasaron de cada cola. Inicialmente son cero.
La tabla reproduce toda la regla de prioridad para las dos cabezas actuales.
Actualizarlas desde el mismo estado anterior reproduce el segundo siguiente
y conserva el invariante. Al terminar una cola, cada coche restante puede
salir en su próximo segundo, así que sumar la cola residual es exacto.
Por tanto el contador final es el tiempo pedido.

Siempre pasa al menos un coche: uno que gira a la izquierda espera al otro
sin giro izquierdo, o pasan ambos. Para longitudes iniciales `s`, `t`,
el tiempo es `O(s+t)`, con estado auxiliar `O(1)` y espacio `O(s+t)`
incluyendo las cadenas. La respuesta está entre `max(s,t)` y `s+t`, hasta 2 000.

En el primer ejemplo, el primer segundo pasan sur `R` y norte `F`.
En el segundo, sur `L` espera al siguiente norte `F`. Después sur `L` y
sur `F` emplean los segundos tercero y cuarto. En el segundo ejemplo ambos
giros izquierdos pasan durante un solo segundo.

Trampas:

- Decidir ambas salidas antes de avanzar: una cabeza recién expuesta
  actúa el segundo siguiente.
- El giro izquierdo también cede a un giro derecho, no solo a quien sigue recto.
- Dos giros izquierdos opuestos se realizan simultáneamente.
- Incluir el tiempo de la cola residual cuando termina la otra.

## Soluciones optimizadas

La solución optimizada en C++ lee las dos colas con `scanf` en arreglos
globales de `char` de 1001 bytes, ya que una cola tiene como mucho 1000
coches, en lugar de `std::string` leídos mediante `iostream`; las
recorre hasta sus ceros finales e imprime con `printf`:
{2020_simulation_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `2020_simulation_optimized.cpp`: reducción de tiempo +0.00%; reducción
  de memoria +72.63%; base: `2020_simulation.cpp`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [2020_simulation.py](2020_simulation.py).
- [2020_simulation.rs](2020_simulation.rs).

Las cinco versiones recorren las cadenas con dos índices. Python suma
valores booleanos; las demás los convierten o incrementan condicionalmente.
Los enteros ordinarios bastan para el resultado.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2020_simulation.cpp](2020_simulation.cpp) | G++ 13.2 x64 | simulation | O(s + t) | AC | 0.015 s | 380 KB | 11292679 |
| [2020_simulation.go](2020_simulation.go) | Go 1.14 x64 | simulation | O(s + t) | AC | 0.031 s | 1116 KB | 11292686 |
| [2020_simulation.java](2020_simulation.java) | Java 1.8 | simulation | O(s + t) | AC | 0.093 s | 444 KB | 11307207 |
| [2020_simulation.py](2020_simulation.py) | Python 3.12 x64 | simulation | O(s + t) | AC | 0.062 s | 424 KB | 11292688 |
| [2020_simulation.rs](2020_simulation.rs) | Rust 1.75 x64 | simulation | O(s + t) | AC | 0.015 s | 228 KB | 11292699 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2020_simulation_optimized.cpp](2020_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(s + t) | AC | 0.015 s | 104 KB | 11307208 |
