import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Initialiseren van DataFrames voor klantgegevens, voorraad en contacten
if 'klantgegevens' not in st.session_state:
    st.session_state.klantgegevens = pd.DataFrame(columns=['Naam', 'E-mail', 'Telefoonnummer', 'Bedrijf'])

if 'voorraad' not in st.session_state:
    st.session_state.voorraad = pd.DataFrame(columns=['Productnaam', 'Aantal', 'Prijs', 'Leverancier'])

if 'contacten' not in st.session_state:
    st.session_state.contacten = pd.DataFrame(columns=['Naam', 'E-mail', 'Telefoonnummer', 'Relatie'])

# Functie om een klant toe te voegen aan de DataFrame
def voeg_klant_toe(naam, email, telefoonnummer, bedrijf):
    nieuwe_klant = pd.DataFrame([{
        'Naam': naam,
        'E-mail': email,
        'Telefoonnummer': telefoonnummer,
        'Bedrijf': bedrijf
    }])
    st.session_state.klantgegevens = pd.concat([st.session_state.klantgegevens, nieuwe_klant], ignore_index=True)

# Functie om een product toe te voegen aan de voorraad DataFrame
def voeg_product_toe(productnaam, aantal, prijs, leverancier):
    nieuw_product = pd.DataFrame([{
        'Productnaam': productnaam,
        'Aantal': aantal,
        'Prijs': prijs,
        'Leverancier': leverancier
    }])
    st.session_state.voorraad = pd.concat([st.session_state.voorraad, nieuw_product], ignore_index=True)

# Functie om een contact toe te voegen aan de contacten DataFrame
def voeg_contact_toe(naam, email, telefoonnummer, relatie):
    nieuw_contact = pd.DataFrame([{
        'Naam': naam,
        'E-mail': email,
        'Telefoonnummer': telefoonnummer,
        'Relatie': relatie
    }])
    st.session_state.contacten = pd.concat([st.session_state.contacten, nieuw_contact], ignore_index=True)

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

    # Genereer willekeurige bezoekersgegevens voor de afgelopen 30 dagen
    einddatum = datetime.now()
    startdatum = einddatum - timedelta(days=30)
    datums = pd.date_range(start=startdatum, end=einddatum, freq='D')
    bezoekers = np.random.poisson(lam=100, size=len(datums))
    bezoekers_df = pd.DataFrame({'Datum': datums, 'Bezoekers': bezoekers})

    # Toon de bezoekersgegevens in een grafiek
    st.subheader('Website Bezoekers per Dag')
    fig, ax = plt.subplots()
    ax.plot(bezoekers_df['Datum'], bezoekers_df['Bezoekers'], marker='o')
    ax.set_xlabel('Datum')
    ax.set_ylabel('Aantal Bezoekers')
    ax.set_title('Website Bezoekers per Dag')
    ax.grid(True)
    st.pyplot(fig)

elif pagina == "Voorraad":
    st.title('Voorraadbeheer')

    # Formulier om voorraadgegevens toe te voegen
    with st.form(key='voorraad_formulier'):
        productnaam = st.text_input(label='Productnaam')
        aantal = st.number_input(label='Aantal', min_value=0)
        prijs = st.number_input(label='Prijs', min_value=0.0, format="%.2f")
        leverancier = st.text_input(label='Leverancier')
        submit_button = st.form_submit_button(label='Voeg product toe')

        if submit_button:
            voeg_product_toe(productnaam, aantal, prijs, leverancier)
            st.success('Product succesvol toegevoegd!')

    # Toon de huidige voorraadgegevens
    st.header('Voorraadgegevens')
    st.dataframe(st.session_state.voorraad)

elif pagina == "Contacten":
    st.title('Contacten')

    # Formulier om contactgegevens toe te voegen
    with st.form(key='contacten_formulier'):
        naam = st.text_input(label='Naam')
        email = st.text_input(label='E-mail')
        telefoonnummer = st.text_input(label='Telefoonnummer')
        relatie = st.text_input(label='Relatie')
        submit_button = st.form_submit_button(label='Voeg contact toe')

        if submit_button:
            voeg_contact_toe(naam, email, telefoonnummer, relatie)
            st.success('Contact succesvol toegevoegd!')

    # Toon de huidige contactgegevens
    st.header('Contactgegevens')
    st.dataframe(st.session_state.contacten)
