# 1915. Una pila que puede duplicarse

[Timus 1915](https://acm.timus.ru/problem.aspx?space=1&num=1915) · difficulty 229 · simulation

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

## Notas por lenguaje

Valores y operaciones caben en enteros de 32 bits. C++, Go, Java y Rust
guardan también un arreglo compacto de P resultados. Python usa dos
`array('i')` y bloques de 8192 cadenas de salida, evitando un millón
de objetos enteros o cadenas; lee una operación por línea. Go analiza
bytes y reutiliza un búfer decimal; Java usa entrada/salida por bytes
sin asignar una cadena por moneda. Los demás usan flujos estándar almacenados en búfer.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1915_simulation.cpp](1915_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.187 s | 11640 KB |
| [1915_simulation.go](1915_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.093 s | 21804 KB |
| [1915_simulation.java](1915_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.296 s | 12368 KB |
| [1915_simulation.py](1915_simulation.py) | PyPy 3.10 x64 | simulation | O(n) | AC | 0.515 s | 16716 KB |
| [1915_simulation.rs](1915_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.046 s | 16904 KB |
