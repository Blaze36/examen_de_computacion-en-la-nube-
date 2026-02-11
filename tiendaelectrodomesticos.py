import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Tienda de Electrodomésticos", layout="wide")


st.title(" Tienda de Electrodomésticos - Examen I Parcial")


productos_catalogo = {
    "Refrigeradora": {"precio": 8500, "categoria": "Cocina"},
    "Lavadora": {"precio": 6200, "categoria": "Ropa"},
    "Microondas": {"precio": 2800, "categoria": "Cocina"},
    "Licuadora": {"precio": 850, "categoria": "Cocina"},
    "Aire Acondicionado": {"precio": 7500, "categoria": "refigeracion"},
    "Plancha": {"precio": 450, "categoria": "Ropa"},
    "Televisor": {"precio": 5900, "categoria": "Entretenimiento"},
    "Cafetera": {"precio": 1200, "categoria": "Cocina"}
}

st.sidebar.header("Filtros")
precio_max = st.sidebar.slider("Filtro por precio máximo", 0, 10000, 10000, step=500)


productos_filtrados = {k: v for k, v in productos_catalogo.items() if v["precio"] <= precio_max}


col1, col2 = st.columns(2)

with col1:
    st.header("Selección de Producto")
    
    producto_seleccionado = st.selectbox(
        "Seleccionar un producto:",
        list(productos_filtrados.keys())
    )
    
    precio_unitario = productos_filtrados[producto_seleccionado]["precio"]
    categoria = productos_filtrados[producto_seleccionado]["categoria"]
    
    st.write(f"**Categoría:** {categoria}")
    st.write(f"**Precio unitario:** L. {precio_unitario:,.2f}")

with col2:
    st.header("Recibo")
    
    cantidad = st.number_input("Cantidad:", min_value=1, step=1)
    subtotal_producto = precio_unitario * cantidad
    
    st.metric("Subtotal del producto", f"L. {subtotal_producto:,.2f}")

st.header(" Catálogo Disponible")
df_catalogo = pd.DataFrame([
    {"Producto": k, "Precio": f"L. {v['precio']:,.2f}", "Categoría": v["categoria"]}
    for k, v in productos_filtrados.items()
])
st.dataframe(df_catalogo, use_container_width=True, hide_index=True)


st.header("Datos del Cliente")
col1, col2 = st.columns(2)

with col1:
    nombre_cliente = st.text_input("Nombre del cliente:")
    rtn_cliente = st.text_input("RTN / Identidad:")

with col2:
    fecha_compra = st.date_input("Fecha de compra:", datetime.now())


st.header(" Resumen de Facturación")

if nombre_cliente and rtn_cliente:

    impuesto = 0.15
    subtotal_general = subtotal_producto
    monto_impuesto = subtotal_general * impuesto
    total_pagar = subtotal_general + monto_impuesto
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Datos de Facturación")
        st.write(f"**Cliente:** {nombre_cliente}")
        st.write(f"**RTN/Identidad:** {rtn_cliente}")
        st.write(f"**Fecha:** {fecha_compra.strftime('%d/%m/%Y')}")
    
    with col2:
        st.subheader("Detalle de Compra")
        st.write(f"**Producto:** {producto_seleccionado}")
        st.write(f"**Cantidad:** {cantidad}")
        st.write(f"**Precio unitario:** L. {precio_unitario:,.2f}")
        st.write(f"**Subtotal:** L. {subtotal_producto:,.2f}")
    
    
    st.divider()
    st.subheader("Cálculos Finales")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Subtotal General", f"L. {subtotal_general:,.2f}")
        st.metric("ISV (15%)", f"L. {monto_impuesto:,.2f}")
    
    with col2:
        st.metric("TOTAL A PAGAR", f"L. {total_pagar:,.2f}", delta=None)
    
    
    if st.button(" Generar Factura"):
        st.success("¡Factura correcta!")
        st.balloons()
else:
    st.warning(" Por favor, completa los datos del cliente para ver la factura")