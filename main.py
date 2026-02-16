from servicios.gestores import GestorClientes, GestorProveedores, GestorProductos, GestorOrdenes
from pagos.pago_efectivo import PagoEfectivo
from pagos.pago_tarjeta import PagoTarjeta
from pagos.pago_transferencia import PagoTransferencia


def leer_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("❌ Ingresa un número entero válido.")


def leer_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("❌ Ingresa un número válido.")


def pausa():
    input("\nPresiona ENTER para continuar...")


def menu_crud_clientes(gestor: GestorClientes):
    while True:
        print("\n--- CLIENTES ---")
        print("1) Agregar")
        print("2) Modificar")
        print("3) Eliminar")
        print("4) Listar")
        print("5) Volver")
        op = input("Opción: ").strip()

        if op == "1":
            nombre = input("Nombre: ")
            tel = input("Teléfono: ")
            c = gestor.agregar(nombre, tel)
            print("✅ Guardar cambios -> Confirmación")
            print("Cliente agregado:", c)

        elif op == "2":
            cid = leer_int("ID del cliente: ")
            c = gestor.buscar_por_id(cid)
            if not c:
                print("❌ No existe ese cliente.")
            else:
                nombre = input("Nuevo nombre: ")
                tel = input("Nuevo teléfono: ")
                gestor.modificar(cid, nombre, tel)
                print("✅ Guardar cambios -> Confirmación")
                print("Cliente actualizado.")

        elif op == "3":
            cid = leer_int("ID del cliente: ")
            if gestor.eliminar(cid):
                print("✅ Guardar cambios -> Confirmación")
                print("Cliente eliminado.")
            else:
                print("❌ No existe ese cliente.")

        elif op == "4":
            print("\nLista de clientes:")
            for c in gestor.listar():
                print("  ", c)

        elif op == "5":
            return
        else:
            print("❌ Opción inválida.")


def menu_crud_proveedores(gestor: GestorProveedores):
    while True:
        print("\n--- PROVEEDORES ---")
        print("1) Agregar")
        print("2) Modificar")
        print("3) Eliminar")
        print("4) Listar")
        print("5) Volver")
        op = input("Opción: ").strip()

        if op == "1":
            nombre = input("Nombre: ")
            tel = input("Teléfono: ")
            p = gestor.agregar(nombre, tel)
            print("✅ Guardar cambios -> Confirmación")
            print("Proveedor agregado:", p)

        elif op == "2":
            pid = leer_int("ID del proveedor: ")
            p = gestor.buscar_por_id(pid)
            if not p:
                print("❌ No existe ese proveedor.")
            else:
                nombre = input("Nuevo nombre: ")
                tel = input("Nuevo teléfono: ")
                gestor.modificar(pid, nombre, tel)
                print("✅ Guardar cambios -> Confirmación")
                print("Proveedor actualizado.")

        elif op == "3":
            pid = leer_int("ID del proveedor: ")
            if gestor.eliminar(pid):
                print("✅ Guardar cambios -> Confirmación")
                print("Proveedor eliminado.")
            else:
                print("❌ No existe ese proveedor.")

        elif op == "4":
            print("\nLista de proveedores:")
            for p in gestor.listar():
                print("  ", p)

        elif op == "5":
            return
        else:
            print("❌ Opción inválida.")


def menu_crud_productos(gestor: GestorProductos, gestor_prov: GestorProveedores):
    while True:
        print("\n--- PRODUCTOS ---")
        print("1) Agregar")
        print("2) Modificar")
        print("3) Eliminar")
        print("4) Listar")
        print("5) Volver")
        op = input("Opción: ").strip()

        if op == "1":
            nombre = input("Nombre del producto: ")
            precio = leer_float("Precio: ")
            stock = leer_int("Stock: ")
            prov = input("ID Proveedor (opcional, ENTER para saltar): ").strip()
            prov_id = int(prov) if prov else None
            if prov_id is not None and gestor_prov.buscar_por_id(prov_id) is None:
                print("❌ Ese proveedor no existe. Se guardará como N/A.")
                prov_id = None
            prod = gestor.agregar(nombre, precio, stock, prov_id)
            print("✅ Guardar cambios -> Confirmación")
            print("Producto agregado:", prod)

        elif op == "2":
            pid = leer_int("ID del producto: ")
            p = gestor.buscar_por_id(pid)
            if not p:
                print("❌ No existe ese producto.")
            else:
                nombre = input("Nuevo nombre: ")
                precio = leer_float("Nuevo precio: ")
                stock = leer_int("Nuevo stock: ")
                prov = input("Nuevo ID Proveedor (opcional, ENTER para saltar): ").strip()
                prov_id = int(prov) if prov else None
                if prov_id is not None and gestor_prov.buscar_por_id(prov_id) is None:
                    print("❌ Ese proveedor no existe. Se guardará como N/A.")
                    prov_id = None
                gestor.modificar(pid, nombre, precio, stock, prov_id)
                print("✅ Guardar cambios -> Confirmación")
                print("Producto actualizado.")

        elif op == "3":
            pid = leer_int("ID del producto: ")
            if gestor.eliminar(pid):
                print("✅ Guardar cambios -> Confirmación")
                print("Producto eliminado.")
            else:
                print("❌ No existe ese producto.")

        elif op == "4":
            print("\nLista de productos:")
            for p in gestor.listar():
                print("  ", p)

        elif op == "5":
            return
        else:
            print("❌ Opción inválida.")


def seleccionar_cliente(gestor_clientes: GestorClientes):
    if not gestor_clientes.listar():
        print("❌ No hay clientes. Primero agrega uno en 'Clientes'.")
        return None

    print("\nClientes disponibles:")
    for c in gestor_clientes.listar():
        print("  ", c)
    cid = leer_int("Selecciona ID cliente: ")
    cliente = gestor_clientes.buscar_por_id(cid)
    if not cliente:
        print("❌ Cliente no válido.")
        return None
    return cliente


def seleccionar_producto(gestor_productos: GestorProductos):
    if not gestor_productos.listar():
        print("❌ No hay productos. Primero agrega uno en 'Productos'.")
        return None

    print("\nProductos disponibles:")
    for p in gestor_productos.listar():
        print("  ", p)
    pid = leer_int("Selecciona ID producto: ")
    prod = gestor_productos.buscar_por_id(pid)
    if not prod:
        print("❌ Producto no válido.")
        return None
    return prod


def flujo_orden_compra(gestor_clientes, gestor_productos, gestor_ordenes):
    cliente = seleccionar_cliente(gestor_clientes)
    if not cliente:
        return

    orden = gestor_ordenes.crear(cliente.id)
    print(f"\n✅ Crear nueva OrdenCompra #{orden.id} para cliente {cliente.nombre}")

    while True:
        resp = input("\n¿Agregar productos? (s/n): ").strip().lower()
        if resp != "s":
            break

        prod = seleccionar_producto(gestor_productos)
        if not prod:
            continue

        cant = leer_int("Ingresa cantidad: ")
        ok = orden.agregar_item(prod, cant)
        if ok:
            print("✅ Producto agregado a la orden.")
        else:
            print("❌ No se pudo agregar (cantidad inválida o stock insuficiente).")

        otro = input("¿Agregar otro producto? (s/n): ").strip().lower()
        if otro != "s":
            break

    if not orden.items:
        print("❌ Orden vacía. Fin.")
        return

    print("\n--- Calcular total ---")
    print(orden)

    resp_pago = input("\n¿Procesar pago? (s/n): ").strip().lower()
    if resp_pago != "s":
        print("Fin (sin pago).")
        return

    while True:
        print("\nSeleccionar Método de Pago")
        print("1) PagoEfectivo")
        print("2) PagoTarjeta")
        print("3) Transferencia")
        metodo = input("Opción: ").strip()

        pago = None
        if metodo == "1":
            entregado = leer_float("Monto entregado: ")
            pago = PagoEfectivo(orden.total(), entregado)
        elif metodo == "2":
            num = input("Número de tarjeta (16 dígitos): ")
            cvv = input("CVV (3 o 4 dígitos): ")
            pago = PagoTarjeta(orden.total(), num, cvv)
        elif metodo == "3":
            ref = input("Referencia de transferencia: ")
            pago = PagoTransferencia(orden.total(), ref)
        else:
            print("❌ Opción inválida.")
            continue

        exitoso, msg = pago.procesar()
        if exitoso:
            print("✅ ¿Pago exitoso? Sí ->", msg)
            orden.estado = "PAGADA"
            print("✅ Confirmar")
            print("✅ Actualizar estado Orden ->", orden.estado)
        else:
            print("❌ ¿Pago exitoso? No ->", msg)
            orden.estado = "ERROR"
            print("❌ Mostrar error")
            print("✅ Actualizar estado Orden ->", orden.estado)

        print("Fin.")
        break


def main():
    clientes = GestorClientes()
    proveedores = GestorProveedores()
    productos = GestorProductos()
    ordenes = GestorOrdenes()

    # Datos de ejemplo
    clientes.agregar("Juan Pérez", "664-111-2222")
    proveedores.agregar("Proveedor Norte", "664-333-4444")
    productos.agregar("Teclado", 250.0, 10, 1)
    productos.agregar("Mouse", 150.0, 15, 1)

    while True:
        print("\n==============================")
        print("   MOSTRAR MENÚ PRINCIPAL")
        print("==============================")
        print("1) Clientes")
        print("2) Proveedores")
        print("3) Productos")
        print("4) Orden de Compra")
        print("5) Salir")
        op = input("Opción: ").strip()

        if op == "1":
            menu_crud_clientes(clientes)
        elif op == "2":
            menu_crud_proveedores(proveedores)
        elif op == "3":
            menu_crud_productos(productos, proveedores)
        elif op == "4":
            flujo_orden_compra(clientes, productos, ordenes)
            pausa()
        elif op == "5":
            print("Saliendo... Fin.")
            break
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()
