# 1945. Colorear familias multiplicativas con valoraciones

[Timus 1945](https://acm.timus.ru/problem.aspx?space=1&num=1945) · difficulty 3181 · number_theory

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados enteros positivos distintos y g salas, asignar cada valor a una.
a,b pueden ser hermanos si a=p·i y b=p·j para algún entero p>0 y
ordinales distintos 1≤i,j≤g. Deben ir separados para todo posible p,
aunque el padre u otros miembros no aparezcan. Hallar cualquier asignación.
Límites: 1 segundo, 64 MB.

## Entrada

n,g con 1≤n≤50000 y 2≤g≤5, seguidos de n enteros distintos a₁,…,a_n
en 1..10^9. Conservar su orden en la respuesta.

## Salida

Yes y n números enteros de sala en 1..g, o No si es imposible. Respetar
mayúsculas. Cualquier asignación válida sirve; la prueba siguiente muestra
que toda entrada válida es factible.

## Evaluación

Un comprobador revisa todos los pares de valores que podrían ser
hermanos para algún padre y acepta cualquier asignación válida. Por la
construcción de abajo, `No` nunca es correcto dentro de los límites.

## Ejemplos

```
5 2
1
2
3
4
6
```

```
Yes
1
2
1
1
2
```

## Solución

Sea v_p(a) el exponente del primo p. Tomar w₃=min(g−1,3) y definir
F(a)=v₂(a)+w₃·v₃(a)+4·v₅(a) módulo g. Asignar sala F(a)+1.
Obtener solo esos exponentes por división repetida; los factores restantes
no importan. Tabla completa de pequeños multiplicadores:

| g | w₃=min(g−1,3) | F(1),…,F(g) modulo g |
|---:|---:|---|
| 2 | 1 | 0, 1 |
| 3 | 2 | 0, 1, 2 |
| 4 | 3 | 0, 1, 3, 2 |
| 5 | 3 | 0, 1, 3, 2, 4 |

Fijar F(2)=1 fuerza F(4)=2. Para g=3 elegir F(3)=2; para g=4 o 5,
F(3)=3. Con g=5 el residuo restante lo ocupa F(5)=4. Para menores g
los multiplicadores no utilizados no imponen condiciones, así que el
coeficiente de v₅ queda igual. Cada fila contiene todos los residuos una vez.

Las valoraciones son aditivas: v_q(p·i)=v_q(p)+v_q(i). Luego
F(p·i)=F(p)+F(i) módulo g para cualquier padre. La traslación común
F(p) conserva residuos distintos. La familia posible completa p,2p,…,gp
usa g salas distintas; cualquier subconjunto presente también es válido.
Toda entrada válida tiene solución, por eso siempre se imprime Yes.
Solo se usa suma cíclica, incluso con g=4 compuesto; no se supone g primo.

Tiempo O(n log A), A=max a_i≤10^9: hasta 29 divisiones exitosas por valor
y tres pruebas fallidas. Color escalar con espacio auxiliar O(1).
Los programas completos usan como máximo O(n); C++ y Go procesan entrada
y etiquetas con búferes limitados. Acumulador≤4·29, bastan 32 bits con signo.

El cociente de hermanos puede no ser entero:4 y 6 comparten padre 2 para
g≥3. La pareja 3,4 puede compartir sala con g=3, pero no con g=4.
El padre no necesita estar en la cola. Usar w₃ dependiente de g, sumar uno
al residuo, preservar orden y capitalización Yes/No. La respuesta puede
diferir del ejemplo y seguir siendo válida.

## Notas por lenguaje

Solo aritmética entera, una sala por línea. Java y Rust construyen salida;
Python conserva entrada y resultados. Dividir por 2,3,5 basta; no se necesita
factorización hasta sqrt(A), coloreado general ni buscar un caso imposible.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1945_number_theory.cpp](1945_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log A) | AC | 0.031 s | 436 KB |
| [1945_number_theory.go](1945_number_theory.go) | Go 1.14 x64 | number_theory | O(n log A) | AC | 0.109 s | 2740 KB |
| [1945_number_theory.java](1945_number_theory.java) | Java 1.8 | number_theory | O(n log A) | AC | 0.125 s | 3760 KB |
| [1945_number_theory.py](1945_number_theory.py) | Python 3.12 x64 | number_theory | O(n log A) | AC | 0.187 s | 7052 KB |
| [1945_number_theory.rs](1945_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log A) | AC | 0.031 s | 2148 KB |
