# INITIALIZATION

# LangChain imports
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# general imports
import os
from dotenv import load_dotenv

# load API key from .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# MODEL

llm = OpenAI(temperature=0.6)


# PROMPT MANAGEMENT


def generate_recipe_names(selected_items):
    prompt_template_recipe_name = PromptTemplate(
        input_variables=["ingredients"],
        template="Generate a list of meal names that can be prepared using the provided ingredients. "
        "Ingredients are {ingredients}. "
        "It's not necessary to use all of the ingredients, "
        "and the list can include both simple and complex meal names. "
        "Please consider the ingredients provided and suggest meal names accordingly.",
    )
    recipe_name_chain = LLMChain(
        llm=llm, prompt=prompt_template_recipe_name, output_key="recipe_name"
    )

    chain = SequentialChain(
        chains=[recipe_name_chain],
        input_variables=["ingredients"],
        output_variables=["recipe_name"],
    )
    response = chain({"ingredients": selected_items})

    return response


def generate_recipe(recipe_name):
    prompt_template_recipe = PromptTemplate(
        input_variables=["recipe_name"],
        template="Generate a recipe for {recipe_name}. Please include a list of ingredients and "
        "step-by-step instructions for preparing {recipe_name}. "
        "Please include the cooking time and any special instructions.",
    )
    recipe_chain = LLMChain(llm=llm, prompt=prompt_template_recipe, output_key="recipe")

    chain = SequentialChain(
        chains=[recipe_chain],
        input_variables=["recipe_name"],
        output_variables=["recipe"],
    )
    response = chain({"recipe_name": recipe_name})

    return response
