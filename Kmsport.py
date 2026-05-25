import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="KMSPORT | Catálogo Oficial",
    page_icon="💪",
    layout="wide"
)

# --- 2. CARGA DE DATOS REALES (EXTRAÍDOS DE TU ARCHIVO EXCEL/CSV) ---
@st.cache_data
def cargar_catalogo_kmsport():
    # Cargamos la data exacta de tu archivo con sus precios base
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

# --- RUTA DE IMÁGENES (Para tu repositorio local o servidor) ---
# Si tus imágenes están en una carpeta llamada 'images' dentro de tu repositorio, déjalo así:
IMG_DIR = "images" 

# --- 3. BARRA LATERAL (NAVEGACIÓN) ---
with st.sidebar:
    # Intenta cargar tu logo real desde tu carpeta de imágenes
    logo_path = os.path.join(IMG_DIR, "logo.png") # Cambia "logo.png" por el nombre exacto de tu archivo
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.markdown("# 👟 **KMSPORT**")
        
    st.markdown("---")
    menu = st.radio("Secciones del Sitio:", ["🏠 Inicio", "🛍️ Catálogo por Secciones", "📩 Contacto"])
    st.markdown("---")
    st.success("🚚 Envíos a toda Venezuela")
    st.info("💡 Descuentos especiales por volumen de compra")

# --- 4. SECCIÓN: INICIO (PÁGINA PRINCIPAL) ---
if menu == "🏠 Inicio":
    st.title("Bienvenidos a KMSPORT")
    st.subheader("Tu aliado estratégico en ropa y accesorios deportivos masivos.")
    
    # Imagen de portada de tienda deportiva
    st.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=1200", use_container_width=True)
    
    col_nos, col_val = st.columns(2)
    with col_nos:
        st.markdown("### 🏆 Sobre Nosotros")
        st.write(
            "En KMSPORT nos dedicamos a la distribución de indumentaria y accesorios "
            "deportivos de alta calidad. Nos enfocamos en ofrecer las últimas tendencias "
            "del mercado retail fitness, garantizando precios altamente competitivos para revendedores "
            "y tiendas a nivel nacional."
        )
        
    with col_val:
        st.markdown("### ✨ ¿Por qué elegirnos?")
        st.write("* **Variedad en Tendencias:** Catálogo actualizado para Damas, Caballeros y Accesorios.")
        st.write("* **Logística Eficiente:** Despachos rápidos y coordinados a todo el territorio nacional.")
        st.write("* **Relación Calidad-Precio:** Productos seleccionados con excelentes márgenes de ganancia.")

# --- 5. SECCIÓN: CATÁLOGO DIVIDIDO EN SECCIONES ---
elif menu == "🛍️ Catálogo por Secciones":
    st.title("🔎 Explorar Catálogo")
    st.write("Usa los filtros o navega por las pestañas dedicadas por sección:")
    
    # Buscador global rápido
    query = st.text_input("¿Buscas algo en específico?", placeholder="Ej: Mono, Guantes, Dewbera, Camiseta...")
    
    # Filtrar data global por la búsqueda antes de armar las pestañas
    df_filtrado = df_km.copy()
    if query:
        df_filtrado = df_filtrado[df_filtrado["Producto"].str.contains(query, case=False)]

    # --- CREACIÓN DE PESTAÑAS (HOMBRE / MUJER / ACCESORIOS) ---
    tab_mujer, tab_hombre, tab_acc = st.tabs(["💃 Línea Mujer", "🏃‍♂️ Línea Hombre", "🎒 Accesorios y Equipamiento"])
    
    # Función interna para mostrar los productos en una cuadrícula bonita de tarjetas
    def mostrar_cuadricula(categoria_nombre, df_data):
        df_cat = df_data[df_data["Categoría"] == categoria_nombre]
        
        if df_cat.empty:
            st.warning("No se encontraron productos en esta sección para tu búsqueda.")
            return

        # Crear filas con 3 columnas cada una
        cols = st.columns(3)
        for idx, row in enumerate(df_cat.itertuples()):
            col_actual = cols[idx % 3]
            with col_actual:
                with st.container(border=True):
                    # Manejo de la imagen del producto
                    img_item_path = os.path.join(IMG_DIR, row.Imagen)
                    if os.path.exists(img_item_path):
                        st.image(img_item_path, use_container_width=True)
                    else:
                        # Imagen provisional si no encuentra tu archivo local aún
                        st.image("https://via.placeholder.com/300x300.png?text=KM+SPORT", use_container_width=True)
                    
                    st.markdown(f"#### **{row.Producto}**")
                    st.markdown(f"### **${row.Precio:.2f}**")
                    
                    # Enlace de WhatsApp personalizado para CADA producto
                    texto_wa = f"Hola KMSPORT! Me interesa el producto: {row.Producto} (Precio: ${row.Precio:.2f})"
                    link_pedido = f"https://wa.me/584120195510?text={texto_wa.replace(' ', '%20')}"
                    
                    st.link_button("📥 Ordenar / Consultar", link_pedido, use_container_width=True)

    with tab_mujer:
        mostrar_cuadricula("Mujer", df_filtrado)
        
    with tab_hombre:
        mostrar_cuadricula("Hombre", df_filtrado)
        
    with tab_acc:
        mostrar_cuadricula("Accesorios", df_filtrado)

# --- 6. SECCIÓN: CONTACTO ---
elif menu == "📩 Contacto":
    st.title("📩 Canales de Atención Oficiales")
    st.write("Ponte en contacto directo con nuestro equipo de ventas para cotizaciones de volumen.")
    
    c_info, c_qr = st.columns(2)
    with c_info:
        st.markdown("### 📍 Información de la Empresa")
        st.markdown("**📍 Ubicación:** Caracas, Venezuela (Despachos y envíos nacionales)")
        st.markdown("**📞 Teléfonos Principales:** 0412-0195510 / 0412-8020434")
        st.markdown("**✉️ Correo Electrónico:** Juanbarcenass18@gmail.com")
        st.markdown("**🕒 Horario de atención:** Lunes a Sábado - 8:00 AM a 6:00 PM")
    
    with c_qr:
        st.markdown("### 📲 ¡Escríbenos Directo!")
        wa_general = "https://wa.me/584120195510?text=Hola%20KMSPORT,%20solicito%20información%20general."
        st.link_button("💬 Chat General de WhatsApp", wa_general, type="primary", use_container_width=True)

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} KMSPORT | Creado para potenciar tu rendimiento comercial.")
