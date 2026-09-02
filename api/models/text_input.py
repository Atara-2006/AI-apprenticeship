from pydantic import BaseModel, validator

class TextInput(BaseModel):
    text: str

    @validator("text")
    def text_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("text cannot be empty")
        return v
