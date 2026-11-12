# 1571. Intérpretes

[Timus 1571](https://acm.timus.ru/problem.aspx?space=1&num=1571) · dificultad 451 · constructive

Problema original de Sergey Pupyrev, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de N ≤ 100 equipos de obra habla un idioma. Un intérprete sabe
dos idiomas cualesquiera. Cada dos equipos deben poder hablar, y ningún
otro equipo debe entender su conversación. Hay que imprimir el menor
número de intérpretes con sus idiomas como `idioma1-idioma2`, o
`Impossible`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego el idioma de cada equipo.

## Salida

El número de intérpretes y sus pares de idiomas, o `Impossible`. Se
acepta cualquier conjunto óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
russian
french
german
```

Salida:

```
3
russian-english
english-german
english-french
```

## Solución

Si dos equipos comparten idioma, un tercer equipo, si lo hay, no puede
hablar con el primero sin que el segundo lo entienda; con solo esos dos
equipos no hace falta nadie. Si no, sean distintos los k idiomas. Un
equipo no necesita a nadie, y dos equipos necesitan un intérprete de
sus dos idiomas.

Para k ≥ 3, una conversación que pasa por el idioma de otro equipo la
oye ese equipo, así que entre cada dos equipos los intérpretes deben
formar una cadena cuyos idiomas interiores no hable ningún equipo. Si
los intérpretes usaran solo los idiomas de los equipos, formarían un
grafo conexo sobre esos k idiomas, y con solo k − 1 aristas sería un
árbol, donde alguna cadena pasa por un tercer idioma. Así que hacen
falta k intérpretes, y k bastan: el idioma de cada equipo emparejado con
un idioma que nadie habla, como english. Si un equipo habla english, el
idioma central es el primer nombre libre de una o dos letras: los
idiomas de la respuesta tampoco pueden pasar de diez letras, y 100
equipos no pueden ocupar los 702 nombres así. `O(N log N)` en C++;
`O(N)` en promedio en los demás lenguajes.

Detalles a tener en cuenta:

- dos equipos de un mismo idioma no necesitan a nadie, pero tres equipos
  con un idioma repetido son imposibles (pruebas 03, 05);
- un equipo puede hablar english, así que el idioma central debe ser uno
  que ningún equipo hable (pruebas 06, 08);
- se aceptan otras respuestas, como un triángulo de pares directos para
  tres equipos, así que un verificador comprueba la privacidad.

## Soluciones optimizadas

Las nuevas versiones C++, Go y Rust ordenan una tabla acotada de hasta 100 nombres de 11 bytes, incluido el terminador cero. Los vecinos iguales detectan duplicados. Para al menos tres equipos distintos, se marcan los nombres de una y dos letras y se elige un centro libre entre 26+26² candidatos: 100 equipos no pueden ocuparlos todos. Conectar cada equipo a ese idioma mantiene la construcción privada y el número óptimo de intérpretes. El almacenamiento acotado sustituye conjuntos, mapas y listas temporales. Ordenar cuesta O(N log N), con nombres de hasta diez letras; no mejora asintóticamente las bases con hash. C++/Rust usan el C runtime, Go manejadores estándar. Se conservan las bases; Java/Python reutilizan las ya admitidas sin duplicarlas.

Las implementaciones base aceptadas [1571_constructive.java](1571_constructive.java), [1571_constructive.py](1571_constructive.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1571_constructive.cpp](1571_constructive.cpp) | G++ 13.2 x64 | constructive | O(N log N) | AC | 0.015 s | 436 KB | 11287792 |
| [1571_constructive.go](1571_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1144 KB | 11287793 |
| [1571_constructive.java](1571_constructive.java) \* | Java 1.8 | constructive | O(N) | AC | 0.156 s | 1712 KB | 11287796 |
| [1571_constructive.py](1571_constructive.py) \* | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 548 KB | 11287794 |
| [1571_constructive.rs](1571_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 456 KB | 11287797 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1571_constructive_sorting.cpp](1571_constructive_sorting.cpp) | G++ 13.2 x64 | constructive, sorting | O(N log N) | AC | 0.015 s | 128 KB | 11315139 |
| [1571_constructive_sorting.go](1571_constructive_sorting.go) \* | Go 1.14 x64 | constructive, sorting | O(N log N) | AC | 0.015 s | 304 KB | 11315142 |
| [1571_constructive_sorting.rs](1571_constructive_sorting.rs) \* | Rust 1.75 x64 | constructive, sorting | O(N log N) | AC | 0.031 s | 48 KB | 11315152 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
