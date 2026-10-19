# 2028. Generar un programa de sumas triangulares en cuadrícula

[Timus 2028](https://acm.timus.ru/problem.aspx?space=1&num=2028) · dificultad 880 · constructive

Problema original de Kirill Borozdin, del Concurso Regional de Programación por Equipos de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Imprime un programa fijo en el lenguaje de cuadrícula descrito abajo. Al
recibir un entero `n`, para cada `1 ≤ n ≤ 100` debe imprimir exactamente
un entero `1+2+…+n` y terminar normalmente. Se acepta cualquier programa
correcto. El generador no recibe `n`: su única entrada es `Good luck!`,
que puede ignorar. Límites del generador: 1 segundo y 64 MB.

El programa generado es una cuadrícula `H×W`, con `1 ≤ H,W ≤ 100`. Tiene
un registro actual y 26 de memoria `A`…`Z`, todos a cero. El puntero
empieza arriba a la izquierda, mirando a la derecha. Cada paso ejecuta
una instrucción y se mueve una celda en la dirección resultante, sin
conectar los bordes.

| Instrucción | Significado |
| --- | --- |
| `^`, `>`, `v`, `<` | Fijar arriba, derecha, abajo, izquierda, respectivamente. |
| `.` | No hacer nada. |
| `A`…`Z` | Intercambiar el registro actual con el de memoria indicado. |
| `?` | Leer al registro actual; agotada la única entrada, repetir `n`. |
| `!` | Imprimir el valor actual y ponerlo a cero. |
| `+`, `-` | Incrementar o decrementar en uno. |
| `@` | Girar antihorario para cero y horario para cualquier valor no nulo. |
| `#` | Terminar inmediatamente sin moverse. |

Un valor absoluto mayor que 100000 causa `OVERFLOW ERROR` antes de
moverse; salir de la cuadrícula causa `RUNTIME ERROR`. Completar 1000000
pasos sin terminar ni otro error causa `TIME LIMIT EXCEEDED`. El
programa requerido debe evitar todos estos errores; imprimir el número
correcto antes de un error no basta.

## Entrada

Una línea `Good luck!`, que pertenece al generador. La entrada independiente del
programa generado es el entero `n`.

## Salida

Imprime `H W` y exactamente `H` filas de `W` instrucciones válidas. El
programa debe resolver todos los valores de destino permitidos, no solo
uno.

## Evaluación

Un comprobador ejecuta el programa impreso para cada n de 1 a 100 y lo
acepta si cada ejecución imprime una sola vez la suma correcta y se
detiene normalmente. El programa del ejemplo oficial solo muestra el
formato y no es una respuesta correcta, así que la salida guardada del
ejemplo se marca como `format_only` y no se comprueba.

## Ejemplos

```
Good luck!
```

```
4 6
?A?v>v
>..>@A
-...A!
^A.+<#
```
Este ejemplo oficial solo muestra el formato. Su programa no resuelve la
tarea: para el destino 1 produce 2 en lugar de 1. Los generadores
imprimen el programa correcto de abajo, por lo que no deben coincidir
con esta ilustración.

## Solución

```text
6 11
>?v........
.>>.......v
..@A+AB+B-<
..B........
..-........
.^@A!#.....
```
Usa `A` como suma y `B` como contador temporal. El registro actual
guarda el contador exterior `q`, inicialmente `n`. Para `q=n,n-1,…,1`,
añade `q` unidades a `A`, restaura `q` desde `B` y lo decrementa. Cuando
vale cero, intercambia `A` al registro actual, lo imprime y termina.

La macro interior `-B+BA+A` decrementa el valor actual, incrementa `B`
mediante intercambio, suma y nuevo intercambio, y hace lo mismo con `A`.
Tras `j` repeticiones, el actual es `q-j`, `B=j` y `A=old_sum+j`. Al
llegar a `j=q`, el actual es cero, `B=q` y se ha añadido todo `q`. La
salida `B-` restaura `q`, limpia `B` y deja `q-1`.

Con coordenadas desde cero, el `@` interior está en `(2,2)` y se alcanza
mirando a la izquierda. No cero gira arriba hacia el rectángulo
interior; cero gira abajo a `B-`. El cuerpo se recorre de derecha a
izquierda y aparece impreso al revés. El `@` exterior en `(5,2)` se
alcanza hacia abajo: no cero gira a la izquierda a `^` y al corredor de
regreso por `(1,1)` y `(1,2)`; cero gira a la derecha a `A!#`. La
lectura en `(0,1)` ocurre una sola vez.

El invariante exterior es actual `q`, `B=0` y `A` igual a la suma ya
procesada de `n` hasta `q+1`. El invariante interior demuestra que cada
vuelta añade exactamente `q` y restaura el estado para `q-1`. Al llegar
a cero, `A=1+…+n`; la única salida ocurre al final y va seguida de una
parada normal. Todos los valores están entre 0 y 5050 y el recorrido
permanece dentro de la cuadrícula 6×11.

Para `S=n(n+1)/2`, hay tres pasos iniciales, 18 por unidad añadida, ocho
entre vueltas exteriores y seis en la salida final. El total exacto es
`3+18S+8(n-1)+6 = 18S+8n+1`, como máximo 91701 con `n=100`, menos de un
millón.

El generador imprime 66 celdas fijas y usa `O(1)` tiempo y espacio. El
programa emitido usa `O(n²)` tiempo y `O(1)` registros. Son fases
distintas: calcular una fórmula en el generador no entrega por sí solo
un programa de cuadrícula funcional.

Trampas:

- Conserva el ejemplo oficial de formato, pero no lo trates como
  solución correcta.
- El generador no recibe `n`; el programa impreso debe atender todos sus
  valores.
- Las letras intercambian valores; la macro debe restaurar el contador actual.
- Revisa las direcciones de entrada a ambos `@` y la escritura inversa
  del cuerpo.
- Exige una única salida correcta y parada normal; un error posterior
  también invalida.

## Notas por lenguaje

Los cinco generadores imprimen las mismas filas literales con constantes
nombradas para altura y anchura, e ignoran la entrada. La salida fija es
la construcción pedida: sus ciclos funcionan para todos los valores. Los
puntos son instrucciones vacías; conserva exactamente anchuras y
direcciones.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2028_constructive.cpp](2028_constructive.cpp) | G++ 13.2 x64 | constructive | O(1) | AC | 0.001 s | 356 KB |
| [2028_constructive.go](2028_constructive.go) | Go 1.14 x64 | constructive | O(1) | AC | 0.001 s | 1024 KB |
| [2028_constructive.java](2028_constructive.java) | Java 1.8 | constructive | O(1) | AC | 0.078 s | 304 KB |
| [2028_constructive.py](2028_constructive.py) | Python 3.12 x64 | constructive | O(1) | AC | 0.046 s | 248 KB |
| [2028_constructive.rs](2028_constructive.rs) | Rust 1.75 x64 | constructive | O(1) | AC | 0.001 s | 184 KB |
