# 1519. Fórmula 1

[Timus 1519](https://acm.timus.ru/problem.aspx?space=1&num=1519) · dificultad 466 · dp

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un terreno de N × M casillas (2 ≤ N, M ≤ 12) tiene algunas casillas
ocupadas por madrigueras. Un circuito es un único lazo cerrado que pasa
exactamente una vez por cada casilla libre, moviéndose entre casillas
con un lado común. Hay que contar los circuitos; su número cabe en 63
bits.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, y luego N filas de M caracteres: '.' libre, '*' madriguera. Hay
al menos cuatro casillas libres.

## Salida

El número de circuitos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
**..
....
....
....
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
4 4
....
....
....
....
```

Salida:

```
6
```

## Solución

Programación dinámica sobre un perfil quebrado, casilla a casilla por
filas, con la conectividad de los trozos que cruzan el perfil como
estado. El perfil tiene M + 1 conectores: los lados inferiores de las
casillas de la fila anterior o actual y el lado
izquierdo de la casilla actual. Cada conector está vacío o es un
extremo de un trozo de camino, y los dos extremos de cada trozo se
anidan como paréntesis, así que un conector es «(», «)» o nada: 2 bits,
y un estado cabe en 26 bits. En una casilla libre con conector
izquierdo L y superior U:

- sin conectores: se abre un trozo nuevo hacia la derecha y hacia abajo;
- un conector: se continúa a la derecha o hacia abajo;
- «(» y «(»: se unen los trozos, y el «)» pareja de U pasa a «(»;
- «)» y «)»: se unen, y el «(» pareja de L pasa a «)»;
- «)» y «(»: se unen dos trozos en uno;
- «(» y «)»: esto cierra un lazo, permitido solo en la última casilla
  libre y sin otros conectores, y entonces cuenta.

Una madriguera solo deja pasar estados con ambos conectores vacíos. Al
final de cada fila el perfil se desplaza un conector. En el terreno vacío
de 12 × 12 hay como mucho unos 14000 estados a la vez, y el trabajo es
`O(N·M²·S)` con S estados.

Detalles a tener en cuenta:

- el lazo solo puede cerrarse en la última casilla libre, cuando no
  queda nada abierto (prueba 09);
- un número impar de casillas libres, o una zona libre separada del
  resto, da 0 (pruebas 05, 06, 08);
- el terreno vacío de 12 × 12 tiene unos 1.08·10¹⁸ circuitos, así que
  los números necesitan 64 bits (prueba 03);
- las madrigueras sueltas casi nunca dejan circuitos, así que las
  pruebas generadas recortan sobre todo bloques enteros de 2 × 2 (gen1,
  gen2, gen3).

## Soluciones optimizadas

Se mantienen las transiciones de paréntesis y el cierre solo en la última celda libre sin otros extremos. Se transpone si hace falta para tener altura H = max(N, M) y ancho W = min(N, M). C++, Go y Rust reutilizan dos arreglos densos de estados32 y conteos64, con una tabla de65536 posiciones16 para fusionar. El sondeo lineal compara las claves completas. El perfil tiene hasta 13 posiciones. Para t parejas se eligen 2t posiciones y se rellenan con una secuencia equilibrada. Al sumar binom(13, 2t) por el número de Catalan correspondiente se obtienen 41 835 estados. La capacidad inicial de 16 384 crece según se necesita. El desplazamiento de fila es inyectivo y modifica claves sin otro mapa. Python descarta desconexión, desequilibrio de colores y grado menor que dos, integra el emparejamiento y reutiliza dos diccionarios; condiciones necesarias, sin aproximar. Con un máximo de S estados por capa, el tiempo esperado es O(H·W²·S). Los arreglos reducen asignaciones. Se conservan las cinco bases; Java reutiliza la admitida. Python muestra el intérprete de su Accepted real.

La versión nueva usa CPython y la original usa PyPy. Se recortan los bordes formados solo por obstáculos antes de elegir el sentido. Si la altura recortada es par y las mitades son reflejos, calcula solo los perfiles de la mitad superior. La reflexión da los mismos conteos de emparejamientos para la inferior. Solo se unen perfiles con las mismas columnas de cruce. Con más de dos extremos, una pareja común crea un ciclo separado de dos aristas. Una máscara descarta ese caso antes del recorrido. Desde un extremo se alternan las parejas de arriba y de abajo. Si el ciclo pasa por todos los extremos, se multiplican los conteos y se cuentan ambos órdenes cuando los perfiles son distintos. Con cuatro o seis extremos y sin arista común se forma un solo ciclo. La reflexión entre columnas da grupos de igual aporte cuando hay simetría en ambos ejes. En un campo asimétrico ancho se elige el corte con menos cruces posibles en el tercio central y se recorre cada lado hacia él. Tras el recorte ambos lados contienen celdas libres y un ciclo cruza al menos dos veces. Los campos asimétricos estrechos se recorren completos. Si P suma los cuadrados de los tamaños combinados por máscara de cruce, la unión cuesta O(W·P).

El envío aceptado en Python 3.12 x64 tarda 0.703 s frente a 0.609 s de la base y usa 4 880 KB frente a 10768 KB.

Las implementaciones base aceptadas [1519_dp.java](1519_dp.java) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

La base Python fue Accepted con PyPy y excedió el límite con CPython en el test18. El nuevo fuente se verifica por separado; la tabla indica su intérprete Accepted real. No se transfieren veredictos entre fuentes o runtimes.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1519_dp.cpp](1519_dp.cpp) | G++ 13.2 x64 | dp | O(N * M^2 * S) | AC | 0.203 s | 2076 KB | 11287360 |
| [1519_dp.go](1519_dp.go) | Go 1.14 x64 | dp | O(N * M^2 * S) | AC | 0.203 s | 10420 KB | 11287361 |
| [1519_dp.java](1519_dp.java) \* | Java 1.8 | dp | O(N * M^2 * S) | AC | 0.328 s | 18436 KB | 11287364 |
| [1519_dp.py](1519_dp.py) | PyPy 3.10 x64 | dp | O(N * M^2 * S) | AC | 0.609 s | 10768 KB | 11287363 |
| [1519_dp.rs](1519_dp.rs) | Rust 1.75 x64 | dp | O(N * M^2 * S) | AC | 0.062 s | 1600 KB | 11287365 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1519_dp_optimized.cpp](1519_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(H·W²·S) | AC | 0.031 s | 444 KB | 11315274 |
| [1519_dp_optimized.go](1519_dp_optimized.go) \* | Go 1.14 x64 | dp | O(H·W²·S) | AC | 0.031 s | 848 KB | 11315276 |
| [1519_dp_optimized.rs](1519_dp_optimized.rs) | Rust 1.75 x64 | dp | O(H·W²·S) | AC | 0.046 s | 440 KB | 11315281 |
| [1519_dp_optimized.py](1519_dp_optimized.py) \* | Python 3.12 x64 | dp | O(H·W²·S + W·P) | AC | 0.703 s | 4880 KB | 11316056 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
