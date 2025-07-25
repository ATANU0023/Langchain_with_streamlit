from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import AgentType
from langchain.agents import initialize_agent

load_dotenv()


def generate_pet_name(animal_type, pet_color):
    llm = ChatGroq(temperature=0.7, model="llama3-8b-8192")
    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} Pet and I want a cool name for it. It is {pet_color} in color. Suggest me five cool names for my pet."
    )
    llm_chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key="pet_name")

    response = llm_chain({'animal_type': animal_type, 'pet_color': pet_color})
   
    response['pet_name'] = response['pet_name'].replace("**", "")
    return response

def langchain_agent(prompt, animal_type):
    llm = ChatGroq(temperature=0.5, model="llama3-8b-8192")
    

    prompt = f"""
    Answer the prompt related to animals: {animal_type}, prompt: {prompt},
    For other type of questions, just answer I can only help you with your Pet.
    """
    
    result = llm.invoke(prompt)
    result.content = result.content.replace("**", "")
    return result.content


if __name__ == "__main__":
    #print(generate_pet_name("dog", "brown"))
    result = langchain_agent("Name few types of dogs", "dog")
    print(result)