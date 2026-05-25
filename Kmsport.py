import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="KMSPORT | Catálogo Showroom",
    page_icon="👟",
    layout="wide"
)

# --- 2. CARGA DE DATOS REALES (EXTRAÍDOS DE TU ARCHIVO EXCEL/CSV) ---
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

# Carpeta local para fotos de productos (si las tienes ahí)
IMG_DIR = "images" 

# --- 🚀 URL DE TU LOGO EN GITHUB ---
# REMANZAR AQUÍ: Ve a tu GitHub, haz clic en tu logo, presiona el botón "Raw" y copia ese enlace exacto aquí:
URL_LOGO_GITHUB = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPOSITORIO/main/logo.png"

# --- 3. BARRA LATERAL (NAVEGACIÓN) ---
with st.sidebar:
    # Mostramos el logo directamente usando la URL de GitHub
    st.image(URL_LOGO_GITHUB, caption="KMSPORT", use_container_width=True)
        
    st.markdown("---")
    menu = st.radio("Secciones:", ["🏠 Inicio", "🛍️ Ver Catálogo", "📩 ¿Cómo comprar?"])
    st.markdown("---")
    st.warning("📍 Entregas en Caracas")
    st.info("🛵 Delivery disponible / Pick up")

# --- 4. SECCIÓN: INICIO ---
if menu == "🏠 Inicio":
    st.title("KMSPORT")
    st.subheader("¡Tu nueva marca favorita de ropa y accesorios deportivos!")
    
    # Imagen estética de fondo
    st.image("https://images.unsplash.com/photo-1483721310020-03333e577078?q=80&w=1200", use_container_width=True)
    
    st.markdown("### 👋 ¡Hola! Bienvenido a nuestro emprendimiento")
    st.write(
        "Somos un equipo apasionado por el fitness que está empezando a traer "
        "las mejores tendencias en conjuntos, monos y accesorios deportivos a Caracas. "
        "Buscamos ofrecerte prendas cómodas, modernas y de excelente calidad para que "
        "lo des todo en tus entrenamientos sin gastar una fortuna."
    )

# --- 5. SECCIÓN: CATÁLOGO ---
elif menu == "🛍️ Ver Catálogo":
    st.title("🛍️ Nuestro Catálogo")
    st.write("Explora lo que tenemos disponible. Si te gusta algo, dale clic al botón para escribirnos directamente al WhatsApp.")
    
    query = st.text_input("Buscar producto:", placeholder="Ej: Mono, Guantes...")
    
    df_filtrado = df_km.copy()
    if query:
        df_filtrado = df_filtrado[df_filtrado["Producto"].str.contains(query, case=False)]

    tab_mujer, tab_hombre, tab_acc = st.tabs(["💃 Damas", "🏃‍♂️ Caballeros", "🎒 Accesorios"])
    
    def mostrar_cuadricula(categoria_nombre, df_data):
        df_cat = df_data[df_data["Categoría"] == categoria_nombre]
        
        if df_cat.empty:
            st.warning("No tenemos productos que coincidan con tu búsqueda en esta sección.")
            return

        cols = st.columns(3)
        for idx, row in enumerate(df_cat.itertuples()):
            col_actual = cols[idx % 3]
            with col_actual:
                with st.container(border=True):
                    # Carga de la foto del artículo
                    img_item_path = os.path.join(IMG_DIR, row.Imagen)
                    if os.path.exists(img_item_path):
                        st.image(img_item_path, use_container_width=True)
                    else:
                        st.image("https://via.placeholder.com/300x300.png?text=KMSPORT", use_container_width=True)
                    
                    st.markdown(f"##### **{row.Producto}**")
                    st.markdown(f"### **${row.Precio:.2f}**")
                    
                    # Mensaje personalizado de WhatsApp
                    texto_wa = f"¡Hola! Me interesó este producto de tu catálogo: {row.Producto} (${row.Precio:.2f}). ¿Tienen disponibilidad?"
                    link_pedido = f"https://wa.me/584120195510?text={texto_wa.replace(' ', '%20')}"
                    
                    st.link_button("📲 Consultar Disponibilidad", link_pedido, use_container_width=True)

    with tab_mujer:
        mostrar_cuadricula("Mujer", df_filtrado)
    with tab_hombre:
        mostrar_cuadricula("Hombre", df_filtrado)
    with tab_acc:
        mostrar_cuadricula("Accesorios", df_filtrado)

# --- 6. SECCIÓN: CÓMO COMPRAR ---
elif menu == "📩 ¿Cómo comprar?":
    st.title("📩 Métodos de Entrega y Pago")
    st.write("Al ser un emprendimiento en crecimiento, coordinamos las ventas de forma personalizada:")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🛵 Métodos de Entrega (Caracas)")
        st.write("* **Pick Up:** Entregas personales previo acuerdo (puedes coordinar el punto de encuentro por WhatsApp).")
        st.write("* **Delivery:** Contamos con servicio de delivery express en zonas de Caracas con un costo adicional.")
        st.write("* **Envíos Nacionales:** Si estás fuera de Caracas, podemos enviártelo cobro en destino por Zoom o MRW.")
    
    with c2:
        st.markdown("### 💳 Métodos de Pago")
        st.write("* Efectivo ($)")
        st.write("* Pago Móvil")
        st.write("* Zelle (Consultar previamente)")
        
    st.markdown("---")
    st.markdown("### 📲 ¿Quieres hablar con nosotros?")
    st.write("Escríbenos para cualquier duda, consulta de tallas o coordinar una entrega:")
    st.write("📞 **Teléfonos:** 0412-0195510 / 0412-8020434")
    
    wa_general = "https://wa.me/584120195510?text=Hola%20KMSPORT,%20quiero%20hacerles%20una%20consulta."
    st.link_button("💬 Chatear por WhatsApp", wa_general, type="primary")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} KMSPORT | Impulsando tu estilo deportivo.")
