from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secrete_key import openai_key
import os
os.environ['OPENAI_API_KEY'] = openai_key

llm = OpenAI(temperature=0.6)

def generate_resturant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['name'],
        template="Give me a fancy name for a {name} resturant."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='resturant_name')

    prompt_template_items = PromptTemplate(
        input_variables=['resturant_name'],
        template="Give me some menu items for {resturant_name}. Return it as comma seperated list"
    )
    food_item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=['name'],
        output_variables=['resturant_name', 'menu_items']
    )
    response = chain({'name': cuisine})

    return response

if __name__ == "__main__":
    print(generate_resturant_name_and_items("Sri Lankan"))
