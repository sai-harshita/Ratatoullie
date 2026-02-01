import streamlit as st

# Call set_page_config() as the first Streamlit command
st.set_page_config(page_title="CheffBot",
                    layout='centered',
                    initial_sidebar_state='collapsed')

# CSS styling
st.markdown(
"""
<style>
    :root{
    --tenne-tawny: #213032;
    --tenne-tawny-dark: #97a2a3;
    --blah: #ffffff
    }
    .stApp {
    margin: auto;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    overflow: auto;
    background: linear-gradient(315deg, #222c2d 3%, #456266 38%, #73a9b0 68%, #222c2d 150%);
    animation: gradient 15s ease infinite;
    background-size: 400% 400%;
    background-attachment: fixed;
}
.stApp > header {
    background-color: transparent;
}
    .stButton button{
    width: 155px;
    height: 60px;
    font-size: 1.8rem;
    background: var(--tenne-tawny);
    color: #fff;
    border: none;
    border-top-right-radius: 2rem;
    border-bottom-right-radius: 2rem;
    transition: all 0.4s linear;
    -webkit-transition: all 0.4s linear;
    -moz-transition: all 0.4s linear;
    -ms-transition: all 0.4s linear;
    -o-transition: all 0.4s linear;
    }
    .stButton button:hover{
    background: var(--tenne-tawny-dark);
    }
    .stTextInput>div>div>input {
        background-color: var(--blah);
        color: var(--tenne-tawny);
    }
    .stSelectbox>div>div>div>div>div>div {
        background-color: var(--tenne-tawny);
        color: var(--tenne-tawny-dark);
    }
</style>
""",
unsafe_allow_html=True)

# Main application code
st.header("ChefBot")

item = st.text_input("Enter the key ingredient")

# Creating four more columns for additional two fields
col1, col2, col3, col4 = st.columns([5, 5, 5, 5])

with col1:
    cusine = st.selectbox('Choose your cuisine',
                          ('Indian', 'Chinese', 'Mexican', 'Italian', 'Continental', 'Japanese', 'Korean', 'French', 'Thai'), index=0)
with col2:
    meal_type = st.selectbox('Choose your Meal Type',
                             ('Breakfast', 'Lunch', 'Snacks', 'Dinner', 'Midnight'), index=0)
with col3:
    preference = st.selectbox('Choose your preference', ('Veg', 'Non Veg', 'Eggitarian', 'Vegan', 'Jain'), index=0)
with col4:
    qty = st.text_input('Enter the number of people you want to cook for: ')

submit = st.button("Generate", key="generate")

# Final response
if submit:
    response = getLLamaresponse(item, cusine, meal_type, preference, qty)
    st.write(response)
