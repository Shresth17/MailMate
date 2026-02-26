import os
import uuid
import json
import time, re
from icecream import ic

from simplegmail import Gmail
import sqlalchemy
from simplegmail.query import construct_query
from simplegmail import label
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain_openai import OpenAI, ChatOpenAI
from langchain.schema import HumanMessage
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
from  constants import *

from langchain_core.prompts import PromptTemplate

# from langchain.embeddings import Embeddings

from dotenv import load_dotenv

Base = sqlalchemy.orm.declarative_base()

def load_env():
    load_dotenv("../.env")

load_env()

# global variables
session = None
chromadb_instance = None
embeddings = OpenAIEmbeddings()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
valueble_prompt = PromptTemplate(input_variables=["mail_chunk"],template=IS_VALUABLE_PROMPT)


