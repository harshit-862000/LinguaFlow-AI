from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import boto3
from dotenv import load_dotenv
import os

load_dotenv()

aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
region_name = os.getenv("aws_region_name")

# bedrock client
bedrock_client = boto3.client(
    'bedrock-runtime',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Amazon Nova uses ChatBedrock (Messages API format)
model_id = "amazon.nova-lite-v1:0"

llm = ChatBedrock(
    client=bedrock_client, 
    model_id=model_id,
    model_kwargs={
        "temperature": 0.7,
        "max_tokens": 512
    }
)

def my_chatbot(language, user_text):
    # Use ChatPromptTemplate for chat models
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that can speak multiple languages. Please respond to the user in {language}."),
        ("human", "{user_text}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"language": language, "user_text": user_text})
    return response.content

st.title("🌍 Multilingual Chatbot with AWS Bedrock")
st.caption("Powered by Amazon Nova Lite")

language = st.sidebar.selectbox("Select Language", ["English", "Spanish", "French", "German", "Chinese", "Hindi"])

if language:
    user_text = st.sidebar.text_area(label="Enter your message", max_chars=200)

if user_text:
    with st.spinner("🤔 Generating response..."):
        try:
            response = my_chatbot(language, user_text)
            st.success("✨ Chatbot Response:")
            st.write(response)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")