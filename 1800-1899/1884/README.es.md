# 1884. Camino a la universidad

[Timus 1884](https://acm.timus.ru/problem.aspx?space=1&num=1884) · dificultad 675 · sorting

Problema original de Egor Shchelkonogov, del Concurso Regional por Equipos de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Egor quiere cruzar una calle de dos carriles de 2 metros, andando en
perpendicular a 5 km/h sin pararse. Se circula por la derecha, así que
los n coches que vienen por la izquierda usan el carril cercano y los m
de la derecha el lejano. Cada coche mide 2 m de ancho y 5 m de largo y
va a 20 km/h; se dan las distancias hasta ellos. ¿Cuánto tiempo mínimo
debe esperar Egor antes de empezar?

## Entrada

n (1 ≤ n ≤ 300) y las distancias a los coches de la izquierda, luego m
(1 ≤ m ≤ 300) y las distancias a los de la derecha. Las distancias van
de 1 a 10 000 metros y crecen al menos 5 en cada fila.

## Salida

El menor tiempo de espera en segundos, con al menos seis cifras tras el
punto decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
1
1
100
```

Salida:

```
1.080000
```

## Solución

Se mide el tiempo en unidades de 1/50 s para que todo sea entero: un
coche a 20 km/h recorre un metro en 9 unidades, y Egor cruza un carril
en 72. Un coche a distancia d está en el camino de Egor de 9d a
9(d + 5). Empezando en s, Egor está en el carril cercano de s a s + 72 y
en el lejano de s + 72 a s + 144. Un coche hace malo s cuando estos
tiempos se solapan en más de un punto. Es un intervalo abierto de
salidas malas: (9d − 72, 9(d + 5)) para un coche de la izquierda y
(9d − 144, 9(d + 5) − 72) para uno de la derecha. Se ordenan los
intervalos por su extremo izquierdo y se recorre desde s = 0: mientras
el siguiente intervalo empiece antes de s, s pasa a su extremo derecho
si es posterior. El primer intervalo que empieza en s o después acaba el
recorrido. Se escribe s/50. `O((n + m) log(n + m))`.

En el ejemplo el coche de la izquierda impide las salidas antes de 54
unidades, y el de la derecha solo (756, 873), así que Egor espera
54/50 = 1.08 s.

Trampas:

- rozar un coche solo en un instante está permitido, así que los
  intervalos son abiertos: un coche a 8 m por la izquierda deja salir
  enseguida;
- los coches de la derecha solo importan mientras Egor está en el
  carril lejano, 72 unidades más tarde;
- las unidades enteras evitan errores de redondeo cuando el hueco entre
  coches es justo el necesario.

Las esperas coinciden con una búsqueda sobre cada instante de salida en
pasos de 1/50 s en 26 calles aleatorias, y con una implementación
aceptada independiente en 100.

## Soluciones optimizadas

La versión en C++ mezcla las listas ya ordenadas de inicios de intervalos de ambos carriles. Mantiene la primera hora de partida posible. Si el siguiente intervalo abierto comienza en ese instante o después, se puede partir. De lo contrario, el intervalo puede desplazar la partida hasta su extremo derecho. La mezcla tarda O(n + m) y los datos de los carriles ocupan O(n + m). Las métricas corresponden al envío 11317001.

La versión para Java 1.8 también combina las listas ordenadas de intervalos abiertos y retrasa el inicio solo cuando un intervalo lo cubre. El envío 11317148 tardó 0.234 s y usó 392 KB frente a 0.171 s y 3200 KB de la base.

Rust guarda los intervalos del carril cercano y los combina con los del lejano a medida que los lee. Rust 1.75 x64, envío 11323323. Tiempo 0,015 → 0,046 s, memoria 268 → 56 KB.

La versión para Python 3.12 x64 también combina las listas ordenadas de intervalos abiertos y retrasa el inicio solo cuando un intervalo lo cubre. El envío 11317139 tardó 0.062 s y usó 552 KB frente a 0.078 s y 472 KB de la base.

La versión para Go 1.14 x64 también combina las listas ordenadas de intervalos abiertos y retrasa el inicio solo cuando un intervalo lo cubre. El envío 11317133 tardó 0.015 s y usó 1136 KB frente a 0.046 s y 1192 KB de la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321924 · Java 1.8 №11321925 · Go 1.14 x64 №11322075 · Python 3.12 x64 №11322076 · Rust 1.75 x64 №11321926.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1884_sorting.cpp](1884_sorting.cpp) | G++ 13.2 x64 | sorting | O((n + m) log(n + m)) | AC | 0.015 s | 196 KB | 11321924 |
| [1884_sorting.go](1884_sorting.go) | Go 1.14 x64 | sorting | O((n + m) log(n + m)) | AC | 0.046 s | 1192 KB | 11322075 |
| [1884_sorting.java](1884_sorting.java) | Java 1.8 | sorting | O((n + m) log(n + m)) | AC | 0.14 s | 3228 KB | 11321925 |
| [1884_sorting.py](1884_sorting.py) | Python 3.12 x64 | sorting | O((n + m) log(n + m)) | AC | 0.078 s | 472 KB | 11322076 |
| [1884_sorting.rs](1884_sorting.rs) | Rust 1.75 x64 | sorting | O((n + m) log(n + m)) | AC | 0.015 s | 268 KB | 11321926 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1884_two_pointers.cpp](1884_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n + m) | AC | 0.001 s | 124 KB | 11317001 |
| [1884_two_pointers.go](1884_two_pointers.go) \* | Go 1.14 x64 | two_pointers | O(n + m) | AC | 0.015 s | 1136 KB | 11317133 |
| [1884_two_pointers.py](1884_two_pointers.py) \* | Python 3.12 x64 | two_pointers | O(n + m) | AC | 0.062 s | 552 KB | 11317139 |
| [1884_two_pointers.rs](1884_two_pointers.rs) \* | Rust 1.75 x64 | two_pointers | O(n + m) | AC | 0.046 s | 56 KB | 11323323 |
| [1884_two_pointers.java](1884_two_pointers.java) \* | Java 1.8 | two_pointers | O(n + m) | AC | 0.234 s | 392 KB | 11317148 |

\* La versión en Go está aceptada y aún queda por alcanzar el objetivo de clasificación. La versión en Python está aceptada y aún queda por alcanzar el objetivo de clasificación. La versión en Rust está aceptada y aún queda por alcanzar el objetivo de clasificación. La versión en Java está aceptada y aún queda por alcanzar el objetivo de clasificación.
