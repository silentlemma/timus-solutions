# 1999. Desplazar el lenguaje numérico de un autómata decimal

[Timus 1999](https://acm.timus.ru/problem.aspx?space=1&num=1999) · dificultad 5669 · constructive

Problema original de Denis Dublennykh, preparado por Eugene Kurpilyansky.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un autómata determinista lee enteros decimales no negativos de izquierda
a derecha; los ceros iniciales no cambian el veredicto. El primer estado
es inicial y no terminal, rechazando identificadores vacíos. Construir
un autómata que acepte exactamente los números antiguos aceptados más
`k`, también rechazando vacío y respetando ceros iniciales.

`1≤n≤100`, `1≤k≤8`, como máximo 25600 estados de salida. Tiempo 1
segundo, memoria 64 MB. Bajo estas condiciones la construcción siempre
existe y cabe, por lo que `Impossible` no es necesario.

## Entrada

Primero `k`, después `n`, luego `n` indicadores terminales 0/1. Siguen
`n` filas de destinos para los dígitos 0–9, con estados numerados desde
1 e inicio en 1.

## Salida

Escribir `Success` y el nuevo autómata en el mismo formato, sin `k`. Se
acepta cualquier autómata correcto de hasta 25600 estados, sin exigir
minimización ni numeración del ejemplo. El enunciado permite
`Impossible` si no existe, pero aquí demostramos existencia.

## Evaluación

Un comprobador construye el producto del autómata impreso y del antiguo
desplazado en k y verifica que aceptan los mismos números, además del
límite de tamaño y del identificador vacío; se acepta cualquier autómata
válido.

## Ejemplos

```
3
4
0 0 1 0
1 2 4 4 4 4 4 4 4 4
4 2 4 4 4 4 4 4 3 4
4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4
```

```
Success
5
0 0 0 0 1
1 2 3 4 4 4 4 4 4 4
4 2 3 4 4 4 4 4 4 4
4 5 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4
```

El autómata antiguo acepta 18, 118, 1118, etcétera, con ceros iniciales
opcionales. Sumar 3 produce 21, 121, 1121, etcétera: el lenguaje del
ejemplo de cinco estados. Nuestra construcción tiene ocho estados
alcanzables y reconoce exactamente lo mismo.

## Solución

Sean `δ` las transiciones antiguas y `T` las marcas terminales. Para un
prefijo `s` de valor `v`, guardamos `(q,r,b)`:

- `q` es el estado antiguo tras leer `s`.
- Si `v>0`, `r` es el estado antiguo tras leer `v−1` rellenado con ceros
  a la longitud de `s`; si no, es el marcador inválido `n`.
- `b` es el veredicto requerido para el prefijo como nuevo identificador.

El inicio interno desde cero es `(0,n,0)`. Al añadir dígito `d`,
`q'=δ(q,d)`. Si `d>0`, `r'=δ(q,d−1)`; si `d=0`, un predecesor inválido
sigue inválido y uno válido pasa a `δ(r,9)`, usando `10v−1=10(v−1)+9`.

El nuevo bit se calcula con los `q,r` anteriores y el dígito actual:

- Si `d≥k`, `b'=T[δ(q,d−k)]`.
- Si `d<k` y `r` es válido, `b'=T[δ(r,d+10−k)]`.
- En otro caso el valor es menor que `k` y `b'=0`.

Son los casos de resta sin préstamo y con préstamo.

Por inducción se mantienen ambos estados y el bit acepta exactamente
cuando el número menos `k` es no negativo y aceptado por la máquina
antigua. El relleno de ceros no altera su veredicto por hipótesis. Un
cero antiguo aceptado se lee como cadena no vacía de ceros, no como
vacío. El nuevo vacío y los números menores que `k` se rechazan.

Hay como máximo `2n(n+1)≤20200` tuplas. BFS enumera solo las alcanzables
y asigna 1 a la inicial. Una tabla densa con índice `2·(q·(n+1)+r)+b`
evita hashing. La marca terminal es `b`; se emiten diez transiciones.
Los prefijos de ceros conservan predecesor inválido y bit falso. Los
demás ceros iniciales tampoco cambian el lenguaje: la resta da el mismo
número antiguo rellenado.

### Complejidad

Con alfabeto decimal fijo, tiempo y memoria `O(n²)`, incluida la tabla
de salida. Como máximo 20200 estados y 202000 transiciones. Solo se
manejan índices pequeños; ningún identificador arbitrariamente largo se
convierte a un entero acotado.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1999_constructive.cpp](1999_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.031 s | 840 KB |
| [1999_constructive.go](1999_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 7720 KB |
| [1999_constructive.java](1999_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.109 s | 5124 KB |
| [1999_constructive.py](1999_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.187 s | 6440 KB |
| [1999_constructive.rs](1999_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 2444 KB |
