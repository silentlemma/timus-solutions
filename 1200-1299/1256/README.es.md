# 1256. El guarda del cementerio

[Timus 1256](https://acm.timus.ru/problem.aspx?space=1&num=1256) · dificultad 2290 · geometry

Problema original de Alexander Petrov (preparado por Alexander Mironenko), del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos perros están atados con cadenas de longitud R4 a dos postes. La
caseta del guarda está a R1 del primer poste y a R2 del segundo; los
postes distan R3 (0 ≤ R1, R2, R3 ≤ 20000, 1 ≤ R4 ≤ 20000). Quien hace
la guardia sale de la caseta, deja un cuenco donde cada perro pueda
alcanzarlo y vuelve. Hay que hallar el recorrido más corto, con tres
cifras tras el punto. La vuelta cuenta: en el ejemplo son 1750 de ida y
1750 de vuelta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

R1, R2, R3 en la primera línea (pueden ser fraccionarios) y el entero R4
en la segunda.

## Salida

La longitud del recorrido más corto.

## Ejemplos

### Ejemplo 1

Entrada:

```
1000 2000 1000
250
```

Salida:

```
3500.000
```

## Solución

Cada perro alcanza un disco de radio R = R4 alrededor de su poste. Se
pone el poste A en el origen, el poste B en (R3, 0) y la caseta H a
distancias R1 y R2 de ellos. El recorrido es H → P → Q → H con P en el
disco A y Q en el disco B; el otro orden es el mismo recorrido al revés.

Si la caseta está dentro de uno de los discos, ese perro come en la
puerta y solo hay que ir al otro disco y volver:
2 · max(0, max(R1, R2) − R).

Si no, se fija P. Si el segmento de P a H cruza el disco B, el segundo
cuenco se deja de camino a casa y el resto del recorrido es |PH|. Si no,
Q está en la circunferencia B; el camino P → Q → H se evalúa en 24
puntos de la circunferencia y luego se afina con búsqueda por sección
áurea junto al mejor de ellos.

La longitud total |HP| + (mejor camino de P a H pasando por el disco B)
es convexa en P: la suma |PQ| + |QH| es convexa en el par (P, Q), y
tomar el mínimo sobre Q en un disco convexo conserva la convexidad. Así
que una búsqueda por sección áurea sobre x de búsquedas por sección
áurea sobre y dentro del disco A halla el mínimo. Con S = 70 pasos por
búsqueda y K = 24 puntos es `O(S² · (K + S))`, unos cientos de miles de
distancias.

Detalles a tener en cuenta:

- la caseta puede estar dentro de un disco o de ambos (pruebas 02, 03);
- los postes pueden estar en el mismo sitio, R3 = 0 (prueba 04), y la
  fórmula de la posición de la caseta divide entre cero;
- los tres puntos pueden estar alineados, y bajo la raíz de la altura
  de la caseta aparece entonces un número negativo diminuto (pruebas 01,
  06, 07);
- las distancias de entrada pueden ser fraccionarias (prueba 11).

Las respuestas se compararon con una búsqueda en una malla densa para
ambos cuencos en 150 casos aleatorios y con una búsqueda independiente
por ángulos sobre las dos circunferencias en otros 200.

## Notas por lenguaje

- Todos los lenguajes hacen las mismas búsquedas anidadas.
- C++ toma π como `acos(-1)`, porque `M_PI` no es estándar.
- Java lee los números con `StreamTokenizer`, que acepta también los
  fraccionarios, e imprime con `Locale.ROOT` para obtener punto decimal.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1256_geometry.cpp](1256_geometry.cpp) | G++ 13.2 x64 | geometry | O(S² · (K + S)) | AC | 0.062 s | 204 KB |
| [1256_geometry.go](1256_geometry.go) | Go 1.14 x64 | geometry | O(S² · (K + S)) | AC | 0.078 s | 1104 KB |
| [1256_geometry.java](1256_geometry.java) | Java 1.8 | geometry | O(S² · (K + S)) | AC | 0.734 s | 3888 KB |
| [1256_geometry.py](1256_geometry.py) | Python 3.12 x64 | geometry | O(S² · (K + S)) | AC | 0.734 s | 800 KB |
| [1256_geometry.rs](1256_geometry.rs) | Rust 1.75 x64 | geometry | O(S² · (K + S)) | AC | 0.046 s | 288 KB |
