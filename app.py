try:
    from fastapi import FastAPI
    from src import models, main
    import uvicorn
    import logging
except Exception as e:
    print(f"ERROR al importar las librerias en app.py, {e}")

logger = logging.getLogger("uvicorn.error")

app = FastAPI(
    debug=True,
    title="API desarrollada para la Reserva de Hoteles",
    description="API desarrollada con FastAPI y PortgreSQL, permite crear clientes, servicios, habitaciones, reservas, facturas y pagos",
    version="1.0.0"
)

try:
    @app.post("/clientes", description="Endpoint para guardar CLIENTES")
    def api_agregar_cliente(cliente: models.Cliente):
        return main.agregar_cliente(cliente)

    @app.post("/servicios", description="Endpoint para crear los SERVICIOS")
    def api_agregar_servicio(servicio: models.Servicio):
        return main.agregar_servicio(servicio)

    @app.post("/habitaciones", description="Endpoint para crear las HABITACIONES")
    def api_agregar_habitacion(habitacion: models.Habitacion):
        return main.agregar_habitacion(habitacion)

    @app.post("/reservas", description="Endpoint para crear las RESERVAS")
    def api_agregar_reserva(reserva: models.Reserva):
        return main.agregar_reserva(reserva)

    @app.post("/facturas", description="Endpoint para crear las FACTURAS")
    def api_agregar_factura(factura: models.Factura):
        return main.agregar_factura(factura)

    @app.post("/pagos", description="Endpoint para crear los PAGOS")
    def api_agregar_pago(pago: models.Pago):
        return main.agregar_pago(pago)

    @app.get("/", description="Endpoint RAIZ")
    def home():
        return {"message": "API para Reservas de Hotel en ejecución ..."}
except Exception as e:
    print(f"ERROR, fallaron los enpoints, {e}")

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=9999, reload=True)