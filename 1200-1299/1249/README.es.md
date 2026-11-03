# 1249. ¿Son rectángulos todas las zonas oscuras?

[Timus 1249](https://acm.timus.ru/problem.aspx?space=1&num=1249) · dificultad 221 · implementation

Problema original de Nikita Shamgunov y Leonid Volkov, del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da una imagen binaria `N × M` de como máximo 3000 filas y 3000 columnas. Decide si cada componente de unos conectados por lados es un rectángulo lleno paralelo a los ejes. Tocar solo una esquina no conecta celdas. Tiempo: 2,5 segundos. Memoria: 4 MB.

## Entrada

`N M`, seguidos de `N` filas con `M` ceros o unos separados por espacios.

## Salida

Imprime `Yes` si cada componente es un rectángulo lleno; en otro caso, `No`.

## Evaluación

Comparación por tokens: `Yes` o `No` con las mayúsculas indicadas. Los espacios de formato no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
0 1
1 1
```

Salida:

```
No
```

### Ejemplo 2

Entrada:

```
3 3
0 0 1
1 1 0
1 1 0
```

Salida:

```
Yes
```

## Solución

Una ventana 2 × 2 con exactamente tres celdas oscuras pertenece a una
misma componente que no puede ser un rectángulo lleno. Recíprocamente,
el borde de una componente conectada por lados que no llena un rectángulo
tiene una esquina entrante, también alrededor de un hueco. Esa esquina
produce una ventana con tres celdas oscuras. Basta prohibir esas ventanas.

Guarda solo filas adyacentes y comprueba cada ventana cuando llega su
última celda. Las versiones nativas sencillas prueban las cuatro celdas;
la sencilla de Python usa enteros como máscaras y combina paridad impar
con al menos dos bits activos. La entrada cuesta `O(N M)` y las filas,
`O(M)` memoria. Guardar toda la imagen o el texto de entrada excedería
el límite. Las componentes que solo tocan esquinas siguen separadas.
Se conservan sin cambiar un byte las cinco fuentes Accepted originales.

## Soluciones optimizadas

Para dos filas, `B = previous AND current` marca columnas verticales
llenas y `S = previous XOR current` las de una sola celda oscura. Una
ventana prohibida es una columna llena junto a una sencilla; la expresión
`(B AND (S >> 1)) OR (S AND (B >> 1))` comprueba ambos órdenes.

Python factoriza así su expresión anterior y elimina los blancos de la
fila con una transformación. C++ empaqueta columnas en palabras de 64 bits,
lee con un búfer acotado, comprueba cada palabra en paralelo y verifica
explícitamente las parejas que cruzan su límite. Retiene la fila anterior
empaquetada y la palabra actual. La comprobación lógica por fila cuesta
`O(ceil(M/64))`; leer sigue costando `O(N M)` y las filas ocupan `O(M/64)`
palabras. Python usa `O(M)` bits más la línea actual de entrada.

C++ pasa de 0,531 s / 208 KB a 0,078 s / 128 KB: 85,3% menos tiempo y
38,5% menos memoria. Python pasa de 0,218 s / 1532 KB a 0,125 s / 3684 KB:
42,7% menos tiempo, pero mayor pico de memoria registrado. Python se admite
solo por tiempo; ambas versiones tienen su propio Accepted. No mejoran
necesariamente todos los recursos.

## Notas por lenguaje

Python se comparó en 75.254 imágenes pequeñas con un recorrido
independiente de componentes y sus cajas delimitadoras, incluidas todas
las imágenes binarias con cada dimensión hasta cuatro. Ambos programas
reales superaron 14 entradas del repositorio en Docker, incluidas imágenes
3000 × 3000. Se comprobaron además las cuatro orientaciones de esquina
ausente y contactos diagonales en límites de palabras en C++ y Python.

La instantánea es del 2 de noviembre de 2026. C++ cumple el objetivo:
puesto 5 en tiempo y 1 en memoria entre 61 registros filtrados de otros
autores. Python tiene puestos 1 y 2 frente a un registro y conserva el
asterisco. Java original es primero en ambas métricas frente a cuatro.
Go y Rust no tienen muestras filtradas: su cobertura formal no demuestra
superioridad competitiva.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1249_implementation.cpp](1249_implementation.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.531 s | 208 KB | 11283966 |
| [1249_implementation.go](1249_implementation.go) | Go 1.14 x64 | implementation | O(N M) | AC | 0.093 s | 1096 KB | 11283967 |
| [1249_implementation.java](1249_implementation.java) | Java 1.8 | implementation | O(N M) | AC | 0.156 s | 452 KB | 11283977 |
| [1249_implementation.py](1249_implementation.py) | Python 3.12 x64 | implementation | O(N M) | AC | 0.218 s | 1532 KB | 11283970 |
| [1249_implementation.rs](1249_implementation.rs) | Rust 1.75 x64 | implementation | O(N M) | AC | 0.031 s | 224 KB | 11283979 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1249_implementation_optimized.cpp](1249_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.078 s | 128 KB | 11308213 |
| [1249_implementation_optimized.py](1249_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N M) | AC | 0.125 s | 3684 KB | 11308214 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
