from pydantic import BaseModel, Field


class EmailWriter(BaseModel):
    email_title: str = Field(description="The title of the email")
    email_body: str = Field(description="The body of the email")
    closing_line: str = Field(description="The closing line of the email")
    opening_line: str = Field(description="The opening line of the email")
    content_type: str = Field(description="The content type of the email")
    contains_placeholders: bool = Field(
        description="Whether the email contains placeholders for personalization"
    )
    contains_quote: bool = Field(description="Whether the email contains quote or not")
    direct_quote: str = Field(description="The direct quote from the email")


print(EmailWriter.model_json_schema())
