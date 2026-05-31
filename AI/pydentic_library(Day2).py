# Pydantic is a python library that verifies if our data matches exactly with the defined format.

from pydantic import BaseModel, Field      # Field is for description purpose , in that description llm will follow that format 

from typing import List

class User(BaseModel):
name: str
age: int
email: str

user = User(name='Manoj', age='Thirty', email = 'manoj@digitaledify.ai')

print(user.age)



# with_structured_output: It's a langchain feature that forces an llm to return response in a fixed structure instead of free text.

# Requirement - Review Analyzer

class ReviewAnalysis(BaseModel):
    sentiment: str = Field(description='Overall sentiment of the review')

    positive_points: List[str] = Field(description='Postive aspects mentioned')
    
    negative_points: List[str] = Field(description='Negative aspects mentioned')

    rating: int = Field(description='Overall rating from 1 to 5')

template = """
        You are a AI system analyzer, who analyze customer reviews

        Rules:
        - Identify overall sentiment (Positive, neutral or negative)
        - Extract clear positive and negative points.
        - Assign a rating from 1 (worst) to 5 (best)
        """

Customer review: {review}

prompt = PromptTemplate. from_template(template)

final_prompt = prompt. format(review = "I loved the new coffee shop! The ambience was amazing, coffee was rich, but service was slow.")

structured_llm = llm.with_structured_output(ReviewAnalysis)

response = structured_llm. invoke(final_prompt)

print(response.model_dump())