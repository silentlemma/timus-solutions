# 1972. Camino máximo sin repeticiones entre dos conjuntos

[Timus 1972](https://acm.timus.ru/problem.aspx?space=1&num=1972) · difficulty 3339 · constructive

Problema original de Idea by Alexander Ipatov, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una configuración es un subconjunto de n opciones independientes. Partir
de un conjunto dado y terminar en otro, cambiando exactamente una opción
por paso, sin repetir configuraciones. Maximizar cuántas se visitan,
incluidos ambos extremos, e imprimir el recorrido. Los extremos difieren
y existe solución. Límites: 1 segundo, 64 MB.

## Entrada

n, 1≤n≤16. Las dos líneas siguientes describen los extremos: k seguido
de los k índices activados, con 0≤k≤n y 1≤a₁<…<aₖ≤n.

## Salida

La cantidad máxima m, seguida de m configuraciones en orden de visita,
con cantidad e índices crecientes. Primera y última coinciden con la
entrada. Se acepta cualquier secuencia óptima.

## Evaluación

Un comprobador verifica que cada paso cambia exactamente una opción, que
ninguna configuración se repite y que el camino tiene la mayor longitud
posible: 2ⁿ si los extremos tienen distinta paridad y 2ⁿ − 1 si no. Se
acepta cualquier camino así.

## Ejemplos

```
2
0
2 1 2
```

```
3
0
1 2
2 1 2
```

## Solución

Representar conjuntos con máscaras de n bits. Las configuraciones forman
un hipercubo, con una arista por bit cambiado. Colorear por paridad del
número de bits activos: cada arista cambia color, con 2ⁿ⁻¹ vértices por
clase. Un camino entre colores opuestos usa como máximo 2ⁿ vértices;
entre iguales, 2ⁿ−1. Construimos ambos límites.

### Dividir en dos cubos menores

Mantener extremos a,b y una máscara de dimensiones libres; las demás
coordenadas están fijas. Con una dimensión, devolver ambos extremos si
difieren, o solo uno si son iguales. La igualdad solo se necesita en una
hoja recursiva.

En otro caso elegir una dimensión diferente d entre a,b. Al quitarla
quedan las mitades que contienen a y b. Elegir otra dimensión libre e,
poner u=a XOR 2ᵉ, v=u XOR 2ᵈ, y concatenar los caminos a→u en la primera
mitad y v→b en la segunda. La unión u→v cambia exactamente d.

Excepción necesaria: si v=b y quedan al menos tres dimensiones, cambiar e.
La igualdad significa que los extremos originales solo diferían en d y e;
cualquier otra dimensión restante produce v≠b. Con dos dimensiones se
permite igualdad: la segunda mitad aporta únicamente su extremo final.

### Corrección y optimalidad

a y u tienen paridades opuestas. Por inducción su camino visita los
2ⁿ⁻¹ vértices de la primera mitad. Tras cambiar d otra vez, v comparte
paridad con a. Si a,b eran opuestos, también v,b: se visita toda la
segunda mitad y se obtienen 2ⁿ vértices.

Si a,b eran iguales en paridad, también v,b. La excepción conserva
extremos distintos cuando esa mitad tiene dimensión al menos dos;
la inducción da 2ⁿ⁻¹−1 vértices allí. Para un padre de dimensión dos,
la hoja unidimensional con extremos iguales da uno, la misma fórmula.
Total: 2ⁿ−1. Las mitades son disjuntas y no hay repeticiones. Solo se
alteran coordenadas libres, se conservan los extremos y se termina.
Así se alcanzan las dos cotas superiores.

Construir las máscaras cuesta `O(2^n)` en tiempo y espacio; profundidad
`O(n)`. Formatear índices cuesta `O(n·2^n)`. Con texto almacenado en
búfer el espacio puede ser `O(n·2^n)`; el camino numérico sigue siendo `O(2^n)`.

En el ejemplo, vacío y {1,2} tienen paridad par. No pueden visitarse las
cuatro configuraciones, pero sí vacío → {2} → {1,2}. Se cambia primero
la opción 2 y luego la 1: longitud tres, que alcanza la cota.

Contar configuraciones, no transiciones. Con paridad igual se necesita
2ⁿ−1, no el camino mínimo. Evitar v=b en una mitad de dimensión al menos
dos: devolver un vértice perdería muchos. La hoja unidimensional igual
sí es intencional. Quitar el bit separador en ambas máscaras recursivas.
Imprimir índices crecientes y generar respuestas grandes, aunque la
entrada sea diminuta, en vez de almacenarlas como archivos estáticos.

## Notas por lenguaje

Las cinco versiones extraen el bit activo menor. Rust usa negación
envolvente para máscaras sin signo; C++ usa valores sin signo, Go y Java
enteros no negativos, Python enteros arbitrarios. Java preasigna el
arreglo de recorrido. La profundidad máxima 16 no requiere ajustes de recursión.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1972_constructive.cpp](1972_constructive.cpp) | G++ 13.2 x64 | constructive | O(n*2^n) | AC | 0.078 s | 684 KB |
| [1972_constructive.go](1972_constructive.go) | Go 1.14 x64 | constructive | O(n*2^n) | AC | 0.125 s | 5908 KB |
| [1972_constructive.java](1972_constructive.java) | Java 1.8 | constructive | O(n*2^n) | AC | 0.187 s | 11420 KB |
| [1972_constructive.py](1972_constructive.py) | Python 3.12 x64 | constructive | O(n*2^n) | AC | 0.328 s | 10276 KB |
| [1972_constructive.rs](1972_constructive.rs) | Rust 1.75 x64 | constructive | O(n*2^n) | AC | 0.062 s | 3456 KB |
