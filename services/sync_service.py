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


def make_db_session():
    global session
    try:
        engine = create_engine(os.getenv("DB_URI"))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception as e:
        print(e)

def make_chroma_session():
    global chromadb_instance
    try:
        chromadb_instance = chromadb.PersistentClient(path=os.getenv("CHROMA_DB_PATH"))

    except Exception as e:
        print(e)



# table for mails in the database
class Mail(Base):
    __tablename__ = 'mail'

    message_id = Column(String, primary_key=True)
    thread_id = Column(String)
    sender = Column(String)
    recipient = Column(String)
    subject = Column(String)
    date = Column(String)
    message = Column(String)

    def __repr__(self):
        return f"<Mail(message_id={self.message_id}, sender={self.sender}, recipient={self.recipient}, subject={self.subject}, date={self.date})>\n\n"

class Event(Base):
    __tablename__ = 'event'

    event_id = Column(Integer, primary_key=True)
    event_name = Column(String)
    event_date = Column(String)
    event_time = Column(String)
    event_venue = Column(String)
    sender = Column(String)
    
    def __repr__(self):
        return f"<Event(event_name={self.event_name}, event_date={self.event_date}, event_time={self.event_time}, event_venue={self.event_venue})>"
    
def add_to_db(emails):
    ic(emails)
    ret = []
    for email in emails:
        mail = Mail(
            message_id=email.id,
            thread_id=email.thread_id,
            sender=email.sender,
            recipient=email.recipient,
            subject=email.subject,
            date=email.date,
            message=email.plain,
            # labels=str(email.labels)
        )
        ret.append(mail)
        session.add(mail)
        session.commit()
    return ret

def add_event_to_db(event):
    print(event)
    event = Event(
        event_name=event["event_name"],
        event_date=event["event_date"],
        event_time=event["event_time"],
        event_venue=event["event_venue"],
        sender=event["sender"]
    )
    session.add(event)
    session.commit()
#get lastest added record to the database
