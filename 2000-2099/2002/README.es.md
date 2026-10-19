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

Un mapa hash asocia cada nombre a su contraseña y un indicador de
conexión. Buscar sin insertar, elegir la primera condición aplicable,
añadir la respuesta y realizar solo el cambio permitido por una
operación exitosa.

Al entrar, comprobar existencia, contraseña y finalmente sesión activa.
Una contraseña errónea mantiene prioridad incluso si la cuenta ya está
conectada. Un registro duplicado no reemplaza contraseña ni reinicia
sesión. Salir solo apaga el indicador; una búsqueda fallida no crea
cuenta.

Por inducción, el registro vacío inicial es correcto. Si representa
exactamente las cuentas tras un prefijo, la siguiente búsqueda encuentra
el registro apropiado o su ausencia; las condiciones ordenadas dan la
respuesta requerida y la actualización permitida conserva la
representación. Así todos los resultados y estados posteriores son
correctos.

Con longitud `L≤30`, tiempo esperado `O(n L)` y memoria `O(n L)`
incluyendo entrada y respuestas. Una cota conservadora con colisiones es
`O(n² L)`, pequeña con 100 operaciones. Los cinco lenguajes mantienen la
misma prioridad.

No comprobar conexión antes de contraseña ni conectar automáticamente al
registrar. Los fallos no modifican cuentas. Comparar cadenas completas
con mayúsculas; comillas, barras inversas y nombres de comando son
caracteres ordinarios. Emitir solo el mensaje fijo, sin repetir nombre o
contraseña.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2002_implementation.cpp](2002_implementation.cpp) | G++ 13.2 x64 | implementation | O(n L) | AC | 0.015 s | 516 KB |
| [2002_implementation.go](2002_implementation.go) | Go 1.14 x64 | implementation | O(n L) | AC | 0.046 s | 1124 KB |
| [2002_implementation.java](2002_implementation.java) | Java 1.8 | implementation | O(n L) | AC | 0.109 s | 684 KB |
| [2002_implementation.py](2002_implementation.py) | Python 3.12 x64 | implementation | O(n L) | AC | 0.093 s | 576 KB |
| [2002_implementation.rs](2002_implementation.rs) | Rust 1.75 x64 | implementation | O(n L) | AC | 0.046 s | 460 KB |
