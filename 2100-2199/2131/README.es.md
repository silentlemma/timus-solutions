# 2131. La subcadena más corta de todos los nombres marcados y de ningún otro, a lo largo del tiempo

[Timus 2131](https://acm.timus.ru/problem.aspx?space=1&num=2131) · dificultad 4459 · suffix_structures

Problema original de Mikhail Rubinchik, preparado por Alexander Kulkov, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los nombres de equipos aparecen uno a uno en una clasificación; algunos
están marcados con "+" como equipos del entrenador, y el primer nombre es
el favorito, marcado. Tras cada nombre nuevo, hallar la cadena más corta
que aparece en todos los nombres marcados presentes y en ningún nombre
no marcado presente, impresa como las posiciones l … r de una aparición
en el nombre favorito; entre las más cortas, la de menor l, e imprimir
"−1 −1" si no hay ninguna. Los límites son 2 segundos y 256 MB.

## Entrada

n, y luego los n nombres distintos en orden de aparición, con letras
minúsculas y "_", con un "+" tras los marcados; la longitud total es a
lo sumo 2 · 10⁵.

## Salida

l y r, o −1 −1, tras cada nombre.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
mit_kotiki+
sjtu_koty+
itmo_first
msu_koshki
mipt_alot
spbsu_kot
```

Salida:

```
0 0
2 2
4 4
5 6
4 6
-1 -1
```

## Solución

Todo candidato es una subcadena del favorito. Una subcadena es válida
desde el principio hasta uno de dos momentos: aparece el primer nombre
no marcado que la contiene, o el primer nombre marcado que no la
contiene. Así que cada subcadena tiene un momento de caducidad, y la
respuesta tras el nombre t es la mejor subcadena que caduca después de t.

Un autómata de sufijos de todos los nombres juntos agrupa las
subcadenas en estados cuyas cadenas aparecen exactamente en los mismos
nombres. Para cada estado se recoge, por su subárbol de enlaces de
sufijo:

- la primera posición final en el favorito, si aparece allí;
- el primer nombre no marcado que la contiene;
- el conjunto de nombres marcados que la contienen, fundiendo el menor
  en el mayor, y su menor elemento ausente, que solo crece hacia la
  raíz.

La mejor cadena de un estado es la más corta, de longitud una más que la
de su enlace de sufijo, terminando en la primera posición del favorito.
Se guarda bajo el momento de caducidad del estado, se toman mínimos de
sufijo sobre los momentos y se lee la respuesta de cada momento. El
trabajo es O(S log S) para la longitud total S, dominado por las fusiones
de conjuntos.

En el ejemplo la primera respuesta es una sola letra, "m", el comienzo
del favorito; al llegar "itmo_first" la opción más corta pasa a ser la
"k" de la posición 4, luego "ot" y "kot", y en cuanto aparece
"spbsu_kot" ya no sirve nada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2131_suffix_structures.cpp](2131_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(S log S) | AC | 0.343 s | 80288 KB |
| [2131_suffix_structures.go](2131_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(S log S) | AC | 0.328 s | 110800 KB |
| [2131_suffix_structures.java](2131_suffix_structures.java) | Java 1.8 | suffix_structures | O(S log S) | AC | 0.421 s | 93620 KB |
| [2131_suffix_structures.py](2131_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(S log S) | AC | 1.609 s | 148908 KB |
| [2131_suffix_structures.rs](2131_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(S log S) | AC | 0.218 s | 73324 KB |
