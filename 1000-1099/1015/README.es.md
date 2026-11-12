# 1015. Agrupar dados que son rotaciones unos de otros

[Timus 1015](https://acm.timus.ru/problem.aspx?space=1&num=1015) · dificultad 458 · hashing, implementation

Problema original del Ural State University Internal Contest '99 #2.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` dados (`1 ≤ N ≤ 100 000`), numerados desde 1 en el orden de la
entrada. Un dado se da por los números de sus caras izquierda, derecha,
superior, frontal, inferior y trasera, en ese orden: una permutación de
`1..6`. Dos dados son del mismo tipo si alguna rotación de uno da el otro
(una imagen especular no es una rotación). Reparte los dados por tipos.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas de seis números: izquierda, derecha, superior,
frontal, inferior, trasera.

## Salida

El número `Q` de tipos y luego `Q` líneas, una por tipo: los números de sus
dados en orden creciente. Las líneas van ordenadas por su primer número, así
que la primera empieza por 1.

## Evaluación

La salida se compara línea a línea; dentro de una línea, token a token.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 6 2 3 5 4
2 5 6 3 1 4
1 6 2 4 5 3
3 4 1 2 6 5
```

Salida:

```
2
1 2 4
3
```

### Ejemplo 2

Entrada:

```
1
4 3 1 6 2 5
```

Salida:

```
1
1
```

## Solución

**Las 24 rotaciones.** Una rotación se escribe como una permutación de las
seis posiciones. Dos cuartos de vuelta las generan todas: alrededor del eje
vertical (izquierda ← frente ← derecha ← detrás ← izquierda; arriba y abajo
quietos) y alrededor del eje izquierda-derecha (arriba ← detrás ← abajo ←
frente ← arriba). Empezando por la identidad y aplicando ambos giros hasta
que no aparezca nada nuevo se obtienen exactamente 24 permutaciones. Solo se
generan rotaciones, nunca reflexiones, así que un dado y su imagen especular
quedan separados.

**Una clave para cada dado.** Se aplican al dado las 24 rotaciones, cada
resultado se lee como un número de 6 cifras (base 7 basta) y se toma el
menor: los dados del mismo tipo reciben la misma clave y los de tipos
distintos, claves distintas. Solo hay `720 / 24 = 30` tipos.

**Agrupación.** Se recorren los dados en orden; un mapa hash de clave a
grupo crea un grupo nuevo la primera vez que aparece una clave y si no añade
el dado al existente. Así los grupos se crean en el orden de su menor dado y
la lista de cada grupo es creciente: justo la salida pedida.

Tiempo `O(24 · 6 · N)`. También se puede precalcular la clave de cada uno de
los 720 dados posibles y buscarla, como hace la versión en Python.

Detalles a tener en cuenta:

- reflexiones: las seis caras se pueden permutar de 720 maneras, pero solo
  24 son rotaciones; una clave hecha solo con el conjunto de pares opuestos
  junta imágenes especulares;
- hasta `10^5` números de dados en la salida: constrúyela en un búfer.

## Soluciones optimizadas

El nuevo C++ genera una vez las mismas 24 rotaciones propias y clasifica las 720 permutaciones. El rango por inversiones indexa una tabla de 720 bytes: cada dado requiere un rango y consulta, sin probar todas las rotaciones. Los grupos se numeran al aparecer; se guarda un byte de grupo por dado. Un recorrido por grupo (hasta 30) imprime índices crecientes y grupos en orden de aparición. Los recorridos adicionales evitan vectores de índices y la cadena completa de salida. Ambas versiones son lineales en N; cambian constantes y almacenamiento. Las clases se calculan al ejecutar. Se conservan las bases; las otras cuatro familias reutilizan las ya admitidas.

Las implementaciones base aceptadas [1015_hashing.go](1015_hashing.go), [1015_hashing.java](1015_hashing.java), [1015_hashing.py](1015_hashing.py), [1015_hashing.rs](1015_hashing.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Las bases C++, Go, Java y Rust prueban24 rotaciones por dado; Python ya precalcula720 claves. El nuevo C++ también precalcula las permutaciones, guarda un byte por dado e imprime mediante recorridos por grupo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1015_hashing.cpp](1015_hashing.cpp) | G++ 13.2 x64 | hashing | O(24 · 6 · N) | AC | 0.031 s | 356 KB | 11278124 |
| [1015_hashing.go](1015_hashing.go) | Go 1.14 x64 | hashing | O(24 · 6 · N) | AC | 0.001 s | 1280 KB | 11278132 |
| [1015_hashing.java](1015_hashing.java) | Java 1.8 | hashing | O(24 · 6 · N) | AC | 0.093 s | 1524 KB | 11278141 |
| [1015_hashing.py](1015_hashing.py) \* | Python 3.12 x64 | hashing | O(N) after a 720-entry table | AC | 0.093 s | 2748 KB | 11278138 |
| [1015_hashing.rs](1015_hashing.rs) | Rust 1.75 x64 | hashing | O(24 · 6 · N) | AC | 0.015 s | 856 KB | 11278146 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1015_hashing_optimized.cpp](1015_hashing_optimized.cpp) | G++ 13.2 x64 | hashing | O(720 + 30N) | AC | 0.015 s | 104 KB | 11315195 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
