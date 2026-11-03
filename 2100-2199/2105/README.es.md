# 2105. Encuentros de dos ciclistas en sentidos opuestos

[Timus 2105](https://acm.timus.ru/problem.aspx?space=1&num=2105) · dificultad 206 · math

Problema original de Nikita Sivukhin, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos niños recorren un camino circular de longitud L en sentidos
opuestos con velocidades v_A y v_B, saliendo juntos, durante T segundos;
a veces uno de ellos se detiene un rato. Un encuentro es un momento en
que están en el mismo punto sin haberlo estado justo antes. Contar los
encuentros. Los límites son 1 segundo y 64 MB.

## Entrada

L ≤ 10⁹, T ≤ 10⁶, v_A, v_B ≤ 10³ y después n ≤ 10⁵ paradas: quién,
inicio y duración; dos paradas de un mismo niño se intersecan a lo sumo en un punto.

## Salida

El número de encuentros.

## Evaluación

Comparar un token entero exacto, ignorando espacios de formato. El nuevo código Python exacto pasó 13 pruebas del repositorio con PyPy 3.10. Las otras variantes conservan sus propias pruebas de destino y Accepted exactos. La salida se compara según el verificador del problema.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 10 2 1
3
1 1 1
1 2 2
2 2 1
```

Salida:

```
2
```

## Solución

Yendo en sentidos opuestos, los dos están en el mismo punto exactamente
cuando la distancia recorrida entre ambos es múltiplo de L. Esa
distancia nunca decrece y empieza en 0, así que cada múltiplo kL con
k ≥ 1 hasta la distancia final se alcanza una vez y cuenta como un
encuentro, aunque los dos se queden quietos allí un rato; el comienzo
no cuenta. Dos paradas de un niño se intersecan a lo sumo en un punto, así que cada uno rueda
T menos la suma de sus paradas, y la respuesta es
⌊(v_A · ride_A + v_B · ride_B) / L⌋, con enteros de 64 bits (precisión arbitraria en Python).

En el ejemplo Alice rueda 7 segundos y Bob 9, juntos 2 · 7 + 9 = 23
metros en un camino de 10: dos encuentros.

## Soluciones optimizadas

La distancia relativa es monótona: (speedA+speedB)*T menos speed*duration de cada parada del ciclista correspondiente. Al no solaparse sus paradas, la resta es exacta sin depender del inicio. Cada nuevo múltiplo de la longitud crea un encuentro; detenerse en un múltiplo ya alcanzado no crea otros. El cociente es la respuesta. Las variantes compactas solo guardan el acumulado y descartan cada parada leída. Python usa los flujos existentes y enteros exactos. Se conservan las cinco bases.

- `2105_math_optimized.py`: 0.125 s / 264 KB; base `2105_math.py`: 0.062 s / 440 KB; cambio respecto a la base: tiempo +101.6%, memoria -40.0%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `2105_math.cpp`; fuente que cubre `2105_math.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 62/61.

- Go: base didáctica preferida `2105_math.go`; fuente que cubre `2105_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `2105_math.java`; fuente que cubre `2105_math.java`; puestos tiempo/memoria 1/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `2105_math.py`; fuente que cubre `2105_math_optimized.py`; puestos tiempo/memoria 95/1, registros de otros autores 101/101.

- Rust: base didáctica preferida `2105_math.rs`; fuente que cubre `2105_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2105_math.cpp](2105_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 136 KB | 11294747 |
| [2105_math.go](2105_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.015 s | 1084 KB | 11294750 |
| [2105_math.java](2105_math.java) | Java 1.8 | math | O(n) | AC | 0.093 s | 388 KB | 11309241 |
| [2105_math.py](2105_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.062 s | 440 KB | 11294751 |
| [2105_math.rs](2105_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 196 KB | 11309404 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2105_math_optimized.py](2105_math_optimized.py) \* | PyPy 3.10 x64 | math | O(K) | AC | 0.125 s | 264 KB | 11309678 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
