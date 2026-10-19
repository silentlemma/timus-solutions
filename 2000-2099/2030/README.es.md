# 2030. Difundir valores a vecinos de un árbol

[Timus 2030](https://acm.timus.ru/problem.aspx?space=1&num=2030) · dificultad 517 · dfs

Problema original de Nikita Sivukhin, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol no dirigido y conexo tiene `n` vértices numerados de 1 a `n`.
El vértice `v` empieza con un entero `a[v]`. Procesa las peticiones en
orden:

- `1 v`: toma el valor actual de `v` y suma esa instantánea a cada vecino.
  El valor de `v` permanece igual.
- `2 v`: muestra el valor actual de `v` módulo `P = 1000000007`.

Los vecinos reciben incrementos, sin reemplazar sus valores. Una
difusión usa el valor anterior a esa petición; las siguientes incluyen
todos los incrementos anteriores. Límites: `1 ≤ n,m ≤ 100000`, `0 ≤ a[v]
≤ 1000000000`, 2 segundos, 64 MB.

## Entrada

Primero `n`, seguido de una línea con los `n` valores iniciales. Las siguientes
`n-1` líneas contienen extremos `x y`, con `1 ≤ x,y ≤ n`, `x ≠ y`; se garantiza
conexión. Después aparecen `m` y `m` parejas `t v`, con `t` igual a 1 o 2,
`1 ≤ v ≤ n`.

## Salida

Para cada petición de tipo 2 imprime un residuo de `[0,P-1]` en una línea.
Si no hay consultas, no imprimas nada. Una difusión en un único vértice aislado
no cambia su valor.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
4
1 1 1 1
1 2
1 3
2 4
9
2 1
2 2
2 3
2 4
1 1
2 1
2 2
2 3
2 4
```

```
1
1
1
1
1
2
2
1
```

```
2
1 1
1 2
14
2 2
2 1
1 1
2 2
1 2
2 1
1 1
2 2
1 2
2 1
1 1
2 2
1 2
2 1
```

```
1
1
2
3
5
8
13
21
```

## Solución

Enraíza el árbol en el vértice 1 con un recorrido iterativo. Cada vecino es el
único padre, si existe, o un hijo. Divide una difusión en un incremento directo
al padre y un incremento diferido compartido por todos los hijos.

Guarda `direct[v]`, inicialmente `a[v]`, y `broadcast[v]`, inicialmente cero.
El segundo suma todas las instantáneas difundidas por `v`; el primero contiene
el valor inicial y los incrementos difundidos por sus hijos. El invariante es
`value(v) = direct[v] + broadcast[parent[v]] (mod P)` para un vértice no raíz;
la raíz tiene solamente `direct[root]`.

Primero calcula `delta = value(v)` en ambas peticiones. Una consulta lo
imprime. Una difusión suma `delta` a `broadcast[v]` y, si hay padre, a
`direct[parent[v]]`. Reduce todas las sumas módulo `P`. Las peticiones
nunca recorren los vecinos.

### Corrección

Al inicio no hay difusiones y el invariante da los valores iniciales.
Supón que se cumple antes de una difusión. Cada hijo de `v` lee
`broadcast[v]`; aumentar ese campo compartido añade exactamente `delta`
a todos los hijos. El padre recibe la misma cantidad en su propio
`direct`. La fuente lee su `direct` y el `broadcast` de su padre, campos
que no cambian, por lo que su valor sigue igual. Los demás vértices no
leen ningún campo modificado y tampoco cambian. Se realiza exactamente
la operación pedida y el invariante se conserva. Las consultas solo leen
el invariante; por inducción todas las respuestas son correctas. Reducir
durante el proceso es válido porque solo se hacen sumas enteras.

En el primer ejemplo las cuatro consultas iniciales dan unos. Difundir
desde el vértice 1 cambia solo los vértices 2 y 3 a dos; 1 y 4 siguen en
uno. En el segundo, difusiones alternas sobre una única arista generan
los valores consultados `1,1,2,3,5,8,13,21`.

El recorrido cuesta `O(n)` y cada petición `O(1)`: tiempo total
`O(n+m)`. El árbol, los padres y los valores usan `O(n)` de espacio de
trabajo. Python almacena hasta `O(m)` cadenas de salida y Rust también
conserva la entrada, por lo que el total con búferes es `O(n+m)`. C++,
Go y Java procesan las peticiones y la salida como flujos.

Trampas:

- La fuente no recibe su propio incremento: no hay bucles.
- Captura el valor actual antes de modificar campos.
- Usa la suma difundida por el padre, no el valor actual del padre.
- Trata la raíz aparte para evitar una contribución ficticia de sí misma.
- Usa recorrido iterativo ante una cadena de 100000 vértices.
- Sin consultas no se debe imprimir un cero extra.

## Notas por lenguaje

Normaliza después de cada suma: dos residuos suman como máximo `2000000012`,
seguro incluso en los arreglos `int` de Java. C++, Go y Rust usan campos más
anchos. Basta una resta condicional. Java usa arreglos primitivos de adyacencia
y análisis por bytes. Python lee por líneas y libera la adyacencia temporal
después de construir padres iterativamente. No se necesita recursión, umbral
de grado ni estructura logarítmica.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2030_dfs.cpp](2030_dfs.cpp) | G++ 13.2 x64 | dfs | O(n+m) | AC | 0.109 s | 9368 KB |
| [2030_dfs.go](2030_dfs.go) | Go 1.14 x64 | dfs | O(n+m) | AC | 0.062 s | 14016 KB |
| [2030_dfs.java](2030_dfs.java) | Java 1.8 | dfs | O(n+m) | AC | 0.156 s | 8516 KB |
| [2030_dfs.py](2030_dfs.py) | Python 3.12 x64 | dfs | O(n+m) | AC | 0.546 s | 26824 KB |
| [2030_dfs.rs](2030_dfs.rs) | Rust 1.75 x64 | dfs | O(n+m) | AC | 0.062 s | 18652 KB |
