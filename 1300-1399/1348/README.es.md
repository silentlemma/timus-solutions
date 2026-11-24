# 1348. La cabra en el huerto 2

[Timus 1348](https://acm.timus.ru/problem.aspx?space=1&num=1348) · dificultad 177 · geometry

Problema original de Pavel Egorov, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cabra está atada al punto C con una cuerda de longitud L, así que
alcanza todo lo que está a L o menos de C. Un bancal de piñas es el
segmento AB. Hay que hallar cuánto hay que alargar la cuerda para que la
cabra alcance al menos una piña, y cuánto para alcanzarlas todas, con
dos cifras tras el punto. Todos los números son enteros, L ≥ 0, y las
coordenadas valen como mucho 10 000 en valor absoluto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las coordenadas de A, B y C y la longitud L.

## Salida

Los dos alargamientos, uno por línea.

## Evaluación

Las pruebas del repositorio comparan tokens numéricos con |resultado-referencia| <= 0.01·max(1,|referencia|), rechazan valores no finitos y comparan exactamente los tokens no numéricos.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 -6 8 6
0 0 7
```

Salida:

```
1.00
3.00
```

## Solución

El punto más cercano del bancal es la proyección de C sobre la recta
AB, llevada a A o a B si cae fuera del segmento. El punto de un segmento
más lejano de cualquier punto es uno de sus extremos. Así que las
respuestas son max(0, d_cerca − L) y max(0, max(|CA|, |CB|) − L). La
proyección usa t = (C − A) · (B − A) / |B − A|², limitado entre 0 y 1, y
un bancal de un solo punto, A = B, toma t = 0.

L no tiene cota superior, así que se lee como número de coma flotante y
no como entero, que se desbordaría. Un L enorme se convierte en un
número enorme o en infinito, y entonces ambas respuestas son 0, lo cual
es correcto: toda distancia es como mucho 20000√2 < 30000. La geometría
tarda `O(1)`; contando la entrada, el tiempo y el espacio son `O(k)`,
donde k es el número de caracteres de entrada.

Detalles a tener en cuenta:

- el bancal puede ser un solo punto (pruebas 02 y 08);
- con C en la recta del bancal más allá de un extremo, el punto más
  cercano es ese extremo, no la proyección (prueba 04);
- una cuerda que ya basta necesita 0, no un número negativo (prueba 05);
- L puede superar los rangos enteros y de coma flotante (pruebas 09–11):
  como número de coma flotante se vuelve infinito y ambas respuestas son
  0, mientras que un tipo entero se desbordaría.

## Soluciones optimizadas

`1348_geometry_optimized.rs`. Mantiene la proyección acotada al segmento, el extremo lejano y max(distancia-cuerda,0). scanf de siete f64 y printf de dos respuestas a dos decimales sustituyen texto y formato de Rust. El segmento nulo usa su extremo; una cuerda interpretada como infinita da extensiones cero. La geometría usa O(1) operaciones y estado explícito; leer un token de cuerda de k caracteres requiere O(k) tiempo. Su propio Accepted acredita la mejora de memoria.

Frente a `1348_geometry.rs`: tiempo 0.031 s → 0.031 s; memoria 244 KB → 116 KB.

`1348_geometry_optimized.cpp`. Mantiene la proyección sobre el segmento con parámetro limitado a [0,1] y el extremo más lejano para la distancia máxima. scanf/printf de C sustituyen los flujos C++ y la cadena explícita de longitud de cuerda. La geometría sigue en f64; si la cuerda se analiza como infinito positivo, ambas extensiones son cero. Leer su representación de k caracteres cuesta O(k), con estado geométrico explícito constante.

Frente a `1348_geometry.cpp`: tiempo 0.015 s → 0.015 s; memoria 396 KB → 144 KB.

`1348_geometry_optimized.java`. Conserva la misma proyección limitada y geometría de extremos. Un lector de bytes acotado sustituye Scanner; el token de cuerda sin límite de longitud aún se decodifica y pasa a Double.parseDouble. Infinito produce correctamente dos extensiones nulas. Elimina el coste de Scanner sin atribuir memoria constante a una representación arbitrariamente larga: tiempo y almacenamiento del token O(k).

Frente a `1348_geometry.java`: tiempo 0.140 s → 0.109 s; memoria 1856 KB → 1 072 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1348_geometry_optimized.cpp`: puesto de tiempo 1/276 y de memoria 8/276 en esta muestra comparable.

`1348_geometry_optimized.java`: puesto de tiempo 10/47 y de memoria 9/47 en esta muestra comparable.

`1348_geometry_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1348_geometry.cpp](1348_geometry.cpp) | G++ 13.2 x64 | geometry | O(k) | AC | 0.015 s | 396 KB | 11307276 |
| [1348_geometry.go](1348_geometry.go) | Go 1.14 x64 | geometry | O(k) | AC | 0.031 s | 1080 KB | 11307278 |
| [1348_geometry.java](1348_geometry.java) | Java 1.8 | geometry | O(k) | AC | 0.140 s | 1856 KB | 11307281 |
| [1348_geometry.py](1348_geometry.py) | Python 3.12 x64 | geometry | O(k) | AC | 0.078 s | 496 KB | 11307292 |
| [1348_geometry.rs](1348_geometry.rs) | Rust 1.75 x64 | geometry | O(k) | AC | 0.031 s | 244 KB | 11307285 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1348_geometry_optimized.cpp](1348_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(k) | AC | 0.015 s | 144 KB | 11325059 |
| [1348_geometry_optimized.java](1348_geometry_optimized.java) | Java 1.8 | geometry | O(k) | AC | 0.109 s | 1072 KB | 11324783 |
| [1348_geometry_optimized.rs](1348_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(k) | AC | 0.031 s | 116 KB | 11325502 |
