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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1884_sorting.cpp](1884_sorting.cpp) | G++ 13.2 x64 | sorting | O((n + m) log(n + m)) | AC | 0.031 s | 216 KB |
| [1884_sorting.go](1884_sorting.go) | Go 1.14 x64 | sorting | O((n + m) log(n + m)) | AC | 0.031 s | 1196 KB |
| [1884_sorting.java](1884_sorting.java) | Java 1.8 | sorting | O((n + m) log(n + m)) | AC | 0.171 s | 3200 KB |
| [1884_sorting.py](1884_sorting.py) | Python 3.12 x64 | sorting | O((n + m) log(n + m)) | AC | 0.093 s | 524 KB |
| [1884_sorting.rs](1884_sorting.rs) | Rust 1.75 x64 | sorting | O((n + m) log(n + m)) | AC | 0.031 s | 280 KB |
