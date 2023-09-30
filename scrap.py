import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Streamlit App Title
st.title("Web Scraping 101")

# Function to scrape data from a URL
def scrape_data(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find and extract data from the HTML (customize this part according to your needs)
        k = soup.findAll('div', attrs={'class':'elementor-text-editor elementor-clearfix'})
        output = []
        for i in k[2:]:
            print(i.text)
            t = " ".join(i.text.split())
            output.append(" ".join(i.text.split()))
            print("----------------------")
        names = []
        roles = []
        descriptions = []
        for i in output:
            if len(i.split()) == 2:
                names.append(i)
            elif '|' in i:
                roles.append(i)

            if len(i)>60:
                descriptions.append(i)

        data = pd.DataFrame(list(zip(names, roles, descriptions)), columns=['Names', 'Roles', 'Descriptions'])

        return data
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return []

# Streamlit User Interface
st.sidebar.header("Settings")

# Input for the URL to scrape
url = st.sidebar.text_input("Enter the URL to scrape:", value="https://servicebyte.com/team/", disabled=True)

# Button to trigger scraping
if st.sidebar.button("Scrape"):
    if url:
        st.info(f"Scraping data from {url}...")
        scraped_data = scrape_data(url)
        st.dataframe(scraped_data)
    else:
        st.warning("Please enter a URL to scrape.")

# Footer
st.sidebar.markdown(
    """
    **Note:** This is a basic web scraping example using BeautifulSoup and Streamlit.
    """
)