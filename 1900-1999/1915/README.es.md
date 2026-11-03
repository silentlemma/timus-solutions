# 1915. Ruinas de los titanes: reconstrucción del pasado

[Timus 1915](https://acm.timus.ru/problem.aspx?space=1&num=1915) · difficulty 228 · simulation

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Comenzar con una pila vacía. Un positivo se apila; −1 retira y muestra
la cima; 0 pone una copia completa encima, manteniendo el orden desde
el fondo hasta la cima. Mostrar todos los valores retirados en orden.
Se garantiza que la pila no está vacía en cada retirada. Su altura real
puede crecer exponencialmente. Límites: 2 segundos, 128 MB.

## Entrada

n, 1≤n≤1 000 000, y n líneas con un entero x por línea:
−1, 0, o un valor en [1,1 000 000 000].

## Salida

Un valor retirado por línea, en orden cronológico. Sin retiradas, salida vacía.

## Evaluación

Comparación exacta de los tokens enteros y su orden.

## Ejemplos

```
8
3
4
0
-1
-1
-1
-1
1
```

```
4
3
4
3
```

## Solución

Guardar las operaciones y contar sus P retiradas. Sea r el número de
retiradas pendientes. Conservar solo los últimos min(h,r) valores de
la pila real, cuya altura h puede ser enorme. Nada más profundo puede
aparecer sin gastar más de r retiradas. Si P=0 no hay salida; con r=0
las operaciones restantes no importan.

Usar un arreglo circular de capacidad física P, fondo lógico b y tamaño s.
La capacidad lógica r disminuye y puede ser menor que P. Al apilar,
si s=r, descartar primero el fondo guardado y añadir al nuevo extremo
lógico. Al retirar, mostrar el último valor y decrementar s y r.

Al duplicar, mantener intacta la parte superior existente. Si s=r,
ignorar la copia: ya se conocen todos los valores observables. En otro
caso se conoce la pila real completa de tamaño s. Añadir debajo solo
q=min(s,r−s) valores: el sufijo de longitud q de la pila anterior.
El fondo nuevo es (b−q) mod P y la fuente comienza en (b+s−q) mod P.
El destino ocupa posiciones libres, sin sobrescribir la fuente.
Una pila vacía o capacidad lógica llena produce q=0.

### Corrección

El invariante conserva exactamente los últimos min(h,r) valores reales.
Apilar requiere solo los anteriores r−1 superiores y el nuevo valor,
por lo que descartar el fondo es seguro. Retirar requiere después
min(h−1,r−1), exactamente uno menos, y muestra la cima verdadera.
Duplicar con h≥r no cambia los últimos r; con h<r se conoce toda
la pila, y su duplicación termina con ella precedida por el sufijo descrito.
Todas las operaciones mantienen el invariante y producen respuestas correctas.

### Coste amortizado

Cada retirada reduce s en uno. Una inserción no llena lo aumenta en uno;
una llena no lo cambia. Una copia lo aumenta en q. Inicialmente s=0,
y después de la última retirada r=s=0. La suma de q es P menos las
inserciones que aumentan el tamaño, por tanto no supera P. Tiempo `O(n)`
y memoria `O(n)`, incluso con muchísimas copias consecutivas.

En el ejemplo [3,4] se transforma en [3,4,3,4], y salen 4,3,4,3.
La última inserción ya no afecta la salida.

Duplicar conserva el orden, no invierte. Se antepone un sufijo bajo la
parte guardada. La capacidad lógica baja solo al retirar. Con r<P,
una inserción llena debe quitar el fondo y añadir al extremo lógico;
sobrescribir solamente la antigua celda inferior es incorrecto.
Tratar copias vacías y ausencia de salida, sin expandir pilas exponenciales
ni desplazar arreglos completos repetidamente.

## Soluciones optimizadas

Se conserva solo la parte superior de la pila que puede afectar las extracciones restantes, según el invariante del anillo decreciente. Las monedas extraídas se emiten por bloques, sin copiarlas a un arreglo completo de respuestas. El retorno condicional sustituye módulos frecuentes. La cota cuenta todas las copias durante la ejecución, no por comando separado. Python usa el intérprete registrado en su fila Accepted.

- `1915_simulation_optimized.cpp`: 0.062 s / 7492 KB; base `1915_simulation.cpp`: 0.187 s / 11640 KB; cambio respecto a la base: tiempo -66.8%, memoria -35.6%.
- `1915_simulation_optimized.go`: 0.078 s / 9548 KB; base `1915_simulation.go`: 0.093 s / 21804 KB; cambio respecto a la base: tiempo -16.1%, memoria -56.2%.
- `1915_simulation_optimized.java`: 0.250 s / 8448 KB; base `1915_simulation.java`: 0.390 s / 12292 KB; cambio respecto a la base: tiempo -35.9%, memoria -31.3%.
- `1915_simulation_optimized.py`: 0.359 s / 37668 KB; base `1915_simulation.py`: 0.515 s / 16716 KB; cambio respecto a la base: tiempo -30.3%, memoria +125.3%.
- `1915_simulation_optimized.rs`: 0.062 s / 7856 KB; base `1915_simulation.rs`: 0.046 s / 16904 KB; cambio respecto a la base: tiempo +34.8%, memoria -53.5%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1915_simulation.cpp`; versión que cubre `1915_simulation_optimized.cpp`; puestos tiempo/memoria 4/9, registros de otros autores 45/45.

- Go: base didáctica preferida `1915_simulation.go`; versión que cubre `1915_simulation.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1915_simulation.java`; versión que cubre `1915_simulation_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1915_simulation.py`; versión que cubre `1915_simulation_optimized.py`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Rust: base didáctica preferida `1915_simulation.rs`; versión que cubre `1915_simulation.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1915_simulation.cpp](1915_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.187 s | 11640 KB | 11291421 |
| [1915_simulation.go](1915_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.093 s | 21804 KB | 11291424 |
| [1915_simulation.java](1915_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.390 s | 12292 KB | 11309214 |
| [1915_simulation.py](1915_simulation.py) | PyPy 3.10 x64 | simulation | O(n) | AC | 0.515 s | 16716 KB | 11291425 |
| [1915_simulation.rs](1915_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.046 s | 16904 KB | 11291432 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1915_simulation_optimized.cpp](1915_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(N+P) | AC | 0.062 s | 7492 KB | 11308596 |
| [1915_simulation_optimized.go](1915_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N+P) | AC | 0.078 s | 9548 KB | 11308605 |
| [1915_simulation_optimized.java](1915_simulation_optimized.java) | Java 1.8 | simulation | O(N+P) | AC | 0.250 s | 8448 KB | 11308601 |
| [1915_simulation_optimized.py](1915_simulation_optimized.py) | PyPy 3.10 x64 | simulation | O(N+P) | AC | 0.359 s | 37668 KB | 11309401 |
| [1915_simulation_optimized.rs](1915_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N+P) | AC | 0.062 s | 7856 KB | 11308602 |
