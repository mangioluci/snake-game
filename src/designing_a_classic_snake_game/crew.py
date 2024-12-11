from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import Pygame
from crewai_tools import Python

@CrewBase
class DesigningAClassicSnakeGameCrew():
    """DesigningAClassicSnakeGame crew"""

    @agent
    def game_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['game_designer'],
            
        )

    @agent
    def game_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['game_developer'],
            
        )


    @task
    def design_game_layout_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_game_layout_task'],
            tools=[],
        )

    @task
    def implement_game_logic_task(self) -> Task:
        return Task(
            config=self.tasks_config['implement_game_logic_task'],
            tools=[],
        )

    @task
    def create_game_controls_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_game_controls_task'],
            tools=[Pygame()],
        )

    @task
    def add_scoring_system_task(self) -> Task:
        return Task(
            config=self.tasks_config['add_scoring_system_task'],
            tools=[Python()],
        )

    @task
    def test_game_functionality_task(self) -> Task:
        return Task(
            config=self.tasks_config['test_game_functionality_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the DesigningAClassicSnakeGame crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
