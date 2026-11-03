# 1645. Carrera de esquí

[Timus 1645](https://acm.timus.ru/problem.aspx?space=1&num=1645) · dificultad 200 · fenwick

Problema original de Eugene Kurpilyansky y Alexey Samsonov, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los esquiadores 1 a n salen uno tras otro con 30 segundos de diferencia,
y la clasificación final los ordena por su propio tiempo. Solo se conoce
el orden de llegada. Para cada esquiador hay que hallar el mejor y el
peor puesto que puede ocupar.

## Entrada

n (1 ≤ n ≤ 2000) y luego los esquiadores en el orden de llegada.

## Salida

Para cada esquiador i, el mejor y el peor puesto posibles.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
3 5 1 4 2 6
```

Salida:

```
3 6
4 6
1 4
2 5
1 3
1 6
```

## Solución

Los números indican el orden de salida, con intervalos de 30 segundos.
Respecto de `i`, quien sale después pero llega antes es necesariamente más
rápido; quien sale antes pero llega después es necesariamente más lento.
Los otros órdenes permiten ambas comparaciones. El mejor puesto es
`1 + forzosamente_más_rápidos`; el peor, `n − forzosamente_más_lentos`.

Ambas cotas son alcanzables simultáneamente para todos los rivales
indeterminados del esquiador elegido. Para su mejor puesto, agrupa todas
las llegadas anteriores justo antes de la suya en menos de 30 segundos,
y aleja las posteriores más de `30n` segundos. Quienes salieron y llegaron
antes tardarán más; quienes salieron y llegaron después también. Para su
peor puesto, adelanta las llegadas anteriores más de `30n` segundos y agrupa
las posteriores justo después, en menos de 30 segundos. Todos los rivales
indeterminados serán más rápidos. Conserva el orden estricto de cada grupo
y suma una constante grande a todas las llegadas para obtener duraciones
positivas, que se pueden elegir distintas. Se construye por separado para
cada esquiador y cota; no se exige que todos alcancen extremos en una misma carrera.

Sean `p=place[i]` y `e` quienes salieron y llegaron antes. Hay `p−1−e`
forzosamente más rápidos e `i−1−e` más lentos; las respuestas son `p−e`
y `n−i+e+1`.

Procesa por orden de salida. Un árbol Fenwick contiene exactamente las
posiciones de llegada de los que salieron antes. Su prefijo hasta `p−1`
da `e`; imprime ambas cotas e inserta `p` después. El invariante y la
inducción prueban cuentas y respuestas. Tiempo `O(n log n)`, espacio `O(n)`;
con `n≤2000` los contadores e índices caben en enteros de máquina. Llegar
en orden de salida permite todos los puestos; el orden inverso los fija.

## Evaluación

Se comparan dos tokens enteros por esquiador en orden de salida.
Las fórmulas se validaron con 10078 construcciones exactas de tiempos:
ambas cotas de cada objetivo en todas las permutaciones hasta seis personas,
con duraciones positivas distintas y el orden de llegada correcto. Se
comprueba alcanzabilidad, no solo condiciones necesarias por parejas.
Por separado, los programas C++/Rust reales reformateados pasaron cada uno
996 entradas extra contra cuentas directas: las 873 permutaciones hasta
seis personas, 120 carreras aleatorias y tres máximas. Cada uno pasó además
13 entradas del repositorio en Docker y tiene Accepted de sus bytes exactos.
Las construcciones son comprobaciones matemáticas, no 10078 ejecuciones
de cada programa nativo.

## Notas por lenguaje

Se conserva el mismo algoritmo Fenwick en los cinco lenguajes. C++ y
Rust solo cambian por la salida exacta del formateador, cada uno con nuevo
Accepted y sus propias mediciones. Los bytes originales se guardan en la
copia local de la revisión. Go, Java y Python coinciden byte por byte con
el archivo Accepted. No se llama optimización al formato ni se crean duplicados.

La instantánea guardada del 2 de noviembre de 2026 cumple la meta acordada
para todas las bases actuales: C++ en el 15% superior o los primeros diez
puestos de ambas métricas; otras familias, primero en ambas. Una muestra
filtrada vacía solo ofrece cobertura formal, no superioridad. Los candidatos
didácticos más sencillos por parejas siguen pendientes del juez y no se
incluyen como Accepted.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1645_fenwick.cpp](1645_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n) | AC | 0.015 s | 184 KB | 11308415 |
| [1645_fenwick.go](1645_fenwick.go) | Go 1.14 x64 | fenwick | O(n log n) | AC | 0.031 s | 1176 KB | 11288492 |
| [1645_fenwick.java](1645_fenwick.java) | Java 1.8 | fenwick | O(n log n) | AC | 0.093 s | 652 KB | 11288494 |
| [1645_fenwick.py](1645_fenwick.py) | Python 3.12 x64 | fenwick | O(n log n) | AC | 0.093 s | 852 KB | 11288493 |
| [1645_fenwick.rs](1645_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n log n) | AC | 0.046 s | 268 KB | 11308416 |
