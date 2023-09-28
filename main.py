import streamlit as st
import langChain_helper

st.title("Recipe Genertor")


vegetables = st.sidebar.multiselect(
    'vegetables',
    ["Carrots", "Potatoes", "Broccoli", "Spinach", "Tomatoes", "Bell peppers"])
fruits = st.sidebar.multiselect(
    'fruits',
    ["Apples", "Bananas", "Oranges", "Strawberries", "Grapes", "Kiwis"])
proteins = st.sidebar.multiselect(
    'proteins',
    ["Chicken breast", "Salmon", "Tofu", "Ground beef", "Eggs", "Lentils"])
grains = st.sidebar.multiselect(
    'grains',
    ["Rice", "Pasta", "Quinoa", "Oats", "Bread", "Barley"])
dairy = st.sidebar.multiselect(
    'dairy',
    ["Milk", "Cheese", "Yogurt", "Butter", "Cream", "Sour cream"])
baking_supplies = st.sidebar.multiselect(
    'baking_supplies',
    ["Flour", "Sugar", "Baking soda", "Baking powder", "Chocolate chips", "Vanilla extract"])
seafood = st.sidebar.multiselect(
    'seafood',
    ["Shrimp", "Cod", "Crab", "Clams", "Mussels", "Tilapia"])

selected_items = vegetables + fruits + proteins + grains + dairy + baking_supplies + seafood


if selected_items:
    response1 = langChain_helper.generate_recipe_names(selected_items)
    recipe_names = response1['recipe_name'].strip().split(',')
    recipe_name = st.multiselect(
        'Select a meal :',
        recipe_names)

    response2 = langChain_helper.generate_recipe(recipe_name)
    st.write(response2)
    # menu_items = response['menu_items'].strip().split(',')


    # for item in menu_items:
    #     st.write("-",item)
