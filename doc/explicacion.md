# Explicacion de nuestro programa

## El Metodo `BaseAgent.Update`

El comportamiento del agente sigue estas pasos en orden:

1. Actualiza el `MappedGrid` modelo con la informacion nueva en `perception`.
2. Si lo ve, atira al jugador, centro comando, una bala o el otro agente y devuelve el movimiento eligido.
3. Si no, adquire el mejor movimiento desde los datos del `MappedGrid` con uso del algoritmo floodfill.
4. Si esta atrapado y quiere mover en el mismo direccion que antes, elige un movimiento aleatorio en su panico.
5. Si no, devuelve el movimiento adquirido por floodfill.

## Dibujos de maqina de estados

### Final

![maqina de estados final](/doc/dibujofinal.jpg)

### Preliminar

![maqina de estados preliminar](/doc/dibujo_preliminar.jpg)

## Guardado en el objeto `BaseAgent`

Guardamos lo sigiente para empezar en el metodo `BaseAgent.__init__`:

- `self.mapped_grid` que sea una instancia de un objeto `MappedGrid`. Se explica mas en el siguiente seccion.
- `self.old_movement` que sea nuestro movimiento de la ejecución anterior de `Update`.
- `self.old_position` que sea nuestro posicion de la ejecución anterior de `Update`.

## `MappedGrid` - La Actualizacion

El `MappedGrid` es una clase que guarda los partes de la mapa descubrida, debido a la lista `perception`. Este informacion nos ayuda a decidir cual direcion nos acerca mejor al centro de comandos.

Para empezar, asumimos que la mapa entera esta vacio, sin ladrillos ni obstaculos irrompibles (se ve en el metodo `MappedGrid.__init__`).

En cada marco que sigue, ejutamos el metodo `MappedGrid.update`, que lee los contenidos del argumento `perception`, actualizando la mapa hacia arriba, abajo, izquierda y derecha del agente. Tambien actualiza el posicion del agente y el centro de comando. Por esto, queda guardando informacion de ejutaciones anteriores.

## `MappedGrid` - El Algorithmo Floodfill

Despues de actualizar el modelo con la nueva informacion, ejutamos el metodo `MappedGrid.get_next_agent_move` que calcula cual direcion se acerca el ajente hacia el centro comando a traves de / evitando los obstaculos irrompibles.

Se usa un algoritmo [floodfill](https://es.wikipedia.org/wiki/Algoritmo_de_relleno_por_difusi%C3%B3n) para calcular el `cost` (la medida de casillas de distancia) entre el centro commando y cada casilla en la mapa. Despues, elige el direcion en que el `cost` sea minimo.
