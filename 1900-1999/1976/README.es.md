# 1976. Distancias al cuadrado a la base más cercana

[Timus 1976](https://acm.timus.ru/problem.aspx?space=1&num=1976) · dificultad 1295 · geometry

Problema original de Idea by Ilya Bushkov, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Algunas celdas de una cuadrícula rectangular tienen bases en su centro.
Los centros adyacentes distan una unidad. Para cada celda, calcular el
cuadrado de su distancia euclídea a la base más cercana. Las celdas vacías
no son obstáculos ni restringen movimientos. Límites: 2 segundos y 64 MB.

BFS con cuatro vecinos calcula distancia Manhattan: para desplazamiento
(1,1), su cuadrado sería 4 en lugar de 2. Ocho vecinos tampoco dan el
cuadrado euclídeo exacto. Omitir columnas inalcanzables, aplicar techo
con signo, eliminar candidatas con comienzos iguales y conservar los
índices originales de columna.

## Entrada

La primera línea contiene n y m, 1≤n,m≤1000. Después aparecen n filas
de m celdas binarias: 1 indica una base y 0 una celda vacía.
Se garantiza al menos una base y una celda vacía.

## Salida

Imprimir n filas de m enteros. En (r,c), escribir el mínimo de
(r−a)²+(c−b)² sobre todas las bases (a,b), separando los números de
cada fila con un espacio. Una base tiene respuesta cero; no extraer raíces.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3 4
1000
0000
0010
```

```
0 1 4 5
1 2 1 2
4 1 0 1
```

## Solución

### Separar las coordenadas

Fijar la fila destino r y una columna de base q. Sea v[q] la menor
distancia vertical |r−a| a una base (a,q). Un barrido descendente obtiene
la base más cercana por arriba; otro ascendente incorpora las bases
inferiores. Las columnas sin bases permanecen inalcanzables.

Para la columna destino x, buscar el mínimo de v[q]²+(x−q)² sobre q
alcanzables. Con q fijo, el término horizontal es constante: la base
verticalmente más cercana también minimiza el coste completo de esa
columna. Minimizar después sobre q contempla todas las bases.

Se usa far=n+m como separador. Una distancia vertical real no supera
n−1. Una columna sin bases conserva un valor al menos far tras ambos
barridos y se omite en la envolvente. Aunque una fila esté vacía, siempre
existe alguna columna alcanzable porque hay una base en el mapa.

### Envolvente inferior entera de parábolas

Para una columna alcanzable, definir f[q]=v[q]² y
Pq(x)=(x−q)²+f[q]. Todas tienen el mismo coeficiente cuadrático.
Para p<q, la parábola nueva no supera a la anterior exactamente cuando

2(q−p)x ≥ f[q]+q²−f[p]−p².

La primera coordenada entera de cambio es

ceil((f[q]+q²−f[p]−p²)/(2(q−p))).

No hacen falta intersecciones flotantes ni epsilon. Redondear hacia
infinito positivo incluso si el numerador es negativo; la división
truncada habitual no reemplaza esta fórmula en todos los casos.

Guardar una pila de columnas candidatas y la primera coordenada entera
no negativa donde cada una pasa a ser preferible. Procesar q en orden
creciente. Calcular su cambio con la última candidata. Si ocurre antes
o al comienzo del intervalo de esa candidata, ésta ya no conserva un
intervalo óptimo: eliminarla y volver a comparar. Añadir q con el comienzo
obtenido; si la pila queda vacía, su comienzo es cero. En empate, elegir
la parábola nueva sin modificar el valor de la respuesta.

Al restar el término común x² quedan rectas con pendientes −2q
estrictamente decrecientes. La envolvente inferior las visita en orden
creciente de q. Una candidata cubierta antes de empezar ya no puede
ser óptima; eliminarla y comparar las nuevas vecinas conserva exactamente
la envolvente en x≥0.

Recorrer x=0…m−1 y avanzar un puntero cuando se alcanza el comienzo
de la siguiente candidata. Los comienzos son estrictamente crecientes;
el puntero nunca retrocede y siempre selecciona un mínimo.

### Corrección y complejidad

Los barridos verticales calculan exactamente todos los v[q] finitos.
La envolvente y su puntero devuelven minq Pq(x). Por la separación de
coordenadas, esto coincide con la menor distancia al cuadrado a cualquier
base. Así son correctas todas las celdas, incluidas bases, empates,
filas vacías y columnas vacías.

Cada candidata entra y sale de la pila a lo sumo una vez; el puntero
avanza como máximo m veces por fila. El tiempo total es `O(nm)` y la
memoria total `O(nm)`, incluida la tabla vertical y la entrada. La
envolvente de una fila usa `O(m)` adicional. La propia salida tiene nm
valores.

En el ejemplo, las bases tienen coordenadas desde cero (0,0) y (2,2).
Desde (0,3), las distancias al cuadrado son 9 y 5: se imprime 5.
En (1,1) ambas son 2. Desde (2,1), la segunda base está a una unidad,
de modo que se imprime 1. El cálculo completo produce las tres filas mostradas.

## Notas por lenguaje

Las cinco versiones usan la misma envolvente exacta. Python guarda las
distancias verticales como listas de filas para indexarlas directamente.
Antes de barrer detecta las columnas
con bases y deja las demás inalcanzables. Si todas las distancias verticales
de una fila son como máximo uno, ya alcanzan la cota inferior entera:
cero en bases y uno en celdas vacías. Python las devuelve directamente;
las demás filas usan la envolvente completa. Las versiones compiladas usan
arrays enteros. C++ y Go implementan el techo con signo; Java emplea
Math.floorDiv y Rust div_euclid con negación. La salida se almacena por
filas, sin acumular cadenas para toda la matriz. Java reutiliza el constructor
de fila y el búfer de caracteres sin crear un nuevo String de salida por fila.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1976_geometry.cpp](1976_geometry.cpp) | G++ 13.2 x64 | geometry | O(n*m) | AC | 0.203 s | 3884 KB |
| [1976_geometry.go](1976_geometry.go) | Go 1.14 x64 | geometry | O(n*m) | AC | 0.125 s | 18608 KB |
| [1976_geometry.java](1976_geometry.java) | Java 1.8 | geometry | O(n*m) | AC | 0.296 s | 8196 KB |
| [1976_geometry.py](1976_geometry.py) | Python 3.12 x64 | geometry | O(n*m) | AC | 1.859 s | 33996 KB |
| [1976_geometry.rs](1976_geometry.rs) | Rust 1.75 x64 | geometry | O(n*m) | AC | 0.140 s | 6028 KB |
