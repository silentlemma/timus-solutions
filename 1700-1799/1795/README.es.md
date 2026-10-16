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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1795_simulation.cpp](1795_simulation.cpp) | G++ 13.2 x64 | simulation | O(n^2) | AC | 0.031 s | 576 KB |
| [1795_simulation.go](1795_simulation.go) | Go 1.14 x64 | simulation | O(n^2) | AC | 0.046 s | 6376 KB |
| [1795_simulation.java](1795_simulation.java) | Java 1.8 | simulation | O(n^2) | AC | 0.125 s | 4680 KB |
| [1795_simulation.py](1795_simulation.py) | Python 3.12 x64 | simulation | O(n^2) | AC | 0.093 s | 1080 KB |
| [1795_simulation.rs](1795_simulation.rs) | Rust 1.75 x64 | simulation | O(n^2) | AC | 0.031 s | 652 KB |
