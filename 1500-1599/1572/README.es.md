# 1572. El Gran Pozo de Yekaterinozavodsk

[Timus 1572](https://acm.timus.ru/problem.aspx?space=1&num=1572) · dificultad 146 · geometry

Problema original de Alexander Ipatov y Alex Samsonov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La boca de un pozo y hasta 100 tapas de alcantarilla son cada una un
círculo (tipo 1, tamaño = radio), un cuadrado (tipo 2) o un triángulo
equilátero (tipo 3, tamaño = lado), con tamaños enteros 1 … 100. Una
tapa plana se puede girar y mover en el espacio de cualquier manera. Hay
que contar las tapas que se pueden echar al pozo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El tipo y el tamaño del pozo, y luego N (1 ≤ N ≤ 100) y el tipo y el
tamaño de cada tapa.

## Salida

El número de tapas que caben.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 10
3
3 20
1 5
2 11
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
1 5
2
2 10
1 6
```

Salida:

```
1
```

## Solución

Una tapa puesta de canto y empujada hacia abajo corta el plano de la
boca a lo largo de cuerdas paralelas de sí misma, así que pasa cuando,
en alguna dirección, su cuerda más larga cabe en la boca. La mejor
dirección da para un círculo el diámetro 2r, para un cuadrado el lado a
y para un triángulo la altura a·√3/2 (las cuerdas paralelas a una
altura). La boca admite segmentos hasta el más largo suyo: el diámetro
del círculo 2R, la diagonal del cuadrado A·√2 y el lado del triángulo A.

Elevadas al cuadrado y multiplicadas por 4, todas estas longitudes son
enteras: 16r², 4a² y 3a² para las tapas, 16R², 8A² y 4A² para el pozo,
así que la comparación es exacta y una tapa que justo toca los bordes
pasa. `O(N)`. Las respuestas coinciden con un programa independiente
para cada par de pozo y tapa de cualquier forma y tamaño.

Detalles a tener en cuenta:

- el tamaño de un círculo es su radio, no su diámetro;
- un triángulo pasa por su altura, no por su lado, así que un triángulo
  de lado 16 aún entra en un pozo cuadrado de lado 10 (prueba 06);
- los tamaños iguales pasan: un cuadrado de lado 10 pasa por un círculo
  de radio 5 (el segundo ejemplo), así que las comparaciones en coma
  flotante requieren cuidado.

## Soluciones optimizadas

`1572_geometry_optimized.py` se reutiliza byte por byte. Su Accepted exacto en CPython 3.12 #11325457 registra 0.078 s / 720 KB; la comparación guardada de compiladores actuales de la familia Python del 2026-11-20 da tiempo 4/28 y memoria 18/28. Bajo 1024 KB la admisión estricta solo considera tiempo, por lo que cumple los diez primeros. Conserva el asterisco: la meta propia del lenguaje exige primer puesto en ambas métricas. El mismo fuente intacto tiene también Accepted PyPy 3.10 #11325701, 0.14 s / 264 KB: usa menos memoria, mientras la ejecución CPython elegida tiene menor tiempo registrado. Son pares medidos en ejecuciones distintas, sin combinarlos. No se necesita otro fuente, algoritmo ni envío; se conservan todas las versiones didácticas.

`1572_geometry_optimized.py`. Conserva comparación exacta de cuerdas cuadradas por NARROWEST/WIDEST, incluida igualdad. Lee, compara cuadrado escalado y descarta cada tapa, sin lista. O(n) tiempo y estado geométrico constante más buffers. Vacía respuesta antes de salir del intérprete; conserva derivación sencilla.

Frente a `1572_geometry.py`: CPython seleccionado, tiempo 0.093 s → 0.078 s; memoria 384 KB → 720 KB. El tiempo baja 16.13%, pero la memoria sube 87.5%; se admite por puesto temporal, no por mejora del 30%. Arriba se conserva la medición anterior PyPy de 0.14 s / 264 KB como alternativa de memoria.

`1572_geometry_optimized.rs`. Conserva comparación exacta de cuerdas cuadradas mediante factores NARROWEST/WIDEST, incluida igualdad. Lee cada tapa, compara cuadrado escalado u64 y descarta, sin vector completo. Salida directa sustituye formato. O(n) tiempo y O(1) espacio auxiliar; conserva derivación geométrica y fuente básica.

Frente a `1572_geometry.rs`: tiempo 0.031 s → 0.046 s; memoria 228 KB → 60 KB.

La solución optimizada en Java analiza los números a mano desde un búfer
de 4 KB que se llena desde `System.in`, en lugar de crear un `Scanner`,
así que la JVM no carga el escáner ni sus expresiones regulares; la
comparación de las longitudes al cuadrado es la misma:
{1572_geometry_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y cumple la regla aplicable de clasificación o mejora. El registro Python elegido cumple por puesto temporal; las reducciones Java de abajo corresponden a sus propios pares medidos. Se conservan las bases. Una reducción negativa indica mayor coste; el asterisco solo expresa la meta de clasificación propia del lenguaje.

- `1572_geometry_optimized.java`: reducción de tiempo +44.29%; reducción
  de memoria +80.86%; base: `1572_geometry.java`.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1572_geometry_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1572_geometry.cpp](1572_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 128 KB | 11287799 |
| [1572_geometry.go](1572_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1072 KB | 11287801 |
| [1572_geometry.java](1572_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.140 s | 1776 KB | 11287805 |
| [1572_geometry.py](1572_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 384 KB | 11287803 |
| [1572_geometry.rs](1572_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 228 KB | 11287810 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1572_geometry_optimized.java](1572_geometry_optimized.java) | Java 1.8 | geometry | O(N) | AC | 0.078 s | 340 KB | 11304529 |
| [1572_geometry_optimized.rs](1572_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n) time; O(1) space | AC | 0.046 s | 60 KB | 11325506 |
| [1572_geometry_optimized.py](1572_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(n) time; O(1) state plus bounded token buffers | AC | 0.078 s | 720 KB | 11325457 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
