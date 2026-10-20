# 2139. El zumo que queda en un polígono que gira con un agujero en un lado

[Timus 2139](https://acm.timus.ru/problem.aspx?space=1&num=2139) · dificultad 3641 · geometry, binary_search

Problema original de Vadim Barinov, del Concurso de Programación por Equipos de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

A un polígono convexo lleno de zumo se le hace un agujero en un punto H
de un lado, así que todo lo que está por encima de la horizontal que
pasa por H se derrama. Después se gira lentamente alrededor del origen
por q ángulos dados, uno tras otro. Imprimir la cantidad de zumo que
queda tras hacer el agujero y tras cada giro, con error absoluto o
relativo a lo sumo 10⁻⁴. Los límites son 4 segundos y 256 MB.

## Entrada

n, 3 ≤ n ≤ 10⁵, los vértices en sentido antihorario, el agujero, luego
q, 0 ≤ q ≤ 10⁵, y los ángulos en grados, −360 ≤ αᵢ ≤ 360; coordenadas y
ángulos tienen exactamente tres decimales y las coordenadas son a lo
sumo 10⁵ en valor absoluto.

## Salida

q + 1 áreas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
-2.000 1.000
1.000 -2.000
4.000 1.000
1.000 1.000
4
45.000
45.000
45.000
45.000
```

Salida:

```
9.000000000
6.750000000
4.500000000
2.250000000
0.000000000
```

## Solución

Girar alrededor del origen mueve el agujero junto con el polígono, así
que solo importa el ángulo total θ girado hasta el momento. La capacidad
c(θ) es el área del polígono por debajo de la horizontal por H en ese
ángulo, y el zumo que queda es la menor capacidad vista durante el giro
lento.

Al cambiar θ, esa recta gira alrededor de H, un punto del borde. Uno de
sus dos rayos desde H sale del polígono enseguida, así que la región por
debajo solo gana área por un lado o solo la pierde, y c(θ) es monótona
entre dos ángulos especiales: cuando el lado de H está horizontal con el
polígono encima (c = 0, el agujero abajo) y cuando está horizontal con el
polígono debajo (c es el área entera). Así que en la circunferencia c
sube de 0 al área completa y vuelve a bajar. Si el ángulo total pasa
alguna vez por un ángulo con el agujero abajo, todo se derrama para
siempre. Si no, el ángulo girado se queda dentro de un arco entre dos
ángulos así, donde c sube y luego baja, así que el mínimo de cualquier
giro está en sus extremos y la respuesta es min(respuesta anterior, c(θ)).

Para calcular c(θ) se guardan los vértices empezando junto al agujero,
con coordenadas enteras exactas en milésimas relativas a H, y sumas
prefijas de los términos de la fórmula del área. Los vértices a un lado
de la recta por H forman un arco de esa lista, así que una búsqueda
binaria sobre las alturas con signo halla la arista por la que sale la
recta, y el área de abajo es un prefijo o sufijo del abanico desde H
más una fracción de un triángulo. Cada giro cuesta O(log n).

En el ejemplo el triángulo empieza con área 9; cada giro de 45° baja el
nivel respecto al polígono, y tras el cuarto el agujero queda abajo y no
queda nada.

## Notas por lenguaje

Para imprimir las mismas cifras en todos los lenguajes, los programas
calculan el seno y el coseno con el mismo polinomio y el mismo orden de
operaciones en lugar de las funciones de biblioteca.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2139_geometry_binary_search.cpp](2139_geometry_binary_search.cpp) | G++ 13.2 x64 | geometry, binary_search | O(n + q log n) | AC | 0.140 s | 2320 KB |
| [2139_geometry_binary_search.go](2139_geometry_binary_search.go) | Go 1.14 x64 | geometry, binary_search | O(n + q log n) | AC | 0.062 s | 13544 KB |
| [2139_geometry_binary_search.java](2139_geometry_binary_search.java) | Java 1.8 | geometry, binary_search | O(n + q log n) | AC | 0.312 s | 16468 KB |
| [2139_geometry_binary_search.py](2139_geometry_binary_search.py) | Python 3.12 x64 | geometry, binary_search | O(n + q log n) | AC | 1.734 s | 51704 KB |
| [2139_geometry_binary_search.rs](2139_geometry_binary_search.rs) | Rust 1.75 x64 | geometry, binary_search | O(n + q log n) | AC | 0.062 s | 12684 KB |
