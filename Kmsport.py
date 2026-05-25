import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="KMSPORT | Catálogo",
    page_icon="👟",
    layout="wide"
)

# --- 2. CARGA DE DATOS REALES ---
@st.cache_data
def cargar_catalogo_kmsport():
    productos = [
        {"Producto": "Conjunto deportivo de sujetador halter plisado y mallas unicolor", "Categoría": "Mujer", "Precio": 24.0, "Imagen": "conjunto_plisado.png"},
        {"Producto": "Conjunto deportivo de top halter sin espalda y leggings unicolor", "Categoría": "Mujer", "Precio": 24.0, "Imagen": "conjunto_halter.png"},
        {"Producto": "Slayform Mono ajustado de yoga sin espalda con cuello halter", "Categoría": "Mujer", "Precio": 20.0, "Imagen": "mono_slayform.png"},
        {"Producto": "Core Rhythm Mono sin espalda sin costuras para mujer", "Categoría": "Mujer", "Precio": 18.0, "Imagen": "mono_core.png"},
        {"Producto": "Pantalones rectos para mujer para hacer ejercicio (ligeros)", "Categoría": "Mujer", "Precio": 20.0, "Imagen": "pantalon_mujer.png"},
        {"Producto": "SHEIN EZwear Set de 3 piezas de mono sin mangas", "Categoría": "Mujer", "Precio": 12.0, "Imagen": "set_shein.png"},
        
        {"Producto": "GymBeat Camiseta deportiva de manga larga con estampado gráfico", "Categoría": "Hombre", "Precio": 15.0, "Imagen": "camisa_grafica.png"},
        {"Producto": "GymBeat Camiseta de manga larga con estampado de cabeza de toro", "Categoría": "Hombre", "Precio": 15.0, "Imagen": "camisa_toro.png"},
        {"Producto": "Camiseta de manga larga para correr (Primavera/Otoño)", "Categoría": "Hombre", "Precio": 15.0, "Imagen": "camisa_correr.png"},
        {"Producto": "3 piezas Pantalones cortos deportivos con cordón y bolsillos", "Categoría": "Hombre", "Precio": 15.0, "Imagen": "shorts_3pcs.png"},
        {"Producto": "Pantalones deportivos casuales versátiles para exteriores", "Categoría": "Hombre", "Precio": 20.0, "Imagen": "pantalon_hombre.png"},
        
        {"Producto": "Bolsa de gimnasio impermeable de gran capacidad (Fin de semana)", "Categoría": "Accesorios", "Precio": 15.0, "Imagen": "bolso_gym.png"},
        {"Producto": "Bolsa reflectante para correr y hacer ejercicio (Cruzada e invisible)", "Categoría": "Accesorios", "Precio": 5.0, "Imagen": "bolso_correr.png"},
        {"Producto": "1 par de guantes de fitness de medios dedos (Antideslizantes)", "Categoría": "Accesorios", "Precio": 5.0, "Imagen": "guantes_fitness.png"},
        {"Producto": "1 par de guantes deportivos de media mano para levantamiento de pesas", "Categoría": "Accesorios", "Precio": 5.0, "Imagen": "guantes_pesas.png"},
        {"Producto": "1 pieza Rodillera ajustable unisex transpirable", "Categoría": "Accesorios", "Precio": 5.0, "Imagen": "rodillera.png"},
        {"Producto": "Bandas de resistencia de yoga de alta resistencia (Pack variado)", "Categoría": "Accesorios", "Precio": 3.0, "Imagen": "bandas_yoga.png"},
        {"Producto": "Toallas de microfibra de secado rápido y altamente absorbentes", "Categoría": "Accesorios", "Precio": 2.0, "Imagen": "toallas.png"}
    ]
    return pd.DataFrame(productos)

df_km = cargar_catalogo_kmsport()

# --- 3. CONFIGURACIÓN DEL LOGO LOCAL ---
# Buscamos el nombre exacto del archivo que tienes en tu repositorio
NOMBRE_LOGO = "LogoKmsport.png" 

# --- 4. BARRA LATERAL (NAVEGACIÓN) ---
with st.sidebar:
    # Verificamos si el archivo existe localmente en el repositorio cargado
    if os.path.exists(NOMBRE_LOGO):
        st.image(NOMBRE_LOGO, use_container_width=True)
    else:
        st.subheader("KMSPORT")
        
    st.markdown("---")
    menu = st.radio("Navegación:", ["Inicio", "Catálogo", "Información de Compra"])
    st.markdown("---")
    st.write("📍 Entregas personales en Caracas")
    st.write("🛵 Servicio de delivery disponible")

# --- 5. SECCIÓN: INICIO ---
if menu == "Inicio":
    st.title("KMSPORT")
    st.markdown("#### Ropa y accesorios deportivos")
    
    st.image("https://images.unsplash.com/photo-1483721310020-03333e577078?q=80&w=1200", use_container_width=True)
    
    st.markdown("### Bienvenido")
    st.write(
        "Somos un emprendimiento dedicado a seleccionar las mejores tendencias en indumentaria "
        "y artículos deportivos. Nos enfocamos en ofrecer prendas modernas, cómodas y de alta calidad "

    )

# --- 6. SECCIÓN: CATÁLOGO ---
elif menu == "Catálogo":
    st.title("Catálogo de Productos")
    st.write("Explora nuestras categorías. Para consultar disponibilidad o iniciar un pedido, haz clic en el botón de WhatsApp de la prenda.")
    
    query = st.text_input("Buscar por nombre:", placeholder="Ej: Mono, Guantes, Conjunto...")
    
    df_filtrado = df_km.copy()
    if query:
        df_filtrado = df_filtrado[df_filtrado["Producto"].str.contains(query, case=False)]

    tab_mujer, tab_hombre, tab_acc = st.tabs(["Línea Dama", "Línea Caballero", "Accesorios"])
    
    def mostrar_productos(categoria_nombre, df_data):
        df_cat = df_data[df_data["Categoría"] == categoria_nombre]
        
        if df_cat.empty:
            st.warning("No se encontraron artículos que coincidan con la búsqueda.")
            return

        cols = st.columns(3)
        for idx, row in enumerate(df_cat.itertuples()):
            col_actual = cols[idx % 3]
            with col_actual:
                with st.container(border=True):
                    # Si tienes las fotos guardadas en el mismo repositorio, las busca por su nombre
                    if os.path.exists(row.Imagen):
                        st.image(row.Imagen, use_container_width=True)
                    else:
                        st.image("https://via.placeholder.com/300x300.png?text=KMSPORT", use_container_width=True)
                    
                    st.markdown(f"**{row.Producto}**")
                    st.markdown(f"### ${row.Precio:.2f}")
                    
                    # Mensaje simplificado para WhatsApp
                    texto_wa = f"Hola KMSPORT, estoy interesado en el siguiente artículo de su catálogo: {row.Producto} (${row.Precio:.2f}). ¿Tienen disponibilidad?"
                    link_pedido = f"https://wa.me/584120195510?text={texto_wa.replace(' ', '%20')}"
                    
                    st.link_button("Consultar producto", link_pedido, use_container_width=True)

    with tab_mujer:
        mostrar_productos("Mujer", df_filtrado)
    with tab_hombre:
        mostrar_productos("Hombre", df_filtrado)
    with tab_acc:
        mostrar_productos("Accesorios", df_filtrado)

# --- 7. SECCIÓN: INFORMACIÓN DE COMPRA ---
elif menu == "Información de Compra":
    st.title("Métodos de Pago y Despacho")
    st.write("Coordinamos cada una de las entregas de forma directa y personalizada a través de nuestros canales de atención.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Entregas y Envíos")
        st.write("* **Pick Up:** Entregas personales en Caracas previo acuerdo.")
        st.write("* **Delivery:** Despachos express a domicilio en zonas urbanas (costo adicional).")
        
    with c2:
        st.markdown("### Métodos de Pago")
        st.write("* Efectivo ($)")
        st.write("* Pago Móvil")
        st.write("* USDT")
        st.write("* Zelle (Consultar condiciones)")
        
    st.markdown("---")
    st.markdown("### Contacto Directo")
    st.write("Líneas de atención: 0412-0195510 / 0412-8020434")
    
    wa_general = "https://wa.me/584120195510?text=Hola%20KMSPORT,%20solicito%20información."
    st.link_button("Contactar por WhatsApp", wa_general, type="primary")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} KMSPORT | Catálogo Informativo")
