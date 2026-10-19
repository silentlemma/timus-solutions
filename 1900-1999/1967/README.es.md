# 1967. Concatenación decimal mínima de bloques binarios

[Timus 1967](https://acm.timus.ru/problem.aspx?space=1&num=1967) · difficulty 5141 · greedy

Problema original de Ilya Zvigintsev, del Concurso Individual Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Concatenar las representaciones binarias de 1,2,…,n para formar S.
Dividir S en bloques no vacíos, cortando solo antes de un bit 1, sin
ceros iniciales. Convertir cada bloque a entero decimal positivo y
concatenar sus representaciones en orden. Minimizar el entero final y
dar cualquier partición óptima mediante longitudes en bits. La
representación inicial de 1 pertenece a S. Límites: 1 segundo, 64 MB.

## Entrada

Un entero n, 2≤n≤100 000.

## Salida

Dos líneas: número de bloques y sus longitudes positivas de izquierda
a derecha, cubriendo S exactamente. Cualquier partición que produzca
el mínimo entero decimal es válida.

## Evaluación

Un comprobador verifica el número de bloques, la longitud total y los
inicios válidos, y comprueba la optimalidad con el criterio de
intercambio demostrado abajo; se acepta cualquier división óptima.

## Ejemplos

```
5
```

```
2
1 10
```

## Solución

Para n=5, S=11011100101. El sufijo de cuatro bits 0101 empieza en cero
y no sirve. El de siete bits 1100101 vale 101, que no es menor que 100.
El de diez bits 1011100101 vale 741<1000. La regla toma esos diez bits
y deja el primer 1 aparte: 1||741=1741, frente a 1765 al unirlo todo.

### Regla de intercambio estricto

Sean A,B bloques binarios consecutivos de valores positivos a,b.
B tiene q bits y b tiene d cifras decimales. Separados dan a·10^d+b;
unidos, a·2^q+b. Separar mejora estrictamente si y solo si 10^d<2^q;
llamemos económico a B en ese caso. Si no, unir mejora estrictamente.
La igualdad es imposible con d positivo porque diez tiene factor cinco.

Reemplazar un número decimal local por otro menor también mejora la
concatenación completa con bloques exteriores fijos: una representación
más corta reduce el total de cifras y, a igual longitud, vence el menor
orden lexicográfico tras el mismo prefijo. La regla vale dentro de
cualquier partición.

### El último bloque es forzoso

Si una partición óptima tiene varios bloques, el último debe ser
económico; de otro modo, unir los dos últimos mejora. Tampoco puede
contener un sufijo económico más corto, pues separarlo mejoraría ese
bloque. Por tanto el último es el sufijo propio económico más corto
de toda la cadena restante. Una partición de un bloque también mejora
al separar ese sufijo, cuando existe.

Elegirlo y repetir sobre el prefijo. El prefijo debe ser óptimo porque
añadir el bloque decimal final fijo conserva el orden numérico. Si no
hay sufijo propio económico, cualquier partición múltiple acabaría en
un bloque no económico: dejar el prefijo entero es óptimo. La prueba
sirve para toda cadena binaria que empieza por 1.

### Buscar sin aproximaciones

Un valor de q bits cumple 2^(q−1)≤b<2^q. Si es económico, T=10^d está
entre b y 2^q, por lo que tiene q bits. A la inversa, si 10^d tiene
q bits y un sufijo de q bits es menor, entonces b≥2^(q−1)>10^(d−1):
b tiene realmente d cifras decimales y es económico.

Enumerar 10,100,1000,… por longitud binaria creciente. Exigir que el
sufijo comience por 1 y sea estrictamente menor lexicográficamente
que el umbral de igual longitud. El primero es el sufijo económico más
corto. Si la longitud alcanza la cadena restante, no hay sufijo propio
válido: emitir todo el prefijo. Quitar bloques de derecha a izquierda
y al final invertir sus longitudes.

Generar y guardar potencias bajo demanda. Las versiones nativas
multiplican cadenas binarias arbitrarias por diez con acarreo desde
la derecha; Python usa enteros y bin. No hay límite fijo de longitud,
restricción de entero máquina, logaritmos aproximados ni conversión
decimal del resultado completo.

Sean L=|S| y K la máxima longitud de umbral probada. Una cota conservadora
es tiempo `O(n log n + L K²)` y espacio `O(L+K²)`, incluidos caché y salida.
Cada búsqueda prueba `O(K)` umbrales y compara hasta `O(K²)` bits;
formar S cuesta `O(n log n)`.

`python tests/gen.py 100000 certify` examina los 1 568 946 finales de prefijo
de S para n=100 000 y acumula el trabajo para todo n permitido. Obtiene
K≤226, hasta 461 145 pruebas de umbral, una cota de 2 780 158 caracteres
comparados y 131 447 bloques. El programa no usa esas cifras como tope
ni trunca búsquedas: la prueba de intercambio da corrección y el
certificado reproducible explica el trabajo de todo el dominio finito.

Minimizar primero cifras decimales y después orden lexicográfico.
Incluir el 1 inicial y cortar solo antes de 1. La comparación con 10^d
es estricta. Buscar sufijos de menor a mayor e invertir la respuesta.
Ni 64 ni 128 bits bastan para umbrales; incluso entradas pequeñas usan
bloques largos. No imponer una longitud supuesta ni usar logaritmos flotantes.

## Notas por lenguaje

C++, Go 1.14, Java 8 y Rust 1.75 guardan potencias como cadenas binarias
o vectores de bytes y multiplican por diez con un acarreo pequeño.
Python 3.12 usa enteros exactos y bin, sin convertir el resultado a
decimal gigante. Java compara caracteres sin asignar subcadenas. Todos
usan solo bibliotecas estándar y no usan recursión.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1967_greedy.cpp](1967_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n+L*K^2) | AC | 0.031 s | 3456 KB |
| [1967_greedy.go](1967_greedy.go) | Go 1.14 x64 | greedy | O(n log n+L*K^2) | AC | 0.062 s | 10772 KB |
| [1967_greedy.java](1967_greedy.java) | Java 1.8 | greedy | O(n log n+L*K^2) | AC | 0.187 s | 14964 KB |
| [1967_greedy.py](1967_greedy.py) | Python 3.12 x64 | greedy | O(n log n+L*K^2) | AC | 0.343 s | 9656 KB |
| [1967_greedy.rs](1967_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n+L*K^2) | AC | 0.031 s | 4704 KB |
