# 1067. Un árbol de carpetas reconstruido a partir de rutas completas

[Timus 1067](https://acm.timus.ru/problem.aspx?space=1&num=1067) · dificultad 363 · trees, sorting

Problema original del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan `N` rutas de carpetas distintas (`1 ≤ N ≤ 500`), de hasta 80
caracteres cada una, con los nombres de carpeta separados por barras
invertidas. Un nombre tiene de 1 a 8 caracteres: letras mayúsculas,
dígitos y los caracteres especiales ``!#$%&'()-@^_`{}~``. Imprime el árbol
de carpetas: cada carpeta en su propia línea, sangrada con un espacio por
nivel, con las subcarpetas de cada carpeta justo después de ella y las
carpetas de cada nivel en orden lexicográfico.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con las rutas.

## Salida

El árbol, una carpeta por línea.

## Evaluación

La salida debe ser igual al texto esperado; solo se ignoran los espacios
en blanco del final. Los espacios iniciales forman parte de la respuesta.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
WINNT\SYSTEM32\CONFIG
GAMES
WINNT\DRIVERS
HOME
WIN\SOFT
GAMES\DRIVERS
WINNT\SYSTEM32\CERTSRV\CERTCO~1\X86
```

Salida:

```
GAMES
 DRIVERS
HOME
WIN
 SOFT
WINNT
 DRIVERS
 SYSTEM32
  CERTSRV
   CERTCO~1
    X86
  CONFIG
```

## Solución

Cada ruta se coloca en un árbol de carpetas: se baja desde la raíz por los
nombres de la ruta y se crean las carpetas que faltan. Después, un
recorrido en profundidad imprime cada carpeta con tantos espacios como su
profundidad, visitando las subcarpetas en orden. Con un mapa ordenado en
cada carpeta el orden sale solo. `O(L log N)` para la longitud total `L` de
las rutas.

Detalles a tener en cuenta:

- ordenar las rutas completas como cadenas no basta: la barra invertida
  está en medio de la tabla de códigos, después de las mayúsculas y los
  dígitos pero antes de `^`, `_`, `` ` ``, `{`, `}` y `~`, así que `A!`
  quedaría entre `A` y `A\X`; los nombres hay que compararlos nivel por
  nivel;
- una carpeta en medio de una ruta puede no aparecer nunca sola, y nombres
  iguales bajo padres distintos son carpetas distintas;
- las rutas no tienen espacios, así que se pueden leer como tokens
  separados por espacios en blanco, lo que además ignora los retornos de
  carro.

Las respuestas se comprobaron ordenando todos los prefijos de todas las
rutas como tuplas de nombres: así cada carpeta queda justo antes de todo
su subárbol.

## Notas por lenguaje

- C++, Java y Rust guardan las subcarpetas en un mapa ordenado
  (`std::map`, `TreeMap`, `BTreeMap`); Go y Python guardan una tabla hash
  y ordenan sus claves al imprimir.
- Todos los lenguajes comparan los nombres por códigos de carácter, que es
  el orden que pide el problema para estos caracteres.
- Java divide una ruta con la expresión regular `\\`, una sola barra
  invertida escapada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1067_trees_sorting.cpp](1067_trees_sorting.cpp) | G++ 13.2 x64 | trees, sorting | O(L log N) | AC | 0.015 s | 3472 KB |
| [1067_trees_sorting.go](1067_trees_sorting.go) | Go 1.14 x64 | trees, sorting | O(L log N) | AC | 0.015 s | 8376 KB |
| [1067_trees_sorting.java](1067_trees_sorting.java) | Java 1.8 | trees, sorting | O(L log N) | AC | 0.093 s | 7380 KB |
| [1067_trees_sorting.py](1067_trees_sorting.py) | Python 3.12 x64 | trees, sorting | O(L log N) | AC | 0.078 s | 6692 KB |
| [1067_trees_sorting.rs](1067_trees_sorting.rs) | Rust 1.75 x64 | trees, sorting | O(L log N) | AC | 0.031 s | 12116 KB |
