# 1996. Mínimo de cambios del bit bajo para una subcadena de bytes

[Timus 1996](https://acm.timus.ru/problem.aspx?space=1&num=1996) · dificultad 1239 · strings

Problema original de Denis Dublennykh, preparado por Oleg Dolgorukov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una imagen contiene `n` bytes y un mensaje contiene `m`. Solo se puede
invertir el bit menos significativo de cada byte de la imagen. Hay que
formar el mensaje como bloque contiguo con el mínimo número de
inversiones. En caso de empate se escoge el inicio más temprano. Los
siete bits superiores permanecen fijos. Límites: `1≤n,m≤250000`, 2
segundos y 64 MB.

## Entrada

Primero `n m`; después dos líneas con la imagen y el mensaje. Cada byte
se escribe como ocho dígitos binarios, del bit más significativo al
menos significativo, con espacios entre bytes.

## Salida

Escribir `No` si no hay una posición factible. En otro caso escribir
`Yes` y, en la siguiente línea, el mínimo de inversiones y el índice
inicial contado desde 1.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3 2
11110001 11110001 11110000
11110000 11110000
```

```
Yes
1 2
```

```
3 1
11110000 11110001 11110000
11110000
```

```
Yes
0 1
```

En el primer ejemplo ambos inicios coinciden en los siete bits altos. El
inicio 1 requiere dos cambios; el 2, uno. En el segundo ejemplo los
inicios 1 y 3 cuestan cero, así que se elige 1.

## Solución

Sean `A[i]` y `B[j]` los valores de los bytes. KMP busca `B[j]>>1`
dentro de `A[i]>>1`. Sus apariciones son exactamente los inicios
factibles: una diferencia superior no se puede reparar, mientras que el
bit bajo siempre se puede ajustar si las partes altas coinciden. Tras
cada aparición se restaura el estado de la función prefijo para
conservar solapamientos. Si `m>n` o no hay apariciones, la respuesta es
`No`.

Definimos `a[i]=A[i]&1`, `b[j]=B[j]&1`, las sumas prefijas `P` de `a` y
`q=sum(b)`. Invertimos `b` y calculamos su convolución `C` con `a`. Para
el inicio `s` desde cero, `C[s+m−1]=sum(a[s+j]·b[j])`. La identidad
binaria `x xor y=x+y−2xy` da el coste exacto

`P[s+m]−P[s]+q−2·C[s+m−1]`.

Examinamos solo inicios factibles, en orden creciente, y sustituimos la
respuesta únicamente si mejora estrictamente. Así se conserva el primer
mínimo. No es útil modificar bytes fuera del bloque elegido.

### NTT exacta en C++, Go, Java y Rust

El módulo es `998244353=119·2^23+1`, con raíz primitiva 3. Se completa
con ceros hasta una potencia de dos `L≥n+m−1`; `L≤524288`, por lo que
existen las raíces necesarias. Dos transformadas directas, producto
puntual y una inversa recuperan la convolución. Cada coeficiente entero
está entre 0 y `m≤250000`, menor que el módulo; el residuo es, por
tanto, el valor exacto. No hay redondeo ni comparación probabilística.
Los productos usan 64 bits y la suma de dos residuos cabe en 32 bits con
signo. Hasta 32 posiciones factibles se comparan directamente.

### Multiplicación entera exacta en Python

Tomamos `R=2^18`, `X=sum(a[i]R^i)` e `Y=sum(b[m−1−j]R^j)`. Los dígitos
del producto en base `R` son los coeficientes. Ninguno supera 250000 y
todos son menores que 262144, evitando acarreos entre coeficientes. Una
tabla de 16 entradas empaqueta cuatro bits originales en nueve bytes.
Completar el último grupo con ceros no modifica el número. Al convertir
el producto a bytes de menor a mayor peso, cada dígito de 18 bits
comienza con desplazamiento 0, 2, 4 o 6 dentro de un byte; tres bytes
bastan para extraerlo.

Con hasta 2048 inicios factibles se empaquetan los bits bajos uno por
dígito binario. Desplazamiento, XOR, una máscara de longitud `m` y
popcount dan el coste. La inversión coloca el primer byte en el bit
bajo; la máscara elimina la cola sobrante. Como el umbral es fijo, esta
rama es lineal en la entrada. Una parte alta completamente uniforme
permite construir las apariciones directamente. Todas las ramas
mantienen el coste y el desempate.

### Complejidad

Las versiones NTT usan tiempo `O(n+m+L log L)` y memoria `O(n+m+L)`,
equivalentes a `O((n+m) log(n+m))` y `O(n+m)`. Si `M(u,v)` es el coste
de multiplicar enteros de hasta `u` y `v` bits, Python necesita
`O(n+m+M(18n,18m))` tiempo, almacenamiento lineal más el espacio de
trabajo de la multiplicación. Esta cota corresponde a multiplicación
entera, no a una implementación FFT en Python.

Comprobar los siete bits inmutables. Invertir el mensaje y leer el
coeficiente `s+m−1`. Minimizar solo en posiciones factibles y no
reemplazar por un empate. Los ceros iniciales forman parte del byte. Se
prueban productos nulos, coeficientes grandes, solapamientos, `m>n` y un
único bloque.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1996_strings.cpp](1996_strings.cpp) | G++ 13.2 x64 | strings | O((n+m) log(n+m)) | AC | 0.156 s | 7028 KB |
| [1996_strings.go](1996_strings.go) | Go 1.14 x64 | strings | O((n+m) log(n+m)) | AC | 0.156 s | 22660 KB |
| [1996_strings.java](1996_strings.java) | Java 1.8 | strings | O((n+m) log(n+m)) | AC | 1.000 s | 11184 KB |
| [1996_strings.py](1996_strings.py) | Python 3.12 x64 | strings | O(n+m+M(18n,18m)) | AC | 1.421 s | 35828 KB |
| [1996_strings.rs](1996_strings.rs) | Rust 1.75 x64 | strings | O((n+m) log(n+m)) | AC | 0.125 s | 17348 KB |
