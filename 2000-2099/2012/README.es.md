# 2012. Doce Tareas Antes del Límite

[Timus 2012](https://acm.timus.ru/problem.aspx?space=1&num=2012) · dificultad 17 · math

Problema original de Alexander Ipatov, preparado por Olga Soboleva, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una sesión de cinco horas contiene doce tareas. Durante la primera hora
se terminan exactamente `f`. Aunque se acaben antes, la tarea siguiente
comienza solo al terminar esa hora completa. Cada tarea restante ocupa
exactamente 45 minutos y se trabaja en secuencia. Decide si todas
terminan dentro de la sesión.

## Entrada

Un entero `f`, `1 ≤ f ≤ 11`. Tiempo límite 1 segundo, memoria 64 MB.

## Salida

Escribe `YES` en mayúsculas si el plan termina a tiempo, o `NO` en caso
contrario. La respuesta única se compara por tokens.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
7
```

```
YES
```

```
5
```

```
NO
```

Con `f=7` quedan cinco tareas y se necesitan `60+5·45=285` minutos, como
máximo 300. Con `f=5` quedan siete y el tiempo es `60+7·45=375`, que
supera el límite.

## Solución

Convierte las duraciones a minutos. La primera fase ocupa 60 y quedan
`12−f` tareas. El tiempo de finalización es `T=60+45·(12−f)`. Devuelve
`YES` exactamente cuando `T≤300`.

La condición es necesaria y suficiente. La primera hora fija y las
tareas restantes consecutivas necesitan exactamente ese tiempo; si
supera el límite es imposible terminar. Si no supera 300, empezar el
resto inmediatamente después del minuto 60 permite acabar a tiempo. Los
minutos libres dentro de la primera hora no adelantan el inicio de la
segunda fase.

Equivalentemente, después de la primera hora quedan 240 minutos. Solo
caben `floor(240/45)=5` tareas adicionales, por lo que `12−f≤5`, es
decir, `f≥7`. Los programas mantienen la expresión temporal con
constantes con nombre, evitando un umbral sin explicar. Terminar justo
en el límite también es válido.

Tiempo `O(1)` y espacio adicional `O(1)`. El mayor tiempo posible es
`60+11·45=555`, por lo que bastan enteros ordinarios con signo. No hacen
falta coma flotante ni redondeos.

## Notas por lenguaje

Reserva la primera hora completa, cuenta las tareas que faltan y mantén
las mismas unidades. La salida es `YES`/`NO` en mayúsculas. El Scanner
de Java 8 basta para un entero; los otros lenguajes usan sus lectores
habituales. CPython sirve para este cálculo de tamaño constante. Los
cinco programas usan la misma desigualdad entera exacta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2012_math.cpp](2012_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 380 KB |
| [2012_math.go](2012_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1080 KB |
| [2012_math.java](2012_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1564 KB |
| [2012_math.py](2012_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 348 KB |
| [2012_math.rs](2012_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 236 KB |
