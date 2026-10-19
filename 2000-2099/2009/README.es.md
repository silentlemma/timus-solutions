# 2009. Dos colas con un segundo de servicio por persona

[Timus 2009](https://acm.timus.ru/problem.aspx?space=1&num=2009) · dificultad 833 · simulation

Problema original de Alexey Kungurtsev, del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los estudiantes llegan a dos colas, izquierda y derecha. Cada servicio
tarda un segundo y empieza en cuanto es posible. Una persona puede ir a
cualquier final de cola o ponerse inmediatamente detrás de un conocido
de su lista que siga en ella. Elegir la posición con menos personas
delante; en empate, la cola derecha. Después no puede cambiar de cola.
Un grupo llega simultáneamente pero decide persona por persona en el
orden dado. Si coinciden servicio completado y llegada, primero se
completan los servicios de ambas colas. Hallar salida y cola de cada
estudiante.

## Entrada

`n m`, `5 ≤ n ≤ 1000`, `1 ≤ m ≤ n`, con estudiantes 1..n. Las siguientes
`n` líneas enumeran como máximo 100 IDs ajenos tras los que esa persona
puede colocarse y terminan en 0. El permiso es dirigido, no
necesariamente mutuo, y no incluye el propio ID. Cada grupo tiene una
línea `t k` y otra con sus `k` IDs en orden de llegada. Los tiempos son
enteros crecientes `1 ≤ t ≤ 10^9`; cada persona aparece exactamente una
vez. Tiempo 1 segundo, memoria 64 MB.

## Salida

Imprimir `n` líneas por orden de ID, cada una con la salida y `left` o
`right`. Los números y palabras únicos se comparan token a token.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
5 1
0
0
0
0
1 0
1 5
1 2 3 4 5
```

```
2 right
2 left
4 right
3 left
3 right
```

Tras las primeras cuatro llegadas, derecha es `[1,3]` e izquierda
`[2,4]`. El estudiante 5 puede colocarse detrás de 1, dejando derecha
`[1,5,3]`. Todos llegan en 1, por lo que los frentes salen en 2. El 5
sale en 3 y el 3 en 4; la salida sigue ordenada por ID.

## Solución

Guardar ambas colas como arreglos ordenados. Cada persona tiene cola
actual, o −1 si no espera, y posición desde cero. Cada cola no vacía
guarda el próximo tiempo de finalización del frente. Una posición
antigua de quien salió se ignora mediante la marca de pertenencia.

Antes del grupo en `t`, avanzar ambos servicios. Si el próximo final es
`u≤t`, salen exactamente `min(longitud,t−u+1)` personas del frente.
Registrar tiempos `u,u+1,…`, marcar ausentes, borrar ese prefijo y
actualizar posiciones restantes. Si quedan personas, sumar el número
servido al próximo final; si no, marcar inactividad. Así los huecos de
hasta `10^9` se saltan aritméticamente.

Para cada llegada empezar con las dos posiciones finales. Cada conocido
listado todavía presente ofrece su posición más uno en su cola. Tomar
los mínimos. Elegir izquierda solo cuando su posición sea estrictamente
menor; en otro caso derecha. Insertar y actualizar el sufijo desplazado.
Si la cola estaba vacía, el nuevo frente termina en `t+1`. Después del
último grupo registrar las salidas restantes a intervalos de un segundo
desde el próximo final de cada cola.

Inducción sobre llegadas. Al principio arreglos, pertenencia y relojes
describen colas vacías. En un intervalo sin llegadas, el frente termina
en el tiempo guardado y las siguientes personas en segundos consecutivos
según el arreglo. La fórmula del prefijo servido ejecuta exactamente
todos los finales hasta `t`, incluida la igualdad, y restaura posiciones
antes de cualquier nueva llegada.

Las posiciones legales son precisamente los finales y los lugares tras
conocidos listados presentes. Los mínimos y el desempate derecho
seleccionan la posición exigida. En una cola no vacía toda inserción
legal tiene índice al menos uno, por lo que nunca desplaza al frente en
servicio ni cambia su reloj. En una cola vacía el servicio empieza ahora
y termina un segundo después. Actualizar el sufijo conserva todos los
hechos para la siguiente persona del mismo grupo. El vaciado final es el
mismo proceso sin nuevas llegadas. Todos los registros son correctos.

Sea `F≤100n` el total de conocidos listados. Hasta `n` inserciones y
`2m` lotes de servicio desplazan o recalculan como máximo `n` posiciones
cada uno, y las consultas de conocidos suman `F`. Tiempo `O(n²+F)`,
memoria `O(n+F)` con entrada y salida. No se recorren los segundos
reales. Toda salida es como máximo `max_llegada+n≤1000001000`, dentro
del entero con signo de 32 bits.

## Notas por lenguaje

Completar servicios antes de todas las llegadas simultáneas e ignorar
conocidos futuros o ya salidos. Los permisos son dirigidos. Nuevos
seguidores se insertan justo tras la persona, antes de seguidores
anteriores; no forman un grupo permanente. Los empates eligen derecha,
el reloj inactivo reinicia desde la nueva llegada y los resultados se
guardan por ID. Los cinco programas usan arreglos o listas iterativos;
Java utiliza entrada con búfer y filas primitivas de conocidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2009_simulation.cpp](2009_simulation.cpp) | G++ 13.2 x64 | simulation | O(n^2 + F) | AC | 0.015 s | 640 KB |
| [2009_simulation.go](2009_simulation.go) | Go 1.14 x64 | simulation | O(n^2 + F) | AC | 0.078 s | 5532 KB |
| [2009_simulation.java](2009_simulation.java) | Java 1.8 | simulation | O(n^2 + F) | AC | 0.140 s | 1684 KB |
| [2009_simulation.py](2009_simulation.py) | Python 3.12 x64 | simulation | O(n^2 + F) | AC | 0.109 s | 10744 KB |
| [2009_simulation.rs](2009_simulation.rs) | Rust 1.75 x64 | simulation | O(n^2 + F) | AC | 0.046 s | 1780 KB |
