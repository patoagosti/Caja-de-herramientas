import streamlit as st
import yt_dlp as youtube_dl

st.set_page_config(page_title="Caja de Herramientas de Pato", layout="wide")
st.title("🧰 Caja de Herramientas de Pato")

st.sidebar.title("Categorías")
opcion = st.sidebar.radio(
    "Seleccioná una categoría",
    ["Conversores", "Mensajes", "Datos", "Automatizaciones"]
)

if opcion == "Conversores":
    st.header("🔄 Herramientas de Conversión")
    st.write("Acá vas a poder convertir archivos, como PDF a Word, imágenes, etc.")

    st.subheader("📥 Descargar video de YouTube")
    link = st.text_input("Pegá el link de YouTube")

    if st.button("Descargar video"):
        if link != "":
            try:
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': '%(title)s.%(ext)s',
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=True)
                    st.success(f"Descarga completada ✅ ({info['title']})")
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
        else:
            st.warning("Pegá un link primero.")

elif opcion == "Mensajes":
    st.header("💬 Armadores de Mensajes")
    st.write("Acá vas a poder crear textos automáticos para mails, WhatsApp, etc.")

elif opcion == "Datos":
    st.header("📊 Herramientas de Datos")
    st.write("Acá vas a poder limpiar listas, comparar datos, organizar Excel, etc.")

elif opcion == "Automatizaciones":
    st.header("🤖 Automatizaciones")
    st.write("Acá vas a tener scripts que hagan tareas repetitivas por vos.")

