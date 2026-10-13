# 1461. La guirnalda de Año Nuevo

[Timus 1461](https://acm.timus.ru/problem.aspx?space=1&num=1461) · dificultad 987 · greedy

Problema original de Alexander Toropov, con agradecimiento especial a Dmitry Ivankov, del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una guirnalda de longitud N (2 ≤ N ≤ 100000) es una línea quebrada de
(0, 0) a (N, 0) cuyos tramos avanzan una unidad a la derecha y suben
(u), bajan (d) o siguen rectos (h). Ningún vértice puede quedar por
debajo del eje x, y no puede haber dos vértices consecutivos sobre él.
Todas las guirnaldas están listadas como cadenas en orden lexicográfico.
Dada una guirnalda, hay que imprimir la siguiente de la lista, o «No
solution» si es la última.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego la guirnalda como cadena de u, d y h.

## Salida

La siguiente guirnalda o «No solution».

## Ejemplos

### Ejemplo 1

Entrada:

```
6
uhduhd
```

Salida:

```
uhhdud
```

## Solución

Un tramo horizontal sobre el eje pondría dos vértices seguidos en él,
así que la regla es: nunca por debajo del eje y ninguna h sobre él. El
orden de las letras es d < h < u. Si una guirnalda aún puede terminarse
desde la altura y con r tramos restantes tiene respuesta sencilla: desde
el eje el siguiente tramo debe subir, así que r es 0 o al menos 2; por
encima del eje los tramos horizontales rellenan cualquier sobrante, así
que basta r ≥ y.

Como siempre para la siguiente cadena en orden lexicográfico, se busca
la última posición cuya letra puede subirse, a h o a u, de modo que el
prefijo siga siendo válido y la guirnalda aún pueda terminarse; se
conserva todo lo anterior y el resto se rellena con las letras más
pequeñas que mantengan posible el final, probando d, luego h y luego u
en cada paso. Si ninguna posición puede subirse, la guirnalda es la
última. `O(N)`.

Detalles a tener en cuenta:

- h nunca se permite sobre el eje, así que desde el eje solo se puede
  subir, y el resto tras la letra subida no siempre empieza abajo
  (pruebas 03, 05);
- la última guirnalda, que sube todo lo que puede, no tiene siguiente
  (pruebas 02, 04, 06, gen2, gen3);
- las longitudes impares necesitan un tramo horizontal en algún punto
  por encima del eje (pruebas 05, 07, 09).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1461_greedy.cpp](1461_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.031 s | 916 KB |
| [1461_greedy.go](1461_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 3260 KB |
| [1461_greedy.java](1461_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.093 s | 4648 KB |
| [1461_greedy.py](1461_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.218 s | 6648 KB |
| [1461_greedy.rs](1461_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.046 s | 1244 KB |
