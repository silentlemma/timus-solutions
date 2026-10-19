# 2027. Ejecutar una cuadrícula de registros acotados

[Timus 2027](https://acm.timus.ru/problem.aspx?space=1&num=2027) · dificultad 540 · simulation

Problema original de Kirill Borozdin, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Interpreta una cuadrícula rectangular de instrucciones. Hay un registro
entero actual y 26 registros de memoria `A` a `Z`, todos inicialmente
cero. El puntero empieza arriba a la izquierda mirando a la derecha.
Cada paso ejecuta primero su celda y después avanza una celda en la
dirección resultante. Los bordes no se conectan.

| Instrucción | Efecto antes de moverse |
| --- | --- |
| `^`, `>`, `v`, `<` | Fijar arriba, derecha, abajo, izquierda, respectivamente. |
| `.` | No hacer nada. |
| `A`…`Z` | Intercambiar el valor actual y el registro indicado. |
| `?` | Sustituir el valor actual por la siguiente entrada; agotadas las entradas, repetir siempre la última. |
| `!` | Imprimir el valor actual y después ponerlo a cero. |
| `+`, `-` | Incrementar o decrementar en uno. |
| `@` | Girar en sentido antihorario si el valor es cero; en caso contrario, horario, incluidos negativos. |
| `#` | Terminar inmediatamente sin moverse. |

Tras la instrucción, un valor fuera de `[-100000,100000]` causa
`OVERFLOW ERROR`. Si el movimiento posterior sale de la cuadrícula,
causa `RUNTIME ERROR`. Tras completar 1000000 pasos sin terminar ni
causar esos errores, se produce `TIME LIMIT EXCEEDED`. Conserva todos
los números ya impresos. Operación y desbordamiento preceden al
movimiento, y ambos errores preceden al límite de pasos. Terminar en el
paso 1000000 es válido.

Dimensiones `1 ≤ H,W ≤ 100`; hay `1 ≤ N ≤ 100000` enteros de entrada, de
valor absoluto como máximo 100000. No consumir toda la entrada está
permitido. Límites: 2 segundos y 64 MB.

## Entrada

Lee `H W`, las `H` filas de `W` instrucciones válidas, después `N` y los
`N` enteros, uno en cada línea.

## Salida

Por cada `!` ejecutado, imprime un entero en su propia línea. Si ocurre
un error, añade su mensaje exacto en una línea. La terminación normal no
añade nada; la salida puede estar vacía.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
4 6
?A?v>v
>..>@A
-...A!
^A.+<#
2
2
3
```

```
5
```

```
2 4
?!>v
##^<
1
0
```

```
0
TIME LIMIT EXCEEDED
```

```
1 4
??!#
1
1
```

```
1
```

## Solución

Simula directamente coordenadas, dirección, valor actual, memoria,
cursor y búfer de salida. Codifica las direcciones en orden horario:
derecha, abajo, izquierda, arriba. En `@`, suma uno módulo cuatro para
un valor no nulo, o resta uno para cero. Tras consumir el último número,
deja el cursor en su índice.

En cada uno de hasta 1000000 pasos, ejecuta la instrucción. Devuelve
inmediatamente al encontrar `#`. En otro caso comprueba desbordamiento,
mueve el puntero y comprueba los bordes. El primer error termina la
ejecución. Si el bucle se agota, añade el mensaje de tiempo. El búfer
conserva valores anteriores a un error. No hace falta detectar ciclos:
volver a una posición todavía puede generar muchas salidas que no se
pueden omitir.

La demostración es por inducción sobre los pasos. Inicialmente coinciden
registros, puntero, dirección, entrada pendiente y salida vacía. Cada
instrucción hace su actualización: el intercambio conserva ambos
valores, la lectura toma el siguiente número o repite el último, y la
salida ocurre antes del reinicio a cero. Los cambios de dirección
preceden al movimiento. Así coinciden el estado siguiente y el prefijo
de salida. Las comprobaciones en sus fases producen el mismo primer
error; `#` termina antes de moverse. Después del millonésimo paso
completo solo queda el límite temporal. Por tanto, toda la salida y el
error final son exactos.

El primer ejemplo transfiere unidades mediante `A` y produce 5. El
segundo imprime cero, limpia el registro y entra en un ciclo sin parada,
por lo que añade el límite. El tercero lee dos veces su único número: la
segunda lectura repite 1, que se imprime antes de terminar.

Para `S ≤ 1000000` pasos y `B` caracteres de salida, el tiempo es `O(HW
+ N + S + B)`. Con búferes, el espacio es `O(HW + N + B)`; los registros
y el puntero ocupan espacio constante. La salida en flujo podría
eliminar el término de almacenamiento `B`, conservando todo lo anterior
al error.

Trampas:

- La letra intercambia valores, no copia; `!` pone a cero después de imprimir.
- Agotada la entrada, se repite el último número; sobrar entradas no es
  un error.
- Los valores negativos también giran en sentido horario en `@`.
- No conectes bordes ni muevas tras `#`; el desbordamiento gana al
  movimiento fuera.
- Ejecuta la instrucción y el movimiento del paso un millón antes de
  decidir el límite.
- Conserva salidas grandes; terminar inmediatamente ni siquiera exige un
  salto de línea.

## Notas por lenguaje

Bastan enteros ordinarios con signo para los valores y la detección de
desbordamiento en un paso. C++ usa una cadena, Go `strings.Builder`,
Java `StringBuilder`, Rust `String`, y Python `StringIO` en vez de casi
un millón de cadenas numéricas separadas. Todos usan lectura con búfer y
ejecutan el límite completo sin saltarse ciclos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2027_simulation.cpp](2027_simulation.cpp) | G++ 13.2 x64 | simulation | O(HW + N + S + B) | AC | 0.031 s | 8132 KB |
| [2027_simulation.go](2027_simulation.go) | Go 1.14 x64 | simulation | O(HW + N + S + B) | AC | 0.109 s | 13240 KB |
| [2027_simulation.java](2027_simulation.java) | Java 1.8 | simulation | O(HW + N + S + B) | AC | 0.171 s | 21472 KB |
| [2027_simulation.py](2027_simulation.py) | Python 3.12 x64 | simulation | O(HW + N + S + B) | AC | 0.781 s | 21780 KB |
| [2027_simulation.rs](2027_simulation.rs) | Rust 1.75 x64 | simulation | O(HW + N + S + B) | AC | 0.046 s | 6276 KB |
