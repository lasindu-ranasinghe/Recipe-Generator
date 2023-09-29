# IMPORTS

import streamlit as st
import langChain_helper


# PAGE SETUP

# Page name, favicon and layout
st.set_page_config(
    page_title="Recipe Generator", page_icon=":man_cook:", layout="centered"
)

# Set main title for page
st.title("👨‍🍳 Recipe Generator")

# Define food categories
vegetables = ["Carrots", "Potatoes", "Broccoli", "Spinach", "Tomatoes", "Bell peppers"]
fruits = ["Apples", "Bananas", "Oranges", "Strawberries", "Grapes", "Kiwis"]
proteins = ["Chicken breast", "Salmon", "Tofu", "Ground beef", "Eggs", "Lentils"]
grains = ["Rice", "Pasta", "Quinoa", "Oats", "Bread", "Barley"]
dairy = ["Milk", "Cheese", "Yogurt", "Butter", "Cream", "Sour cream"]
baking_supplies = [
    "Flour",
    "Sugar",
    "Baking soda",
    "Baking powder",
    "Chocolate chips",
    "Vanilla extract",
]
seafood = ["Shrimp", "Cod", "Crab", "Clams", "Mussels", "Tilapia"]

# Create multiselect widgets for each food category
vegetables_selected = st.sidebar.multiselect("Vegetables", vegetables)
fruits_selected = st.sidebar.multiselect("Fruits", fruits)
proteins_selected = st.sidebar.multiselect("Proteins", proteins)
grains_selected = st.sidebar.multiselect("Grains", grains)
dairy_selected = st.sidebar.multiselect("Dairy", dairy)
baking_supplies_selected = st.sidebar.multiselect("Baking Supplies", baking_supplies)
seafood_selected = st.sidebar.multiselect("Seafood", seafood)


# INTERACTION WITH THE PAGE

# When "Generate Recipes" button is clicked...
if st.sidebar.button("Generate Recipes"):
    selected_items = (
        vegetables_selected
        + fruits_selected
        + proteins_selected
        + grains_selected
        + dairy_selected
        + baking_supplies_selected
        + seafood_selected
    )
    print(f"selected_items: {selected_items}")

    # Get list of recipe names from the LLM
    recipe_names = langChain_helper.generate_recipe_names(selected_items)

    # Convert LLM response to Python list
    recipe_names = [
        line.strip() for line in recipe_names["recipe_name"].split("\n") if line.strip()
    ]
    print(f"recipe_names: {recipe_names}")

    # Store the recipe names in session_state
    st.session_state.recipe_names = recipe_names


# If a list of recipes has been generated (and is stored in session_state)...
if hasattr(st.session_state, "recipe_names"):
    selected_recipe = st.selectbox("Select a recipe:", st.session_state.recipe_names)

    # When "View the Recipe" button is clicked...
    if st.button("View the Recipe"):
        # Get recipe from LLM
        recipe = langChain_helper.generate_recipe(selected_recipe)

        # Render recipe on page
        st.title(recipe["recipe_name"])
        st.header("Instructions:")
        st.markdown(recipe["recipe"])
