import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

@CrewBase
class ResearchCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            # model="gpt-4o-mini",
            model="gpt-3.5-turbo",
            # max_rpm=1
        )

    @agent
    def planner_agent(self) -> Agent:
        print(self.agents_config['planner_agent']['role'])
        return Agent(
            config = self.agents_config['planner_agent'],
            llm = self.llm
        )

    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['writer_agent'],
            llm = self.llm
        )

    @agent
    def editor_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['editor_agent'],
            llm = self.llm
        )

    @task
    def plan_task(self) -> Task:
        return Task(
            config = self.tasks_config['plan_task'],
            agent = self.planner_agent()
        )

    @task
    def write_task(self) -> Task:
        return Task(
            config = self.tasks_config['write_task'],
            agent = self.writer_agent()
        )

    @task
    def edit_task(self) -> Task:
        return Task(
            config = self.tasks_config['edit_task'],
            agent = self.editor_agent()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True
        )

    