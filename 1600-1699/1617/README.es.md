# 1617. Planos en las ruedas

[Timus 1617](https://acm.timus.ru/problem.aspx?space=1&num=1617) · dificultad 65 · implementation

Problema original de Vladimir Yakovlev, del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un depósito tiene n pares de ruedas (1 ≤ n ≤ 150), cada uno con un
diámetro entero de 600 a 700 mm. Un vagón de tranvía necesita cuatro
pares de ruedas del mismo diámetro. ¿Cuántos vagones se pueden equipar?

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

n, luego los n diámetros.

## Salida

El número de vagones.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
9
689
690
690
689
689
690
689
688
688
```

Salida:

```
1
```

## Solución

Contamos los pares de cada diámetro. Un diámetro con c pares equipa
⌊c / 4⌋ vagones, y los diámetros no interactúan, así que la respuesta es
la suma sobre todos ellos. `O(n)`.

Detalles a tener en cuenta:

- los pares sobrantes de diámetros distintos no se pueden combinar
  (prueba 01);
- ocho pares de un mismo tamaño equipan dos vagones, no uno (prueba 03).

## Soluciones optimizadas

`1617_implementation_optimized.py`. Conserva 101 frecuencias de diámetros 600..700 y suma floor(frequency/4). Lee binario directamente y escribe respuesta corta completa con os.write antes de os._exit(0). split retiene tokens: O(I+101) espacio, I bytes de entrada, sin streaming de espacio constante. O(N+101) operaciones, procesa todos los pares declarados. Conserva Counter didáctico.

Accepted exacto Python 3.12 x64 #11327789: 0.062 s / 660 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/104, memoria 90/104. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11325072 era 0.125 s / 244 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1617_implementation_optimized.py`: 0.062 s / 660 KB; base didáctica conservada `1617_implementation.py`: 0.093 s / 368 KB.

`1617_implementation_optimized.java`. Agrupa en una pasada diámetros 600..700. Un byte guarda resto módulo cuatro; al llegar a cuatro reinicia y cuenta vagón. Entre lecturas queda como máximo tres, cabe en byte con signo; sin pasada final de frecuencias. O(N) tiempo y 101 bytes de grupos. Consume todos los campos numéricos usados antes de emitir. Reutiliza un arreglo de 256 bytes primero para entrada y luego salida, reservando doce bytes por int con signo y revirtiendo solo los dígitos nuevos. Elimina arreglos separados sin sobrescribir datos aún necesarios. Análisis/salida lineales en bytes consumidos, búfer fijo.

Accepted exacto Java 1.8 #11327764: 0.078 s / 368 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/221, memoria 6/221. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303764 era 0.109 s / 336 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1617_implementation_optimized.java`: 0.078 s / 368 KB; base didáctica conservada `1617_implementation.java`: 0.14 s / 1680 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1617_implementation.cpp](1617_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11288341 |
| [1617_implementation.go](1617_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1092 KB | 11288342 |
| [1617_implementation.java](1617_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1680 KB | 11288344 |
| [1617_implementation.py](1617_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 368 KB | 11288343 |
| [1617_implementation.rs](1617_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 240 KB | 11303771 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1617_implementation_optimized.java](1617_implementation_optimized.java) | Java 1.8 | implementation | O(N) time; 101 byte remainders | AC | 0.078 s | 368 KB | 11327764 |
| [1617_implementation_optimized.py](1617_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N+101) time; O(I+101) storage | AC | 0.062 s | 660 KB | 11327789 |
