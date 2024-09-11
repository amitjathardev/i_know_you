from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

#from langchain_ollama import ChatOllama

def ice_break_with(name: str):
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock=True)

    summary_template = '''
            given the LinkedIn information {information} about a person from i want you to create:
            1. a short summary
            2. two interesting facts about them
        '''

    summary_prompt_template = PromptTemplate(input_variable="information", template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://gist.githubusercontent.com/amitjathardev/9fe9609598cf215bfd96f4731260c087/raw/77d05be4916fe8733d0935ac63b9149d7f4114c1/amitjathar-dev.jason",mock=True
    )
    res = chain.invoke(input={"information": linkedin_data})

    print(res)




if __name__ == '__main__':
    load_dotenv()
    print("Ice Breaker Enter")
    ice_break_with(name="Amit Jathar Opentext")


    # llm = ChatOllama(model="llama3.1")
    # llm = ChatOllama(model="mistral")

