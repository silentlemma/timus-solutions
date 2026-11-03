# 1183. La secuencia de paréntesis correcta más corta que contiene una dada

[Timus 1183](https://acm.timus.ru/problem.aspx?space=1&num=1183) · dificultad 197 · dp

Problema original de Andrew Stankevich, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados hasta 100 caracteres de `(`, `)`, `[`, `]`, hay que imprimir una
secuencia correcta de paréntesis lo más corta posible que los contenga
como subsecuencia.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los paréntesis en una línea, que puede estar vacía.

## Salida

Una secuencia correcta más corta que los contenga.

## Evaluación

Verificar equilibrio por tipos, entrada como subsecuencia y longitud mínima añadida. El nuevo Java pasó 507 main con cargador nuevo; oráculo independiente de pares no cruzados, incluidas cadena vacía y longitud 100.

## Ejemplos

### Ejemplo 1

Entrada:

```
([(]
```

Salida:

```
()[()]
```

## Solución

Sea `d[i][j]` el mínimo de inserciones para regularizar `s[i..j)`.
El intervalo vacío cuesta cero; un símbolo, uno. Para intervalos mayores,
prueba envolver `d[i+1][j−1]` si los extremos forman una pareja de apertura
y cierre, y todas las divisiones `d[i][k]+d[k][j]`, `i<k<j`.

Las parejas de una secuencia regular no se cruzan. Un óptimo no necesita
dos símbolos insertados emparejados entre sí: quitarlos mantiene regularidad
y la subsecuencia original. Si el primer símbolo original no tiene pareja
original, complétalo como singleton y divide. Si la tiene, es el último
original (envolver) o uno anterior (dividir tras él). El no cruce hace
independientes las partes. Inducción por longitud prueba la recurrencia;
guardar la elección reconstruye una supersecuencia óptima sin perder letras.
Tiempo `O(n³)`, espacio `O(n²)`, `n≤100`.

Lee una línea completa, incluida la vacía, cuya salida también es vacía.
Se permite cualquier respuesta regular mínima con la entrada como subsecuencia.
Las cinco bases Accepted guardan decisiones; Python reconstruye con pila
explícita y los otros lenguajes con recursión de profundidad a lo sumo `n`.

## Soluciones optimizadas

Se mantiene la DP de inserciones mínimas. C++ guarda costes en bytes, corta las particiones al alcanzar la cota de paridad y reconstruye sin tabla de decisiones. Java almacena solo intervalos semiabiertos `i≤j`, incluidos los vacíos, en el triángulo superior: índice `i(2N+1−i)/2+j`, con `(N+1)(N+2)/2` bytes. Los costes están entre cero y N≤100 y caben en bytes con signo. La reconstrucción Java usa una pila acotada: extremos emparejados programan el interior y el cierre; una partición programa derecha y luego izquierda. Conserva la entrada como subsecuencia y emite una solución óptima de hasta 2N corchetes. Permanecen `O(N^3)` tiempo y `O(N^2)` espacio; se reducen representación y reconstrucción. Se conservan todas las bases claras.

- `1183_dp_optimized.cpp`: 0.015 s / 80 KB; base `1183_dp.cpp`: 0.015 s / 460 KB; cambio respecto a la base: tiempo -0.0%, memoria -82.6%.
- `1183_dp_optimized.java`: 0.109 s / 416 KB; base `1183_dp.java`: 0.078 s / 616 KB; cambio respecto a la base: tiempo +39.7%, memoria -32.5%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1183_dp.cpp`; fuente que cubre `1183_dp_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 89/89.

- Go: base didáctica preferida `1183_dp.go`; fuente que cubre `1183_dp.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1183_dp.java`; fuente que cubre `1183_dp_optimized.java`; puestos tiempo/memoria 2/1, registros de otros autores 6/6.

- Python/PyPy: base didáctica preferida `1183_dp.py`; fuente que cubre `1183_dp.py`; puestos tiempo/memoria 1/1, registros de otros autores 23/23.

- Rust: base didáctica preferida `1183_dp.rs`; fuente que cubre `1183_dp.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1183_dp.cpp](1183_dp.cpp) | G++ 13.2 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.015 s | 460 KB | 11283343 |
| [1183_dp.go](1183_dp.go) | Go 1.14 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.031 s | 1232 KB | 11283344 |
| [1183_dp.java](1183_dp.java) | Java 1.8 | dp | O(N^3) time; O(N^2) space | AC | 0.078 s | 616 KB | 11283347 |
| [1183_dp.py](1183_dp.py) | Python 3.12 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.078 s | 876 KB | 11283345 |
| [1183_dp.rs](1183_dp.rs) | Rust 1.75 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.001 s | 308 KB | 11283349 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1183_dp_optimized.cpp](1183_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N^3) time; O(N^2) space | AC | 0.015 s | 80 KB | 11308418 |
| [1183_dp_optimized.java](1183_dp_optimized.java) \* | Java 1.8 | dp | O(N^3) time; O(N^2) space | AC | 0.109 s | 416 KB | 11309557 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
