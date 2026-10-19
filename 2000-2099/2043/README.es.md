# 2043. Recorrido serpenteante con recargas por el borde sur

[Timus 2043](https://acm.timus.ru/problem.aspx?space=1&num=2043) · difficulty 4147 · math

Problema original de Ilya Kuchumov (Prepared by Kirill Borozdin), del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula tiene `n` columnas de oeste a este y `m` filas de sur a
norte. Procese las celdas en serpiente vertical: desde la esquina
suroeste suba por la primera columna, avance una celda al este, baje por
la segunda y siga alternando. La celda inicial no cuesta movimiento;
pasar a una celda vecina por un lado cuesta un paso.

Un recipiente comienza con `k` unidades y procesar una celda gasta una.
Después de cada `k` celdas procesadas, excepto tras la última, camine al
sur hasta la celda inferior de la columna actual, salga un paso para
recargar, vuelva a esa misma celda y llegue a la siguiente celda del
orden por un camino Manhattan mínimo. Salir y volver cuesta dos pasos.
El desplazamiento de recarga no avanza el orden ni consume unidades.
Deténgase al procesar la última celda. Calcule el total de pasos módulo
`1000000007`.

## Entrada

Primero `1≤t≤10`. Cada línea siguiente contiene `n,m,k`, con
`1≤n,m≤10^12`, `1≤k≤10^18` y `min(n,m)≤10^6`. Por ello el área
`N=nm≤10^18`. Anchura y altura tienen funciones distintas y no se pueden
intercambiar. Límites: 4 segundos y 64 MB.

## Salida

Imprima un entero módulo `1000000007` por caso, en orden. Se comparan
las respuestas como tokens enteros.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
1
5 3 5
```

```
20
```

Hay `15` celdas y el recorrido ordinario cuesta `14` pasos. Se recarga
tras las celdas `5` y `10`. En la primera, las alturas actual y
siguiente son `1` y `0`: el trayecto cuesta `1+2+0=3` en vez de uno,
sumando `2`. En la segunda, las alturas `2` y `1` añaden `2+2+1-1=4`.
Total `14+2+4=20`; no se recarga tras la celda `15`.

## Solución

### Coste adicional de una recarga

Use coordenadas desde cero y altura sur cero. Tras la celda ordinal `j`,
la posición actual es `(x,y)` y la siguiente `(u,v)`. La recarga cuesta
`y+2+v+|u-x|`, sustituyendo un paso ordinario. El exceso siempre es par;
llame `f(j)` a su mitad. Hay `F=(N-1)//k` recargas y la respuesta es
`N-1+2Σ f(ik)` para `1≤i≤F`. El límite `N-1` excluye recargar en la
última celda aunque `k` divida `N`.

Escriba `j=qm+r`, `0≤r<m`. Si `r>0`, una columna ascendente tiene
`f(j)=r` y una descendente `f(j)=m-r`, según la paridad de `q`. Con
`r=0`, `q` impar da una transición superior con `f=m`, y `q` par una
inferior con `f=1`. Así, para `P=2m` y `z=j mod P`, `f(j)=min(z,P-z)`,
salvo que `z=0` vale `1`, no cero.

### Sumar por columnas

La columna de índice cero `c` contiene los ordinales de recarga en
`(cm,min((c+1)m,N-1)]`. Los multiplicadores de `k` van de `a=cm//k+1` a
`b=min((c+1)m,N-1)//k`. Si `a>b` no hay ninguno; en otro caso `C=b-a+1`.

Las mitades del coste en una columna ascendente forman una progresión de
`ak-cm` a `bk-cm`; en una descendente van de `(c+1)m-ak` a `(c+1)m-bk`.
Sume `C(first+last)/2`. Si la progresión descendente termina en cero,
añada uno por esa transición inferior. Los intervalos ordinales
particionan exactamente todas las recargas, demostrando este método
`O(n)`.

### Un prefijo corto del período de residuos

Sean `g=gcd(k,2m)` y `L=2m/g`. Los residuos de `ki` tienen período `L` y
visitan una vez `0,g,2g,...,(L-1)g`. Con `h=L//2`, las dos mitades del
triángulo suman `g h(L-h)`, tanto para `L` par como impar. El residuo
cero añade uno, dando el total de período `C=g h(L-h)+1`.

Escriba `F=qL+r`. Los períodos completos aportan `qC`. Para índices no
nulos, `f(ki)=f(k(L-i))`, luego `prefix(r)+prefix(L-r-1)=C-1`. Calcule
solo `W=min(r,L-r-1)` términos iniciales; si el complementario es menor,
réstelo de `C-1`. Genere residuos sumando `k mod 2m` y restando `2m` una
vez cuando haga falta. Un prefijo propio no contiene el residuo cero: su
uno especial ya está incluido en las fórmulas del período y del
complemento.

Como `W≤floor((L-1)/2)≤m/g≤m`, elija columnas si `n<W` y residuos en
otro caso. Se hacen como máximo `min(n,m)≤10^6` iteraciones. La
partición demuestra la primera suma y la permutación de residuos con
simetría demuestra la segunda; elegir cualquiera conserva la respuesta
correcta.

### Períodos cortos de columnas completas en Python

Python agrupa además columnas completas por `T=2k/gcd(m,k)`. Aumentar
`c` en `T` conserva su paridad y `cm mod k`, así que el coste de una
columna completa se repite. `T` es par y `k` divide `Tm`. La función
`columns(T,m,k)` omite la recarga inferior final: añadir uno recupera el
ciclo completo. Para un grupo parcial de `R` columnas, añada la recarga
terminal omitida solo si `k` divide `Rm`; su mitad de coste es `m` para
`R` impar y uno para `R` par. Después de combinar ciclos y el grupo
parcial, reste la recarga de la última celda real si `k` divide `N`.

El atajo se usa solo con `2T<min(n,W)`. Un ciclo y su prefijo parcial
visitan menos de `2T` columnas, sin empeorar la cota original de
iteraciones. Los cálculos siguen siendo exactos módulo la respuesta.

Por caso el tiempo es `O(min(n,m)+log(max(k,m)))` y el espacio
aritmético adicional `O(1)`. El término logarítmico corresponde a los
gcd. La entrada completa contiene como máximo diez casos.

El área, los productos ordinales utilizados y la suma del prefijo
seleccionado caben en 64 bits: esta última no supera `m·10^6≤10^18`. Las
sumas completas de progresiones y ciclos pueden rondar `10^30`. C++ y
Rust usan intermedios de 128 bits. Go, Java y Python dividen primero un
factor par de la progresión entre dos y luego reducen los factores
módulo el módulo; el producto reducido es menor que `MOD²<2^63`. Go y
Java reducen también los factores del ciclo completo. Esto conserva la
respuesta y evita desbordamiento.

No gire la cuadrícula, recargue tras la última celda ni cobre un paso
inicial. El residuo triangular cero cuesta uno. El prefijo
complementario tiene longitud `L-r-1`, descontando el uno especial final
del período. Conserve las correcciones de transiciones superior e
inferior. Divida el factor par antes de multiplicar módulo y no
construya la cuadrícula ni enumere todas las recargas.

## Notas por lenguaje

Todas las versiones usan gcd entero y bucles escalares. C++ y Rust
conservan sumas grandes exactas en 128 bits; Go 1.14 y Java 8 mantienen
sumas modulares de 64 bits, con entrada numérica con búfer en Java.
Python usa el período adicional de columnas y acumulación modular
acotada, y se selecciona PyPy 3.10. Los búferes solo contienen hasta
diez casos y sus respuestas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2043_math.cpp](2043_math.cpp) | G++ 13.2 x64 | math | O(min(n,m)+log(max(k,m))) | AC | 0.187 s | 440 KB |
| [2043_math.go](2043_math.go) | Go 1.14 x64 | math | O(min(n,m)+log(max(k,m))) | AC | 0.328 s | 1108 KB |
| [2043_math.java](2043_math.java) | Java 1.8 | math | O(min(n,m)+log(max(k,m))) | AC | 1.218 s | 552 KB |
| [2043_math.py](2043_math.py) | PyPy 3.10 x64 | math | O(min(n,m)+log(max(k,m))) | AC | 0.171 s | 2328 KB |
| [2043_math.rs](2043_math.rs) | Rust 1.75 x64 | math | O(min(n,m)+log(max(k,m))) | AC | 0.218 s | 248 KB |
