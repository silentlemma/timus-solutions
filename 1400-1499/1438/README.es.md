# 1438. Time Limit Exceeded

[Timus 1438](https://acm.timus.ru/problem.aspx?space=1&num=1438) · dificultad 2917 · simulation

Problema original de Alexander Klepinin, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que ejecutar un programa de un lenguaje diminuto con 2000 líneas
como mucho. Cada línea tiene una etiqueta, un comando o una etiqueta
seguida de un comando. Los comandos son `end`, `print x`, asignaciones
`v = x`, `v = x op y` con op entre `+ - * / % or and xor`, `v = not x`,
`goto label` e `if x cmp y goto label` con las seis comparaciones
habituales; x e y son variables o números. Las etiquetas y las palabras
clave no distinguen mayúsculas, los nombres de variables sí. Los
valores son enteros de 32 bits y nunca se desbordan.

Se imprime lo que imprime el programa. Si tras diez millones de
comandos sigue en marcha, se detiene y se añade la línea «Program
terminated. Variables state:» seguida de «nombre: valor» para cada
variable que ya recibió un valor, ordenadas por nombre.

Límite de tiempo: 1.5 segundos. Límite de memoria: 64 MB.

## Entrada

El programa; puede haber cualquier cantidad de espacios en cualquier
sitio salvo entre una etiqueta y sus dos puntos.

## Salida

Los valores impresos y, si el programa se detuvo, el informe.

## Ejemplos

### Ejemplo 1

Entrada:

```
X = 5
      Y = 1
loop: Y = Y * X
      X = X - 1
      if X >= 1 goto LOOP
      Print Y
      y = Y - 5
      Print y
      end
```

Salida:

```
120
115
```

### Ejemplo 2

Entrada:

```
value = 15
        value = not value
        value = value or 4
        print value
        value = 0
loop:   
        value = value - 1
        Value = value % 6
        ValueA = value % -6
        goto loop
```

Salida:

```
-12
Program terminated. Variables state:
Value: 3
ValueA: 3
value: -2499999
```

## Solución

Primero se compila y después se ejecuta. Cada línea se parte en
palabras; una primera palabra que acaba en «:» es una etiqueta y apunta
al índice del comando siguiente, así que una línea con solo una
etiqueta, o varias seguidas, llevan al comando que viene después. Cada
variable y cada número ocupan una casilla en una única tabla de
valores, de modo que cada comando se convierte en un registro pequeño:
un tipo, números de casilla, un código de operación y un destino de
salto. La ejecución es un bucle simple sobre esos registros con un
contador; mientras corre el programa no se busca nada por nombre.

Los comandos se distinguen por su forma: una segunda palabra «=» indica
una asignación, y su longitud dice si es una copia, un `not` o una
operación binaria. La división redondea hacia cero, y el resto se toma
como `(a mod b + |b|) mod |b|`, que nunca es negativo: el segundo
ejemplo necesita que `% 6` y `% -6` den 3 para un valor negativo. El
informe se imprime cuando se ejecutaron exactamente diez millones de
comandos y el último no fue `end`, aunque ese comando estuviera en la
última línea. `O(L + K)` con L la longitud del programa y K = 10⁷ el
límite de pasos.

Detalles a tener en cuenta:

- una etiqueta sola en una línea, o dos seguidas (prueba 03), y una
  etiqueta que se llama como una palabra clave (prueba 11);
- variables cuyo nombre empieza por una palabra clave, como `ifi`
  (prueba 10);
- una asignación saltada deja la variable fuera del informe (prueba 04);
- `end` como comando diez millones es un final normal, cualquier otro
  comando ahí no lo es (pruebas 12, 13, 17);
- los nombres se ordenan por códigos de carácter, así que las mayúsculas
  van primero (prueba 16).

## Notas por lenguaje

- Python se ejecuta con PyPy: los bucles más largos tardan unos 1,6 s
  con CPython y unos 0,4 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1438_simulation.cpp](1438_simulation.cpp) | G++ 13.2 x64 | simulation | O(L + K) | AC | 0.281 s | 1864 KB |
| [1438_simulation.go](1438_simulation.go) | Go 1.14 x64 | simulation | O(L + K) | AC | 0.125 s | 4840 KB |
| [1438_simulation.java](1438_simulation.java) | Java 1.8 | simulation | O(L + K) | AC | 0.421 s | 7320 KB |
| [1438_simulation.py](1438_simulation.py) | PyPy 3.10 x64 | simulation | O(L + K) | AC | 0.843 s | 8448 KB |
| [1438_simulation.rs](1438_simulation.rs) | Rust 1.75 x64 | simulation | O(L + K) | AC | 0.140 s | 2096 KB |
