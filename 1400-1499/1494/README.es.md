# 1494. Monobillar

[Timus 1494](https://acm.timus.ru/problem.aspx?space=1&num=1494) · dificultad 90 · simulation

Problema original de Alex Samsonov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las bolas 1, 2, …, N (1 ≤ N ≤ 100000) deben meterse en la única
tronera en este orden. De vez en cuando un inspector sacaba de la
tronera la última bola que había entrado, y al final las sacó todas.
Dado el orden en que el inspector sacó las bolas, hay que escribir
«Cheater» si no pudieron meterse en el orden correcto, y «Not a proof»
en otro caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego las N bolas en el orden en que las sacó el inspector.

## Salida

«Cheater» o «Not a proof».

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2
1
```

Salida:

```
Not a proof
```

### Ejemplo 2

Entrada:

```
3
3
1
2
```

Salida:

```
Cheater
```

## Solución

La tronera es una pila: las bolas entran como 1, 2, …, N y el inspector
siempre saca la de arriba. Se repite la partida: se meten las bolas en
orden y, tras cada una, se sacan bolas mientras la de arriba sea la
siguiente de la lista del inspector. Esperar nunca ayuda, porque una
bola que no está arriba sigue tapada hasta que se va todo lo que tiene
encima. Si así se saca toda la lista, el orden era posible. `O(N)`.

Detalles a tener en cuenta:

- una bola tapada por otra posterior no puede salir antes: 3, 4, 1, 2
  es imposible (pruebas 02, 05);
- sacar todas las bolas al final invierte el orden, y sacar cada una al
  momento lo mantiene; ambos son posibles (gen4, gen5);
- un solo intercambio en una partida real suele bastar para hacerla
  imposible (gen3).

## Soluciones optimizadas

`1494_bitmask_simulation.py`. Representa la pila pendiente con paquetes no vacíos ordenados de 32 bits, no una celda entera por bola. Un máximo nuevo inserta solo el intervalo omitido; una bola antigua debe ser el bit mayor del último paquete antes de quitarlo. Índice y máscara van juntos: sin copiar un entero de N bits ni recorrer palabras vacías. N<=100000 limita cada paquete a 44 bits; O(N) trabajo total, O(ceil(N/32)) paquetes más lector de 4096 bytes. bitmask_simulation determinista difiere de las pilas explícitas conservadas. Métrica actual PyPy, par previo CPython separado.

Fuente exacto: PyPy 3.10 x64 Accepted #11327514: 0.14 s / 3764 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 20/164; 1/164. Admisión estricta usa tiempo y memoria con 1024 KB o más: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Conserva asterisco por la meta propia de primer puesto en ambas. La variante anterior conservada tiene su par propio #11326685 (Python 3.12 x64): 0.14 s / 4160 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1494_bitmask_simulation.py`: 0.14 s / 3764 KB; base didáctica conservada `1494_simulation.py` (Python 3.12 x64): 0.14 s / 15568 KB.

`1494_simulation_optimized.py`. Simula al leer cada bola: apila las aún no introducidas hasta ella y exige esa bola en la cima; termina ante la primera contradicción. Usa una lista Python preasignada de N celdas en vez de array sin signo. Cada bola entra/sale una vez: O(N) tiempo, O(N) espacio más tokens de la línea actual, sin otra lista del orden observado. Conserva la simulación legible.

Accepted exacto CPython 3.12 #11326685: 0.14 s / 4160 KB. Comparación guardada 2026-11-20 de compiladores actuales: tiempo 20/164, memoria 1/164. Ambas métricas exigidas pasan diez primeros o 15% superior, redondeando el corte porcentual hacia arriba. El asterisco sigue la meta separada Python de primer puesto en ambas.

El envío optimizado documentado antes #11303753 (Python 3.12 x64) registró 0.171 s / 832 KB. El actual CPython 3.12 registra menor tiempo y mayor memoria. Son medidas emparejadas de ejecuciones distintas; la comparación incluye elección de intérprete y variabilidad del juez.

- `1494_simulation_optimized.py`: 0.14 s / 4160 KB; base didáctica conservada `1494_simulation.py` (Python 3.12 x64): 0.14 s / 15568 KB.

Las soluciones optimizadas simulan la tronera mientras leen: para cada bola sacada meten las bolas hasta ese número, y entonces arriba de la tronera debe estar esa bola; el primer desacuerdo termina el programa. Así nunca guardan el orden de las bolas; la tronera es un arreglo usado como pila. C++ analiza los números con `getchar` (0.031 s en lugar de 0.093 s y 512 KB en lugar de 1540 KB), Go los analiza a mano, escribe la respuesta sin `fmt` y guarda la tronera en un arreglo de `int32` reservado de antemano, ya que los números de las bolas son a lo sumo 100 000 (1312 KB en lugar de 7684 KB, con el mismo tiempo), Java lee bloques de 4 KB y los analiza a mano en lugar de `StreamTokenizer` (844 KB en lugar de 1300 KB, con el mismo tiempo) y Rust analiza a mano desde un búfer de 4 KB (604 KB en lugar de 2704 KB, con el mismo tiempo).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1494_simulation.cpp](1494_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.093 s | 1540 KB | 11287211 |
| [1494_simulation.go](1494_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.062 s | 7684 KB | 11303301 |
| [1494_simulation.java](1494_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.109 s | 1300 KB | 11303468 |
| [1494_simulation.py](1494_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.140 s | 15568 KB | 11287213 |
| [1494_simulation.rs](1494_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 2704 KB | 11287216 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1494_simulation_optimized.cpp](1494_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.031 s | 512 KB | 11303751 |
| [1494_simulation_optimized.go](1494_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.046 s | 1312 KB | 11303612 |
| [1494_simulation_optimized.java](1494_simulation_optimized.java) | Java 1.8 | simulation | O(N) | AC | 0.125 s | 844 KB | 11303752 |
| [1494_simulation_optimized.py](1494_simulation_optimized.py) | Python 3.12 x64 | simulation | O(N) time and space | AC | 0.14 s | 4160 KB | 11326685 |
| [1494_bitmask_simulation.py](1494_bitmask_simulation.py) | PyPy 3.10 x64 | bitmask, simulation | O(N) time; O(ceil(N/32)) packets + fixed buffer | AC | 0.14 s | 3764 KB | 11327514 |
| [1494_simulation_optimized.rs](1494_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.015 s | 604 KB | 11303754 |
