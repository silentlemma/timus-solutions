# 1304. Paralelepípedo

[Timus 1304](https://acm.timus.ru/problem.aspx?space=1&num=1304) · dificultad 1909 · bruteforce

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una caja A tiene vértices (0, 0, 0) y (u, v, w), todos los lados por
debajo de 1000. Dentro hay hasta 50 puntos, y no hay dos en una recta
paralela a una cara de A, así que todas sus x, todas sus y y todas sus
z son distintas. Hay que hallar la caja G más grande con aristas
paralelas a las de A que está dentro de A y no tiene ningún punto
estrictamente dentro (se permiten puntos en su superficie). Se imprime
su volumen redondeado a dos decimales, con las mitades hacia arriba.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

u, v y w; luego n; luego n líneas con las coordenadas de los puntos.
Todos los números tienen como mucho dos decimales.

## Salida

El volumen de G con dos decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
1.0 1.0 1.0
1
0.5 0.5 0.5
```

Salida:

```
0.50
```

## Solución

Cada coordenada se lee como un número entero de centésimas, así que los
volúmenes son enteros exactos en millonésimas y el redondeo final
también es exacto.

Una caja máxima no se puede ensanchar, así que cada una de sus seis
caras está sobre una cara de A o toca un punto. La búsqueda va así:

- las dos caras en x se eligen entre 0, u y las x de los puntos, unos
  52 · 51 / 2 pares;
- solo los puntos estrictamente entre ellas en x pueden frenar la caja;
  llamémoslos P;
- la cara inferior en y está en 0 o en un punto de P;
- la cara superior en y baja desde v. En cada posición, los puntos de P
  estrictamente entre las dos caras en y cortan [0, w] en huecos, y el
  hueco más ancho da la mejor altura.

Cuando la cara superior baja más allá de un punto, ese punto sale de la
capa y los dos huecos alrededor de su z se funden en uno. Una lista
doblemente enlazada sobre las z ordenadas hace cada fusión en tiempo
constante, y el hueco más ancho solo crece. Los puntos con z igual a 0
o a w nunca parten un hueco y se dejan fuera de la lista.

Para un par de caras en x con k puntos entre ellas el trabajo es del
orden de k², y sobre todos los pares suma unos n⁴ / 12, medio millón de
pasos para n = 50. Dos cotas baratas recortan aún más: para cada x1 las
x2 se prueban desde la más ancha, y un par o una cara inferior en y se
descarta en cuanto ni con toda la altura y la profundidad podría
superar la mejor caja hallada.

Detalles a tener en cuenta:

- los puntos en la superficie de A, incluso en un vértice, no recortan
  nada (pruebas 02 y 03);
- un punto puede estar fuera de A; nunca puede estar dentro de G, así
  que se descarta antes de la búsqueda, y si no su x daría a G una cara
  fuera de A (pruebas 09, 10, gen6);
- el redondeo lleva las mitades hacia arriba: un volumen de exactamente
  0.005 se imprime como 0.01 (prueba 07), y un producto en coma
  flotante puede quedar justo por debajo de esa mitad;
- el volumen llega casi a 10⁹, es decir, 10¹⁵ millonésimas, así que
  hacen falta enteros de 64 bits (prueba 06).

Los resultados se compararon con una comprobación directa de todos los
pares de caras en x y en y en 200 entradas aleatorias pequeñas, muchas
con puntos en las caras de A.

## Notas por lenguaje

- Python hace el mismo barrido con diccionarios como lista enlazada y
  tarda unos 0,2–0,3 s con 50 puntos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1304_bruteforce.cpp](1304_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n^4) | AC | 0.031 s | 256 KB |
| [1304_bruteforce.go](1304_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n^4) | AC | 0.062 s | 6564 KB |
| [1304_bruteforce.java](1304_bruteforce.java) | Java 1.8 | bruteforce | O(n^4) | AC | 0.187 s | 7084 KB |
| [1304_bruteforce.py](1304_bruteforce.py) | Python 3.12 x64 | bruteforce | O(n^4) | AC | 0.468 s | 832 KB |
| [1304_bruteforce.rs](1304_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(n^4) | AC | 0.046 s | 364 KB |
