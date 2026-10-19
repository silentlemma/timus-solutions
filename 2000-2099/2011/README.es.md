# 2011. Al Menos Seis Ordenaciones Distintas

[Timus 2011](https://acm.timus.ru/problem.aspx?space=1&num=2011) · dificultad 103 · combinatorics

Problema original de Alexey Kungurtsev, del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dispones de `n` símbolos de tres tipos posibles. Ordena todos para
formar una palabra de longitud `n`; los símbolos iguales son
indistinguibles. Decide si existen al menos seis palabras diferentes.
Cada símbolo disponible debe usarse exactamente una vez.

## Entrada

La primera línea contiene `n`, `1 ≤ n ≤ 100`. La segunda contiene `n`
enteros entre 1 y 3 que indican los tipos. Tiempo límite 0,5 segundos y
memoria 64 MB.

## Salida

Escribe `Yes` si existen al menos seis palabras, y `No` en caso
contrario. Se distinguen mayúsculas y minúsculas. La respuesta única se
compara por tokens.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
6
1 2 2 3 3 3
```

```
Yes
```

Las multiplicidades son 1, 2 y 3. Hay `6!/(1!·2!·3!)=60` palabras
distintas, de modo que la respuesta es `Yes`.

## Solución

Para un prefijo de longitud `i` con cantidades `c1,c2,c3`, el número
exacto es `i!/(c1!·c2!·c3!)`: intercambiar símbolos iguales no cambia la
palabra. Los factoriales completos desbordarían enteros de tamaño fijo.
Solo necesitamos alcanzar seis.

Empieza con los tres contadores a cero y `ways=1` para el prefijo vacío.
Añade los símbolos en su orden de entrada. Si el tipo añadido es `v`,
aumenta su cantidad a `c` y la longitud a `i`, y actualiza `ways =
ways·i/c`. Primero multiplica y después divide. El cociente es exacto:
el numerador gana el factor `i`, mientras que en el denominador solo el
factorial del tipo añadido gana el factor `c`.

Cuando `ways≥6`, devuelve `Yes`. Los símbolos restantes no pueden
reducir la cantidad: añade una misma secuencia fija de los símbolos
restantes a cada palabra distinta del prefijo. Las palabras completas
siguen siendo diferentes y usan todos los símbolos. Si ningún prefijo
alcanza seis, el resultado exacto final es menor y se devuelve `No`.

Por inducción, el contador es exacto en cada paso anterior al retorno,
pues la actualización es la razón de dos coeficientes multinomiales
consecutivos. La extensión con un sufijo fijo prueba la validez de una
respuesta positiva temprana. Sin retorno temprano, el contador final
exacto decide la condición. Esto demuestra la corrección.

Antes de actualizar, `ways≤5` e `i≤100`, así que el producto no supera
500. Bastan enteros ordinarios; no hay redondeo, módulo, saturación
imprecisa ni factoriales desbordados. Se guardan tres cantidades con
índice `v−1`. Cinco símbolos iguales y uno distinto producen exactamente
seis palabras; cuatro y uno producen cinco. Si todos son iguales siempre
hay una sola palabra.

Tiempo `O(n)` y estado de conteo adicional `O(1)`. Los programas
completos conservan los símbolos de entrada y usan espacio total `O(n)`.
Otra opción consiste en multiplicar coeficientes binomiales para las
tres cantidades y detenerse al alcanzar el mismo umbral.

## Notas por lenguaje

Cuenta palabras distintas, no permutaciones de piezas numeradas.
Exactamente seis también sirve. No dividas `ways/c` antes de
multiplicar: la división intermedia podría no ser exacta. No limites el
valor a seis para seguir una recurrencia exacta; devuelve
inmediatamente. Los cinco programas hacen división entera después de
multiplicar. Python usa CPython y no necesita aritmética de grandes
enteros en el solucionador. Go 1.14, Java 8 y Rust 1.75 solo requieren
enteros comunes y tres contadores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2011_combinatorics.cpp](2011_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.031 s | 380 KB |
| [2011_combinatorics.go](2011_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 1112 KB |
| [2011_combinatorics.java](2011_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.109 s | 408 KB |
| [2011_combinatorics.py](2011_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.109 s | 516 KB |
| [2011_combinatorics.rs](2011_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 232 KB |
