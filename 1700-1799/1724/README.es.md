# 1724. El origen del hombre aclarado

[Timus 1724](https://acm.timus.ru/problem.aspx?space=1&num=1724) · dificultad 658 · strings

Problema original de Alex Samsonov (preparado por Ivan Burmistrov), del Concurso Regional Escolar de Programación de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las cadenas de ADN usan los nucleótidos `A`, `C`, `G`, `T` y sus
antinucleótidos `a`, `c`, `g`, `t`. Una cadena humana es la vacía, dos
cadenas humanas seguidas, o una cadena humana con un nucleótido delante
y su antinucleótido al final. Responder si ciertas subcadenas de una
cadena son humanas.

## Entrada

Una cadena de longitud L (1 ≤ L ≤ 100 000) sobre `ACGTacgt`, luego q
(1 ≤ q ≤ 50 000) y q pares l y r (1 ≤ l ≤ r ≤ L), la primera y la
última posición de una subcadena.

## Salida

Una línea de q caracteres: `1` si la subcadena es humana y `0` si no.

## Ejemplos

### Ejemplo 1

Entrada:

```
caAgtGTtgAacCc
5
2 3
6 9
10 11
1 14
13 14
```

Salida:

```
01101
```

## Solución

Las cadenas humanas son secuencias de paréntesis de cuatro clases: un
nucleótido abre y su antinucleótido cierra. Una subcadena es humana
justo cuando una pila, alimentada con sus letras, nunca encuentra un
cierre que no encaje con la cima y termina vacía.

Se alimenta toda la cadena a una sola pila y se da un nombre a la pila
tras cada prefijo, un nodo de un árbol. Apilar crea un hijo nuevo del
nodo actual, un cierre que encaja vuelve al padre, y un cierre que no
encaja, o que llega al fondo, empieza un nodo suelto nuevo. Una
subcadena de l a r es humana justo cuando el nodo tras r es el nodo
tras l − 1: un trozo humano solo apila lo que vuelve a desapilar, y un
trozo que baja de su inicio, o encuentra un cierre equivocado, ya no
puede volver, porque cada apilado posterior crea un nodo nuevo. Así cada
consulta es una comparación. `O(L + q)`.

En el ejemplo son humanas `GTtg` (6–9), `Aa` (10–11) y `Cc` (13–14),
mientras que `aA` (2–3) cierra antes de abrir, igual que la cadena
entera.

Trampas:

- `cC` y `GTgt` no son humanas: importan el orden y el anidamiento;
- un cierre que encaja con la pila global puede pertenecer a una
  apertura anterior a l, por eso no basta con que la pila tenga el
  mismo contenido y el nodo debe ser el mismo;
- con 50 000 consultas y un límite de 0,5 s, cada consulta debe
  responderse sin recorrer su subcadena.

Las respuestas coinciden con una búsqueda directa desde la gramática
para todas las subcadenas de 300 cadenas cortas aleatorias, y con una
implementación aceptada independiente en las largas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1724_strings.cpp](1724_strings.cpp) | G++ 13.2 x64 | strings | O(L + q) | AC | 0.031 s | 1604 KB |
| [1724_strings.go](1724_strings.go) | Go 1.14 x64 | strings | O(L + q) | AC | 0.093 s | 6976 KB |
| [1724_strings.java](1724_strings.java) | Java 1.8 | strings | O(L + q) | AC | 0.125 s | 5808 KB |
| [1724_strings.py](1724_strings.py) | Python 3.12 x64 | strings | O(L + q) | AC | 0.140 s | 13904 KB |
| [1724_strings.rs](1724_strings.rs) | Rust 1.75 x64 | strings | O(L + q) | AC | 0.031 s | 3420 KB |
