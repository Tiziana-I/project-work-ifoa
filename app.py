import streamlit as st
import app_home, app_fede, app_sere, app_tiz, app_update, app_province

def main():
    #st.beta_set_page_config( layout='wide')

    pages = {
        "Il progetto": app_home,
        "Conteggio delle positività": app_province,
        "Modello di stima dell'indice Rt" : app_sere,
        "Zone colore dell'Italia": app_tiz,
        "Modello predittivo delle zone": app_fede,
        "Aggiornamento dati" : app_update
    }
    st.sidebar.title('Menu')
    selection = st.sidebar.radio("Vai a", list(pages.keys()))
    page = pages[selection]
    page.page()
    

if __name__ == '__main__':
    main()