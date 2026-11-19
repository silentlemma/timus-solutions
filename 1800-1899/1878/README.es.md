# 1878. El cubo de Rubinchik

[Timus 1878](https://acm.timus.ru/problem.aspx?space=1&num=1878) · dificultad 219 · implementation

Problema original de Denis Mukhametianov, del Concurso Regional Escolar de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un rompecabezas consta de cuatro capas transparentes de 4 × 4 en un
eje común. Cada capa tiene cuatro cuadritos de color, uno de cada uno
de cuatro colores, colocados de modo que un cuarto de vuelta de la capa
lleva cada uno al cuadrante siguiente. Los cuatro cuadritos de cada capa
forman una órbita de ese giro. Todas las capas comparten el mismo orden
cíclico de colores en sentido horario, salvo rotación, como en el
[diagrama original de las capas](https://acm.timus.ru/image/get.aspx/a394d0eb-f9d5-4bc2-846a-74ef972e9e4b).
Vistas desde arriba, las capas
llenan la cuadrícula 4 × 4. Está resuelto cuando cada cuadrante de
2 × 2 es de un solo color. Un movimiento gira una capa 90° en cualquier
sentido. Dada la vista desde arriba, hay que hallar el menor número de
movimientos que lo resuelve.

## Entrada

Cuatro líneas de cuatro colores de 1 a 4: la vista desde arriba.

## Salida

El menor número de movimientos.

## Evaluación

Se comparan los tokens; los espacios adicionales no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1 2 3
1 1 2 2
4 4 3 3
1 4 3 4
```

Salida:

```
1
```

## Solución

Todas las capas comparten el mismo orden cíclico de colores, por lo que
alinear sus cuadritos de color 1 también alinea los demás colores.
Cada capa tiene exactamente un cuadrito de color 1, y su cuadrante
indica la orientación de la capa. Se numeran los cuadrantes en el orden
en que un cuarto de vuelta lleva un cuadrito por ellos (arriba a la
izquierda, arriba a la derecha, abajo a la derecha, abajo a la
izquierda). Está resuelto cuando los cuatro cuadritos de color 1 están
en el mismo cuadrante t. Una capa cuyo cuadrito está en el cuadrante p
necesita min(d, 4 − d) movimientos, con d = (p − t) mod 4. Se prueban
los cuatro t y se toma el más barato. `O(1)`.

En el ejemplo tres cuadritos de color 1 están arriba a la izquierda y
uno abajo a la izquierda, a un cuarto de vuelta: un movimiento.

Trampas:

- alinear solo el color 1 depende del orden cíclico común de los colores
  (como en la prueba 01); tener cada color una vez por capa no basta;
- en el estado resuelto el color 1 puede estar en cualquier cuadrante:
  el cubo puede quedar girado entero;
- una capa a media vuelta cuesta dos movimientos gire hacia donde gire;
- los cuadrantes deben numerarse en círculo, no por filas, para que las
  distancias salgan bien.

La solución en Python coincide con una búsqueda en anchura independiente
mediante giros de las capas físicas en los 1536 estados resolubles,
incluidas todas las correspondencias entre números y colores.

## Soluciones optimizadas

`1878_implementation_optimized.go`. Mantiene barrido de costes hacia cuatro cuadrantes. Lee dieciséis celdas directamente a cuatro contadores y calcula índices horarios aritméticamente, sin guardar celdas. Mismas distancias circulares y empates. Tiempo y espacio constantes para 4×4. Buffers acotados de entrada de 256 bytes y salida de 64 usan syscall.Read/Write de Go 1.14, reintentan EINTR/escrituras parciales y tratan EOF de cero bytes. Elimina inicialización fmt/bufio/os.File. Pruebas Linux y compilación cruzada Windows validan funcionamiento y construcción; las métricas pareadas siguientes vienen de nuestro Accepted exacto en juez Windows. Se conserva fuente didáctica legible.

Frente a `1878_implementation.go`: tiempo 0.031 s → 0.015 s; memoria 1084 KB → 292 KB.

`1878_implementation_optimized.rs`. Mantiene cuatro posibles cuadrantes destino y sus costes. Lee dieciséis celdas a cuatro contadores blancos u8, cada uno hasta cuatro, derivando cuadrante horario aritméticamente sin guardar celdas ni tabla. Salida entera directa. Tiempo y espacio constantes para puzzle 4×4; mantiene distancia circular mínima y empates.

Frente a `1878_implementation.rs`: tiempo 0.046 s → 0.031 s; memoria 208 KB → 60 KB.

Una fórmula de desequilibrio del tablero fijo reemplaza enumerar colores objetivo y distancias modulares. Se cuenta un color en cada cuadrante por filas, se comparan desequilibrios opuestos y se toma el complemento correspondiente. Es esencial el orden cíclico de colores del dibujo; permutar cuadrantes arbitrariamente no equivale. Al ser fijo el tablero, almacenamiento y operaciones son constantes.

- `1878_math.java`: 0.109 s / 440 KB; base `1878_implementation.java`: 0.140 s / 1668 KB; cambio respecto a la base: tiempo -22.1%, memoria -73.6%.
- `1878_math.py`: 0.125 s / 288 KB; base `1878_implementation.py`: 0.093 s / 432 KB; cambio respecto a la base: tiempo +34.4%, memoria -33.3%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1878_implementation_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1878_implementation.cpp](1878_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 108 KB | 11309211 |
| [1878_implementation.go](1878_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1084 KB | 11291010 |
| [1878_implementation.java](1878_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1668 KB | 11291012 |
| [1878_implementation.py](1878_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 432 KB | 11309212 |
| [1878_implementation.rs](1878_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 208 KB | 11309213 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1878_math.java](1878_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 440 KB | 11308562 |
| [1878_math.py](1878_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 288 KB | 11309395 |
| [1878_implementation_optimized.rs](1878_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(1), fixed 16-cell puzzle | AC | 0.031 s | 60 KB | 11325617 |
| [1878_implementation_optimized.go](1878_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(1), fixed 16-cell puzzle | AC | 0.015 s | 292 KB | 11325658 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
