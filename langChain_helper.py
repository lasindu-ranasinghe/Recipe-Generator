from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secrete_key import openai_key
import os
os.environ['OPENAI_API_KEY'] = openai_key

llm = OpenAI(temperature=0.6)

def generate_recipe_names(selected_items):
    # prompt_template_recipe = PromptTemplate(
    #     input_variables=['ingredients'],
    #     template="Generate a popular recipe that includes ingredients from {ingredients}. "
    #              "Feel free to use any of these ingredients and be creative with the cooking instructions. "
    #              "It can be as simple or as complex as you like. "
    #              "Please include the cooking time and any special instructions."
    # )
    # recipe_chain = LLMChain(llm=llm, prompt=prompt_template_recipe, output_key='recipe')

    prompt_template_recipe_name = PromptTemplate(
        input_variables=['ingredients'],
        template="Please provide popular meal names that include ingredients from {ingredients}. "
                 "I need only meal names "

    )
    recipe_name_chain = LLMChain(llm=llm, prompt=prompt_template_recipe_name, output_key='recipe_name')

    # prompt_template_recipe = PromptTemplate(
    #     input_variables=['recipe_name'],
    #     template="Generate a recipe for {recipe_name}. Please include a list of ingredients and "
    #              "step-by-step instructions for preparing {recipe_name}."
    #              "Please include the cooking time and any special instructions."
    # )
    # recipe_chain = LLMChain(llm=llm, prompt=prompt_template_recipe, output_key='recipe')

    chain = SequentialChain(
        chains=[recipe_name_chain],
        input_variables=['ingredients'],
        output_variables=['recipe_name']
    )
    response = chain({'ingredients': selected_items})

    # chain = SequentialChain(
    #     chains=[recipe_chain],
    #     input_variables=['ingredients'],
    #     output_variables=['recipe']
    # )
    # response = chain({'ingredients': selected_items})

    return response


def generate_recipe(recipe_name):
    prompt_template_recipe = PromptTemplate(
        input_variables=['recipe_name'],
        template="Generate a recipe for {recipe_name}. Please include a list of ingredients and "
                 "step-by-step instructions for preparing {recipe_name}."
                 "Please include the cooking time and any special instructions."
    )
    recipe_chain = LLMChain(llm=llm, prompt=prompt_template_recipe, output_key='recipe')

    chain = SequentialChain(
        chains=[recipe_chain],
        input_variables=['recipe_name'],
        output_variables=['recipe']
    )
    response = chain({'recipe_name': recipe_name})

    return response




# if __name__ == "__main__":
#     print(generate_resturant_name_and_items("Sri Lankan"))
