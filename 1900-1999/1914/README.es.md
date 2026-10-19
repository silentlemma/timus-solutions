# 1914. Entradas fraccionarias con salidas enteras

[Timus 1914](https://acm.timus.ru/problem.aspx?space=1&num=1914) · difficulty 3724 · matrix

Problema original de Alexander Ipatov (preparado por Dmitry Ivankov), de la subregión oriental del NEERC 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una matriz entera n×n transforma los giros reales de n controles accesibles
en los de n controles protegidos. Inicialmente los giros son enteros.
Determinar si existe un vector real x con alguna coordenada no entera
tal que todas las coordenadas de Ax sean enteras. Solo se pide existencia.
Límites: 2 segundos, 64 MB.

## Entrada

n, 1≤n≤100, seguido de n filas de n enteros en [−100,100].
El elemento de fila j y columna i indica la respuesta del control protegido
j a una vuelta antihoraria del accesible i. Los valores negativos indican
sentido horario; los giros de entrada pueden ser reales arbitrarios.

## Salida

Escribir `Power of magic saves lives` si existe el vector; en otro caso,
`Death`.

## Evaluación

Comparación exacta de tokens; no se imprimen giros ni determinantes aproximados.

## Ejemplos

```
3
1 2 0
4 3 0
0 0 0
```

```
Power of magic saves lives
```

## Solución

La respuesta es `Death` exactamente cuando det(A)=±1.

Si A es singular, escalar un vector no nulo de su núcleo hasta que alguna
coordenada tenga valor absoluto entre 0 y 1; su imagen es cero. Si det(A)=±1,
la fórmula de la adjunta hace A⁻¹ entera, y Ax entero implica x entero.
Si |det(A)|>1, alguna columna de A⁻¹ debe ser no entera: de lo contrario
una matriz entera tendría determinante no entero 1/det(A). Esa columna
se transforma en un vector unitario entero y satisface la condición.

### Certificado modular exacto

C++, Go, Java y Rust calculan determinantes mediante eliminación gaussiana
módulo distintos primos fijos p entre 2²⁹ y 2³⁰. Se intercambian filas,
se invierte cada pivote con a^(p−2) mod p, y un pivote inexistente da
determinante cero. Normalizar negativos y registrar el signo de los intercambios.

Un determinante entero ±1 debe conservar el mismo signo en todos los
primos. Si algún residuo no es 1 ni p−1, o los signos discrepan, no es
unitario. La comprobación es determinista y finita: cada norma de fila es
≤100√n≤1000<2¹⁰ y Hadamard da |det(A)|<2^(10n).
Tomar K=ceil((10n+1)/29)≤35 primos: su producto M>2^(10n+1).
Si todos los residuos corresponden al mismo signo s, M divide det(A)−s,
cuyo valor absoluto es menor que M. Por tanto det(A)=s exactamente.
No se reconstruye el número ni se necesita aritmética grande.
Los productos modulares son menores que 2⁶⁰ y caben en 64 bits.

### Python sin fracciones

Python usa enteros de precisión arbitraria con Bareiss. Si p es el pivote
actual y q el anterior, inicialmente 1, cada elemento pendiente se reemplaza
por (aᵢⱼp−aᵢₖaₖⱼ)/q, y se anula la columna bajo el pivote. La identidad
de menores garantiza divisiones exactas. Intercambiar una fila no nula
cuando sea necesario; si no existe, la matriz es singular. El último
elemento diagonal es el determinante salvo el signo de los intercambios,
irrelevante al comparar su valor absoluto. Para n=1 se comprueba el único valor.

Ambos métodos deciden el mismo criterio exacto. Las versiones modulares
usan `O(n³K + nK log p)` operaciones modulares y `O(n²)` palabras.
Bareiss usa `O(n³)` operaciones con enteros grandes y `O(n²)` enteros;
el coste aritmético depende de su longitud en bits.

El ejemplo es singular por su fila final nula. El escalar cero permite
solución, ±1 no, y el coeficiente 2 convierte media vuelta en salida entera.

La invertibilidad no es el criterio: solo ±1 impiden la entrada requerida.
Conservar el signo entre primos, tratar pivotes cero y negativos e intercambios,
y no limitarse a unos pocos módulos aleatorios. El determinante flotante
puede perder un pequeño entero tras cancelaciones. Transponer no altera
el determinante; intercambiar filas cambia el signo.

## Notas por lenguaje

Los cuatro puertos modulares usan productos de 64 bits y hasta 35 primos
verificados. Rust guarda residuos sin signo; los demás los normalizan
como enteros no negativos. Java usa entrada por bytes. Python divide
exactamente, sin eliminación flotante. Cada programa usa solo la biblioteca estándar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1914_matrix.cpp](1914_matrix.cpp) | G++ 13.2 x64 | matrix | O(K n^3) | AC | 0.125 s | 544 KB |
| [1914_matrix.go](1914_matrix.go) | Go 1.14 x64 | matrix | O(K n^3) | AC | 0.156 s | 4660 KB |
| [1914_matrix.java](1914_matrix.java) | Java 1.8 | matrix | O(K n^3) | AC | 0.359 s | 3412 KB |
| [1914_matrix.py](1914_matrix.py) | Python 3.12 x64 | matrix | O(K n^3) | AC | 0.390 s | 2820 KB |
| [1914_matrix.rs](1914_matrix.rs) | Rust 1.75 x64 | matrix | O(K n^3) | AC | 0.140 s | 388 KB |
