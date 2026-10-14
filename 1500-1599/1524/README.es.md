# 1524. Hombres de negro

[Timus 1524](https://acm.timus.ru/problem.aspx?space=1&num=1524) · dificultad 9705 · simulation

Problema original de Dmitry Gozman, del concurso n.º 1 de Dmitry Gozman en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que simular una agencia de como mucho 26 agentes, cada uno con una
letra en clave y cinco rasgos entre 0 y 1: precisión, velocidad al
andar, inteligencia, experiencia y habilidad al volante. La agencia
tiene también coches (cada uno de un tipo con una habilidad mínima para
conducirlo y una distancia que puede recorrer antes de romperse) y una
lista de clases de monstruos. Los eventos llegan en orden de tiempo:
entra un agente nuevo (que toma la letra libre más cercana a la inicial
de su nombre, la menor en caso de empate), se compra un coche o llega
una misión: una entrega, matar a un monstruo, una investigación o unas
negociaciones a cierta distancia de la oficina.

Una misión la hace un agente o una pareja, a pie o en un coche, ida y
vuelta. Una pareja anda a la velocidad del más lento y conduce con la
mejor habilidad; su precisión es la media y su experiencia e
inteligencia se combinan como 1 − (1 − a)(1 − b). Matar lleva evasión /
precisión, investigar tiempo mínimo / inteligencia, negociar tiempo
mínimo / experiencia, y cada clase exige mínimos en los rasgos. Cada
tramo de tiempo se redondea al minuto por separado. Un coche que agota
su distancia se rompe y el resto del camino se hace a pie. Una misión
empieza en cuanto alguien puede hacerla, las recibidas antes primero;
gana el equipo más rápido, un agente solo antes que una pareja, luego
las letras menores; se toma un coche solo si es estrictamente más
rápido, y luego el de menor id. Tras una misión los rasgos de cada agente
crecen según las fórmulas dadas, y un agente cuya experiencia llega al
nivel de retiro se va.

Hay que imprimir con su hora cada coche comprado, coche roto, monstruo
muerto, misión acabada, agente cansado, agente nuevo y misión empezada,
en ese orden dentro de un minuto y lexicográficamente por mensaje dentro
de cada tipo.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

Los agentes, tipos de coche, coches y clases de monstruos, luego la
distancia máxima a pie, la evasión máxima, la experiencia máxima por
monstruo y la experiencia de retiro, y después hasta 2000 eventos.

## Salida

Líneas `dddd:hh:mm    mensaje`, como se describe arriba.

## Ejemplos

### Ejemplo

Entrada:

```
1
James 0.8 0.7 0.75 0.5 0.85 J

1
0.4 100 mibLexus

2
mibLexus 0 pq123bu
mibLexus 12 ab891ah

1
0.2 0.3 18 100 cockroach

200 20 200 0.95

4
10 newagent Klint 0.9 0.8 0.5 0.7 0.86
20 quest run 48
30 newcar mibLexus 47 aa890bu
43 quest kill 100 cockroach
```

Salida:

```
0000:00:10    New agent Klint got a letter K.
0000:00:20    Agent J started quest 1 using car pq123bu.
0000:00:30    MIB bought a car of class mibLexus.
0000:00:43    Agent K started quest 2 using car ab891ah.
0000:02:12    Agent J finished quest 1.
0000:02:25    Car ab891ah was broken.
0000:03:00    Agent K killed monster cockroach.
0000:05:05    Agent K finished quest 2.
```

## Solución

Una simulación por eventos. Cuando una misión empieza, todo su curso ya
se conoce: los momentos en que el coche se rompe, el monstruo muere y la
misión termina, contados desde el inicio. Esos momentos van a una cola
de prioridad ordenada por tiempo y luego por tipo (rotura, muerte,
final), que es también el orden de los mensajes dentro de un minuto.

En cada momento se procesan los eventos vencidos de la cola, después se
aplica el evento externo y luego se prueban las misiones en espera en
orden de llegada, una y otra vez mientras alguna pueda empezar. Para una misión
se prueba cada agente libre y cada pareja de agentes libres sin coche y
con cada coche libre; con coche hay cinco casos: se rompe a la ida, al
llegar, a la vuelta, justo al regresar o no se rompe. Los mensajes de un
minuto se ordenan por tipo y texto antes de imprimirlos.

Detalles a tener en cuenta:

- cada tramo se redondea por separado: conducir y andar tras una avería
  son dos redondeos, con `floor(t + 0.5 + 10⁻⁹)` para que el 0,5 no se
  pierda por la representación binaria;
- los requisitos se comparan con ≥ y sin tolerancia (prueba 05);
- un coche que solo iguala a ir andando no se toma; entre coches
  permitidos e igual de rápidos gana el de menor id (empates entre coches:
  prueba 06);
- una pareja solo es mejor si es estrictamente más rápida que cualquier
  agente solo libre que cumpla los requisitos;
- un coche se rompe justo cuando agota su distancia, también al llegar
  o al regresar (prueba 04);
- un agente cansado libera su letra en el acto (prueba 07);
- una misión posterior puede empezar mientras una anterior aún espera a
  alguien capaz de hacerla (prueba 03).

La salida se comparó con una implementación aceptada independiente en
las pruebas de aquí y en 100 agencias aleatorias.

## Notas por lenguaje

- Python se ejecuta con PyPy: la prueba más grande de aquí tarda unos
  10 s con CPython y 1,7 s con PyPy. Además, entre los coches que no se
  romperán en el viaje solo prueba el primero por id que pueda conducir,
  porque todos tardan lo mismo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1524_simulation.cpp](1524_simulation.cpp) | G++ 13.2 x64 | simulation | O(N²) | AC | 0.093 s | 696 KB |
| [1524_simulation.go](1524_simulation.go) | Go 1.14 x64 | simulation | O(N²) | AC | 0.093 s | 7912 KB |
| [1524_simulation.java](1524_simulation.java) | Java 1.8 | simulation | O(N²) | AC | 0.296 s | 8992 KB |
| [1524_simulation.py](1524_simulation.py) | PyPy 3.10 x64 | simulation | O(N²) | AC | 2.593 s | 17972 KB |
| [1524_simulation.rs](1524_simulation.rs) | Rust 1.75 x64 | simulation | O(N²) | AC | 0.093 s | 1576 KB |
