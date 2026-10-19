# 1891. Lenguaje Ocean

[Timus 1891](https://acm.timus.ru/problem.aspx?space=1&num=1891) · dificultad 711 · parsing

Problema original de Alex Samsonov, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Comprobar los tipos de una secuencia de declaraciones de variables.
Los tipos disponibles son `int`, `real` y `string`. Cada declaración
inicializa una nueva variable mediante una llamada a función. El tipo
declarado puede ser uno de estos tres o `auto`, que adopta el tipo
devuelto por la función.

Las funciones pueden compartir nombre. Una llamada selecciona una
función por su nombre y la lista ordenada de tipos de los argumentos,
incluida su cantidad. Los argumentos deben ser variables declaradas
en líneas anteriores. Los tipos deben coincidir exactamente: no hay
conversiones implícitas. Los nombres de funciones y variables pertenecen
a espacios separados, así que pueden coincidir.

Encontrar la primera declaración errónea. Dentro de una misma línea,
comprobar los errores en este orden de prioridad:

- `Double declaration`: el nombre de la variable ya fue declarado;
- `Unknown variable`: al menos un argumento todavía no está declarado;
- `No such function`: ninguna función tiene el nombre y los tipos requeridos;
- `Invalid initialization`: el tipo explícito difiere del tipo devuelto.

Si todo el programa es válido, listar los tipos inferidos de las
variables `auto` en orden de declaración. Los límites son 1 segundo
y 64 MB.

## Entrada

Primero se indica f, el número de cabeceras de funciones, con
1 ≤ f ≤ 100. Las siguientes f líneas tienen la forma
`name(type, ..., type) : type`; la lista de parámetros puede estar vacía.
No hay dos cabeceras con el mismo nombre y la misma lista ordenada
de tipos de parámetros a la vez.

Después se indica n, el número de declaraciones, con 1 ≤ n ≤ 100.
Las siguientes n líneas tienen la forma
`type variable = name(argument, ..., argument)`, donde `type` también
puede ser `auto` y los argumentos son nombres de variables. Cada
cabecera y llamada tiene como máximo 10 argumentos.

Los nombres contienen de 1 a 20 letras. Los nombres de variables solo
usan letras inglesas minúsculas; los de funciones también pueden usar
mayúsculas y distinguen entre ambas. Las palabras `int`, `real`,
`string` y `auto` no pueden ser nombres. Los espacios siguen los ejemplos;
la sintaxis es válida y solo deben comprobarse los errores semánticos
indicados.

## Salida

Si hay un error, escribir `Error on line k: message`, usando el número
de declaración desde 1 y el texto exacto del error. En este caso no se
escriben tipos inferidos, ni siquiera los de líneas anteriores válidas.

En otro caso, escribir `name : type` para cada variable `auto` en orden
de declaración. Si no hay declaraciones `auto`, la salida está vacía.

## Evaluación

Las salidas se comparan como secuencias de tokens.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
ReadInt() : int
IntToReal(int) : real
3
auto a = ReadInt()
auto b = IntToReal(a)
int c = ReadInt()
```

Salida:

```
a : int
b : real
```

### Ejemplo 2

Entrada:

```
1
ReadInt() : int
2
int x = ReadInt()
int x = ReadInt()
```

Salida:

```
Error on line 2: Double declaration
```

### Ejemplo 3

Entrada:

```
3
ReadInt() : int
ReadReal() : real
SumRealInt(real, int) : real
4
auto x = ReadInt()
auto y = ReadReal()
real z = SumRealInt(y, x)
real q = SumRealInt(x, y)
```

Salida:

```
Error on line 4: No such function
```

## Solución

Analizar las cabeceras y guardar un mapa de firma de función a tipo
devuelto. Una firma contiene el nombre y la secuencia ordenada de tipos
de parámetros; la secuencia vacía representa una función sin parámetros.
Otro mapa guarda los nombres y tipos de las variables declaradas.
Los signos de puntuación separan campos y no aparecen dentro de nombres.

Procesar las declaraciones en orden. Primero comprobar si el nuevo
nombre ya existe. Solo entonces buscar cada argumento: cualquiera
desconocido produce `Unknown variable` antes de intentar resolver la
función. Construir la firma con los tipos de los argumentos y buscarla
en el mapa de funciones. Si existe, comparar el tipo devuelto con el
tipo explícito, o adoptarlo como tipo inferido para `auto`.

Añadir la nueva variable solo después de superar todas las comprobaciones.
Para `auto`, añadir también su nombre y tipo a una lista de salida.
Escribir esta lista solo si todo el programa es válido; si una línea
posterior falla, escribir únicamente su error.

Antes de cada línea, el mapa de variables contiene exactamente los
tipos establecidos por las declaraciones anteriores válidas. Por tanto,
la búsqueda de argumentos usa precisamente las variables permitidas.
La firma aplica la regla exacta de sobrecarga, y la comparación del tipo
devuelto comprueba la inicialización. Ejecutar los pasos en el orden
exigido obtiene el error de mayor prioridad de la primera línea errónea.

Sea L la longitud total de la entrada. Con tablas hash, el análisis,
la construcción de firmas y las búsquedas cuestan `O(L)` esperado,
con memoria `O(L)`.

En el primer ejemplo, `a` obtiene el tipo `int` y `b` el tipo `real`;
la declaración explícita de `c` no aparece en la salida. El segundo
ejemplo vuelve a declarar `x` en la línea de declaración 2. En el tercero,
`SumRealInt(y, x)` coincide con `(real, int)`, pero `(int, real)` en la
línea 4 no coincide. Aunque los tipos de `x` e `y` se infirieron antes,
no se imprimen porque el programa contiene un error.

Trampas:

- conservar el orden de argumentos y las mayúsculas del nombre de función;
- un argumento desconocido tiene prioridad sobre una función inexistente;
- comprobar la redeclaración antes de examinar la parte derecha;
- la nueva variable no puede referirse a sí misma antes de declararse;
- `auto` pasa a ser un tipo concreto y nunca aparece en una firma de llamada;
- no convertir `int` a `real` implícitamente;
- son válidas las funciones sin argumentos y la salida vacía de un programa correcto.

Las respuestas coinciden con un intérprete aparte de las reglas en 237
casos que cubren programas válidos y los cuatro tipos de error.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1891_parsing.cpp](1891_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 516 KB |
| [1891_parsing.go](1891_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.046 s | 1180 KB |
| [1891_parsing.java](1891_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.109 s | 1288 KB |
| [1891_parsing.py](1891_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 644 KB |
| [1891_parsing.rs](1891_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.062 s | 492 KB |
