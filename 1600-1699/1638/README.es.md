# 1638. Ratón de biblioteca

[Timus 1638](https://acm.timus.ru/problem.aspx?space=1&num=1638) · dificultad 66 · math

Problema original de Alex Samsonov, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cien tomos están en una estantería, juntos y en orden creciente de
izquierda a derecha. Cada tomo tiene páginas de un grosor total dado y
dos tapas de un grosor dado. Un gusano empieza en la primera página de
un tomo y roe en línea recta hasta llegar a la última página de otro
tomo. ¿Qué longitud tiene su camino?

## Entrada

Cuatro enteros positivos hasta 100: el grosor de las páginas de un tomo,
el grosor de una tapa, el tomo donde empieza el gusano y el tomo donde
se detiene.

## Salida

La longitud del camino.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 1 1 2
```

Salida:

```
2
```

## Solución

El truco está en dónde quedan las páginas. Un libro colocado en la
estantería con el lomo hacia fuera tiene la primera página a la derecha
y la última a la izquierda, así que la primera página del tomo a toca la
tapa que mira al tomo a + 1, y la última página del tomo b toca la tapa
que mira al tomo b − 1. Con w = páginas + 2 · tapa para un tomo entero:

- a < b: solo la tapa derecha de a, los tomos intermedios y la tapa
  izquierda de b: 2 · cover + (b − a − 1) · w; el ejemplo da 2;
- a > b: el gusano atraviesa además todas las páginas de ambos tomos:
  2 · pages + 2 · cover + (a − b − 1) · w;
- a = b: solo las páginas de ese tomo.

`O(1)`.

Detalles a tener en cuenta:

- la respuesta intuitiva para los tomos 1 y 2 es un libro entero o dos,
  pero el gusano solo atraviesa las dos tapas (el ejemplo);
- en sentido contrario el camino es mucho más largo (prueba 02).

Las respuestas coinciden con una implementación aceptada independiente
en 200 pruebas aleatorias.

## Soluciones optimizadas

`1638_math_optimized.java`. Java mantiene los tres casos de orientación de los libros. Con whole=pages+2*cover, avanzar atraviesa 2*cover+(stop-start-1)*whole; retroceder, 2*pages+2*cover+(start-stop-1)*whole; dentro del mismo volumen, pages. Un búfer de entrada de 256 bytes y otro de salida directa de 128 bytes evitan Scanner y el formato general de cadenas. Los límites permiten aritmética int; tiempo y espacio auxiliar O(1). Todos los pares de volúmenes inicial y final, en las cuatro combinaciones extremas de grosores, se verificaron con coordenadas absolutas de páginas: 40000 comparaciones.

Accepted exacto Java 1.8 #11327466: 0.109 s / 368 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 33/359, memoria 2/359. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303627 era 0.14 s / 380 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1638_math_optimized.java`: 0.109 s / 368 KB; base didáctica conservada `1638_math.java`: 0.125 s / 1616 KB.

Multiplicar la distancia entre índices por el grosor completo y ajustar el resultado por un bloque de páginas según la dirección. El envío aceptado 11324252 tardó 0.140 s y usó 228 KB. La versión sencilla tardó 0.078 s y usó 364 KB. El tiempo registrado es mayor que el de la versión sencilla.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1638_math.cpp](1638_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11288456 |
| [1638_math.go](1638_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1060 KB | 11288457 |
| [1638_math.java](1638_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1616 KB | 11288459 |
| [1638_math.py](1638_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 364 KB | 11288458 |
| [1638_math.rs](1638_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB | 11303473 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1638_math_optimized.java](1638_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.109 s | 368 KB | 11327466 |
| [1638_math_optimized.py](1638_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.140 s | 228 KB | 11324252 |

\* Accepted; aún no alcanza la meta de clasificación separada: C++ requiere los diez primeros o el 15% superior tanto en tiempo como en memoria; las demás familias de lenguajes requieren el primer puesto en ambas. Esta marca es independiente de los criterios de admisión; la versión admite más optimización.
