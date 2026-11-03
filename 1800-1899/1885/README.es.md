# 1885. Comodidad de los pasajeros

[Timus 1885](https://acm.timus.ru/problem.aspx?space=1&num=1885) · dificultad 186 · math

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un avión debe subir a h metros en los primeros t segundos y luego
mantener esa altura. Sube como mucho v metros por segundo y no puede
bajar antes de llegar a h. A los pasajeros se les tapan los oídos
exactamente mientras el avión sube a más de x metros por segundo. Hay
que hallar el menor y el mayor tiempo posible con los oídos tapados.

## Entrada

h, t, v, x (5000 ≤ h ≤ 12 000, 50 ≤ t ≤ 1200, 1 ≤ x < v ≤ 100,
h ≤ t·v).

## Salida

El menor y el mayor tiempo, cada uno con error absoluto o relativo de como mucho 10⁻⁶.

## Evaluación

Comparar dos reales con tolerancia absoluta o relativa 1e-6. El nuevo Python pasó 6953 casos de destino, incluidas fronteras del repositorio; la cota analítica demuestra el redondeo para todas las entradas.

## Ejemplos

### Ejemplo 1

Entrada:

```
10000 500 50 10
```

Salida:

```
125.0 500.0
```

## Solución

El menor: cada segundo a velocidad x o menos no cuenta, y en cada uno se
ganan como mucho x metros. Si t·x ≥ h, el avión sube a x y los oídos
nunca se tapan. Si no, debe subir a x todos los segundos menos τ, y a v
durante τ, con τ·v + (t − τ)·x = h, así que τ = (h − t·x)/(v − x).
Hacer los segundos rápidos a menos de v solo los alarga.

El mayor: los oídos solo se tapan al subir, así que como mucho t
segundos y como mucho h/x segundos. Subir un poco por encima de x
se aproxima a este último límite, o, si
h/x > t, el avión sube a h/t > x durante los t segundos. La respuesta es
min(t, h/x). `O(1)`.

En el ejemplo t·x = 5000 < 10 000, así que hacen falta 5000/40 = 125
segundos a 50 m/s, y subir a h/t = 20 > 10 m/s durante los 500 segundos
mantiene los oídos tapados todo el tiempo.

Trampas:

- el mayor tiempo es un límite: subir exactamente a x no tapa los
  oídos, pero cualquier velocidad mayor sí, así que la respuesta es min(t, h/x);
- cuando t·x ≥ h el menor tiempo es 0;
- subir a menos de x no cuenta, así que mezclar velocidades lentas
  nunca mejora una subida a x.

Las respuestas coinciden con una implementación aceptada independiente
en todas las pruebas.

## Soluciones optimizadas

Se conservan las fórmulas del mínimo y supremo. Calcular numeradores exactos y redondear divisiones no negativas a seis decimales con `S=10^6`: `floor((a*S+floor(b/2))/b)`. El error máximo es media unidad decimal, `0.5·10^-6`, dentro de la tolerancia. Limitar el mínimo por cero y el máximo por t. Emitir partes enteras y fraccionarias rellenadas directamente, sin conversión flotante, formateador general ni concatenar el resultado. Los intermedios caben en 64 bits con signo; Python está aceptado con PyPy 3.10. Cambia la representación, no las fórmulas; se conservan las bases flotantes cortas. Tiempo y espacio adicional constantes.

- `1885_math_optimized.py`: 0.109 s / 272 KB; base `1885_math.py`: 0.078 s / 392 KB; cambio respecto a la base: tiempo +39.7%, memoria -30.6%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1885_math.cpp`; fuente que cubre `1885_math.cpp`; puestos tiempo/memoria 1/4, registros de otros autores 106/106.

- Go: base didáctica preferida `1885_math.go`; fuente que cubre `1885_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1885_math.java`; fuente que cubre `1885_math.java`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Python/PyPy: base didáctica preferida `1885_math.py`; fuente que cubre `1885_math_optimized.py`; puestos tiempo/memoria 13/1, registros de otros autores 23/23.

- Rust: base didáctica preferida `1885_math.rs`; fuente que cubre `1885_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1885_math.cpp](1885_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 132 KB | 11308434 |
| [1885_math.go](1885_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1088 KB | 11291093 |
| [1885_math.java](1885_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1788 KB | 11291097 |
| [1885_math.py](1885_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 392 KB | 11291095 |
| [1885_math.rs](1885_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 248 KB | 11308435 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1885_math_optimized.py](1885_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 272 KB | 11309564 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
