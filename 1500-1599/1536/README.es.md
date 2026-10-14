# 1536. Las delicias de la hierba para pipa

[Timus 1536](https://acm.timus.ru/problem.aspx?space=1&num=1536) · dificultad 7443 · dp

Problema original de Sergey Pupyrev, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una expresión a1+a2=b (cada número menor que 10⁸) está hecha de
palillos, un símbolo por celda. Cada celda tiene doce lugares para un
palillo: los siete de un visor digital (arriba, centro, abajo y cuatro
lados), una diagonal «/» en la mitad superior y otra en la inferior, la
barra vertical del signo más y las dos barras del signo igual. El dibujo
del enunciado traza los símbolos así (todas las diagonales se inclinan
igual):

| Símbolo | Palillos | Lugares |
|---|---|---|
| `0` | 6 | arriba, los dos lados superiores, los dos inferiores, abajo |
| `1` | 3 | diagonal superior, superior derecho, inferior derecho |
| `2` | 4 | arriba, superior derecho, diagonal inferior, abajo |
| `3` | 4 | arriba, diagonal superior, centro, diagonal inferior |
| `4` | 4 | superior izquierdo, superior derecho, centro, inferior derecho |
| `5` | 5 | arriba, superior izquierdo, centro, inferior derecho, abajo |
| `6` | 5 | diagonal superior, centro, inferior izquierdo, inferior derecho, abajo |
| `7` | 3 | arriba, diagonal superior, inferior izquierdo |
| `8` | 7 | los siete lugares habituales de un dígito |
| `9` | 5 | arriba, superior izquierdo, superior derecho, centro, diagonal inferior |
| `+` | 2 | el centro y una barra vertical por el medio |
| `=` | 2 | dos barras cortas propias |

Moviendo como mucho K palillos (0 ≤ K ≤ 100), hay que convertir la
expresión en una suma verdadera X+Y=Z con el mismo número de caracteres,
donde X, Y y Z tienen de 1 a 8 cifras y no tienen ceros a la izquierda.
No se pueden añadir ni quitar palillos. Hay que escribir esa suma o
«Impossible».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La expresión en la primera línea y K en la segunda.

## Salida

Una expresión verdadera alcanzable con K movimientos como mucho, o
`Impossible`.

## Ejemplos

### Ejemplo 1

Entrada:

```
33+88=127
2
```

Salida:

```
33+88=121
```

### Ejemplo 2

Entrada:

```
3+3=7
1
```

Salida:

```
Impossible
```

## Solución

Si la nueva expresión usa tantos palillos como la antigua, el menor
número de movimientos son los palillos de la nueva que no ocupan un
lugar que la antigua ya llena en la misma celda: el resto se queda, y
estos hay que moverlos. Así que se maximiza el número de palillos que se
quedan, con el total sin cambiar.

Se prueban todas las longitudes de X e Y (Z se queda con el resto y no
puede ser más corto que ninguno de los dos); eso fija las celdas del más
y del igual. Luego se rellenan las columnas de derecha a izquierda, como
en la suma escrita. El estado es la columna, el acarreo y los palillos
usados hasta ahora, y el valor es el máximo de palillos que se quedan;
un paso elige las cifras de X e Y en la columna, que fijan la cifra de Z
y el acarreo siguiente. Las cifras más allá del final de X o de Y no
existen y no cuestan palillos; la primera cifra de un número de más de
una cifra no puede ser 0. Un reparto de longitudes sirve si tras la
última columna el acarreo es 0, se han usado todos los palillos y se
quedan al menos total − K; las elecciones guardadas dan las cifras.
Unos 64 repartos × 8 columnas × 2 acarreos × 180 cantidades de palillos
× 100 pares de cifras, menos de 2·10⁷ pasos.

Detalles a tener en cuenta:

- la barra del más está justo donde va el palillo central, así que se
  queda en su sitio cuando una cifra con palillo central ocupa la celda
  del más, como el 5 en la prueba 05: la respuesta necesita 17
  movimientos, y 18 sin eso;
- los signos pueden moverse: en la prueba 05 el más pasa de la cuarta
  celda a la segunda;
- hay que usar todos los palillos: en la prueba 07 tirar palillos permitiría
  3 movimientos, y conservarlos todos exige 5; en la prueba 09 los ochos
  tienen más palillos que cualquier suma verdadera de esa longitud;
- no se permiten ceros a la izquierda, lo que vuelve imposible una
  respuesta de 9 movimientos en la prueba 06;
- las formas salen del dibujo: el 1 tiene una diagonal arriba, el 7 un
  palillo abajo a la izquierda, y el 3 son dos barras y dos diagonales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1536_dp.cpp](1536_dp.cpp) | G++ 13.2 x64 | dp | O(L^3 * S * 100) | AC | 0.015 s | 504 KB |
| [1536_dp.go](1536_dp.go) | Go 1.14 x64 | dp | O(L^3 * S * 100) | AC | 0.031 s | 2608 KB |
| [1536_dp.java](1536_dp.java) | Java 1.8 | dp | O(L^3 * S * 100) | AC | 0.140 s | 1432 KB |
| [1536_dp.py](1536_dp.py) | Python 3.12 x64 | dp | O(L^3 * S * 100) | AC | 0.140 s | 1172 KB |
| [1536_dp.rs](1536_dp.rs) | Rust 1.75 x64 | dp | O(L^3 * S * 100) | AC | 0.031 s | 496 KB |
