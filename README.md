# Kevin - an AI Software Engineer

Kevin, an adept AI software engineer, possesses the capability to understand human prompts, deconstruct them into actionable steps, conduct pertinent research, and generate code to accomplish specified goals. Leveraging expansive language models, strategic planning algorithms, and adept web browsing skills, Kevin adeptly crafts software solutions.

His mission is to transform software development practices by offering an AI programmer capable of tackling intricate coding challenges with minimal human intervention. Whether it's crafting new functionalities, rectifying bugs, or initiating projects from inception, Kevin stands ready to provide invaluable assistance.

> **_NOTE:_**  Keivn is a simpler version of the [Cognition AI's Devin](https://www.cognition-labs.com/introducing-devin), partially trying to be an open-source alternative to it. 

![Kevin-Screenshot](https://github.com/MohammedAly22/Kevin/assets/90681796/246ae712-b238-46c8-9064-879e69d49943)

> **_NOTE:_**  Kevins' prompt templates and project structure are inspired by [Devika](https://github.com/stitionai/devika); an actual try to clone Cognition's AI Devin.  

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

# System Design
## Kevin Workflow
Kevin's workflow entails several steps. Firstly, the user selects a base model, currently limited to options such as `Cohere` and `Gemini-Pro`, and provides the corresponding `API_KEY`. Subsequently, the user is directed to Kevin's workspace page where they input a prompt related to a code-assistance task. This prompt is then processed by Kevin's `DecisionTaker` agent, which determines the appropriate course of action. 

In scenarios involving ordinary conversation, Kevin responds to code-related queries with pertinent answers; otherwise, users are reminded that Kevin specializes in assisting with code-related inquiries as an AI software engineer.

For coding projects, Kevin initiates by generating a step-by-step plan using its `Planner` agent, visually presented in the Kevin Planner tab. The prompt's keywords are extracted utilizing the `KeywordExtractor`, then utilized by Kevin's `Researcher` agent to formulate search queries, expanding its knowledge base. Subsequently, Kevin conducts internet searches based on these queries, presenting the retrieved results in JSON format within the Kevin Browser tab. The `Coder` agent then utilizes the step-by-step plan and acquired information to write code in the Kevin Coder tab. Finally, Kevin's `Project Creator` agent generates and executes Python code to create and organize project directories and files.

## Kevin Planner
Kevin employs sophisticated AI planning to dissect overarching goals into manageable actions. The planning process comprises the following stages:

1. Objective Comprehension: Kevin scrutinizes the provided goal or task description to grasp the user's intentions and needs.
2. Step Formulation: Drawing from the objective and context, Kevin devises a series of broad steps to achieve the task.
3. Implementation: Kevin carries out each step in the plan, utilizing diverse sub-components and modules as required.

## Kevin Keywords Extractor
To streamline focused research and data collection, Kevin utilizes keyword extraction methodologies. This process encompasses the following stages:

1. Keyword Extraction: Kevin employs the BERT (Bidirectional Encoder Representations from Transformers) model to discern crucial keywords and phrases from the preprocessed text. BERT's extensive pre-training enables it to grasp semantic nuances and comprehend the significance of words within the given context.
2. Utilizing keywords: the `KeyBert` model is used to extract the keywords and rank them based on their relevance to the user's prompt. 

By pinpointing contextually significant keywords, Kevin can channel his research endeavors effectively, retrieving pertinent information to aid in task completion.

## Kevin Researcher
To generate helpful search queries, Kevin does the following:
1. Utilize Contextual Keywords: Kevin considers contextual keywords previously generated from the user's prompt.
2. Generate Search Queries: Based on the contextual keywords, Kevin creates helpful search queries that can be later used with the `googlesearch-python` library.
3. Retrieve Web Page Content: Kevin employs the `requests` module to fetch the web pages corresponding to the generated search queries.
4. Extract Content: Using the `beautifulsoup` library, Kevin extracts the content from the retrieved web pages for further processing.

## Kevin Coder
Kevin's code generation module crafts code based on the outlined plan, research insights, and user specifications. This process encompasses the following stages:

1. Code Structure Creation: Drawing from the plan and language-specific conventions, Kevin constructs the foundational structure of the code, encompassing classes, functions, and modules.
2. Code Implementation: Kevin populates the code structure with pertinent logic, algorithms, and data manipulation instructions. It utilizes research findings, snippets from the knowledge repository, and its comprehension of programming principles to produce coherent code.

Kevin's proficiency in code generation empowers him to produce functional and optimized code across various programming languages, tailored to each project's specific demands and nuances.

## Kevin Project Creator
1. Script Generation: Following code generation, Kevin initiates the creation of a Python script utilizing the os module.
2. Project File Organization: Kevin begins organizing the project files and folders generated previously during the coding phase of the project.
3. Ensuring Completeness: Throughout the process, Kevin ensures the completeness of the project, aligning with its slogan: "from idea to code".
