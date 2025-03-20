import streamlit as st
import pandas as pd

# Initialiseren van een lege DataFrame voor klantgegevens
if 'klantgegevens' not in st.session_state:
    st.session_state.klantgegevens = pd.DataFrame(columns=['Naam', 'E-mail', 'Telefoonnummer', 'Bedrijf'])

# Functie om een klant toe te voegen aan de DataFrame
def voeg_klant_toe(naam, email, telefoonnummer, bedrijf):
    nieuwe_klant = pd.DataFrame([{
        'Naam': naam,
        'E-mail': email,
        'Telefoonnummer': telefoonnummer,
        'Bedrijf': bedrijf
    }])
    st.session_state.klantgegevens = pd.concat([st.session_state.klantgegevens, nieuwe_klant], ignore_index=True)

# Zijbalkmenu voor navigatie
st.sidebar.title("Navigatie")
pagina = st.sidebar.radio("Ga naar", ("CRM", "Dashboard", "Voorraad", "Contacten"))

# Inhoud van de pagina's
if pagina == "CRM":
    st.title('CRM-applicatie')

    # Formulier om klantgegevens toe te voegen
    with st.form(key='klant_formulier'):
        naam = st.text_input(label='Naam')
        email = st.text_input(label='E-mail')
        telefoonnummer = st.text_input(label='Telefoonnummer')
        bedrijf = st.text_input(label='Bedrijf')
        submit_button = st.form_submit_button(label='Voeg klant toe')

        if submit_button:
            voeg_klant_toe(naam, email, telefoonnummer, bedrijf)
            st.success('Klant succesvol toegevoegd!')

    # Toon de huidige klantgegevens
    st.header('Klantgegevens')
    st.dataframe(st.session_state.klantgegevens)

elif pagina == "Dashboard":
    st.title('Dashboard')
    st.write("Hier kun je een overzicht van belangrijke metrics en statistieken zien.")

elif pagina == "Voorraad":
    st.title('Voorraadbeheer')
    st.write("Beheer hier je voorraad en bekijk de beschikbare producten.")

elif pagina == "Contacten":
    st.title('Contacten')
    st.write("Hier kun je contactgegevens beheren en bijhouden.")

