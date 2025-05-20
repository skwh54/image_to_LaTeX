import streamlit as st
from reponse_image import reponse_image

st.title("Image to LaTeX Converter")

model_choice = st.selectbox(
    "Select a model:",
    ["gemma3:latest", "llama3.2-vision"]
)

uploaded = st.file_uploader(
    "Upload an image of a math equation (PNG/JPG):",
    type=["png","jpg","jpeg"]
)

if uploaded and st.button("Convert"):
    st.image(
        uploaded,
        caption="Equation",
        use_container_width=True
    )

    img_bytes = uploaded.read()
    with st.spinner("Converting..."):
        latex = reponse_image(img_bytes, model_choice)
    st.subheader("Generated LaTeX")
    st.code(latex, language="latex")
