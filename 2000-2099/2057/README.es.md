# 2057. Mínimo y máximo de factores no palindrómicos

[Timus 2057](https://acm.timus.ru/problem.aspx?space=1&num=2057) · difficulty 3259 · strings

Problema original de Nikita Sivukhin, del Concurso Palindrómico del 11 de julio de 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dividir una cadena de letras inglesas en trozos contiguos no vacíos,
ninguno de los cuales sea un palíndromo; importan las mayúsculas y se
permite un solo trozo. Hallar el menor y el mayor número posible de
trozos. Los límites son 1 segundo y 64 MB.

## Entrada

Una cadena de 1 a 200 000 letras inglesas.

## Salida

`-1` si no hay división; si no, el menor y el mayor número de trozos.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
a
```

```
-1
```

```
abba
```

```
2 2
```

```
babcbcb
```

```
1 2
```

`a` no admite parte válida. `abba` es palíndroma pero `ab|ba` produce
dos, y longitud cuatro impide más. `babcbcb` sirve como una parte o como
`babcb|cb`. Tres partes tendrían longitudes 2, 2 y 3 en algún orden; las
tres elecciones contienen un palíndromo, por lo que el máximo es dos.

## Solución

### Consultas exactas de palíndromos

Calculamos radios impares y pares de Manacher: `odd[c]` incluye la letra
central, `even[c]` corresponde al hueco anterior a `c`. Para `[l,r)`,
longitud `L` y centro `c=floor((l+r)/2)`, la condición es
`odd[c]≥floor(L/2)+1` si `L` es impar, o `even[c]≥L/2` si es par. Se
copia el radio reflejado dentro del palíndromo más a la derecha,
limitado por su borde, y se expande; cada nueva posición del borde se
paga una vez por pasada. Preprocesamiento `O(n)` y consultas exactas
`O(1)`.

### Máximo: dos niveles y dos cortes por nivel

Sea `d[i]` el máximo de partes del prefijo `s[0:i]`, o `-1` si es
imposible; `d[0]=0`. La recurrencia completa toma `1+max d[j]` entre
`j≤i−2` cuyo sufijo `s[j:i]` no sea palíndromo. En el paso `i`
insertamos el nuevo corte `i−2`. Conservamos primer y último corte de
cada puntuación, y la mayor puntuación insertada `M`. Probamos `M,M−1`
en ese orden, usando sus dos extremos. El primer éxito da nivel más uno;
sin éxito queda `-1`. Demostramos ambas reducciones.

Entre dos cortes de la misma puntuación exacta `v` hay un palíndromo: de
lo contrario podríamos mejorar la puntuación posterior. Las palabras
entre cortes consecutivos y las concatenaciones adyacentes son
palíndromas; por tanto las palabras adyacentes conmutan y todas son
potencias de una raíz primitiva palíndroma `U`. La propiedad de palabras
conmutantes se obtiene cancelando repetidamente el prefijo menor en
`XY=YX`, como Euclides. Si los sufijos extremos `T` y `U^k T` son
palíndromos, invertir da `U^k T=T U^k`, así que `T` también es potencia
de `U`. Todos los sufijos intermedios son palíndromos. Basta probar los
extremos de cada nivel.

Ahora probamos que, si existe, `d[i]` vale `M` o `M+1`. La cota superior
viene de la recurrencia; `M≤1` es inmediato. Supongamos `M≥2` y un
prefijo factible con `d[i]<M`. Todo corte de puntuación al menos `M−1`
debe dejar un sufijo palíndromo. Elegimos un prefijo óptimo de `M`
factores y cola `Y` de longitud al menos dos; llamamos `Q,P` a sus
últimos factores. Tanto `Y` como `PY` son palíndromos.

Sea `a^r` la racha final de `PY`, incluyendo letras de `P` si `Y` es
constante. El palíndromo `PY` comienza exactamente por `a^r b`, `b≠a`,
dentro del no palíndromo `P`. Si `Qa^r` no fuera palíndromo, mover el
corte antes de `b` daría `M` partes. Por tanto es palíndromo. Para
`r≥2`, `Qa^(r−1)` no es palíndromo: dos prefijos palíndromos
consecutivos forzarían período uno y `Q` constante. El sufijo restante
tiene rachas inicial y final de longitudes distintas 1 y `r`, de modo
que tampoco es palíndromo; otra contradicción. Luego `r=1`.

`Qa` es palíndromo y comienza por `a`, así que `Qab` no lo es. Su corte
tiene puntuación al menos `M−1` y fuerza `(PY)[2:]` palíndromo. Junto
con `PY` palíndromo implica período dos. Sus primeras letras distintas
hacen `PY` alternante impar, `Y` alternante impar de longitud al menos
tres y `P` potencia de `ab` de longitud par.

Propagamos hacia atrás. Si las partes posteriores a `A_h` junto con `Y`
forman una cola alternante impar de longitud al menos `2(M−h)+3`,
entonces `A_h a` o `A_h aba` no palíndromo permitiría completar `M`
partes: dividimos la cola alternante par restante en `M−h` longitudes
pares positivas. Por tanto ambas extensiones son palíndromas; su
diferencia de longitud dos fuerza el mismo período y longitud par de
`A_h`. Todos los factores originales serían potencias de `ab` de longitud
par, dejando la cadena completa alternante impar. Sus factores no
palíndromos siempre miden par, imposibles de sumar a una longitud impar.
La contradicción prueba la cota y, por inducción, el DP reducido.

### Mínimo: uno o dos cuando es factible

Si `AB,BC,ABC` son palíndromos, `B` también lo es. `ABC` tiene períodos
`|A|,|C|` por sus sufijo y prefijo palíndromos. Su longitud supera la
suma, así que el máximo común divisor es período. La regla es elemental:
para `p<q` y longitud al menos `p+q`, comparar `i→i−p→i−p+q` si `i≥p` e
`i→i+q→i+q−p` en otro caso da período `q−p`; se repite Euclides. La
reflexión lleva `B` a una subcadena igual de larga que empieza en `|C|`
en vez de `|A|`; los comienzos son congruentes módulo ese período, luego
`B` es su reverso.

En tres factores no palíndromos consecutivos, fusionamos una pareja si
su concatenación no es palíndroma. Si ambas parejas son palíndromas, la
concatenación triple debe ser no palíndroma por el lema y fusionamos los
tres. Repetir reduce cualquier partición válida a una o dos. Tras
comprobar factibilidad mediante DP, el mínimo es uno para la cadena
completa no palíndroma, y dos en caso contrario.

## Notas por lenguaje

Manacher, DP y consulta final cuestan `O(n)` tiempo y `O(n)` espacio.
Como cada parte mide al menos dos, hay como máximo `floor(n/2)` niveles
positivos. Todos usan bucles iterativos e índices enteros; Python se
ejecuta en CPython 3.12. Se conserva la entrada completa.

Insertar `i−2`, no `i−1`; la puntuación cero corresponde al prefijo
vacío. Ignorar prefijos imposibles y guardar ambos extremos. Un
palíndromo puede dividirse, como `abba`; una cadena no constante puede
ser imposible, como `ababa`. Son incorrectos el prefijo válido más corto
y limitar partes a longitudes dos o tres. Respetar mayúsculas y las dos
paridades de centro. No se usa hash probabilístico ni recorrido de todos
los niveles en las soluciones.

No confundir longitud par con exponente par de `ab`: en el test `edge_05`
(`ababa`), `Y=aba` y `PY=ababa` son palíndromos con `P=(ab)^1`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2057_strings.cpp](2057_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 3528 KB |
| [2057_strings.go](2057_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.046 s | 8564 KB |
| [2057_strings.java](2057_strings.java) | Java 1.8 | strings | O(n) | AC | 0.140 s | 6444 KB |
| [2057_strings.py](2057_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.875 s | 19968 KB |
| [2057_strings.rs](2057_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 6044 KB |
