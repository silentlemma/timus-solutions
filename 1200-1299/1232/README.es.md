# 1232. Aterrizar una sonda dentro de un cono

[Timus 1232](https://acm.timus.ru/problem.aspx?space=1&num=1232) · dificultad 2375 · geometry

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una estación flota a altura h sobre un asteroide plano, en el eje z. Una
sonda sale de la estación y se mueve en tramos rectos de longitud exacta
d; cada tramo debe bajarla, y todo el camino debe quedar dentro del cono
de ángulo α en el vértice bajo la estación, donde llegan sus señales. El
último tramo también debe medir d y terminar en la superficie. Hay que
encontrar un camino con el menor número de tramos o decir que aterrizar
es imposible.

Límites: 0.5 ≤ h ≤ 99.9999, 1 ≤ d ≤ 5, 0.1 ≤ α ≤ 2 (radianes), todos con
como mucho cuatro decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

h, d y α.

## Salida

El número de tramos n, o -1 si no se puede aterrizar; después los n
puntos donde terminan los tramos, como `x y z`, el último en la
superficie. Las coordenadas necesitan precisión 0.0001.

## Evaluación

El camino no es único, así que se acepta cualquier camino válido con el
menor número de tramos. Nuestro verificador compara n con la respuesta
esperada y comprueba la longitud de cada tramo, que baje, que cada punto
esté dentro del cono y que el último esté en la superficie, todo con
margen 0.0001.

## Ejemplos

### Ejemplo 1

Entrada:

```
11 5 2
```

Salida:

```
3
0 3 7
3 3 3
3 -1 0
```

## Solución

**Cuántos tramos.** Un tramo baja como mucho d, así que hacen falta al
menos `n = ⌈h/d⌉` tramos, y n basta siempre que se pueda aterrizar: si
aterriza un camino más largo, sus primeros n tramos terminan
estrictamente por encima de la superficie, y como las profundidades
alcanzables con n tramos forman un intervalo hasta `n·d`, la profundidad
h también se alcanza con n. Así que la respuesta es n o -1.

**Construir el camino.** Todo el trabajo está en perder la altura
sobrante: con L tramos por delante, `extra = z − (L−1)·d` está en
`(0, d]`, y en cuanto un tramo baja exactamente `extra`, los demás van
recto hacia abajo. Un tramo puede hacerlo si `extra` es al menos la
bajada mínima disponible desde el punto actual. Desde un punto de la
pared del cono a profundidad t bajo la estación, donde el cono mide
`w = 2t·tan(α/2)` de ancho, esa bajada mínima es 0 si `w ≥ d` (el tramo
puede ser casi horizontal), y si no la da el tramo que cruza hasta la
pared opuesta:

```text
bajada = (√(d²(1 + tan²) − w²) − w·tan) / (1 + tan²),  tan = tan(α/2)
```

Mientras la altura sobrante no se pueda perder en un tramo, el camino,
dentro del plano y = 0, hace el tramo que menos baja, cruzando hasta la
pared opuesta, de modo que el siguiente tramo vuelve a salir de una
pared.

**Cuándo falla la codicia.** Cruzar con la máxima inclinación no siempre
es lo mejor. Un punto más hondo de la pared ve un cono más ancho, y
mientras allí el cono mide un poco menos de d, empezar más hondo puede
dejar un final más alto tras el siguiente cruce. Por eso el programa
prueba también caminos cuyos primeros j tramos bajan deslizándose por la
pared antes de empezar el zigzag, para j = 0, 1, …, n, e imprime el
primero que aterriza. j = 0 es el zigzag voraz simple; en la prueba 05
(α = 0.496, d = 1, h = 2.01) acaba bajo la superficie, mientras que dos
deslizamientos y un cruce aterrizan. `O(n²)` con n ≤ 100.

Detalles a tener en cuenta:

- el primer tramo sale del vértice del cono, así que incluso el más
  inclinado baja `d·cos(α/2)`; si h es menor, no se puede aterrizar
  (pruebas 02, 06, 10);
- `⌈h/d⌉` necesita una pequeña tolerancia, o con h múltiplo de d
  (prueba 04) sale un tramo de más.

Nuestro verificador acepta estos caminos; además, las respuestas (n o -1)
se compararon con una búsqueda exhaustiva por profundidad y distancia al
eje en una malla fina, para ángulos en todo el rango, justo por encima y
justo por debajo de cada umbral donde aterrizar se vuelve posible, y
coincidieron en todos los casos. Es una comprobación numérica, no una
demostración de que deslizar y luego hacer zigzag siempre baste.

## Notas por lenguaje

- Todos los lenguajes hacen la misma simulación con la misma tolerancia e
  imprimen seis decimales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1232_geometry.cpp](1232_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.015 s | 220 KB |
| [1232_geometry.go](1232_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.015 s | 1164 KB |
| [1232_geometry.java](1232_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.125 s | 1636 KB |
| [1232_geometry.py](1232_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.078 s | 688 KB |
| [1232_geometry.rs](1232_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.031 s | 256 KB |
