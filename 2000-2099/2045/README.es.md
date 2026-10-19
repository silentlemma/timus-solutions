# 2045. Construir una cantidad exacta de palíndromos distintos

[Timus 2045](https://acm.timus.ru/problem.aspx?space=1&num=2045) · dificultad 478 · constructive

Problema original de Mikhail Rubinchik, del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada entero `1≤i≤n`, construir una palabra de longitud `n` formada
por letras latinas minúsculas y con exactamente `i` subcadenas
palíndromas no vacías distintas, o indicar que no existe. Las subcadenas
son contiguas. Un mismo valor cuenta una sola vez aunque aparezca en
varias posiciones. Un palíndromo se lee igual en ambos sentidos.

## Entrada

Un entero `1≤n≤2000`. Límites: 0,5 segundos y 64 MB.

## Salida

Imprimir `n` líneas en orden. La línea `i` tiene formato `i : word` o `i
: NO`. Cada palabra debe tener exactamente `n` letras minúsculas y `i`
palíndromos no vacíos distintos.

Se acepta cualquier construcción válida. El comprobador verifica número
y orden de líneas, dos puntos, longitud, alfabeto y cantidad real de
palíndromos distintos mediante un árbol de palíndromos. Solo acepta `NO`
cuando `i<min(n,3)`; no compara la palabra con una construcción fija.

## Evaluación

Un comprobador verifica el formato, la longitud y las letras de cada
palabra y cuenta sus palíndromos distintos con un árbol palindrómico;
`NO` solo se acepta si no existe ninguna palabra. Se acepta cualquier
palabra válida.

## Ejemplos

```
4
```

```
1 : NO
2 : NO
3 : abca
4 : bbca
```

Una palabra de longitud cuatro no puede tener solo uno o dos palíndromos
distintos. `abca` contiene únicamente `a,b,c`; `bbca` contiene
`b,c,a,bb`. Los programas pueden imprimir otras palabras válidas.

## Solución

Tratar primero las longitudes más pequeñas. Para `n=1` usar `a`. Para
`n=2` es imposible un único palíndromo y `aa` proporciona dos: `a` y
`aa`.

Con `n≥3`, imprimir `NO` para los objetivos uno y dos. Para cada
`3≤i≤n`, definir `k=i-3`. Imprimir `k` copias de `a` y después los
primeros `n-k` caracteres de la palabra periódica infinita `bcdbcdbcd…`.

### Corrección

Toda palabra de longitud al menos tres contiene al menos tres
palíndromos distintos. Si emplea tres letras o más, bastan sus
subcadenas de una letra. Si solo emplea una, sus prefijos de longitudes
uno, dos y tres son diferentes palíndromos. Si emplea exactamente dos
letras, ya existen ambos palíndromos unitarios; dos letras iguales
adyacentes dan un tercero de longitud dos, y si ninguna pareja adyacente
coincide, las primeras tres letras alternan y forman un tercero de
longitud tres. Para longitud dos, el mínimo es dos: letras diferentes
dan dos unitarios, e iguales dan el unitario y la pareja. Los objetivos
imposibles son, por tanto, exactamente `i<min(n,3)`.

La cola construida tiene longitud `n-k=n-i+3≥3` e incluye `b,c,d`. No
tiene palíndromos de longitud dos ni tres, porque letras adyacentes y
separadas por una posición son distintas. Todo palíndromo mayor contiene
uno central de longitud dos o tres al eliminar sus extremos
repetidamente. Así la cola tiene exactamente sus tres palíndromos
unitarios.

El bloque inicial aporta precisamente `a,a²,…,a^k`, ninguno si `k=0`.
Una subcadena que cruza la frontera empieza por `a` y termina en `b,c` o
`d`, por lo que no es palíndroma. Los dos conjuntos son disjuntos; suman
`k+3=i` valores y la longitud total es `k+(n-k)=n`. Junto con los casos
pequeños y la cota inferior, esto prueba todas las palabras y todos los
`NO`.

### Complejidad

Construir e imprimir una palabra cuesta `O(n)`. Hay `n` líneas, por lo
que el tiempo total es `O(n^2)` y el espacio auxiliar es `O(n)`
escribiendo cada línea inmediatamente. Para `n` grande son obligatorias
`n-2` palabras de longitud `n`; la propia salida ya requiere `Ω(n^2)`
tiempo.

Trampas:

- Contar valores distintos, no apariciones ni particiones en palíndromos.
- Mantener al menos tres caracteres de cola, incluso para `i=n`.
- La letra del bloque inicial no debe aparecer en la cola; una cola
  binaria alterna crea palíndromos largos.
- Separar los casos `n=1` y `n=2`.
- El comprobador debe admitir palabras válidas distintas del ejemplo y
  de la construcción del programa.

## Notas por lenguaje

Los cinco puertos construyen una sola cola periódica y escriben una
línea cada vez. C++, Go, Python y Rust combinan un prefijo repetido con
el inicio de la cola. Java rellena un arreglo de caracteres por línea.
La salida con búfer evita escribir carácter por carácter y ningún puerto
guarda la respuesta cuadrática completa. Se selecciona CPython 3.12.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2045_constructive.cpp](2045_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.031 s | 1088 KB |
| [2045_constructive.go](2045_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 5888 KB |
| [2045_constructive.java](2045_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.156 s | 5140 KB |
| [2045_constructive.py](2045_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.203 s | 692 KB |
| [2045_constructive.rs](2045_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 956 KB |
