# 1635. Mnemotecnia y palíndromos

[Timus 1635](https://acm.timus.ru/problem.aspx?space=1&num=1635) · dificultad 202 · dp

Problema original de Igor Chevdar, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Partir una cadena de letras minúsculas en la menor cantidad de
palíndromos e imprimir cuántos son y los trozos en orden. Se acepta
cualquier partición óptima.

## Entrada

Una cadena no vacía de letras latinas minúsculas, de longitud hasta 4000.

## Salida

El menor número de palíndromos y luego los trozos de una partición
óptima separados por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
pasoib
```

Salida:

```
6
p a s o i b
```

### Ejemplo 2

Entrada:

```
zzzqxx
```

Salida:

```
3
zzz q xx
```

### Ejemplo 3

Entrada:

```
wasitacatisaw
```

Salida:

```
1
wasitacatisaw
```

## Solución

Sea `d[j]` el mínimo de piezas para las primeras `j` letras,
`d[0]=0`. Cada palíndromo `s[l..r]` permite
`d[r+1]=min(d[r+1],d[l]+1)`. Se guarda `l` para reconstruir hacia atrás
y luego invertir las piezas. Toda partición tiene un último palíndromo,
de modo que las transiciones consideran todas las posibilidades.

Las bases C++, Go, Java y Rust expanden los `2n−1` centros pares e impares
de izquierda a derecha. Cada pieza que termina antes de `l` tiene su centro
estrictamente antes de `l`; el centro actual es al menos `l`. Por tanto,
`d[l]` ya es definitivo. Tiempo peor `O(n²)` y espacio `O(n)`, incluida
la reconstrucción, sin matriz cuadrática de palíndromos.

La base Python usa enteros como conjuntos de bits de inicios. Para el
extremo derecho `i`, desplaza los inicios anteriores una posición a la
derecha, interseca con las posiciones de `s[i]`, añade `i` y, si las dos
últimas letras coinciden, `i−1`. Es exactamente la recurrencia del interior
palindrómico con los casos base de longitudes uno y dos.

Añadir una letra cambia el mínimo a lo sumo en uno. La cota superior
usa una pieza de una letra. Para la inferior, quita la última letra del
último palíndromo óptimo: queda su primera letra y su interior palindrómico,
a lo sumo dos piezas en vez de una. Así `d[i+1]` es `d[i]−1,d[i],d[i]+1`.
`level[v]` guarda longitudes previas de prefijos con mínimo `v`; se prueban
los niveles `d[i]−2,d[i]−1` contra los inicios, por orden. Si no hay
intersección, añadir una letra es óptimo; su bit menor da un predecesor.

Con `w` bits por bloque del entero grande, Python requiere `O(n²/w+n)`
operaciones de bloques. Las máscaras de niveles pueden sumar `O(n²)` bits,
más `O(n)` índices/objetos: incluso un único bit necesita espacio hasta
su posición. No es el almacenamiento lineal del DP nativo ni se supone `w=64`.

## Soluciones optimizadas

El C++ nuevo conserva la expansión de centros y el DP, de ahí
`_optimized`. Primero comprueba si toda la cadena es palíndroma: una pieza
es óptima y permite devolver en `O(n)`. En otros casos conserva el peor
`O(n²)`. Para `n≤4000`, cantidades, centinela `n+1`, índices de prefijos
y extremos reconstruidos caben en celdas de 16 bits sin signo. Arreglos
estáticos guardan entrada, mínimos, predecesores y extremos; `fwrite`
imprime segmentos sin objetos de subcadenas ni vector de strings, usando
stdio en lugar de iostream. El programa Accepted completo usa 140 KB
frente a 676 KB: 79,3% menos. Ambos tiempos son 0,015 s; no se afirma
una aceleración medida. Se conservan ambas versiones.

## Evaluación

El verificador comprueba cantidad, palíndromos, concatenación igual
a la entrada y minimalidad; distintas particiones óptimas son válidas.
El nuevo C++ real pasó 693 entradas extra independientes: las 510 cadenas
binarias no vacías de longitudes uno a ocho, 180 aleatorias y tres de
longitud 4000 con óptimos demostrados 1, 2 y 4000. Los casos pequeños usan
un DP independiente que invierte cada sufijo, sin expansión de centros.
Los grandes son una letra repetida, `ab` alternado y `abcd` repetido:
el último carece de palíndromos de longitud dos o tres, y por ello de mayores.
También pasó las 15 entradas del repositorio en Docker y tiene Accepted
de la fuente exacta. Las 693 son ejecuciones C++, no de un nuevo Python.

## Notas por lenguaje

Se conservan byte por byte las cinco fuentes Accepted anteriores.
Se compara el nuevo C++ con su base C++. La muestra usa la regla acordada:
C++ en el 15% superior o primeros diez puestos de ambas métricas; las otras
familias, primero en ambas. Una muestra filtrada vacía solo da cobertura
formal, no superioridad competitiva. Una versión admitida bajo el objetivo
conservaría asterisco y explicación traducida.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1635_dp.cpp](1635_dp.cpp) | G++ 13.2 x64 | dp | O(n²) | AC | 0.015 s | 676 KB | 11288441 |
| [1635_dp.go](1635_dp.go) | Go 1.14 x64 | dp | O(n²) | AC | 0.046 s | 1456 KB | 11288442 |
| [1635_dp.java](1635_dp.java) | Java 1.8 | dp | O(n²) | AC | 0.125 s | 796 KB | 11288444 |
| [1635_dp.py](1635_dp.py) | Python 3.12 x64 | dp | O(n²/w + n) | AC | 0.093 s | 2064 KB | 11288443 |
| [1635_dp.rs](1635_dp.rs) | Rust 1.75 x64 | dp | O(n²) | AC | 0.062 s | 304 KB | 11288445 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1635_dp_optimized.cpp](1635_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n²) | AC | 0.015 s | 140 KB | 11308417 |
