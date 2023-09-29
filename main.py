import streamlit as st
import langChain_helper

st.title("Recipe Generator")

# Define food categories
vegetables = ["Carrots", "Potatoes", "Broccoli", "Spinach", "Tomatoes", "Bell peppers"]
fruits = ["Apples", "Bananas", "Oranges", "Strawberries", "Grapes", "Kiwis"]
proteins = ["Chicken breast", "Salmon", "Tofu", "Ground beef", "Eggs", "Lentils"]
grains = ["Rice", "Pasta", "Quinoa", "Oats", "Bread", "Barley"]
dairy = ["Milk", "Cheese", "Yogurt", "Butter", "Cream", "Sour cream"]
baking_supplies = ["Flour", "Sugar", "Baking soda", "Baking powder", "Chocolate chips", "Vanilla extract"]
seafood = ["Shrimp", "Cod", "Crab", "Clams", "Mussels", "Tilapia"]

# Create multiselect widgets for each food category
vegetables_selected = st.sidebar.multiselect('Vegetables', vegetables)
fruits_selected = st.sidebar.multiselect('Fruits', fruits)
proteins_selected = st.sidebar.multiselect('Proteins', proteins)
grains_selected = st.sidebar.multiselect('Grains', grains)
dairy_selected = st.sidebar.multiselect('Dairy', dairy)
baking_supplies_selected = st.sidebar.multiselect('Baking Supplies', baking_supplies)
seafood_selected = st.sidebar.multiselect('Seafood', seafood)

if st.sidebar.button("Generate Recipes"):
    selected_items = (
        vegetables_selected + fruits_selected + proteins_selected + grains_selected +
        dairy_selected + baking_supplies_selected + seafood_selected
    )

    if selected_items:
        response1 = langChain_helper.generate_recipe_names(selected_items)
        recipe_names = [line.strip() for line in response1['recipe_name'].split('\n') if line.strip()]

        if recipe_names:
            # recipe_names_tuple = tuple(recipe_names)
            selected_recipe = st.selectbox(
                'Select a recipe:',
                (recipe_names))
            print(selected_recipe)

            if st.button("View the Recipe"):
                if selected_recipe:
                    response2 = langChain_helper.generate_recipe(selected_recipe)
                    st.title(response2['recipe_name'])
                    st.header("Instructions:")
                    st.markdown(response2['recipe'])