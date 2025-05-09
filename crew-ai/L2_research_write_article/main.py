from dotenv import load_dotenv
from crew import ResearchCrew

def run():
    inputs = {
        'topic': 'Artificial Intelligence'
    }
    crew = ResearchCrew().crew()
    result = crew.kickoff(inputs=inputs)
    print(result)

if __name__ == '__main__':
    print("Start")
    load_dotenv(override=True)
    run()
    print("Done")