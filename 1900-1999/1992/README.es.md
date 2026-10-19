# 1992. Compartir historiales inmutables de aprendizaje y deshacer

[Timus 1992](https://acm.timus.ru/problem.aspx?space=1&num=1992) · dificultad 372 · trees, simulation

Problema original de Egor Shchelkonogov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La entidad 1 empieza sin programas aprendidos ni historial de deshacer.
Procese `n` órdenes con identificadores de programa `1..m`. Aprender
añade un programa y borra los deshacer de esa entidad. Deshacer quita el
último aprendido y lo registra; rehacer restaura el último deshecho.
Copiar crea una entidad con ambos historiales actuales. Una consulta
pide el último programa aprendido, o `basic` si no hay ninguno.

Límites: `1≤n,m≤500000`. Todas las órdenes son válidas: la entidad
existe, el programa nuevo no está aprendido, deshacer tiene un programa
que quitar y rehacer tiene un registro que restaurar. Un programa
deshecho puede aprenderse otra vez. Tiempo: 2 segundos; memoria: 64 MB.

## Entrada

La primera línea contiene `n m`, seguida de `n` órdenes:

- `learn c p`: aprender `p`, `1≤p≤m`, y borrar los deshacer de `c`.
- `rollback c`: deshacer el último programa aprendido.
- `relearn c`: restaurar el deshacer más reciente.
- `clone c`: copiar ambos historiales a la siguiente entidad nueva.
- `check c`: consultar el último aprendido.

Los identificadores nuevos siguen el orden de creación, después del
inicial 1. Copiar no modifica el original.

## Salida

Para cada `check`, en orden, escriba un identificador o `basic` en
minúsculas, uno por línea. Sin consultas, la salida es vacía.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

Entrada:

```
9 10
learn 1 5
learn 1 7
rollback 1
check 1
clone 1
relearn 2
check 2
rollback 1
check 1
```

Salida:

```
5
7
basic
```

Tras el primer deshacer, la entidad 1 conserva 5 y puede restaurar 7. La
copia conserva ambas partes. La entidad 2 restaura 7 sin cambiar la 1;
el último deshacer deja la 1 en estado básico.

## Solución

Cada entidad tiene dos cabezas: `A`, pila de aprendidos con el más
reciente arriba, y `R`, pila de deshechos con el último rollback arriba.
Todas comparten un depósito de nodos. Un nodo `(programa,anterior)` es
inmutable después de crearse; el índice 0 representa vacío. Insertar `p`
sobre `h` crea `(p,h)`; sacar la cima lee su anterior.

- Aprender: `A=push(p,A)`, `R=0`.
- Deshacer: guardar `t=A`, luego `A=previous[t]`, `R=push(value[t],R)`.
- Rehacer: guardar `t=R`, luego `R=previous[t]`, `A=push(value[t],A)`.
- Copiar: copiar los dos índices enteros.
- Consultar: `value[A]` si `A` es no nulo, o `basic`.

Borrar historial solo pone su cabeza a cero; no elimine nodos
compartidos, pues otra entidad puede necesitarlos. Las copias comparten
colas inmutables y cada modificación sustituye solo sus propias cabezas.
No se recorre ni copia ninguna lista, ni hace falta un conjunto de
programas aprendidos: la entrada ya es válida.

Una cabeza no nula `h` representa `value[h]` seguido de la secuencia de
`previous[h]`; cero representa vacío. Crear un nodo añade exactamente un
elemento a la cima. Como los nodos antiguos nunca cambian, copiar una
cabeza conserva toda su secuencia aunque otras cabezas cambien después.

Por inducción, al inicio ambas historias son vacías. Aprender inserta el
programa y borra la secuencia de rehacer. Deshacer mueve exactamente el
último aprendido a deshechos; rehacer realiza el movimiento inverso.
Copiar mantiene ambas secuencias y consultar lee la cima correcta. Por
tanto, la representación cumple siempre la especificación y todas las
respuestas son correctas.

Aprender, deshacer y rehacer crean un nodo cada uno; copiar y consultar
ninguno. Hay como máximo `n` nodos y `n+1` entidades. Cuatro arreglos de
longitud `n+2` guardan valores, anteriores y las dos tablas de cabezas.
Todo cabe en 32 bits: `4·4·(500000+2)=8000032` bytes máximos, unos 7.63
MiB.

Cada orden requiere `O(1)` trabajo de pilas; tiempo total `O(n)` para
tokens acotados y memoria `O(n)`. Con `I` bytes de entrada y `B` de
salida, Go y Rust retienen además `I`; C++, Go, Python y Rust acumulan
`B`. Java escribe mediante un flujo con búfer y reutiliza un arreglo de
dígitos para no crear una cadena por respuesta numérica. Aquí `B≤7n`,
por lo que la memoria total sigue siendo lineal.

Python usa `array('i')` compacto y lee una orden por línea; tuplas por
nodo o listas copiadas cuestan demasiada memoria. Go usa arreglos de 32
bits y lector de bytes compatible con 1.14. Java usa `int` y entrada por
búfer. Rust usa índices `u32`, convertidos al acceder a vectores. Copiar
listas completas puede dar tiempo y memoria cuadráticos cuando muchas
entidades copian una historia profunda.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1992_trees.cpp](1992_trees.cpp) | G++ 13.2 x64 | trees | O(n) | AC | 0.156 s | 13608 KB |
| [1992_trees.go](1992_trees.go) | Go 1.14 x64 | trees | O(n) | AC | 0.062 s | 32780 KB |
| [1992_trees.java](1992_trees.java) | Java 1.8 | trees | O(n) | AC | 0.171 s | 10724 KB |
| [1992_trees.py](1992_trees.py) | Python 3.12 x64 | trees | O(n) | AC | 0.609 s | 14972 KB |
| [1992_trees.rs](1992_trees.rs) | Rust 1.75 x64 | trees | O(n) | AC | 0.078 s | 13340 KB |
