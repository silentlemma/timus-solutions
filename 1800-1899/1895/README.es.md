# 1895. Filetes a bordo

[Timus 1895](https://acm.timus.ru/problem.aspx?space=1&num=1895) · dificultad 2082 · dp

Problema original de Alex Samsonov, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Programar n pedidos en un equipo que procesa como máximo k pedidos
a la vez. Cada pedido necesita dos pasos separados e ininterrumpidos
de un minuto, con una posible pausa entre ambos. El pedido i debe
terminar como máximo en tᵢ y no puede empezar antes de max(0, tᵢ − x).

Los inicios deben ser enteros no negativos. Minimizar el número de
minutos en los que se ejecuta algún paso y construir un horario.
Los huecos inactivos no cuentan. Los límites son 1 segundo y 64 MB.

## Entrada

La primera línea contiene x y k, con 2 ≤ x ≤ 1000 y 1 ≤ k ≤ 50.
La segunda contiene n, con 1 ≤ n ≤ 50. La tercera contiene
t₁, …, tₙ en orden no decreciente, con 2 ≤ tᵢ ≤ 1000.

## Salida

Si no existe horario, escribir `-1`. En otro caso, escribir el mínimo
de minutos activos y después n pares de inicios, en orden de entrada.
Para el pedido i, aᵢ y bᵢ deben satisfacer
max(0, tᵢ − x) ≤ aᵢ < bᵢ y bᵢ + 1 ≤ tᵢ. En un mismo minuto pueden
empezar como máximo k pasos. Se acepta cualquier horario óptimo.

## Evaluación

Un verificador comprueba ventanas, orden de los pasos y capacidad,
además de que el número declarado de minutos activos sea igual a la
cantidad de inicios distintos. Ese número también debe ser óptimo;
un horario válido pero no óptimo se rechaza.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2
3
2 16 25
```

Salida:

```
5
0 1
11 15
15 17
```

### Ejemplo 2

Entrada:

```
10 2
4
7 8 9 10
```

Salida:

```
4
3 6
4 5
3 6
4 5
```

### Ejemplo 3

Entrada:

```
2 1
2
2 2
```

Salida:

```
-1
```

## Solución

Sea rᵢ = max(0, tᵢ − x). Tanto rᵢ como los plazos tᵢ son no
decrecientes. Puede suponerse que los primeros pasos siguen el orden
de pedidos, y los segundos también. Para probarlo, ordenar por separado
los inicios de primeros pasos a₁ ≤ … ≤ aₙ y de segundos b₁ ≤ … ≤ bₙ,
y asignar las posiciones i al pedido i. Las disponibilidades ordenadas
implican aᵢ ≥ rᵢ, y los plazos ordenados implican bᵢ + 1 ≤ tᵢ.
Los i segundos pasos más tempranos tienen i primeros pasos originales
anteriores a bᵢ, por lo que aᵢ < bᵢ. El número de pasos por minuto
no cambia al reasignarlos.

Usar programación dinámica por cantidad c de minutos activos.
El estado (c, i, j) guarda el último inicio más temprano después de
i primeros pasos y j segundos. Inicialmente (0, 0, 0) tiene tiempo −1.
Basta guardar el tiempo más temprano: ese prefijo puede repetir
cualquier continuación de otro posterior con los mismos contadores,
sin violar ventanas ni capacidad.

Elegir p primeros pasos nuevos, con 0 ≤ p ≤ min(k, n − i). Llenar
el espacio restante con q = min(k − p, i − j) segundos pasos antiguos.
Omitir p + q = 0. Solo pedidos ya empezados pueden recibir el segundo
paso, así que ninguno ejecuta ambos en el mismo minuto. El nuevo inicio
es el tiempo anterior más 1, elevado además a rᵢ₊ₚ si p > 0. Si q > 0,
su final no puede superar tⱼ₊₁, el primer plazo de esos segundos pasos.
Actualizar (c + 1, i + p, j + q) con el mínimo tiempo obtenido.

Tomar el mayor q es seguro: la capacidad libre puede terminar más
pedidos antiguos ahora y sus segundos pasos se eliminan del futuro.
Esos pedidos terminan antes y las demás operaciones conservan su hora.
Por tanto, un q menor no permite una continuación mejor.

Descartar un estado si al siguiente pedido pendiente ya no le queda
tiempo. Después de un último inicio en s, un pedido con el primer paso
hecho no termina antes de s + 2; uno aún sin empezar no termina antes
de s + 3. Son condiciones necesarias y no excluyen un horario factible.

La primera capa que llega a (n, n) da el mínimo de minutos activos.
Guardar predecesores y minutos elegidos para reconstruir ambos inicios.
Si ninguna capa hasta 2n alcanza la meta, escribir −1: cualquier
horario ocupa como máximo 2n minutos distintos.

Hay `O(n³)` estados entre todas las capas y como máximo k + 1
transiciones por estado. El tiempo es `O(n³k)` y la memoria para
reconstruir es `O(n³)`.

En el primer ejemplo, el pedido 1 obliga a usar los minutos 0 y 1.
Las ventanas de los pedidos 2 y 3 comparten solo un minuto, de modo
que esos dos pedidos necesitan al menos otros tres minutos activos.
La salida usa exactamente cinco. En el segundo hay ocho pasos y
capacidad 2: se necesitan al menos cuatro minutos, logrados con 3, 4,
5 y 6. En el tercero, solo se permiten los minutos 0 y 1 y cuatro
pasos no caben con capacidad 1.

Trampas:

- un paso que empieza en tᵢ termina demasiado tarde;
- los dos pasos de un pedido necesitan minutos distintos;
- limitar inferiormente a cero las disponibilidades negativas;
- minimizar minutos ocupados, no el intervalo entre el primero y el último;
- llenar minutos antiguos con una regla voraz puede impedir una mejor reasignación.

Una búsqueda exhaustiva con comprobación por flujo confirma el óptimo en
408 casos pequeños, y 19 horarios rebuscados ponen a prueba el
verificador.

## Notas por lenguaje

Cada versión codifica `(i, j)` como `i·(n+1)+j` y recorre solo los
estados activos de cada capa. Se conservan las capas de tiempos y de
predecesores para reconstruir el horario.

Python usa arreglos de enteros cortos con signo, `array("h")`, para ambas:
el estado codificado no supera `51²−1 = 2600` y el centinela de tiempo no
supera 1001, por lo que caben los valores guardados, incluido −1. Las
versiones compiladas usan arreglos o vectores de enteros nativos; Java
lee con un `StreamTokenizer` sobre entrada con búfer.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1895_dp.cpp](1895_dp.cpp) | G++ 13.2 x64 | dp | O(n³ k) | AC | 0.015 s | 2168 KB |
| [1895_dp.go](1895_dp.go) | Go 1.14 x64 | dp | O(n³ k) | AC | 0.031 s | 6248 KB |
| [1895_dp.java](1895_dp.java) | Java 1.8 | dp | O(n³ k) | AC | 0.125 s | 3568 KB |
| [1895_dp.py](1895_dp.py) | Python 3.12 x64 | dp | O(n³ k) | AC | 0.156 s | 1632 KB |
| [1895_dp.rs](1895_dp.rs) | Rust 1.75 x64 | dp | O(n³ k) | AC | 0.031 s | 3168 KB |
