# 👩‍💻 Kevin - an AI Software Engineer

Kevin, an adept AI software engineer, possesses the capability to understand human prompts, deconstruct them into actionable steps, conduct pertinent research, and generate code to accomplish specified goals. Leveraging expansive language models, strategic planning algorithms, and adept web browsing skills, Kevin adeptly crafts software solutions.

His mission is to transform software development practices by offering an AI programmer capable of tackling intricate coding challenges with minimal human intervention. Whether it's crafting new functionalities, rectifying bugs, or initiating projects from inception, Kevin stands ready to provide invaluable assistance.

> **_NOTE:_**  Keivn is a simpler version of the [Cognition AI's Devin](https://www.cognition-labs.com/introducing-devin), partially trying to be an open-source alternative to it. 

![Kevin-Screenshot](https://github.com/MohammedAly22/Kevin/assets/90681796/246ae712-b238-46c8-9064-879e69d49943)

> **_NOTE:_**  Kevins' prompt templates and project structure are inspired by [Devika](https://github.com/stitionai/devika); an actual try to clone Cognition's AI Devin.  

# ⚙️ Installaion & Usage
To install Kevin locally:
### 1️⃣ Clone the repository:
```bash
git clone https://github.com/MohammedAly22/Kevin.git
```
### 2️⃣ Navigate to the kevin directory:
```bash
cd kevin
```
### 3️⃣ Create a virtual environment:
```bash
python -m venv kevin-env
```
### 4️⃣ Activate the virtual environment:
```bash
kevin-env/Scripts/activate  # On Windows
source kevin-env/bin/activate  # On macOS/Linux
```
### 5️⃣ Install the needed packages:
```bash
pip install -r requirements.txt
```
### 6️⃣ Run this streamlit command to start the application:
```bash
streamlit run frontend/main.py
```

# 🛠️ System Design
## 🚀 Kevin Workflow: From Prompt to Production
Kevin functions as an AI-powered software engineer, capable of transforming user prompts into structured, functional codebases. Here's how Kevin's intelligent workflow unfolds:

### 🔧 Step 1: Model Selection & Initialization

The journey begins when the user selects a base model — currently supporting advanced LLMs like `Cohere` and `Gemini-Pro`. After entering a valid `API_KEY`, the user is taken to Kevin’s **workspace dashboard** to kickstart their project.

### 💬 Step 2: Task Inception

Within the workspace, the user submits a task-related prompt, typically a code-related request. This triggers Kevin’s core logic.

### 🧠 Step 3: Decision Making — `DecisionTaker` Agent

Kevin’s `DecisionTaker` agent analyzes the prompt and determines the next course of action:

- For code assistance tasks, it proceeds with planning.
- For general programming questions, it responds directly.
- For unrelated topics, Kevin courteously reminds users of his code-focused expertise.

> 📊 **Diagram Suggestion**: *Kevin's Workflow Decision Tree*  
> *(DecisionTaker → [Code Prompt → Planner] | [Query → Response] | [Other → Reminder])*

### 🗺️ Step 4: Planning — `Planner` Agent

If the task involves code generation, Kevin's `Planner` agent builds a structured, step-by-step plan, which is displayed in the **Kevin Planner** tab. This plan guides the rest of the process.

### 🧾 Step 5: Keyword Extraction

Kevin’s `KeywordExtractor` processes the user’s prompt using:

- **BERT**: Captures the semantic essence of the task.
- **KeyBERT**: Extracts and ranks the most relevant keywords.

These keywords are used to drive intelligent research.

> 📊 **Diagram Suggestion**: *Keyword Extraction Pipeline*  
> *(Prompt → BERT → KeyBERT → Top Keywords)*

### 🔍 Step 6: Research — `Researcher` Agent

Using the extracted keywords, Kevin performs targeted research:

1. Generates smart queries via `googlesearch-python`.
2. Fetches web pages using `requests`.
3. Parses content using `BeautifulSoup`.
4. Outputs results as structured JSON for downstream agents.

> 📊 **Diagram Suggestion**: *Kevin Research Loop*  
> *(Keywords → Queries → Web Pages → Parsed Content → JSON)*

### 💻 Step 7: Code Generation — `Coder` Agent

Kevin’s `Coder` agent writes high-quality code using the plan and research:

- **Structure**: Builds classes, functions, and modules.
- **Implementation**: Fills in the logic using research insights and programming principles.
- **Presentation**: Displays code in the **Kevin Coder** tab.

> 📊 **Diagram Suggestion**: *Code Generation Flow*  
> *(Plan + Research + Prompt → Code Blocks)*

### 🏗️ Step 8: Project Creation — `Project Creator` Agent

The final stage involves organizing and finalizing the project:

- Uses the `os` module to create Python scripts.
- Automatically sets up file and folder structure.
- Ensures everything is ready for execution or collaboration.

> ✅ Kevin’s core philosophy: **"From idea to code."**

---

## 🧠 Kevin Planner

Kevin’s `Planner` is responsible for converting big-picture goals into concrete tasks:

1. **Objective Comprehension** — Interprets the prompt to understand the user's intent.
2. **Step Formulation** — Breaks down the objective into sequential steps.
3. **Execution Coordination** — Delegates steps to relevant agents (e.g., `Researcher`, `Coder`).

---

## 🗝️ Kevin Keyword Extractor

The `KeywordExtractor` streamlines research by isolating meaningful keywords:

- **Contextual Extraction** — Uses BERT to analyze the prompt.
- **Relevance Ranking** — Applies KeyBERT to prioritize the most critical terms.

This allows Kevin to focus his research precisely on what matters.

---

## 🔎 Kevin Researcher

Kevin’s `Researcher` agent supports intelligent knowledge acquisition:

1. Generates search queries based on extracted keywords.
2. Uses `googlesearch-python` to find relevant pages.
3. Fetches content with `requests`.
4. Extracts meaningful data using `BeautifulSoup`.
5. Structures output for the `Coder` to consume.

---

## 🧑‍💻 Kevin Coder

The `Coder` agent transforms plans into functional code:

- Designs a scalable code structure.
- Implements the logic using research and programming knowledge.
- Produces readable, testable, and extensible code.

Supports multiple programming languages and project types.

---

## 🏁 Kevin Project Creator

The `Project Creator` finalizes the development process:

1. Generates a starter script using Python.
2. Sets up file/folder organization.
3. Verifies the completeness of the project environment.

> 🧠 Kevin lives by the motto:  
> **“From idea to code — intelligently, reliably, and fast.”**
