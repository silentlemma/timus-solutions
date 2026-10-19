# 1956. Una recta con distancia total mínima

[Timus 1956](https://acm.timus.ru/problem.aspx?space=1&num=1956) · difficulty 2303 · geometry

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Pavel Klimov (prepared by Olga Soboleva).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Trasladar n puntos del plano a una misma recta infinita minimizando la
suma de distancias euclídeas recorridas. Se eligen libremente la recta y
las posiciones finales. Puede haber puntos repetidos. Límites: 1 s, 64 MB.

## Entrada

Primero n, 2≤n≤1000, seguido de n pares de coordenadas enteras x,y,
cada una entre −10⁶ y 10⁶, inclusive.

## Salida

Un número real: la distancia total mínima. Error absoluto o relativo
máximo 10⁻⁶. Los programas imprimen doce decimales.

## Evaluación

La respuesta se compara con error absoluto o relativo 10⁻⁶.

## Ejemplos

```
4
0 0
0 1
1 1
1 0
```

```
1.414214
```

## Solución

Para una recta fija, cada punto se mueve a su proyección ortogonal.
Fijada la dirección, las proyecciones sobre la normal unitaria tienen
suma de desviaciones absolutas mínima en una mediana. Por tanto, se
puede elegir una recta óptima de esa dirección que pase por un punto P;
con n par, sirve un extremo del intervalo de medianas.

Fijamos P y giramos la recta. Entre direcciones hacia otras posiciones
distintas, los productos cruzados mantienen sus signos. El coste es
A cos θ+B sin θ≥0 y su segunda derivada es su propio negativo. Si los
puntos no son colineales, es positivo y estrictamente cóncavo: el mínimo
de cada intervalo está en un extremo. Existe así un óptimo global que
pasa por dos posiciones distintas. Si todas coinciden, la respuesta es cero.

Evaluar cada pareja recorriendo todos los puntos cuesta O(n³). Para cada
pivote P formamos v=Q−P, omitimos ceros e invertimos el vector si y<0,
o si y=0 y x<0. Quedan en el semiplano y≥0 con el rayo horizontal
positivo. Invertir no cambia el valor absoluto del producto cruzado.

Ordenamos por k=−x/(|x|+y), estrictamente creciente con el ángulo en [0,π).
R comienza como la suma de los vectores normalizados. En la dirección d,
los pendientes tienen cross(d,v)≥0 y los ya pasados ≤0. Así cross(d,R)
es la suma de productos absolutos y el coste es cross(d,R)/sqrt(d.x²+d.y²).
Tras cada evento v restamos 2v a R. Los colineales aportan cero: no hace
falta agrupar empates. Una pareja se evalúa solo en su índice menor.

Python agrupa posiciones repetidas con Counter: una multiplicidad w
aporta wv y después resta 2wv. Los demás lenguajes guardan las repeticiones
explícitas. Ambos cuentan cada punto. Tiempo O(n² log n), espacio O(n).

### Aritmética exacta y detalles

Cada componente de dirección tiene valor absoluto ≤2·10⁶ y cada denominador
de clave ≤4·10⁶. Claves racionales distintas se separan al menos
1/(4·10⁶)², mucho más que el redondeo binary64 en [−1,1]. Fracciones
iguales redondean igual; no se necesita epsilon ni atan2.

Las componentes de R son menores que 2·10⁹ en valor absoluto; cada producto
es menor que 4·10¹⁵ y la diferencia menor que 8·10¹⁵. Las versiones nativas
usan enteros con signo de 64 bits. Python usa vectores binary64 de valor
entero: productos bajo 2⁵² y resultado entero bajo 2⁵³ hacen exactas estas
operaciones. La norma al cuadrado es ≤8·10¹² y también exacta. Solo raíz
y división redondean, con margen suficiente para 10⁻⁶. No minimizar
distancias al cuadrado, perder multiplicidades, dividir por un vector
nulo o considerar solo ejes. Si todo es colineal, la respuesta es cero.

## Notas por lenguaje

C++ y Rust reutilizan un vector, Go 1.14 usa sort.Slice y Java 8
reutiliza sus objetos de dirección en lugar de crear uno por par. Python
usa Counter, actualizaciones duplicadas precalculadas e itemgetter como
clave de ordenación. Se ejecuta con PyPy: con CPython 3.12 supera el
límite de tiempo en la prueba 49 del juez, mientras que con PyPy 3.10 se
acepta en 0.843 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1956_geometry.cpp](1956_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^2 log n) | AC | 0.046 s | 552 KB |
| [1956_geometry.go](1956_geometry.go) | Go 1.14 x64 | geometry | O(n^2 log n) | AC | 0.218 s | 1300 KB |
| [1956_geometry.java](1956_geometry.java) | Java 1.8 | geometry | O(n^2 log n) | AC | 0.296 s | 4040 KB |
| [1956_geometry.py](1956_geometry.py) | PyPy 3.10 x64 | geometry | O(n^2 log n) | AC | 0.843 s | 11748 KB |
| [1956_geometry.rs](1956_geometry.rs) | Rust 1.75 x64 | geometry | O(n^2 log n) | AC | 0.031 s | 280 KB |
