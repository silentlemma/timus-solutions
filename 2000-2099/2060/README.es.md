# 2060. Contar apariciones palindrómicas adyacentes

[Timus 2060](https://acm.timus.ru/problem.aspx?space=1&num=2060) · difficulty 650 · strings

Problema original de Mikhail Rubinchik, del Concurso Palindrómico del 11 de julio de 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Contar los pares de palíndromos no vacíos adyacentes de una cadena:
ternas 0 ≤ i ≤ j < k < n en las que s[i..j] y s[j+1..k] son palíndromos.
Textos iguales en posiciones distintas cuentan por separado. Los límites
son 1 segundo y 64 MB.

## Entrada

Una cadena de 1 a 300 000 letras latinas minúsculas.

## Salida

La cantidad exacta.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
abaa
```

```
5
```

Para `abaa`, los números de palíndromos terminados en cada posición son
`E=[1,1,2,2]`, y los iniciados allí son `S=[2,1,2,1]`. Las tres
fronteras interiores aportan `1·1`, `1·2` y `2·1`: cinco en total. La
primera cuenta `a|b` aunque no cubra toda la palabra; la última cuenta
`a|a` y `aba|a`.

## Solución

### Elecciones independientes en cada frontera

Sean `E[j]` las apariciones palindrómicas no vacías terminadas en `j` y
`S[j]` las iniciadas en `j`. En la frontera `j|j+1` se elige una
aparición izquierda entre `E[j]` y una derecha entre `S[j+1]`. Sus
posiciones definen una única terna válida. Recíprocamente, cada terna
define una frontera y ambas elecciones. Por ello la respuesta es
`sum(E[j]·S[j+1])` para `0≤j<n−1`. Se cuentan posiciones, no textos
palindrómicos distintos.

### Los radios de Manacher producen intervalos

Un centro impar `c` con radio `r≥1` incluye el carácter central y
representa longitudes `1,3,…,2r−1`. Sus posiciones finales recorren una
vez `[c,c+r−1]` y las iniciales `[c−r+1,c]`. Para un centro par en el
hueco anterior a `c`, radio `r≥0`, los finales son `[c,c+r−1]` y los
inicios `[c−r,c−1]`. Un radio par cero no aporta nada.

Calcular ambas familias con Manacher. Mantener la ventana palindrómica
que llega más a la derecha. Dentro de ella copiar el radio conocido de
la posición reflejada, limitado por el borde derecho, y después extender
comparando caracteres existentes. Fuera comenzar con uno para centros
impares y cero para pares. La reflexión demuestra la parte copiada y las
comparaciones determinan la extensión máxima. Cada centro causa como
máximo una comparación fallida; las nuevas comparaciones exitosas
avanzan el borde derecho. Cada recorrido cuesta `O(n)`.

Añadir cada intervalo a un arreglo de diferencias: para `[l,r]`
inclusivo, sumar uno en `l` y restar uno en `r+1`, en `O(1)`. Tras todos
los centros, las sumas prefijas producen exactamente `E` y `S`. Cada
aparición tiene un centro, paridad y radio únicos, por lo que contribuye
una vez a su inicio y final. No hay pérdidas ni duplicaciones; la
fórmula de las fronteras completa la demostración.

### Memoria y tamaños enteros

Los dos recorridos comparten un arreglo de radios; reiniciar la ventana
entre ellos. Al procesar el centro par `c`, la ventana procede de un
centro anterior `q<c`, y el índice reflejado es `2q−c<c`. Se lee, por
tanto, un radio par ya sobrescrito, nunca un radio impar antiguo. Los
arreglos de diferencias tienen `n+1` posiciones para permitir restar en
`n`; solo `0..n−1` representan posiciones reales.

Cada contador es como máximo `n` y cabe en 32 bits con signo. Sin
embargo, el producto puede excederlos, y la respuesta alcanza
`n(n−1)(n+1)/6`: existen `C(n+1,3)` ternas posibles y todas son válidas
en una cadena constante. Para `n=300000` se obtiene `4499999999950000`.
C++, Go, Java y Rust convierten a 64 bits con signo antes de
multiplicar; Python usa enteros exactos.

## Notas por lenguaje

Los dos recorridos de Manacher, las actualizaciones, las sumas prefijas
y la suma final requieren `O(n)` tiempo y `O(n)` espacio. Las
implementaciones son iterativas y comparan letras exactamente. Python
utiliza CPython 3.12 y tres arreglos compactos de 32 bits con signo; los
demás lenguajes usan arreglos o vectores enteros. La entrada es una
palabra y la salida un número.

No contar solo el mayor palíndromo de cada posición. Incluir letras
individuales y ambas paridades; excluir el palíndromo par vacío. El
intervalo de inicios de un centro par termina en `c−1`, no en `c`.
Multiplicar `E[j]` por `S[j+1]`, no por `S[j]`, y omitir fronteras
exteriores. No deduplicar textos iguales ni exigir cubrir toda la
palabra. Una sola letra da cero. Convertir antes del producto, no
después de que un entero de 32 bits haya desbordado.

La solución en Python se ejecuta con PyPy: con CPython 3.12 supera el
límite de tiempo en la prueba 49 del juez, mientras que con PyPy 3.10 se
acepta en 0.234 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2060_strings.cpp](2060_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 4268 KB |
| [2060_strings.go](2060_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 9932 KB |
| [2060_strings.java](2060_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 5140 KB |
| [2060_strings.py](2060_strings.py) | PyPy 3.10 x64 | strings | O(n) | AC | 0.234 s | 6988 KB |
| [2060_strings.rs](2060_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 4596 KB |
