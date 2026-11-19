# 1375. Inconformismo

[Timus 1375](https://acm.timus.ru/problem.aspx?space=1&num=1375) · dificultad 541 · number_theory

Problema original de Den Raskovalov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados un primo p ≤ 10⁶ y 0 ≤ k ≤ p − 1, hay que imprimir cualesquiera x
e y de 0 a p − 1 con x² + y² ≡ k (mod p), o `NO SOLUTION` si no los
hay.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k y p.

## Salida

x e y, o `NO SOLUTION`.

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. El comprobador exige dos tokens enteros no negativos x,y<p y verifica (x*x+y*y) mod p=k. Acepta cualquier pareja válida. La promesa de primo garantiza solución; rechaza NO SOLUTION.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 3
```

Salida:

```
0 2
```

## Solución

Para un primo impar p, los cuadrados toman (p + 1) / 2 valores
distintos módulo p, y lo mismo los valores k − x². Dos conjuntos de
(p + 1) / 2 valores entre p tienen que cortarse, así que algún x² y algún
y² suman k: siempre hay respuesta, y `NO SOLUTION` no aparece nunca.
Para p = 2 todo k es 0² + 0² o 1² + 0².

Para hallarla, se guarda una raíz de cada cuadrado: para y de 0 a p − 1
se anota y como raíz de y² mod p. Luego se prueba x = 0, 1, 2, … hasta
que k − x² mod p tenga raíz. Alrededor de la mitad de los valores son
cuadrados, así que esto acaba casi enseguida. `O(p)`.

Detalles a tener en cuenta:

- k = 0 tiene la respuesta 0 0 (prueba 07);
- k − x² debe tomarse módulo p como número no negativo;
- y² se acerca a 10¹², más de lo que cabe en 32 bits.

La respuesta se comprobó para todo k y todo primo menor que 300, y las
pruebas se juzgan con un verificador que acepta cualquier par.

## Soluciones optimizadas

`1375_math.py`. Sustituye tabla O(p) por aritmética modular escalar. Recorre x hasta r=(k-x*x) mod p cero o residuo cuadrático según Euler. Para p=2 emite(0,k); con primo impar usa raíz directa si p mod4=3 y Tonelli–Shanks en otro caso. La intersección de cuadrados garantiza éxito; buscar x y no residuo es finito, sin reintentos aleatorios. Peor tiempo O(p log p), sin prometer mejora asintótica sobre tabla; Tonelli–Shanks requiere como máximo O(log²p) multiplicaciones modulares. Espacio O(1) palabras modulares, p<=10^6. Accepted propio y primer puesto en ambas métricas prueban admisión. Conserva tabla didáctica; el algoritmo distinto se llama math.

Frente a `1375_number_theory.py`: tiempo 0.359 s → 0.078 s; memoria 23992 KB → 828 KB.

C++, Go y Rust sustituyen tabla O(p) por aritmética de campo con espacio constante. Para p=2 o k=0, (k,0). Si p≡1 mod4, buscar no residuo z con Euler, i=z^((p−1)/4) da i²=−1. Elegir t impar igual a k o k+p: a=(t+1)/2,b=(t−1)/2 dan a²−b²=t, respuesta (a mod p,ib mod p). Si p≡3 mod4, probar x=0…(p−1)/2 y y=r^((p+1)/4) para r=k−x², verificando el cuadrado. Si r es un residuo cuadrático distinto de cero, y²=r·r^((p−1)/2)=r por Euler. Para r=0 la raíz es cero. El recorrido cubre cada cuadrado una vez. El conjunto de cuadrados S y k−S tienen (p+1)/2 elementos, así que se intersecan y el recorrido encuentra un par. Productos64<10^12. T ensayos cuestan O(1+T log p), peor O(p log p), espacio O(1); no se promete mejor tiempo asintótico que la tabla. Memoria y envíos medidos deciden inclusión. Rust usa I/O C. Se conservan tablas sencillas; Conserva las tablas simples; Python tiene ahora una variante separada con raíz modular.

Conserva la tabla Java aceptada y todas las versiones didácticas. Python tiene ahora un algoritmo distinto de raíz modular, sin copiar bases idénticas. Los asteriscos siguen marcando objetivos de clasificación pendientes.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1375_math.py`: puesto de tiempo 1/16 y de memoria 1/16 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1375_number_theory.cpp](1375_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(p) | AC | 0.031 s | 3656 KB | 11285686 |
| [1375_number_theory.go](1375_number_theory.go) | Go 1.14 x64 | number_theory | O(p) | AC | 0.062 s | 9624 KB | 11285689 |
| [1375_number_theory.java](1375_number_theory.java) | Java 1.8 | number_theory | O(p) | AC | 0.156 s | 5172 KB | 11285695 |
| [1375_number_theory.py](1375_number_theory.py) \* | Python 3.12 x64 | number_theory | O(p) | AC | 0.359 s | 23992 KB | 11285693 |
| [1375_number_theory.rs](1375_number_theory.rs) | Rust 1.75 x64 | number_theory | O(p) | AC | 0.046 s | 7892 KB | 11285697 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1375_math.cpp](1375_math.cpp) | G++ 13.2 x64 | math | O(1 + T log p) | AC | 0.015 s | 108 KB | 11315721 |
| [1375_math.go](1375_math.go) \* | Go 1.14 x64 | math | O(1 + T log p) | AC | 0.031 s | 916 KB | 11315726 |
| [1375_math.rs](1375_math.rs) \* | Rust 1.75 x64 | math | O(1 + T log p) | AC | 0.046 s | 64 KB | 11315729 |
| [1375_math.py](1375_math.py) | Python 3.12 x64 | math | O(p log p) worst; O(1) auxiliary words | AC | 0.078 s | 828 KB | 11325462 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
