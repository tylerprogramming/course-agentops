#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from story_flow.crews.poem_crew.poem_crew import PoemCrew
import os
from agentops.sdk.decorators import agent, operation, workflow, task
import agentops
from dotenv import load_dotenv

load_dotenv()

AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")
agentops.init(
    api_key=AGENTOPS_API_KEY,
    default_tags=['crewai']
)

class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""

class PoemFlow(Flow[PoemState]):

    @start()
    @task
    def generate_sentence_count(self):
        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)

    @task
    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = (
            PoemCrew()
            .crew()
            .kickoff(inputs={"sentence_count": self.state.sentence_count})
        )

        print("Poem generated1", result.raw)
        self.state.poem = result.raw

    @task
    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)


def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
