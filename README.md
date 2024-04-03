# Kevin - an AI Software Engineer

Kevin, an adept AI software engineer, possesses the capability to understand human prompts, deconstruct them into actionable steps, conduct pertinent research, and generate code to accomplish specified goals. Leveraging expansive language models, strategic planning algorithms, and adept web browsing skills, Kevin adeptly crafts software solutions.

His mission is to transform software development practices by offering an AI programmer capable of tackling intricate coding challenges with minimal human intervention. Whether it's crafting new functionalities, rectifying bugs, or initiating projects from inception, Kevin stands ready to provide invaluable assistance.

> **_NOTE:_**  Keivn is a simpler version of the Cognition AI's Devin, partially trying to be an open-source alternative of it. 

![Kevin-Screenshot](https://github.com/MohammedAly22/Kevin/assets/90681796/246ae712-b238-46c8-9064-879e69d49943)


# Installaion & Usage
To install Kevin locally:
1. Clone the repository:
```
git clone https://github.com/MohammedAly22/Kevin.git
```
2. Navigate to the kevin directory:
```
cd kevin
```
3. Create a virtual environment:
```
python -m venv kevin
```
4. Activate the virtual environment:
```
kevin/Scripts/activate
```
5. Install the needed packages:
```
pip install -r requirements.txt
```
6. Run this streamlit command to start the application:
```
streamlit run frontend/main.py
```

# Key Features
-  Highly advanced AI for planning and logical thinking
-  Extracting specific keywords for targeted research
-  Smooth internet surfing and data collection
-  Writing code in various programming languages
-  Tracking and visualizing agent states dynamically
-  Chat interface for conversational interaction
-  Organizing and managing projects systematically
-  Flexible architecture allowing for feature and integration expansion

# System Design
## Kevin Workflow
Kevin's workflow entails several steps. Firstly, the user selects a base model, currently limited to options such as `Cohere` and `Gemini-Pro`, and provides the corresponding `API_KEY`. Subsequently, the user is directed to Kevin's workspace page where they input a prompt related to a code-assistance task. This prompt is then processed by Kevin's `DecisionTaker` agent, which determines the appropriate course of action. 

In scenarios involving ordinary conversation, Kevin responds to code-related queries with pertinent answers; otherwise, users are reminded that Kevin specializes in assisting with code-related inquiries as an AI software engineer.

For coding projects, Kevin initiates by generating a step-by-step plan using its `Planner` agent, visually presented in the Kevin Planner tab. The prompt's keywords are extracted utilizing the `KeywordExtractor`, then utilized by Kevin's `Researcher` agent to formulate search queries, expanding its knowledge base. Subsequently, Kevin conducts internet searches based on these queries, presenting the retrieved results in JSON format within the Kevin Browser tab. The `Coder` agent then utilizes the step-by-step plan and acquired information to write code in the Kevin Coder tab. Finally, Kevin's `Project Creator` agent generates and executes Python code to create and organize project directories and files.

## Kevin Planner


## Kevin Keywords Extractor

## Kevin Researcher

## Kevin Coder

## Kevin Project Creator

# Conclusion
