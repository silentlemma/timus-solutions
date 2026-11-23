# 1258. Billar en la oficina

[Timus 1258](https://acm.timus.ru/problem.aspx?space=1&num=1258) · dificultad 417 · geometry

Problema original de Pavel Egorov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un programador camina en línea recta por una habitación de W × D
(2 ≤ W, D ≤ 1000) y rebota en las paredes como una bola de billar. El
inicio y el final son puntos enteros estrictamente dentro de la
habitación, y los choques con las paredes se dan en orden: L, R, F, B
para la pared izquierda (x = 0), derecha (x = W), delantera (y = 0) y
trasera (y = D), como mucho 1000 choques y nunca en una esquina. Hay que
hallar la longitud del recorrido, redondeada a cuatro cifras tras el
punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

W y D, luego x0 y0, luego x1 y1 y después la cadena de choques (puede
estar vacía).

## Salida

La longitud del recorrido.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 20
9 1
1 19
FLRLRB
```

Salida:

```
52.8015
```

## Solución

En lugar de girar a quien camina, se refleja la habitación en cada
choque: el recorrido se vuelve un único segmento, cuyas extensiones
horizontal y vertical se suman por separado.

En x solo cuentan los choques L y R, que por fuerza se alternan. Si no
hay ninguno, la extensión es |x1 − x0|. Si no, primero se llega a la
primera pared lateral (x0 para L, W − x0 para R), entre cada dos choques
laterales seguidos se cruza la habitación de ancho W, y desde la última
pared lateral se va al final (x1 para L, W − x1 para R):

```text
dx = first + (k − 1) · W + last
```

Lo mismo con F, B y D da dy, y la respuesta es √(dx² + dy²). El orden en
que se intercalan los choques laterales y los delanteros o traseros no
cambia la longitud. `O(K)` para K choques.

Detalles a tener en cuenta:

- incluso en la habitación más pequeña, el recorrido debe evitar las
  esquinas; un solo choque con una pared es posible (prueba 07);
- la línea de choques puede estar vacía o faltar del todo (prueba 02);
- el primer choque de un eje puede ser con cualquiera de sus dos paredes
  (pruebas 03, 06);
- dx y dy llegan a unos 10⁶, así que dx² + dy² necesita 64 bits
  (prueba 08).

Las respuestas se compararon en 200 casos con la longitud del segmento
recto a partir del cual se construyó cada prueba aleatoria (sus cortes
con la cuadrícula reflejada dan los choques).

## Soluciones optimizadas

La nueva versión Python refleja el destino siguiendo los choques al revés: L cambia x por −x, R por 2W−x, F cambia y por −y y B por 2D−y. Cada reflexión deshace un rebote y conserva la longitud, dejando un segmento recto desde el inicio. Desaparecen las listas separadas de choques por eje y la importación de math; se usa la potencia 0.5 y se imprimen cuatro decimales. Tiempo O(K) y espacio O(K) para la entrada dividida en palabras. Se conservan Python ordinario y las demás bases, cuatro de las cuales ya cubren el conjunto rápido.

Las implementaciones base aceptadas [1258_geometry.cpp](1258_geometry.cpp), [1258_geometry.go](1258_geometry.go), [1258_geometry.java](1258_geometry.java), [1258_geometry.rs](1258_geometry.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1258_geometry_implementation_optimized.py`. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328529 (Python 3.12 x64): **0.062 s / 760 KB**. Comparación archivada: `1258_geometry_optimized.py` (Python 3.12 x64) — 0.093 s / 396 KB (#11314897).

`1258_geometry_optimized.rs`. En un recorrido se cuentan los golpes y se recuerdan la primera y última pared de cada eje. Un estado constante sustituye la lista completa y sus dos copias filtradas; no cambia la fórmula de distancia desplegada.

Accepted #11328695 (Rust 1.75 x64): **0.015 s / 244 KB**. Comparación archivada: `1258_geometry.rs` (Rust 1.75 x64) — 0.046 s / 264 KB (#11284107).

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes cuentan los choques por eje y usan la misma
  fórmula.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1258_geometry.cpp](1258_geometry.cpp) | G++ 13.2 x64 | geometry | O(K) | AC | 0.001 s | 220 KB | 11284098 |
| [1258_geometry.go](1258_geometry.go) | Go 1.14 x64 | geometry | O(K) | AC | 0.031 s | 1120 KB | 11284100 |
| [1258_geometry.java](1258_geometry.java) | Java 1.8 | geometry | O(K) | AC | 0.109 s | 1532 KB | 11284105 |
| [1258_geometry.py](1258_geometry.py) | Python 3.12 x64 | geometry | O(K) | AC | 0.125 s | 504 KB | 11284104 |
| [1258_geometry.rs](1258_geometry.rs) | Rust 1.75 x64 | geometry | O(K) | AC | 0.046 s | 264 KB | 11284107 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1258_geometry_optimized.py](1258_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(K) | AC | 0.093 s | 396 KB | 11314897 |
| [1258_geometry_implementation_optimized.py](1258_geometry_implementation_optimized.py) | Python 3.12 x64 | geometry, implementation | O(K) | AC | 0.062 s | 760 KB | 11328529 |
| [1258_geometry_optimized.rs](1258_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(K) | AC | 0.015 s | 244 KB | 11328695 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
