# 1889. Avisos del aeropuerto

[Timus 1889](https://acm.timus.ru/problem.aspx?space=1&num=1889) · dificultad 308 · bruteforce

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Igor oyó n frases de un aviso y conoce el idioma de algunas; las demás
son "unknown". El aviso se leyó en varios idiomas, cada uno como mucho
una vez y con el mismo número de frases en cada uno. ¿En cuántos
idiomas pudo leerse? Hay que listar todas las posibilidades en orden
creciente, o escribir "Igor is wrong." si no hay ninguna.

## Entrada

n (2 ≤ n ≤ 1000) y luego n líneas con el nombre de un idioma (de 4 a 20
letras minúsculas) o "unknown"; al menos una frase es conocida.

## Salida

Todos los números de idiomas posibles en orden creciente, o
"Igor is wrong.".

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
english
unknown
unknown
unknown
german
unknown
```

Salida:

```
2 3 6
```

### Ejemplo 2

Entrada:

```
4
english
french
unknown
english
```

Salida:

```
Igor is wrong.
```

### Ejemplo 3

Entrada:

```
3
zulu
zulu
zulu
```

Salida:

```
1
```

## Solución

Si el aviso se leyó en k idiomas, k divide a n y las frases se reparten
en k bloques consecutivos de n/k, un bloque por idioma. Para cada
divisor k se comprueban dos cosas. Las frases conocidas de un bloque
deben estar todas en un mismo idioma. Ningún idioma puede aparecer en
dos bloques distintos. Los bloques sin frases conocidas pueden ser de
cualquier idioma nuevo. Con conjuntos hash se espera `O(n·d(n))`;
con el conjunto ordenado de C++, `O(n·d(n)·log n)`.

En el primer ejemplo un solo bloque tendría inglés y alemán, así que 1
falla. Con 2 los bloques son "english ? ?" y "? german ?", con 3 son
parejas con el inglés en la primera y el alemán en la tercera, y 6
siempre es posible aquí: la respuesta es 2 3 6.

Trampas:

- el mismo idioma en dos bloques descarta k, como en el tercer ejemplo
  con 3 idiomas;
- un bloque solo con frases desconocidas es válido;
- la línea de salida es "Igor is wrong." con el punto.

Las respuestas coinciden con una implementación aceptada independiente
en 125 avisos aleatorios.

## Soluciones optimizadas

`1889_bruteforce_optimized.java`. Sigue probando divisores k de n y coherencia por bloque. Asigna una vez IDs positivos a idiomas conocidos y cero a unknown. int[] con generaciones impide que un conocido aparezca en dos bloques, sin HashSet nuevo ni comparaciones de cadenas por divisor. Cada bloque permite un ID conocido; bloques desconocidos reciben idiomas distintos sin usar. k creciente y frase de fallo exacta. Con tau(n) divisores y nombres<=20, tiempo esperado O(n·tau(n)), espacio O(n); hash esperado, sin promesa peor caso. Mismo algoritmo exhaustivo con datos compactos y entrada256bytes.

Frente a `1889_bruteforce.java`: tiempo 0.125 s → 0.109 s; memoria 684 KB → 708 KB.

Go comprime las frases conocidas en grupos consecutivos de idioma y guarda el nombre y los índices inicial y final. Una tabla de direccionamiento abierto rechaza un idioma que reaparece tras otro conocido. Para cada divisor de n, cada grupo debe ocupar un único bloque y los grupos distintos deben usar bloques distintos. d(n) cuenta los divisores de n. Las colisiones pueden hacer cuadrática la construcción de grupos en el peor caso. La entrada y salida usan búferes fijos de bytes; los nombres se comparan exactamente en matrices de 20 bytes incluso cuando hay colisiones de hash.

Las implementaciones base aceptadas [1889_bruteforce.cpp](1889_bruteforce.cpp), [1889_bruteforce.java](1889_bruteforce.java), [1889_bruteforce.py](1889_bruteforce.py), [1889_bruteforce.rs](1889_bruteforce.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`1889_bruteforce_optimized.java`: puesto de tiempo 6/22 y de memoria 1/22 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1889_bruteforce.cpp](1889_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n d(n) log n) | AC | 0.001 s | 512 KB | 11325660 |
| [1889_bruteforce.go](1889_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n d(n)) | AC | 0.031 s | 1236 KB | 11291120 |
| [1889_bruteforce.java](1889_bruteforce.java) | Java 1.8 | bruteforce | O(n d(n)) | AC | 0.125 s | 684 KB | 11291124 |
| [1889_bruteforce.py](1889_bruteforce.py) \* | Python 3.12 x64 | bruteforce | O(n d(n)) | AC | 0.078 s | 528 KB | 11325663 |
| [1889_bruteforce.rs](1889_bruteforce.rs) \* | Rust 1.75 x64 | bruteforce | O(n d(n)) | AC | 0.046 s | 448 KB | 11325666 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1889_bruteforce_optimized.go](1889_bruteforce_optimized.go) \* | Go 1.14 x64 | bruteforce | O(n² + n d(n)) worst case | AC | 0.031 s | 792 KB | 11311147 |
| [1889_bruteforce_optimized.java](1889_bruteforce_optimized.java) \* | Java 1.8 | bruteforce | O(n tau(n)) expected | AC | 0.109 s | 708 KB | 11325437 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
