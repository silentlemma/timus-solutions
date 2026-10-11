# 1323. Compañeros de clase

[Timus 1323](https://acm.timus.ru/problem.aspx?space=1&num=1323) · dificultad 831 · bitmask

Problema original con idea de Evgeny Kobzev, preparado por Pavel Atnashev y Alexander Mironenko, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una clase de N ≤ 10 estudiantes tiene M pares que pueden llamarse por
teléfono, en cualquier sentido, y así la noticia puede llegar a todos.
Al principio solo la persona delegada de la clase conoce la noticia. Una
llamada dura exactamente un minuto, y en un minuto cada estudiante que
ya la conoce puede hacer una llamada. Hay que planear las llamadas para
que todos reciban la noticia exactamente una vez, lo antes posible.

Límite de tiempo: 1,5 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego M, luego M líneas con dos nombres cada una, y luego el nombre
de la persona delegada. Los nombres son distintos y tienen hasta 20
letras latinas.

## Salida

El número de minutos y, para cada minuto, el número de llamadas hechas
en él seguido de esas llamadas, una por línea con el nombre de quien
llama y el de quien recibe la llamada. Se acepta cualquier plan óptimo.

## Comprobación

El comprobador compara el número de minutos con el mínimo y luego
reproduce el plan: cada llamada debe usar un par de la entrada, quien
llama debe conocer la noticia desde antes de ese minuto, nadie puede
llamar dos veces en un minuto ni recibir dos llamadas en total, y al
final todos deben conocerla.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
7
Tanya Lena
Tanya Katya
Tanya Masha
Lena Natasha
Lena Vitya
Natasha Vitya
Masha Vitya
Tanya
```

Salida:

```
3
1
Tanya Lena
2
Tanya Masha
Lena Vitya
2
Vitya Natasha
Tanya Katya
```

## Solución

Lo que puede pasar después depende solo de quién conoce ya la noticia,
así que el estado es un conjunto de estudiantes, como mucho 2¹⁰. Desde
un conjunto S, un minuto puede añadir cualquier conjunto T de
estudiantes fuera de S si a cada estudiante de T se le puede asignar en
S una persona distinta que pueda llamarle. Es un emparejamiento
bipartito de T en S, que se halla con caminos de aumento. Una búsqueda
en anchura sobre los conjuntos, probando cada subconjunto T de los
vecinos de S que no saben la noticia, llega a la clase entera en el
menor número de minutos. Guardando el conjunto y el emparejamiento que
llevaron a cada estado se obtiene el plan.

Solo se alcanzan conjuntos que contienen a la persona delegada, y los
subconjuntos T del resto suman como mucho 3⁹ pares (S, T), cada uno con
un emparejamiento sobre diez personas como mucho.

Detalles a tener en cuenta:

- con un solo estudiante la respuesta es 0 y no hay grupos (prueba 02);
- el plan empieza por la persona delegada, cuyo nombre puede ir segundo
  en un par (prueba 03);
- los pares pueden aparecer en los dos sentidos (prueba 07);
- llamar primero a quien está más cerca no siempre es lo mejor: hay que
  llegar antes a la rama que tiene más gente detrás (prueba 08).

Los tiempos mínimos se compararon con una búsqueda en la que cada
estudiante informado llama cada minuto a cualquier vecino o a nadie, en
300 clases aleatorias de hasta 7 estudiantes, y cada plan se reprodujo
con el comprobador.

## Notas por lenguaje

- Las cinco soluciones hacen la misma búsqueda con el mismo
  emparejamiento.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1323_bitmask.cpp](1323_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(3^N·N²) | AC | 0.015 s | 476 KB |
| [1323_bitmask.go](1323_bitmask.go) | Go 1.14 x64 | bitmask | O(3^N·N²) | AC | 0.031 s | 2636 KB |
| [1323_bitmask.java](1323_bitmask.java) | Java 1.8 | bitmask | O(3^N·N²) | AC | 0.109 s | 1596 KB |
| [1323_bitmask.py](1323_bitmask.py) | Python 3.12 x64 | bitmask | O(3^N·N²) | AC | 0.171 s | 912 KB |
| [1323_bitmask.rs](1323_bitmask.rs) | Rust 1.75 x64 | bitmask | O(3^N·N²) | AC | 0.031 s | 480 KB |
