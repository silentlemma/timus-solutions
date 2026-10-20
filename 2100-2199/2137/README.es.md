# 2137. Extender una cadena binaria para maximizar los periodos de sus bordes

[Timus 2137](https://acm.timus.ru/problem.aspx?space=1&num=2137) · dificultad 6004 · dp, strings

Problema original de Alexey Kotelnikov y idea by Mikhail Rubinchik y special thanks to Vladislav Isenbaev, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un borde de una cadena es un prefijo propio no vacío que también es
sufijo. La complejidad de una cadena es el número de periodos distintos
entre sus bordes, y su complejidad dinámica es la suma de las
complejidades de todos sus prefijos. Para una cadena binaria S y cada i
de 1 a 25, hallar la mayor complejidad dinámica de una cadena S + T con
|T| = i. Los límites son 2 segundos y 64 MB.

## Entrada

S, 0 ≤ |S| ≤ 10⁵, sobre los caracteres "X" y ".".

## Salida

25 números, las respuestas para i = 1 … 25.

## Ejemplos

### Ejemplo 1

Entrada:

```
X.X
```

Salida:

```
2
4
5
7
9
12
14
16
19
21
23
26
30
32
35
38
41
45
47
50
54
58
62
67
70
```

## Solución

Los bordes de un prefijo son su borde más largo π, el borde más largo de
ese, y así sucesivamente: la cadena de la función de prefijos. El
periodo de un borde b es b − π(b), y a lo largo de la cadena los
periodos iguales vienen en tramos. Así que con rank(0) = 0 y
rank(b) = rank(π(b)) + [el periodo de b difiere del de π(b)], la
complejidad de un prefijo con borde más largo π es rank(π). Añadir un
carácter actualiza π, el periodo y el rank en O(1) amortizado, y quitar
caracteres de nuevo es un simple truncado.

Los prefijos de S aportan una cantidad fija, así que hay que elegir T
para maximizar la suma de rank(π) sobre los prefijos nuevos. La primera
mitad de T, una docena de caracteres, se enumera por completo con esa
rutina de añadir y deshacer. Para el resto de T el siguiente borde más
largo solo depende del actual y del carácter siguiente, y quedan dos
casos.

- El borde más largo es más corto que el texto ya construido: está en
  texto conocido, así que el siguiente borde sigue el autómata KMP de
  ese texto con transiciones para ambos caracteres. Una DP sobre los
  estados del autómata guarda el mejor total para cada estado alcanzable
  y cada longitud extra.
- El borde más largo es al menos tan largo como el texto construido:
  entonces la cadena tiene un periodo corto p, no mayor que los
  caracteres que quedan. Mantener ese borde significa repetir el
  periodo, lo que se simula directamente para cada p así a lo largo de
  la cadena de bordes. Romper el periodo en algún paso baja el borde al
  texto conocido, y ese estado entra en la DP como un nuevo comienzo.

El mejor valor visto para cada longitud es la respuesta. La enumeración
completa de la primera mitad y el número acotado de estados alcanzables
mantienen el trabajo dentro de los límites; las cinco soluciones
coinciden con una implementación aceptada independiente en cadenas
aleatorias y periódicas.

En el ejemplo "X.X" se extiende con "." con complejidad 2: el prefijo
"X.X." tiene el borde "X." de periodo 2, y el propio "X.X" aporta el
borde "X".

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2137_dp_strings.cpp](2137_dp_strings.cpp) | G++ 13.2 x64 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.031 s | 2976 KB |
| [2137_dp_strings.go](2137_dp_strings.go) | Go 1.14 x64 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.062 s | 12116 KB |
| [2137_dp_strings.java](2137_dp_strings.java) | Java 1.8 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.156 s | 7392 KB |
| [2137_dp_strings.py](2137_dp_strings.py) | Python 3.12 x64 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.875 s | 15324 KB |
| [2137_dp_strings.rs](2137_dp_strings.rs) | Rust 1.75 x64 | dp, strings | O(2^12 (L + 25^2)) | AC | 0.046 s | 4816 KB |
