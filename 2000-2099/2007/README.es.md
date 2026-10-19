# 2007. La cadena mínima tras usar todas las operaciones

[Timus 2007](https://acm.timus.ru/problem.aspx?space=1&num=2007) · dificultad 1922 · strings, greedy

Problema original de Ilya Kuchumov, del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una cadena y un multiconjunto de modificadores de letras, usar cada
modificador exactamente una vez, en cualquier orden. Un modificador `c`
inserta `c` en cualquier posición, incluidos los extremos, o borra una
`c` existente. También puede borrarse una letra insertada anteriormente.
Hallar la cadena final lexicográficamente mínima; un prefijo propio más
corto es menor. Se garantiza que ninguna aplicación de todos los
modificadores produce la cadena vacía.

## Entrada

Dos líneas no vacías: cadena original `S` y modificadores `T`. Solo
contienen letras latinas minúsculas y cada longitud es como máximo
100000. El orden de los modificadores en la entrada no impone orden de
uso. Tiempo 0,5 segundos, memoria 64 MB.

## Salida

La cadena mínima alcanzable, no vacía por la garantía, de longitud no
mayor que `|S|+|T|`.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
abc
bbc
```

```
ab
```

Borrar `c` con su modificador y gastar los dos modificadores `b`
insertando y borrando una `b` extra deja `ab`.

## Solución

### Regla voraz

Sean `R[c]` las letras originales restantes y `K[c]` los modificadores.
Es posible acabar con sufijo vacío exactamente si todo `K[c]≥R[c]` y
`K[c]−R[c]` es par: borrar los originales y gastar los pares sobrantes
con inserción y borrado. Si ocurre, terminar inmediatamente, pues
cualquier extensión supera el prefijo actual.

En otro caso elegir la menor letra siguiente posible: insertar una con
modificadores disponibles, o conservar una aparición original cuyo
prefijo original pueda borrarse con las cantidades actuales. En empate
preferir la aparición original accesible más temprana, borrar su prefijo
y conservarla. Insertar solo si la letra del modificador es
estrictamente menor.

### Por qué es correcto el desempate

Las letras originales conservadas mantienen su orden; las demás
supervivientes son insertadas. Una letra insertada y luego borrada
consume un par neutral de modificadores iguales. Se pueden reordenar
operaciones según esta descripción sin cambiar el resultado.

La original elegida `c` divide el resto como `X+c+Z`. Todas las letras
de `X` son mayores que `c`: cada posición de `X` es accesible, y una `c`
anterior se habría elegido antes. Tampoco hay modificador disponible
menor que `c`. Si una respuesta conserva una `c` original posterior,
intercambiar cuál sobrevive y cuál se borra preserva cantidades y
resultado. Basta la primera.

Comparar conservar esta `c` con insertar primero `c`. Tomar cualquier
continuación del segundo caso. Si se borran todos los originales de `X`
y la `c` original sobrevive, usarla para la primera salida e insertar
`c` en su antigua posición de salida conserva resultado y gasto. Si esa
`c` original se borra, conservarla primero y gastar los dos
modificadores `c` liberados como par neutral produce de nuevo la misma
respuesta tras borrar `X` antes.

Si sobrevive algún original de `X`, antes del primero solo hay letras
insertadas, todas al menos `c`. La continuación empieza con `c^r`
seguido de una letra mayor. Esas `r` copias son insertadas y `r≤K[c]−1`,
pues la primera inserción ya gastó un modificador. Conservar la original
mantiene los `K[c]` modificadores de `c`, ya que `X` no contiene esa
letra. Se pueden emitir `r+1` copias más de `c` y completar legalmente
conservando el sufijo e insertando el resto de modificadores. Esta
continuación es estrictamente menor.

Conservar la original nunca es peor. La menor siguiente letra factible,
este desempate y la prueba de sufijo vacío demuestran optimalidad por
inducción sobre las operaciones y originales restantes.

### Implementación eficiente

Para cada letra guardar sus posiciones originales, cuántas se
consumieron `head[c]`, y centinela `n=|S|`. Definir
`cut[c]=head[c]+K[c]`: la primera aparición que no puede borrarse es
`positions[c][cut[c]]`, o `n` fuera de la lista. Sea `r` el mínimo de
esas posiciones. La primera original restante de una letra es accesible
exactamente si su posición es como máximo `r`, incluyendo `r`.

Borrar una letra del prefijo disminuye `K` y aumenta `head`, dejando
`cut` igual. Conservar una original aumenta su `cut`; insertar lo
disminuye. Además `delta[c]=cut[c]−frecuencia_inicial[c]=K[c]−R[c]`. Una
máscara marca diferencias negativas o impares: basta actualizar la letra
elegida para detectar el final. Otras máscaras registran letras
originales presentes y modificadores disponibles.

Se guarda la menor original accesible hasta conservar otra original.
Solo se inserta una `c` estrictamente menor, sin aparición original en
el prefijo alcanzable. Reducir su cuota no mueve la primera posición
imborrable antes de su primera aparición restante, situada después de
`r`. Así el candidato guardado sigue válido durante toda la serie de
inserciones. Si la original actual carece de modificador igual, es la
única accesible y no requiere búsqueda.

Hay como máximo `n+1` consultas de original, cada una examina hasta
`A=26` letras; cada original se consume una vez y hay como máximo
`m=|T|` inserciones. Tiempo `O(A n+m+A)`, equivalente a `O(n+m)` para
este alfabeto fijo. Memoria `O(n+m+A)`, incluida la salida. No se
almacena el árbol de secuencias de operaciones.

## Notas por lenguaje

Todos los modificadores son obligatorios, pero los pares neutrales no
tienen que permanecer en la respuesta. Probar si cabe un sufijo vacío
antes de elegir letra; la garantía inicial no impide un resto vacío
después. Preferir originales en empate, incluir la primera posición
imborrable en el rango e invalidar el candidato guardado tras conservar
una original. Comprobar `cut` antes de indexar. Los cinco programas usan
arreglos de posiciones, máscaras de 26 bits y bucles iterativos; solo
buscan el bit inferior de máscaras no nulas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2007_strings_greedy.cpp](2007_strings_greedy.cpp) | G++ 13.2 x64 | strings, greedy | O(n + m) | AC | 0.015 s | 1580 KB |
| [2007_strings_greedy.go](2007_strings_greedy.go) | Go 1.14 x64 | strings, greedy | O(n + m) | AC | 0.031 s | 7340 KB |
| [2007_strings_greedy.java](2007_strings_greedy.java) | Java 1.8 | strings, greedy | O(n + m) | AC | 0.125 s | 3008 KB |
| [2007_strings_greedy.py](2007_strings_greedy.py) | Python 3.12 x64 | strings, greedy | O(n + m) | AC | 0.359 s | 5864 KB |
| [2007_strings_greedy.rs](2007_strings_greedy.rs) | Rust 1.75 x64 | strings, greedy | O(n + m) | AC | 0.015 s | 2156 KB |
