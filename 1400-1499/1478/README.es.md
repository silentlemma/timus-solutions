# 1478. Satélites espía

[Timus 1478](https://acm.timus.ru/problem.aspx?space=1&num=1478) · dificultad 3896 · dsu

Problema original de Dmitry Ivankov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N objetos están en puntos enteros del plano (coordenadas de hasta 10⁴
en valor absoluto). Se reparten en bases de modo que dentro de cada
base dos objetos cualesquiera estén estrictamente más cerca que
cualquier objeto de esa base de cualquier objeto de otra base. Para
cada prueba hay que escribir una cadena de N cifras cuya k-ésima cifra
es 1 si existe un reparto en exactamente k bases. Las pruebas terminan
con 0; la suma de N es como mucho 5000, la de N² como mucho 400 000 y
la de N³ como mucho 2,5·10⁸.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Pruebas: N y luego N líneas x y; las pruebas se separan con líneas
vacías; 0 termina la entrada.

## Salida

Una cadena de N ceros y unos por prueba.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
-1 -1
1 1
1 -1
-1 1

4
1 0
2 4
1 1
0 1

0
```

Salida:

```
1001
1101
```

## Solución

Un conjunto C es bueno si su diámetro es menor que su distancia al
resto; un reparto es una partición en conjuntos buenos. Dos conjuntos
buenos nunca se cruzan: si x está en ambos, a solo en A y b solo en B,
entonces d(x, b) > diam A ≥ d(x, a) y d(x, a) > diam B ≥ d(x, b).
Además, si C es bueno y t es su distancia al resto, C es una componente
conexa del grafo que une los objetos a menos de t; y a la inversa, esa
componente es buena justo cuando su diámetro es menor que t. Así, los
conjuntos buenos son nodos del árbol de enlace simple: se ejecuta
Kruskal sobre todos los pares por longitud, añadiendo juntos los pares
de igual longitud, y cada componente que aparece tras un grupo es un
nodo cuyos hijos son las componentes que absorbió. Un nodo es bueno si
su diámetro, actualizado con las distancias cruzadas en cada fusión, es
menor que la longitud del grupo que luego lo absorbe; el último nodo
siempre es bueno.

Todo conjunto bueno dentro de un nodo está dentro de uno de sus hijos,
así que las cantidades posibles de un nodo son {1} si es bueno, junto
con todas las sumas que toman una cantidad posible de cada hijo. Esos
conjuntos se guardan como máscaras de bits y se combinan hijo a hijo.
`O(N² log N)` por la ordenación; las fusiones y las sumas cuestan
`O(N²)` y unas N³/64 operaciones de bits.

Detalles a tener en cuenta:

- los pares de igual longitud deben unirse en un solo grupo: a mitad de
  un empate una componente no lo es de ningún grafo por encima, así que
  una cuadrícula de 25 × 25 solo admite 1 o 625 bases (gen4, gen2);
- la desigualdad es estricta: tres objetos con huecos iguales solo se
  reparten en 1 o 3 bases (prueba 02);
- un nodo que no es bueno aún se divide a través de sus hijos: los
  cinco objetos (0, 0), (2, 0), (4, 0), (0, 1), (4, 1) admiten cualquier
  cantidad salvo 2 (prueba 02).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1478_dsu.cpp](1478_dsu.cpp) | G++ 13.2 x64 | dsu | O(N^2 log N) | AC | 0.031 s | 2600 KB |
| [1478_dsu.go](1478_dsu.go) | Go 1.14 x64 | dsu | O(N^2 log N) | AC | 0.093 s | 9804 KB |
| [1478_dsu.java](1478_dsu.java) | Java 1.8 | dsu | O(N^2 log N) | AC | 0.156 s | 7008 KB |
| [1478_dsu.py](1478_dsu.py) | Python 3.12 x64 | dsu | O(N^2 log N) | AC | 0.640 s | 25816 KB |
| [1478_dsu.rs](1478_dsu.rs) | Rust 1.75 x64 | dsu | O(N^2 log N) | AC | 0.031 s | 2012 KB |
