# 1785. Perdidos en la localización

[Timus 1785](https://acm.timus.ru/problem.aspx?space=1&num=1785) · dificultad 16 · implementation

Problema original del folclore, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un juego nombra el tamaño de un ejército con una palabra en lugar de un
número: 1–4 es "few", 5–9 "several", 10–19 "pack", 20–49 "lots", 50–99
"horde", 100–249 "throng", 250–499 "swarm", 500–999 "zounds", y 1000 o
más "legion". Imprimir la palabra para un número dado de monstruos.

## Entrada

n (1 ≤ n ≤ 2000).

## Salida

La palabra para n.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
```

Salida:

```
several
```

### Ejemplo 2

Entrada:

```
40
```

Salida:

```
lots
```

## Solución

Se guardan los extremos inferiores de los rangos de mayor a menor,
1000, 500, 250, 100, 50, 20, 10, 5, 1, junto a sus palabras. Se saltan
los extremos mayores que n; el primero que no lo es da la palabra.
`O(1)`.

En los ejemplos 7 pasa de 1000 hasta 10 y se detiene en 5, "several";
40 se detiene en 20, "lots".

Trampas:

- los extremos pertenecen a la palabra mayor: 5 es "several", 1000 es
  "legion";
- todo n de 1000 a 2000 es "legion".

Las respuestas coinciden con una implementación aceptada independiente
en cada n de 1 a 2000.

## Soluciones optimizadas

`1785_implementation_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327034 mide 0.078 s / 704 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 18/582, memoria 494/582. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11325075, 0.14 s / 196 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

`1785_implementation_optimized.go`. Conserva los nueve intervalos de nombres con iguales límites inferiores inclusivos. Usa condiciones descendentes en vez de arreglos paralelos e índice; elige la primera válida, incluidas fronteras5,10,20,50,100,250,500,1000. No introduce ordenación ni búsqueda general. Dominio1..2000 y nueve casos fijos dan O(1) tiempo y estado, con idénticas palabras. os.Stdin.Read/os.Stdout.Write portables y conversión entera directa usan búferes fijos de entrada y salida de 4096 bytes. Se atienden escrituras parciales antes de reutilizar el búfer de salida. Se conserva la fuente sencilla original con Accepted.

Frente a `1785_implementation.go`: tiempo 0.031 s → 0.015 s; memoria 1080 KB → 820 KB.

`1785_implementation_optimized.py`. Conserva los nueve intervalos de nombres con iguales límites inferiores inclusivos. Usa condiciones descendentes en vez de arreglos paralelos e índice; elige la primera válida, incluidas fronteras5,10,20,50,100,250,500,1000. No introduce ordenación ni búsqueda general. Dominio1..2000 y nueve casos fijos dan O(1) tiempo y estado, con idénticas palabras. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1785_implementation.py`: tiempo 0.093 s → 0.14 s; memoria 424 KB → 196 KB.

La solución optimizada en C++ busca la palabra en la misma tabla, pero
lee con `scanf` e imprime con `puts` en lugar de `iostream`: 116 KB en
lugar de 376 KB, con el mismo tiempo.

La solución optimizada en Java analiza los números byte a byte desde
`System.in` en lugar de usar `Scanner`: 0.093 s en lugar de 0.125 s y
340 KB en lugar de 1600 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1785_implementation_optimized.go`: puesto de tiempo 1/21 y de memoria 1/21 en esta muestra comparable.

Comparación PyPy anterior: `1785_implementation_optimized.py`: puesto de tiempo 566/582 y de memoria 2/582 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1785_implementation.cpp](1785_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 376 KB | 11303506 |
| [1785_implementation.go](1785_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1080 KB | 11289797 |
| [1785_implementation.java](1785_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1600 KB | 11303507 |
| [1785_implementation.py](1785_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 424 KB | 11289798 |
| [1785_implementation.rs](1785_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 228 KB | 11289801 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1785_implementation_optimized.cpp](1785_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303636 |
| [1785_implementation_optimized.java](1785_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 340 KB | 11303777 |
| [1785_implementation_optimized.go](1785_implementation_optimized.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 820 KB | 11328304 |
| [1785_implementation_optimized.py](1785_implementation_optimized.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 704 KB | 11327034 |
