from ..black_box.casos_de_uso import (crear_pedido_producto, notificar_niveles_minimos_inventario,
                                      ejecutar_algoritmo_reabastecimiento, validar_cantidad_producto_orden_compra,
                                      calcular_disponibilidad_productos, aplicar_descuento_por_nivel_stock,
                                      sincronizar_con_proveedor, confirmar_pedido, acceso_usuario_no_autorizado,
                                      manejar_error_comunicacion_proveedor, publicar_resena_producto,
                                      probar_compatibilidad_navegadores, buscar_producto_por_nombre,
                                      comprar_producto_con_descuento, probar_notificacion_niveles_minimos_inventario,
                                      agregar_producto_al_inventario)
import pytest

# tests

# Caso de prueba 1: Agregar Producto al Inventario


def test_agregar_producto_al_inventario():
    producto_agregado = agregar_producto_al_inventario(
        {"nuevo_producto": "Producto de prueba"})
    assert producto_agregado == True

# Caso de prueba 2: Crear Pedido de Producto


def test_crear_pedido_producto_valido():
    pedido_creado = crear_pedido_producto(True)
    inventario_afectado = crear_pedido_producto(True)
    assert pedido_creado == True
    assert inventario_afectado == True

# Caso de prueba 3: Notificar Niveles Mínimos de Inventario


def test_notificar_niveles_minimos_inventario():
    notificacion_enviada = notificar_niveles_minimos_inventario(True)
    assert notificacion_enviada == True

# Caso de prueba 4: Ejecutar Algoritmo de Reabastecimiento


def test_ejecutar_algoritmo_reabastecimiento():
    productos_reabastecidos = ejecutar_algoritmo_reabastecimiento()
    assert productos_reabastecidos == True

# Caso de prueba 5: Validar Cantidad de Producto en Orden de Compra


def test_validar_cantidad_producto_orden_compra():
    cantidad_valida, mensaje_error = validar_cantidad_producto_orden_compra(10)
    assert cantidad_valida == True
    assert mensaje_error == ""

# Caso de prueba 6: Calcular Disponibilidad de Productos


def test_calcular_disponibilidad_productos():
    disponibilidad = calcular_disponibilidad_productos(100, 20)
    assert disponibilidad == 80

# Caso de prueba 7: Aplicar Descuento por Nivel de Stock


def test_aplicar_descuento_por_nivel_stock():
    descuento_aplicado = aplicar_descuento_por_nivel_stock(15)
    assert descuento_aplicado == True

# Caso de prueba 8: Sincronización con Proveedor


def test_sincronizar_con_proveedor():
    sincronizacion_exitosa, datos_actualizados = sincronizar_con_proveedor()
    assert sincronizacion_exitosa == True
    assert datos_actualizados == True

# Caso de prueba 9: Confirmación de Pedido


def test_confirmar_pedido():
    pedido_confirmado, estado_inventario_actualizado = confirmar_pedido()
    assert pedido_confirmado == True
    assert estado_inventario_actualizado == True

# Caso de prueba 10: Acceso de Usuario no Autorizado


def test_acceso_usuario_no_autorizado():
    acceso_denegado, mensaje_error = acceso_usuario_no_autorizado()
    assert acceso_denegado == True
    assert mensaje_error == ""

# Caso de prueba 11: Manejo de Error en Comunicación con el Proveedor


def test_manejar_error_comunicacion_proveedor():
    error_registrado, mensaje_error = manejar_error_comunicacion_proveedor(
        True)
    assert error_registrado == True
    assert mensaje_error == "Error de comunicación con el proveedor"

# Caso de prueba 12: Publicación de Reseña de Producto


def test_publicar_resena_producto():
    reseña_publicada = publicar_resena_producto("Buena reseña")
    assert reseña_publicada == True

# Caso de prueba 13: Prueba de Compatibilidad con Navegadores


def test_probar_compatibilidad_navegadores():
    compatibilidad_correcta = probar_compatibilidad_navegadores()
    assert compatibilidad_correcta == True

# Caso de prueba 14: Búsqueda de producto por Nombre


def test_buscar_producto_por_nombre():
    resultado = buscar_producto_por_nombre(
        "Producto de prueba", ["Producto de prueba", "Otro producto"])
    assert resultado == True

# Caso de prueba 15: Compra de producto con descuento


def test_comprar_producto_con_descuento():
    precio_final = comprar_producto_con_descuento(15, 100)
    assert precio_final == 90

# Caso de prueba 16: Prueba de notificación al alcanzar niveles mínimos de inventario


def test_probar_notificacion_niveles_minimos_inventario():
    notificacion_enviada = probar_notificacion_niveles_minimos_inventario(True)
    assert notificacion_enviada == True

# Caso de prueba 17: Creación de pedido con datos no validos


def test_crear_pedido_producto_invalido():
    pedido_creado = crear_pedido_producto(True)
    inventario_afectado = crear_pedido_producto(False)
    assert pedido_creado == False
    assert inventario_afectado == False
