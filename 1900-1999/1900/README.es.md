# 1900. Elección de tramos ferroviarios

[Timus 1900](https://acm.timus.ru/problem.aspx?space=1&num=1900) · difficulty 527 · dp

Problema original de Alex Samsonov, preparado por Alexander Fetisov, del Campeonato de los Urales 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las estaciones 1,…,n forman una línea. El peso w(i,j) cuenta los pasajeros
que viajan de i a j, con i < j. Elige exactamente k tramos distintos entre
estaciones consecutivas. Cuenta una sola vez a cada pasajero cuyo viaje
cruce algún tramo elegido. Maximiza el total y construye una selección.
Los límites son 1 segundo y 64 MB.

## Entrada

Primero n y k, con 2 ≤ n ≤ 500 y 1 ≤ k < n. Para cada i = 1,…,n−1,
la siguiente línea contiene w(i,i+1),…,w(i,n), entre 0 y 100 cada uno.

## Salida

Imprime el total máximo y luego k índices de tramos en orden creciente.
El tramo i une i con i+1. Se acepta cualquier selección óptima.

## Evaluación

Se verifican cantidad, rango y orden estricto de los índices, se recalcula
la cobertura y se compara con el óptimo. Los índices pueden diferir de
los de la respuesta guardada.

## Ejemplos

```
4 1
5 0 6
5 3
5
```

```
14
3
```

## Solución

Al cortar la secuencia por los tramos elegidos quedan g = k+1 grupos
contiguos no vacíos. Un pasajero queda sin cubrir exactamente cuando sus
dos extremos están en el mismo grupo. Minimizamos ese peso interno.

C(l,r) suma w(i,j) para l ≤ i < j ≤ r. Se obtiene en `O(n²)`, recorriendo
l en orden descendente: C(l,r)=C(l+1,r)+Σ(j=l+1…r) w(l,j).
La última suma se mantiene al aumentar r.

D(t,r) es el mínimo peso sin cubrir al dividir las primeras r estaciones
en t grupos. D(1,r)=C(1,r), y D(t,r)=min[D(t−1,p)+C(p+1,r)] para
t−1 ≤ p < r. Guarda el p elegido. Basta calcular t ≤ r ≤ n−g+t,
reservando una estación para cada grupo restante.

Los pesos no negativos dan, para a ≤ b ≤ c ≤ d, la desigualdad de Monge:
C(a,c)+C(b,d) ≤ C(a,d)+C(b,c). La diferencia entre ambos lados suma
w(i,j) con a ≤ i < b y c < j ≤ d. Añadir D(t−1,p) a cada fila de
candidatos conserva la desigualdad. Por ello, el óptimo más a la izquierda
no decrece cuando crece r: se pueden eliminar cruces usando la desigualdad,
y elegir el primero resuelve los empates.

Calcula cada capa mediante divide y vencerás. Evalúa el extremo central
con los cortes permitidos. Restringe la mitad izquierda a cortes no mayores
que su óptimo y la derecha a cortes no menores. Conserva el primer corte
en caso de empate. Cada capa cuesta `O(n log n)`. Desde (g,n), sigue los
padres hacia atrás: los cortes son los tramos buscados. Resta el mínimo
peso sin cubrir de C(1,n).

Cada selección corresponde a una partición y viceversa. La recurrencia
considera el último grupo y obtiene el mínimo; la optimización monótona
mantiene un candidato óptimo. Por tanto, la selección reconstruida es óptima.

Tiempo `O(n² + kn log n)`, espacio `O(n² + kn)`=`O(n²)`, pues k < n.
El total no supera 12,475,000; bastan enteros con signo de 32 bits y se
usa 10⁹ como infinito. En el ejemplo, el tramo 3 cubre 6+3+5=14 pasajeros.

Trampas:

- contar una sola vez un viaje que cruza varios tramos elegidos;
- mantener cada grupo no vacío;
- k tramos elegidos producen k+1 grupos.

## Notas por lenguaje

Las cinco versiones usan la misma recurrencia y el primer óptimo en los
empates. Python guarda costes y padres en arreglos compactos; Java usa
entrada con búfer. La profundidad recursiva es `O(log n)`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1900_dp.cpp](1900_dp.cpp) | G++ 13.2 x64 | dp | O(n² + kn log n) | AC | 0.031 s | 3188 KB |
| [1900_dp.go](1900_dp.go) | Go 1.14 x64 | dp | O(n² + kn log n) | AC | 0.046 s | 10088 KB |
| [1900_dp.java](1900_dp.java) | Java 1.8 | dp | O(n² + kn log n) | AC | 0.125 s | 6548 KB |
| [1900_dp.py](1900_dp.py) | Python 3.12 x64 | dp | O(n² + kn log n) | AC | 0.250 s | 10272 KB |
| [1900_dp.rs](1900_dp.rs) | Rust 1.75 x64 | dp | O(n² + kn log n) | AC | 0.031 s | 4996 KB |
