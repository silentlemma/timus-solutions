# 1965. Dos subsecuencias monótonas

[Timus 1965](https://acm.timus.ru/problem.aspx?space=1&num=1965) · difficulty 1005 · dp

Original problem from Open Ural FU Personal Contest 2013 | by Sergey Pupyrev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dividir una permutación de 1,…,n en dos subsecuencias no vacías y
estrictamente monótonas. Cada grupo elige independientemente crecer o
decrecer; pueden tener la misma dirección. Conservar el orden relativo
de entrada y usar cada valor una vez. Imprimir cualquier partición válida
o indicar imposibilidad. Límites: 1 segundo, 64 MB.

## Entrada

n, con 3≤n≤100 000, seguido por n enteros distintos entre 1 y n.

## Salida

Si hay solución, primera línea con dos tamaños entre 1 y n−1; segunda y
tercera con los valores de cada grupo en orden de entrada. Cualquier
respuesta válida sirve. Si no existe, imprimir `Fail`. Un grupo de un
elemento es monótono en cualquier dirección.

## Evaluación

Un comprobador verifica que los dos grupos no están vacíos, cubren cada
valor una vez, conservan el orden de entrada y son estrictamente
monótonos; se acepta cualquier división válida. `Fail` debe coincidir
con la respuesta guardada.

## Ejemplos

```
8
8 7 1 6 4 3 5 2
```

```
3 5
1 4 5
8 7 6 3 2
```

```
6
3 5 1 2 6 4
```

```
3 3
3 5 6
1 2 4
```

```
6
3 5 2 1 6 4
```

```
Fail
```

## Solución

En el primer ejemplo 1,4,5 crece y 8,7,6,3,2 decrece; conservan el orden
y cubren todos los valores. El segundo permite dos grupos crecientes:
3,5,6 y 1,2,4. En el tercero fallan las cuatro parejas de direcciones.

Probar (+,+), (−,−), (+,−), (−,+). Para una pareja fija, procesar de
izquierda a derecha. El último valor procesado v pertenece a un grupo,
el dueño actual, cuyo último valor ya es v. Solo hacen falta el dueño
y el último valor del otro grupo.

Para cada dueño conservar el mejor último valor del otro grupo: menor
si ese grupo crece y mayor si decrece. Un último valor mejor permite
todas las continuaciones de uno peor. Como el del dueño es idéntico,
el estado peor nunca es necesario. Guardar también el dueño predecesor.

Al llegar x hay dos transiciones. Añadirlo al mismo dueño si sigue a v
en su dirección, conservando el otro último valor. O añadirlo al otro
grupo si sigue a su último valor almacenado: cambia el dueño y el nuevo
último del otro grupo pasa a ser v. Para cada dueño nuevo conservar solo
el valor dominante. Si ambos son inalcanzables, la pareja es imposible.

El primer valor puede pertenecer a cualquiera. El grupo creciente vacío
tiene centinela 0 y el decreciente n+1; cualquier valor de entrada puede
seguirlos. Al terminar elegir un estado alcanzable y retroceder por los
dueños predecesores para recuperar los grupos en orden de entrada.

Si un grupo queda vacío, toda la permutación es monótona en el otro.
Mover su último elemento al grupo vacío: quedan n−1≥2 elementos en el
original y el singleton sirve en cualquier dirección. Por ello permitir
grupos vacíos durante la programación dinámica no invalida la dominancia
y aún produce una partición final no vacía.

Por inducción, los estados conservan todas las continuaciones para la
pareja fija: las transiciones contemplan ambos dueños del nuevo elemento
y la dominancia solo descarta colas más débiles. Si fallan las cuatro
parejas, no existe ninguna partición.

Tiempo `O(n)` y espacio `O(n)`: cuatro parejas, dos estados por posición
y un número constante de transiciones. Dos arreglos de bytes guardan
predecesores por intento; entrada y grupos también ocupan espacio lineal.

Ambos grupos pueden ir en la misma dirección. Una única asignación voraz
pierde posibilidades; conservar ambos dueños. La dirección del otro grupo
determina la dominancia. Guardar el predecesor de la transición elegida.
Imprimir valores, no índices, manteniendo el orden, y reparar grupos vacíos
solo tras reconstruir. No comparar una partición token a token con el ejemplo.

## Notas por lenguaje

Python 3.12 usa None para inalcanzable y bytearray para predecesores.
C++/Go/Java/Rust usan −1 para colas inalcanzables, pues los valores y
centinelas vacíos son no negativos. C++ y Go usan arreglos de bytes,
Java byte[][] y Rust Vec<u8>. Java emplea entrada entera almacenada en
búfer y StringBuilder. Rust usa usize para índices e i32 para colas
con signo. No se usa recursión.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1965_dp.cpp](1965_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.031 s | 1880 KB |
| [1965_dp.go](1965_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.109 s | 8772 KB |
| [1965_dp.java](1965_dp.java) | Java 1.8 | dp | O(n) | AC | 0.140 s | 6604 KB |
| [1965_dp.py](1965_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.265 s | 11748 KB |
| [1965_dp.rs](1965_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.031 s | 3516 KB |
