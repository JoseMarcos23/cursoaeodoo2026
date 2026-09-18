# Modelos nuevos

* Modelo de categoría (realestate.category)
  * Nombre
  * Descripción

* Añadir la categoría al modelo de propiedad

* Modelo de oferta (realestate.offer)
  * Propiedad
  * Comprador (contacto)
  * Importe
  * Fecha
  * Estado (Borrador, Enviada, Aceptada, Rechazada)
  * Notas

* Modelo de contrato (realestate.contract)
  * Nombre
  * Tipo (Alquiler, Venta)
  * Propiedad
  * Inquilino (contacto)
  * Fecha de inicio
  * Fecha de fin
  * Renta
  * Fianza
  * Estado (Borrador, En curso, Finalizado, Cancelado)


# Seguridad

Añadir la seguridad para todos los modelos nuevos que hemos creado. El manager
tiene que poder hacerlo todo, el usuario a vuestro gusto, pero mínimo un tipo de
operación a 0.

# Vistas

Crear menú, acción y vista de listado y formulario para cada modelo nuevo.
Añadir la categoría a las vistas de la propiedad.

# Métodos

Añadir métodos que hagan un flujo de estados:
* En la oferta: pasar a enviada, pasar a aceptada, pasar a rechazada y volver a borrador. Al aceptar una oferta, la propiedad tiene que quedar reservada.
* En el contrato: pasar a en curso, pasar a finalizado, pasar a cancelado y volver a borrador.

# Traducir

Traducir todo.
