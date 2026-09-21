## Modelo de propiedad

# Etapas (antes de la kanban)
Crear el modelo de etapas (realestate.property.stage) con nombre y secuencia.
* Campo stage_id (Many2one) en la propiedad, por defecto la primera etapa.
* Añadir la etapa a las vistas de la propiedad.

# Search
Filtro por nombre, referencia y categoría
Filtro con domain disponible / reservada (campo availability)
Agrupación de etapa y categoría
Añadir las vistas nuevas al view_mode de la action

# Vista Kanban
Vista kanban parecida a la de CRM (agrupada por etapa) que muestre el nombre de la propiedad, el precio, la categoría y el responsable asignado

# Vista Pivot
Medida precio / columna categoría / fila responsable asignado

# Vista graph
Estado e importe de medida en vista de ofertas

# Filter domain
Añadir un filter_domain al campo nombre del search de propiedad, que busque también por categoría:
['|', ('category_id.name', 'ilike', self), ('name', 'ilike', self)]

# Añadir domain
Poder seleccionar solo propiedades disponibles en la oferta (domain en el campo propiedad: [('availability', '=', True)])

# Deberes

## Modelo visita

* Filtros de los tres tipos: al escribir, con dominio y con group_by
* Vista kanban (con estado de la visita)
* Vistas pivot, gráficos, calendario
