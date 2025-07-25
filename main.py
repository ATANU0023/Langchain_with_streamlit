import langchain_helper as lch
from unittest import case
from numpy import select
import streamlit as st

st.title("Pet Name Generator")

user_animal_type = st.sidebar.selectbox("What is your pet?", ["dog", "cat", "bird", "fish", "hamster"])

if user_animal_type == "dog":
    pet_color = st.sidebar.text_input("What is your dog's color?", max_chars=15)
if user_animal_type == "cat":
    pet_color = st.sidebar.text_input("What is your cat's color?", max_chars=15)
if user_animal_type == "bird":
    pet_color = st.sidebar.text_input("What is your bird's color?", max_chars=15)
if user_animal_type == "fish":
    pet_color = st.sidebar.text_input("What is your fish's color?", max_chars=15)
if user_animal_type == "hamster":
    pet_color = st.sidebar.text_input("What is your hamster's color?", max_chars=15)

if pet_color:
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name'])


st.sidebar.header("Helping Agent")
user_prompt = st.sidebar.text_input(f"Ask me anything related to your pet {user_animal_type}:", "", max_chars=20)
if user_prompt:
    result = lch.langchain_agent(user_prompt, user_animal_type)
    st.text(result)
