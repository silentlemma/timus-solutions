# 1795. Maridos en una tienda

[Timus 1795](https://acm.timus.ru/problem.aspx?space=1&num=1795) · dificultad 253 · simulation

Problema original de Andrew Gein, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tienda tiene m productos en cantidades dadas, y n maridos hacen
cola delante de Mark, cada uno queriendo cierta cantidad de un
producto. En el mostrador, lo que lleva un minuto, un marido compra su
cantidad si hay suficiente, o se va si el producto no existe o se
agotó. Si hay algo pero no basta, deja pasar a la siguiente persona y
llama a casa, quedándose segundo; le dicen que se lleve el resto,
vuelve y lo compra todo si la cantidad no cambió, se va si no queda
nada, y si no, deja pasar a una persona más y vuelve a llamar. ¿Cuántos
minutos pasan antes de que Mark llegue al mostrador?

## Entrada

m (1 ≤ m ≤ 1000) líneas "amount of name", luego n (1 ≤ n ≤ 1000) líneas
de la misma forma para los maridos, desde el principio de la cola. Las
cantidades van de 1 a 1000, los nombres tienen hasta 20 letras
minúsculas, y un marido puede querer un producto que la tienda no
vende.

## Salida

El número de minutos.

## Evaluación

Se comparan los tokens; los espacios adicionales no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 of sweets
4 of milk
1 of sausage
4
2 of milk
3 of sweets
3 of milk
1 of cheese
```

Salida:

```
6
```

## Solución

Se simula la cola. Cada visita al mostrador es un minuto. Para cada
marido se guarda la cantidad que le dijeron en su última visita. Un
marido que debe llamar vuelve a la cola detrás de la siguiente persona;
si ya no queda nadie antes de Mark, el siguiente es Mark y la cuenta
termina ahí. Cuando vuelve, la cantidad se compara con la que le
dijeron: igual significa que se lo lleva todo, cero que se va, y
cualquier otra cosa, otra llamada. La cola tiene como mucho 1000
maridos y cada llamada mueve al que llama un lugar atrás, así que la
simulación es rápida. `O(n²)`.

En el ejemplo el primer marido compra 2 de las 4 leches. El segundo
encuentra solo 2 dulces y se coloca detrás del tercero, que encuentra
solo 2 leches y también retrocede. Luego ambos vuelven a cantidades sin
cambios y las compran, y el último no encuentra queso: 6 visitas antes
de Mark.

Trampas:

- un marido que vuelve a una cantidad sin cambios la compra entera,
  aunque sea menos de lo que quería;
- un marido que debe llamar siendo el último de la cola deja pasar a
  Mark, así que Mark está en el mostrador justo después de ese minuto;
- cada visita cuenta como un minuto, incluida la que termina en una
  llamada.

Las respuestas coinciden con una implementación aceptada independiente
en 300 casos aleatorios, entre ellos un único producto con raros
compradores de todo que vuelven a llamar tras cada compra pequeña.

## Soluciones optimizadas

Se conserva la simulación del mostrador, resolviendo nombres de productos a IDs enteros solo durante la lectura. La cola usa arreglos y un índice frontal. Intercambiar con el siguiente cliente es un intercambio in situ, no una inserción o borrado que desplaza la cola. Los productos ausentes tienen stock nulo. Se preservan visitas y cambios de stock, eliminando búsquedas repetidas, copias de cola y retención de toda la entrada.

- `1795_simulation_optimized.cpp`: 0.031 s / 272 KB; base `1795_simulation.cpp`: 0.031 s / 552 KB; cambio respecto a la base: tiempo -0.0%, memoria -50.7%.
- `1795_simulation_optimized.go`: 0.031 s / 1132 KB; base `1795_simulation.go`: 0.046 s / 6376 KB; cambio respecto a la base: tiempo -32.6%, memoria -82.2%.
- `1795_simulation_optimized.java`: 0.093 s / 1076 KB; base `1795_simulation.java`: 0.125 s / 4688 KB; cambio respecto a la base: tiempo -25.6%, memoria -77.0%.
- `1795_simulation_optimized.py`: 0.078 s / 612 KB; base `1795_simulation.py`: 0.078 s / 1100 KB; cambio respecto a la base: tiempo -0.0%, memoria -44.4%.
- `1795_simulation_optimized.rs`: 0.031 s / 508 KB; base `1795_simulation.rs`: 0.062 s / 632 KB; cambio respecto a la base: tiempo -50.0%, memoria -19.6%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1795_simulation.cpp`; versión que cubre `1795_simulation_optimized.cpp`; puestos tiempo/memoria 47/1, registros de otros autores 53/53.

- Go: base didáctica preferida `1795_simulation.go`; versión que cubre `1795_simulation.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1795_simulation.java`; versión que cubre `1795_simulation.java`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Python/PyPy: base didáctica preferida `1795_simulation.py`; versión que cubre `1795_simulation.py`; puestos tiempo/memoria 1/1, registros de otros autores 6/6.

- Rust: base didáctica preferida `1795_simulation.rs`; versión que cubre `1795_simulation.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1795_simulation.cpp](1795_simulation.cpp) | G++ 13.2 x64 | simulation | O(n^2) | AC | 0.031 s | 552 KB | 11308937 |
| [1795_simulation.go](1795_simulation.go) | Go 1.14 x64 | simulation | O(n^2) | AC | 0.046 s | 6376 KB | 11289883 |
| [1795_simulation.java](1795_simulation.java) | Java 1.8 | simulation | O(n^2) | AC | 0.125 s | 4688 KB | 11308939 |
| [1795_simulation.py](1795_simulation.py) | Python 3.12 x64 | simulation | O(n^2) | AC | 0.078 s | 1100 KB | 11308940 |
| [1795_simulation.rs](1795_simulation.rs) | Rust 1.75 x64 | simulation | O(n^2) | AC | 0.062 s | 632 KB | 11308942 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1795_simulation_optimized.cpp](1795_simulation_optimized.cpp) \* | G++ 13.2 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.031 s | 272 KB | 11308816 |
| [1795_simulation_optimized.go](1795_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.031 s | 1132 KB | 11308817 |
| [1795_simulation_optimized.java](1795_simulation_optimized.java) | Java 1.8 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.093 s | 1076 KB | 11308818 |
| [1795_simulation_optimized.py](1795_simulation_optimized.py) | Python 3.12 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.078 s | 612 KB | 11308814 |
| [1795_simulation_optimized.rs](1795_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.031 s | 508 KB | 11308820 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
