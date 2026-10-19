# 2058. Particiones palindrómicas de paridad impar y par

[Timus 2058](https://acm.timus.ru/problem.aspx?space=1&num=2058) · difficulty 1673 · strings, dp

Problema original de Mikhail Rubinchik, del Concurso Palindrómico del 11 de julio de 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada prefijo de una cadena, dividirlo en palíndromos contiguos y
hallar el menor número impar y el menor número par de trozos. Los
límites son 1 segundo y 64 MB.

## Entrada

Una cadena de 1 a 300 000 letras inglesas minúsculas.

## Salida

n líneas, una por prefijo: el menor número impar de trozos o `-1` si no
existe, y el menor par o `-2` si no existe.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
abaa
```

```
1 -2
-1 2
1 -2
3 2
```

El prefijo `a` solo tiene una parte; `ab` solo admite `a|b`. `aba` es
palíndromo y también admite tres letras. Para `abaa`, las particiones
`aba|a` y `a|b|aa` dan mínimo par dos e impar tres.

## Solución

### Recurrencia y árbol de palíndromos

Sean `O[i],E[i]` los mínimos de paridad impar y par. Usar infinito
`n+1`, `O[0]=∞` y `E[0]=0`. Si la última parte es un sufijo palindrómico
de longitud `L`, entonces `O[i]=min(E[i−L]+1)` y `E[i]=min(O[i−L]+1)`
sobre todos esos sufijos. Así se cubre cada último corte y se cambia la
paridad exactamente una vez.

Un eertree guarda cada palíndromo distinto en un nodo. Las raíces tienen
longitudes `−1` y `0`; `link[v]` indica el mayor sufijo palindrómico
propio. Al añadir una letra, recorrer enlaces desde el anterior mayor
sufijo hasta que la letra situada antes coincida con la nueva. Una
transición extiende ese palíndromo. Para un nodo nuevo, buscar su enlace
del mismo modo desde el enlace de su padre. Solo el mayor sufijo puede
ser nuevo: cualquier sufijo menor ya aparece como prefijo suyo. Hay como
máximo `n+2` nodos. Un byte cero inicial es un centinela seguro para
letras minúsculas.

### Comprimir los sufijos en series

Definir `d[v]=len[v]−len[link[v]]`. `sl[v]` salta al primer sufijo con
diferencia distinta: tomar `sl[link[v]]` si las diferencias coinciden, o
`link[v]` en caso contrario. La serie empieza en `v` y termina antes de
`sl[v]`; sus longitudes forman una progresión aritmética de paso `d[v]`.
Solo se visitan las cabeceras `last,sl[last],…`.

Guardar dos mínimos de predecesores `C_O[v],C_E[v]` por nodo. En el
extremo `i`, inicializarlos con `O[b],E[b]` para `b=i−len[sl[v]]−d[v]`,
el corte anterior al miembro más corto. Si `d[v]=d[link[v]]`, minimizar
cada componente con la componente guardada de `link[v]`. Después
`C_E[v]+1` mejora `O[i]` y `C_O[v]+1` mejora `E[i]`. El valor heredado
procede de un prefijo anterior: no borrar las cachés ni recalcularlo
como si correspondiese al extremo actual.

### Por qué sirve exactamente la caché antigua

Para una cabecera `v` con `u=link[v]` de igual diferencia, escribir
`d=d[v]` y `m=len[u]`. El menor período de un palíndromo es su longitud
menos la de su mayor borde palindrómico propio. Por ello `u` tiene
período mínimo `d` y `m≥d`. Sus apariciones como prefijo y sufijo de `v`
distan `d`. No hay una aparición intermedia: junto a la última formaría
extremos palindrómicos iguales que cubren su unión, dando un sufijo
palindrómico propio de `v` mayor que `u`. La propiedad de cobertura se
demuestra reflejando posiciones: dos extremos palindrómicos iguales de
longitud al menos la mitad fuerzan todas las parejas simétricas de la
palabra.

En el extremo `i−d`, `u` es cabecera. De lo contrario, su predecesor `z`
en la cadena tendría igual diferencia y longitud `m+d`. Sus bordes
superpuestos `u` determinan `z=v`. Las copias anterior y actual de `v`
cubren entonces un palíndromo `w`. Un sufijo palindrómico propio de `w`
mayor que `v` colocaría su prefijo `u` estrictamente entre las dos
apariciones extremas dentro de `z`, contradiciendo el argumento
anterior. Por tanto `link[w]=v` y `d[w]=d`, contradicción con que `v`
sea cabecera ahora. No termina ninguna aparición de `u` entre `i−d` e
`i`, y la actual no es cabecera. Su caché se escribió por última vez
exactamente en `i−d`.

La serie anterior de `u` contiene las longitudes actuales salvo la
mayor. Restarlas de `i−d` produce exactamente los cortes actuales salvo
el del miembro más corto; la inicialización `b` añade ese corte. Las dos
cachés son, por tanto, los mínimos de toda la serie actual. La
recurrencia completa demuestra por inducción todos los mínimos y las
paridades imposibles.

### Número logarítmico de series

Todo borde de un palíndromo es palíndromo, de modo que `d[v]` es
realmente su período mínimo. Para el último nodo `x` de una serie, poner
`L=len[x]`, `B=len[link[x]]` y `p=L−B`. Suponer `B≥2L/3` implica `B≥2p`.
El borde tiene período `p` y período mínimo `q≤p`. Si `q<p`, su longitud
alcanza `p+q`, por lo que también tiene período `gcd(p,q)`. Esta regla
se obtiene restando períodos: para `p<q`, comparar posiciones
desplazadas por `p` o `q` demuestra período `q−p` cuando la longitud
alcanza su suma; después repetir Euclides. Como el período común divide
`p`, extender el borde con los `p` símbolos restantes lo conserva,
contradiciendo el período mínimo `p` de `x`. Entonces `q=p`, otra
contradicción con el cambio de diferencia. Por ello `B<2L/3`: cada salto
reduce la longitud por un factor constante.

## Notas por lenguaje

La DP ocupa tiempo `O(n log n)` y espacio `O(n)`. Las disminuciones de
longitud de las búsquedas de sufijos suman tiempo lineal: añadir una
letra aumenta las longitudes pertinentes como máximo dos. Los lenguajes
compilados usan listas dispersas de hijos, con hasta 26 letras por
búsqueda, coste constante determinista para este alfabeto. Python usa un
diccionario de claves enteras con acceso constante esperado, arreglos de
32 bits, un objeto infinito compartido y salida en bytes; su cota
temporal es esperada. Java escribe cifras directamente en un búfer de
bytes, sin copias de grandes cadenas de caracteres. Los demás programas
también almacenan la salida en un búfer. Identificadores, longitudes y
cantidades caben en enteros con signo de 32 bits.

Separar las dos paridades, inicializar solo `E[0]=0` e intercambiarlas
al añadir una parte. La DP sigue enlaces de serie, la extensión sigue
enlaces de sufijo. Borrar las cachés destruye su desplazamiento
temporal. Una cadena constante tiene muchos sufijos pero una serie; las
palabras ruler ejercitan muchas series. Imprimir todos los prefijos y
distinguir `-1/-2`. El infinito no representa una cantidad alcanzable.

Los mínimos también describen todas las cantidades superiores de la
misma paridad hasta la longitud del prefijo. Si `k+2≤i`, dividir una
parte de longitud al menos tres en primera letra, centro palindrómico y
última letra; si todas tienen longitud uno o dos, dividir dos partes de
longitud dos. Cada operación añade exactamente dos partes.

La solución en Python se ejecuta con PyPy: con CPython 3.12 supera el
límite de tiempo en la prueba 48 del juez, mientras que con PyPy 3.10 se
acepta en 0.515 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2058_strings.cpp](2058_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.078 s | 17832 KB |
| [2058_strings.go](2058_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.078 s | 25560 KB |
| [2058_strings.java](2058_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.187 s | 21784 KB |
| [2058_strings.py](2058_strings.py) | PyPy 3.10 x64 | strings | O(n log n) | AC | 0.515 s | 54644 KB |
| [2058_strings.rs](2058_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.093 s | 21376 KB |
