import pandas as pd
#import pandas_profiling
import streamlit as st
#from streamlit_pandas_profiling import st_profile_report

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

def change_page(page_name):
    st.session_state.current_page = page_name

if st.session_state.current_page =="home":
    # Configuración de la página
    st.set_page_config(layout="wide", page_title="Sociuslab", page_icon="📱")

    # Barra lateral
    st.sidebar.title("Bienvenido GasCompany")
    #st.sidebar.image("source_media/sociuslab-icon-white.png", use_container_width=True)
    st.sidebar.write("Crecer sin límites")
    st.sidebar.write("Verifique el rubro acorde a su nivel de inversión.")
    if st.sidebar.button("Ingresar"):
        change_page("ingreso")

    # Sección principal
    st.title("SOCIU​​SLAB")
    st.subheader("We help to create great business")

    # Layout de tres columnas
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.image("https://github.com/FJRB10/Final-Project-Henry-DSPT10/blob/main/Images/10%20correlacion%20review%20y%20stars.png?raw=true",use_container_width=True)

    with col2:
        st.image("source_media/sociuslab-icon-white-diff.png",use_container_width=True)

    with col3:
        st.image("source_media/review-main-page.png", caption="Mockup del teléfono" ,use_container_width=True)


elif st.session_state.current_page == "ingreso":

    st.subheader("Seleccione el Rubro")
    rubros = ["Inmobiliaria", "Rubro 2"]
    selected_rubro = st.selectbox("Rubros disponibles:", rubros)

    st.subheader("Ciudades Cubiertas")
    NYcity="https://imgs.search.brave.com/RZln6-uhV4zAV6fmE7aZ__iuyUvgsZXlhWCt0yCYPKo/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAxLzEwLzI0Lzg0/LzM2MF9GXzExMDI0/ODQxNV9idkhGSkNy/elYzRzFqUzJsb0hQ/ekM1S2R0MlNaVXRz/di5qcGc"
    CHcity="https://imgs.search.brave.com/3PAZsZeVMZfQxosvVYKZ-Z1URrVSjYv6R2yjGZOOIEw/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQ0/OTA0Njg1Ni9waG90/by9jaGljYWdvLXRo/ZWF0ZXItYW5kLXN1/YndheS1zdGF0aW9u/LW9mLW5vcnRoLXN0/YXRlLXN0cmVldC5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/cUs4T0FJSlhOUm1v/S04xczZCZVRPR1k0/aDBZZEg3UXIyN3ZC/V2l2OVFSMD0"
    MIcity="https://imgs.search.brave.com/u3tyh2cGWYRw5zvSHOnmLqbJ3_EegIUR7PEz4UT1la4/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTgz/ODYxNDU2L3Bob3Rv/L21pYW1pLWJlYWNo/LXNpZ24taW4tZmxv/cmlkYS11c2EuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPWNV/d2o0dVZtYmdTLWMw/M01LUC10cWxNZDRv/Y2pOaDlmZ0RnZ1FX/dFN5Tms9"
    LAcity="https://imgs.search.brave.com/oke92Ojhj6LOt8oaZKvx3EaJ_tAOA8IayhKa7nlUia8/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly92aWFq/ZWNvc3Rhb2VzdGUu/Y29tL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDIzLzEwL2NhcnRl/bC1ob2xseXdvb2Qt/bG9zLWFuZ2VsZXMt/Mi03MDB4NTQyLmpw/Zw"
    LVcity="https://imgs.search.brave.com/DraB4cW_PyQ33CF6GpmdRKkv36HFrJgelHPiF_kiQn8/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS1waG90/by93ZWxjb21lLWZh/YnVsb3VzLWxhcy12/ZWdhcy1zaWduLWxh/cy12ZWdhcy1uZXZh/ZGEtdXNhLXR3aWxp/Z2h0XzExOTc3OTct/MjcxMTQwLmpwZz9z/ZW10PWFpc19oeWJy/aWQ"
    HOcity="https://imgs.search.brave.com/uOWRNMXnhTblZW3h80bU8xC7Aez5b6OPhT6VTHDuPnk/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTEz/MDkyNDM1My9waG90/by9ob3VzdG9uLXRl/eGFzLXVzYS1kb3du/dG93bi1za3lsaW5l/LWF0LWR1c2suanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPUNS/SmVSREhyMTJoODFh/MmF4YlVFTFBLY2ZH/SVNKRWJvNUZjZm5l/UXVuMHM9"
    BRcity="https://imgs.search.brave.com/rGVJgROUJmVqTDMK3G98hhkE9ZqsaVi8QmRrc0Vkmv0/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNTI5/MTE5NDI0L3Bob3Rv/L21hbmhhdHRhbi1i/cmlkZ2UtaW4tbmV3/LXlvcmsuanBnP3M9/NjEyeDYxMiZ3PTAm/az0yMCZjPTlidzZY/ZE5VWTd1NlZZbzBy/M0F2LTM3ZHhBRHNZ/T29acmw1Smx4S3Jw/ZUk9"
    SAcity="https://imgs.search.brave.com/SrQRe2jin8SDqUyvvZoj92ln-aK-OFpZMRe91z7rBvk/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjE0/MTgyMzQ1My9waG90/by9zYW4tYW50b25p/by1yaXZlcndhbGst/dGV4YXMuanBnP3M9/NjEyeDYxMiZ3PTAm/az0yMCZjPWtxWUZC/bXpXd2pqM0V4WjR2/YklKWkhoRm9hLWQ3/NzV5eVJ0WF9RSTFM/Vk09"
    DAcity="https://imgs.search.brave.com/eDb8dNiZLKeO8U7n8_ld1CiA1Eiqw3CvcZXE04lvGfA/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNjM3/NjM1ODU0L3Bob3Rv/L2RhbGxhcy1jaXR5/LXRleGFzLXVzYS5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/U1BaTWlnQ3FfelFT/S2VKdm45Q0VGdUxi/SUtPWC1EemJVZUZK/TlAxYXAtQT0"
    PHcity="https://imgs.search.brave.com/hXi-nc5fpyWXRKFGgdV6BE9m2-_l81Lv8c0Q6h46cTc/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvOTE5/MDAyOTg2L3Bob3Rv/L2Rvd250b3duLXBo/aWxhZGVscGhpYS1w/ZW5uc3lsdmFuaWEt/c2t5bGluZS5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9dXlz/bnNkNHFSS0dNWWw5/Yjc4TDRsd3BtUEp5/RUxmU3diUFhhamps/bndUZz0"



    city = ['New York','Chicago','Miami','Los Angeles','Las Vegas','Houston','Brooklyn','San Antonio','Dallas','Philadelphia']
    pictures = [NYcity,CHcity,MIcity,LAcity,LVcity,
                HOcity,BRcity,SAcity,DAcity,PHcity,]
    
    selected_buttons, cities = st.columns([1,3]) 

    # Estilo personalizado para la tarjeta seleccionada
    selected_style = """
        <div style="
            border: 3px solid #740938;
            border-radius: 10px;
            background: linear-gradient(45deg, #FF9C73, #FF4545);
            padding: 10px;
            text-align: center;
            color: black">
        """
    default_style = """
        <div style="
            border: 1px solid #001;
            border-radius: 20px;
            padding: 20px;
            text-align: center;">
        """
    with selected_buttons:
        selected_city = st.radio("Selecciona una ciudad:", city, index=0)
    with cities:    
        for i in range(0, len(city), 5):
            cols = st.columns(5)
            for col, ciudad, picture in zip(cols, city[i:i + 5], pictures[i:i + 5]):
                with col:
                    style = selected_style if ciudad == selected_city else default_style
            
                    st.markdown(f"{style}<br><strong>{ciudad}</strong>", unsafe_allow_html=True)
                    st.image(picture, use_container_width=True, channels="BGR")
                    if ciudad == selected_city:
                        st.markdown("- SELECTED CITY ✅")

    if st.button("Busqueda"):
        change_page("busqueda")


elif st.session_state.current_page =="busqueda":
    looker = """
    <iframe style="width: 90vw; height: 80vh; background-color: lightblue;" src="https://lookerstudio.google.com/embed/reporting/233c975f-06ca-4a44-b630-61c0dbc06390/page/hcWRE"
     frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin 
     allow-popups allow-popups-to-escape-sandbox"></iframe>
    """
    st.markdown(looker, unsafe_allow_html=True)
    
    st.title("Aloha inversor")