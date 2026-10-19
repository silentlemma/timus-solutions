# 2044. Máscaras de cantidades de palíndromos para cada prefijo

[Timus 2044](https://acm.timus.ru/problem.aspx?space=1&num=2044) · dificultad 2426 · strings

Problema original de Mikhail Rubinchik, del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da una palabra de `1≤n≤300000` letras latinas minúsculas. Para cada
prefijo no vacío y cada `j` entre `1` y `31`, decidir si puede dividirse
en exactamente `j` palíndromos no vacíos. Los segmentos son
consecutivos, conservan el orden y cubren todas las posiciones;
distintos segmentos pueden ser iguales. Un palíndromo se lee igual en
ambos sentidos.

Codificar las respuestas de un prefijo en un entero no negativo: su bit
`j-1` vale uno si y solo si existe una división en `j` segmentos. El
resultado está entre `0` y `2^31-1`. Límites: 0,5 segundos y 64 MB.

## Entrada

Una línea con la palabra. Su longitud es `n`; no se proporciona un
entero separado con la longitud.

## Salida

Imprimir `n` enteros decimales, uno por línea, en orden creciente de
longitud del prefijo. Los enteros se comparan exactamente como tokens.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
abaa
```

```
1
2
5
14
```

Para `a` solo es posible un segmento; para `ab`, únicamente `a|b`. `aba`
permite el palíndromo completo y `a|b|a`, dando `1+4=5`. Finalmente
`abaa` admite `aba|a`, `a|b|aa` y `a|b|a|a`, con dos, tres y cuatro
segmentos: `2+4+8=14`.

## Solución

### DP de prefijos y árbol de palíndromos

El bit `j` de la máscara interna `D[i]` indica si las primeras `i`
letras admiten exactamente `j` segmentos. A diferencia de la respuesta
impresa, su bit cero representa cero segmentos, de modo que `D[0]=1`. Si
el último segmento es un sufijo palíndromo de longitud `L`, queda el
prefijo `i-L`. Por tanto, `D[i]=OR(D[i-L]<<1)` sobre todos los sufijos
palíndromos. Conservar solo los bits `0..31` e imprimir `D[i]>>1`. Los
estados mayores pueden descartarse: añadir un segmento nunca reduce su
cantidad.

Un eertree contiene un nodo por palíndromo no vacío distinto y dos
raíces de longitudes `-1` y `0`. Una transición `c` rodea el palíndromo
de origen con dos letras `c`. `link[v]` señala su sufijo palíndromo
propio más largo. Al añadir una letra, las búsquedas habituales por
enlaces encuentran un sufijo ampliable, crean como máximo un nodo y
determinan su enlace. Un centinela anterior a la palabra es distinto de
cualquier letra de entrada.

Recorrer todos los sufijos para cada prefijo sería cuadrático con letras
iguales. Definir `diff[v]=len[v]-len[link[v]]`. Las diferencias
consecutivas iguales forman una serie. Si `diff[v]=diff[link[v]]`, usar
`series[v]=series[link[v]]`; en otro caso, `series[v]=link[v]`. Este
enlace salta toda la serie actual.

### Una unión almacenada para cada serie

Mantener una máscara persistente `cache[v]` por nodo. En el extremo `i`,
recorrer las cabeceras desde el sufijo palíndromo más largo mediante
`series`. Para una cabecera `v`, sean `d=diff[v]` y
`B=len[series[v]]+d`: `B` es la longitud mínima de su serie. Asignar
`cache[v]=D[i-B]`. Si las diferencias de `v` y `link[v]` coinciden,
combinar mediante OR `cache[link[v]]`. Incorporar `cache[v]<<1` al
resultado y saltar a la siguiente serie.

La caché del enlace suele proceder de un prefijo anterior. Ese desfase
es necesario; borrar las cachés en cada posición invalida el algoritmo.

### Por qué la caché antigua contiene los cortes correctos

Todo borde de un palíndromo también es palíndromo: el sufijo es el
reverso del prefijo de igual longitud. Como los períodos corresponden a
longitudes complementarias de bordes, `diff[v]` es su período mínimo.

Considerar una serie no trivial con `u=link[v]` y `diff[u]=diff[v]=d`.
Entonces `|v|=|u|+d` y `|u|≥d`. Las copias prefija y sufija de `u`
cubren `v`; sus inicios distan `d`. No puede iniciarse otra copia de `u`
estrictamente entre ambas, pues el solapamiento con la primera daría a
`u` un período positivo menor que `d`. Por ello `u` no aparece como
sufijo en extremos estrictamente entre `i-d` e `i`.

Además `u` era cabecera en el extremo `i-d`. De no serlo, la cadena allí
tendría un predecesor inmediato `z` con `link[z]=u` y diferencia `d`. Su
longitud sería `|v|`; las dos copias de `u` que lo cubren fuerzan `z=v`.
Las copias de `v` terminadas en `i-d` e `i` cubrirían entonces un
palíndromo mayor `W`: la reflexión en el centro total intercambia las
dos copias palíndromas iguales. Su período mínimo es `d`, ya que tiene
ese período y contiene `v`. Así `link[W]=v` con diferencia `d`,
contradiciendo que `v` sea cabecera ahora.

Por tanto `cache[u]` se actualizó por última vez en `i-d`. Por inducción
contiene los valores `D[i-d-L]` para las longitudes antiguas
`L=B,B+d,…,|v|-d`. Son exactamente los cortes actuales de los sufijos
más largos `B+d,…,|v|`. Añadir `D[i-B]` incorpora el más corto. Una
serie de un solo nodo únicamente necesita este último valor.

Cada caché une así precisamente los cortes de su serie actual. Las
series dividen todos los sufijos palíndromos, y desplazar añade el
último segmento. La inducción sobre la longitud del prefijo prueba todas
las máscaras. El argumento trata los índices reales de los cortes y por
eso justifica OR, sin limitarse a una recurrencia de mínimo número de
segmentos.

### Complejidad

Cada dos saltos de serie reducen al menos a la mitad la longitud
positiva. Sean `L,A,B` tres longitudes consecutivas y supongamos
`B>L/2`. Si `d,e` son los períodos mínimos de los dos primeros
palíndromos, el segundo hereda período `d` pero tiene otra diferencia;
por ello `e<d`. Además `e≤A-B`. Sus copias prefija y sufija cubren el
primer palíndromo y se solapan en `2A-L>2e` posiciones. Dos palabras de
período `e` cuyo solapamiento tiene al menos `e` posiciones tienen una
unión de período `e`: cada pareja de posiciones separadas por `e` queda
en alguna copia. Esto contradice la minimalidad de `d`. Luego `B≤L/2`.

Un salto aislado no tiene por qué reducir a la mitad: `aabaaabaa`
produce `9→5`. La propiedad de dos saltos basta para `O(log n)` series
por prefijo. Con las búsquedas amortizadas habituales y el alfabeto
fijo, el tiempo es `O(n log n)` y el espacio `O(n)`. El diccionario de
transiciones de Python usa tiempo esperado de búsqueda; los demás
puertos emplean arreglos con alfabeto acotado.

La técnica básica de enlaces de serie se describe en [Rubinchik y Shur,
EERTREE, sección 4.1](https://arxiv.org/abs/1506.04862). La prueba de
unión de cortes anterior explica su aplicación a las máscaras de
cantidades exactas.

Trampas:

- Los segmentos son no vacíos; el bit interno cero solo corresponde al
  prefijo vacío.
- Usar OR en vez de suma: varios cortes pueden producir la misma cantidad.
- Conservar 32 bits internos y desplazar a la derecha al imprimir. Java
  necesita desplazamiento sin signo.
- Mantener las cachés antiguas: su desfase temporal forma parte de la prueba.
- Una máscara cero puede volver a ser distinta de cero cuando un sufijo
  largo alcanza un corte anterior.
- Las transiciones densas de 64 bits pueden exceder la memoria;
  almacenar los índices de forma compacta.

## Notas por lenguaje

C++ y Go utilizan 26 transiciones de 32 bits por nodo. Rust también
guarda transiciones de 32 bits y convierte los índices al acceder. Java
organiza las aristas salientes dispersas en arreglos primitivos; el
índice de la arista entrante coincide con el del nodo y cada búsqueda
recorre como máximo 26 aristas. La salida está almacenada en búfer.

Python usa objetos `array` compactos para campos y máscaras, un
diccionario con claves `parent*26+letter` y salida por bloques.

La solución en Python se ejecuta con PyPy: con CPython 3.12 supera el
límite de tiempo en la prueba 32 del juez, mientras que con PyPy 3.10 se
acepta en 0.375 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2044_strings.cpp](2044_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.062 s | 38264 KB |
| [2044_strings.go](2044_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.062 s | 41724 KB |
| [2044_strings.java](2044_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.171 s | 12552 KB |
| [2044_strings.py](2044_strings.py) | PyPy 3.10 x64 | strings | O(n log n) | AC | 0.375 s | 34936 KB |
| [2044_strings.rs](2044_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.046 s | 42084 KB |
