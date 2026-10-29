# 2002. Test Task

[Timus 2002](https://acm.timus.ru/problem.aspx?space=1&num=2002) · dificultad 72 · implementation

Problema original de Kirill Borozdin, del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Simular un registro inicialmente vacío con registro de nombre y
contraseña, entrada con contraseña y salida por nombre. Cada petición
emite una respuesta fija siguiendo exactamente la prioridad de errores.
Una cuenta nueva empieza desconectada y las operaciones fallidas no
cambian contraseñas ni sesiones.

## Entrada

`1≤n≤100` solicitudes `register name password`, `login name password` o
`logout name`. Nombres y contraseñas no vacíos, de hasta 30 caracteres
ASCII 33–126, sensibles a mayúsculas. No contienen espacios, pero sí
pueden incluir puntuación o palabras de comando. Tiempo 0,5 segundos;
memoria 64 MB.

## Salida

Una línea por petición, conservando exactamente inglés, dos puntos,
espacios y puntuación. Para cada comando, revisar las filas de arriba
abajo.

| Condición | Respuesta | Cambio |
| --- | --- | --- |
| register: nombre existente | `fail: user already exists` | ninguno |
| register: otro caso | `success: new user added` | guardar contraseña, desconectado |
| login: nombre ausente | `fail: no such user` | ninguno |
| login: contraseña errónea | `fail: incorrect password` | ninguno |
| login: ya conectado | `fail: already logged in` | ninguno |
| login: otro caso | `success: user logged in` | conectado |
| logout: nombre ausente | `fail: no such user` | ninguno |
| logout: ya desconectado | `fail: already logged out` | ninguno |
| logout: otro caso | `success: user logged out` | desconectado |

## Evaluación

El repositorio compara la salida carácter a carácter tras eliminar todos
los caracteres en blanco al final de la salida completa. Se ignoran los
espacios y las líneas vacías finales; los demás blancos deben coincidir.

## Ejemplos

```
6
register vasya 12345
login vasya 1234
login vasya 12345
login anakin C-3PO
logout vasya
logout vasya
```

```
success: new user added
fail: incorrect password
success: user logged in
fail: no such user
success: user logged out
fail: already logged out
```

Registrar guarda `12345` y deja la cuenta desconectada. La contraseña
errónea no cambia nada; la correcta permite entrar. Un nombre
desconocido falla, la primera salida funciona y la siguiente informa que
ya se salió.

## Solución

Se guarda una tabla hash del nombre a su contraseña y una marca de
conectado. Para cada petición se busca el nombre y se comprueban las
condiciones de la tabla de arriba abajo; la primera que se cumple da la
respuesta y el único cambio. `O(n·L)` para nombres de longitud L ≤ 30.

Detalles a tener en cuenta:

- al entrar, una contraseña incorrecta se informa antes que «ya
  conectado»;
- el registro no conecta al usuario;
- las peticiones fallidas no cambian nada, y una búsqueda nunca crea una
  cuenta;
- nombres y contraseñas se comparan exactamente, con mayúsculas y
  minúsculas.

## Soluciones optimizadas

La solución optimizada en C++ lee las palabras con `scanf` en búferes de
31 bytes en lugar de `iostream` y responde a cada petición en el acto,
en lugar de guardar antes todas las peticiones y respuestas: 212 KB en
lugar de 516 KB, con el mismo tiempo.

La solución optimizada en Go analiza las peticiones a mano desde un
lector con búfer de 1 KB en lugar de `fmt.Fscan` y responde cada una
enseguida con un escritor con búfer, sin lista de órdenes: 0.015 s en
lugar de 0.046 s y 936 KB en lugar de 1124 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2002_implementation.cpp](2002_implementation.cpp) | G++ 13.2 x64 | implementation | O(n L) | AC | 0.015 s | 516 KB | 11292443 |
| [2002_implementation.go](2002_implementation.go) | Go 1.14 x64 | implementation | O(n L) | AC | 0.046 s | 1124 KB | 11292444 |
| [2002_implementation.java](2002_implementation.java) | Java 1.8 | implementation | O(n L) | AC | 0.140 s | 664 KB | 11303527 |
| [2002_implementation.py](2002_implementation.py) | Python 3.12 x64 | implementation | O(n L) | AC | 0.093 s | 576 KB | 11292445 |
| [2002_implementation.rs](2002_implementation.rs) | Rust 1.75 x64 | implementation | O(n L) | AC | 0.046 s | 460 KB | 11292448 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2002_implementation_optimized.cpp](2002_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n L) | AC | 0.015 s | 212 KB | 11303656 |
| [2002_implementation_optimized.go](2002_implementation_optimized.go) | Go 1.14 x64 | implementation | O(n L) | AC | 0.015 s | 936 KB | 11303790 |
