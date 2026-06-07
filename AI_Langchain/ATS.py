from typing import List
from pydantic import BaseModel, Field
from langchain community.documentloaders import TextLoader, PyPDFLoader
from langchain_openai import ChatOpenAI  
from langchain_core.prompts import PromptTemplet  



#--- giving required fields for ATS #---
class ResumeAnalysis(BaseModel):
    skills: List[str] = Field(description='Skills found in the resume')
    missing_skills: List[str] = Field(description='Skills missing compared to job description')
    strengths: List[str] = Field(description='Candidate Strengths')
    weaknesses: List[str] = Field(description='Weaknesses or gaps in the resume')
    resume_score: int = Field(description='ATS score from 0 to 100')
    suggestions: List[str] = Field(description='Suggestions to improve resume')


#---Job description loader #-----------
def load_job_description(path: str):
    loader = TextLoader(path)
    docs = loader. load()
    return docs [0].page_content  

#--- resume loader #-----------
def load_resume(path: str):
    loader = PyPDFLoader(path)
    docs = loader. load()
    return '\n'. join(doc.page_content for doc in docs)  #'\n'.join(...) combines all those strings into one large string, 
                                                         #inserting a newline (\n) between them.

#---Passing Paths #--------

def analyze_resume(resume_path, jd_path):
    resume_content = load_resume(resume_path)
    jd_content = load_job_description(jd_path)

    RESUME_ANALYSIS_PROMPT = """
        You are an ATS (Application Tracking System) used by HR platforms.

        Analysis the resume strickly against the job description.

        Rules:
        - Extract only real skills from the resume and compare with job description
        - Identify missing skills
        - Calculate ATS score between 0 to 100

        Resume: {resume_content}

        Job Description: {jd_content}
    """
    prompt = PromptTemplate. from_template(RESUME_ANALYSIS_PROMPT)

    final_prompt = prompt. format(resume_content=resume_content, jd_content=jd_content)
    print(final_prompt)

    llm = ChatOpenAI(
        model = 'gpt-40-mini',
        temperature=0

    )

    structured_llm = llm.with_structured_output(ResumeAnalysis)

    response = structured_llm. invoke(final_prompt)

    print(response)


 # GIVING FILES NAME 
analyze_resume('resume.pdf', 'job_description. txt')
 