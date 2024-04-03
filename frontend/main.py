"""
If you found any errors, regarding file paths, try adding
the Kevin folder in `sys.path`

>>> import sys
>>> sys.path.append("your_path_to/Kevin")
"""


import os
import time
import streamlit as st

from src.agents.decision_taker import DecisionTaker
from src.agents.planner import Planner
from src.agents.researcher import Researcher
from src.agents.coder import Coder
from src.agents.project_creator import ProjectCreator

from src.keyword_extractor import SentenceBert

from utils import stream_text, search_queries, prepare_coding_files


original_working_dir = os.getcwd()


# Loading messages avatars
kevin_avatar = "assets/Kevin_avatar.svg"
mohammed_avatar = "assets/Mohammed_avatar.png"


selected_model = None
google_api_key = None
cohere_api_key = None

# Set page layout
st.set_page_config(layout="wide")

# Set custom CSS styling
with open("frontend/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initalized messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "HI, I am Kevin! how can I help you?"}
    ]


def page_switcher(page):
    st.session_state.runpage = page


def welcome_page():
    with st.container():
        st.title("Welcome, at Kevin!", anchor=False)
        st.write(
            """Jabcob is an advanced AI software engineer that can understand high-level human instructions, break them down into steps, research relevant information, and write code to achieve the given objective. Jabcob utilizes large language models, planning and reasoning algorithms, and web browsing abilities to intelligently develop software. Jabcob aims to revolutionize the way we build software by providing an AI pair programmer who can take on complex coding tasks with minimal human guidance. Whether you need to create a new feature, fix a bug, or develop an entire project from scratch, Jabcob is here to assist you."""
        )
        btn = st.button("Start Now", on_click=page_switcher, args=(configuration_page,))
        if btn:
            st.rerun()


def configuration_page():
    st.title("Configure Some Settings", anchor=False)

    col1, col2 = st.columns(2)

    with col1:
        global selected_model
        selected_model = st.selectbox(
            "Select a model",
            options=["Gemini-Pro", "Cohere"],
            key="selected_model",
        )

    if st.session_state["selected_model"] == "Gemini-Pro":
        global google_api_key
        google_api_key = st.text_input(
            "Google API key",
            placeholder="Enter your Google API key",
            type="password",
        )

    elif st.session_state["selected_model"] == "Cohere":
        global cohere_api_key
        cohere_api_key = st.text_input(
            "Cohere API key",
            placeholder="Enter your Cohere API key",
            type="password",
        )

    with col2:
        project_name = st.text_input(
            "Project name", placeholder="Enter your project name", value="My-Project"
        )

    created = st.button("Create")

    if created:
        if project_name:
            if selected_model == "Cohere":
                if cohere_api_key:
                    os.environ["COHERE_API_KEY"] = cohere_api_key
                    with st.spinner(f"Creating '{project_name}'..."):
                        time.sleep(2)
                        page_switcher(workspace_page)
                        st.rerun()
                else:
                    st.error("Please, enter your Cohere API key!")

            elif selected_model == "Gemini-Pro":
                if google_api_key:
                    os.environ["GOOGLE_API_KEY"] = google_api_key
                    with st.spinner(f"Creating '{project_name}'..."):
                        time.sleep(3)
                        page_switcher(workspace_page)
                        st.rerun()
                else:
                    st.error("Please, enter your Google API key!")

        else:
            st.error("Please, enter your project name!")


def workspace_page():
    api_key = google_api_key if selected_model == "Gemini-Pro" else cohere_api_key

    decision_taker = DecisionTaker(selected_model, api_key)
    planner = Planner(selected_model, api_key)
    reseacher = Researcher(selected_model, api_key)
    coder = Coder(selected_model, api_key)
    project_creator = ProjectCreator(selected_model, api_key)

    # Splitting screen into 2 columns
    col1, col2 = st.columns(2)

    # Kevin Workspace
    with col2:
        workspace = st.container(height=620, border=True)
        with workspace:
            st.title("Kevin Workspace", anchor=False)
            tab1, tab2, tab3, tab4 = st.tabs(
                ["Kevin Planner", "Kevin Browser", "Kevin Coder", "Kevin Project"]
            )

            with tab1:
                planner_area = st.container()

            with tab2:
                browser_area = st.container()

            with tab3:
                coder_area = st.container()

            with tab4:
                project_area = st.container()

    # Kevin Chat
    prompt = st.chat_input(placeholder="Talk to Kevin")
    with col1:
        chat = st.container(height=620, border=True)

        with chat:
            st.title("Kevin Chat", anchor=False)

            # Displaying messages
            for message in st.session_state.messages:
                avatar = mohammed_avatar if message["role"] == "user" else kevin_avatar
                st.chat_message(message["role"], avatar=avatar).write(
                    message["content"]
                )

            # Processing user prompt
            if prompt:
                st.chat_message("user", avatar=mohammed_avatar).write(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})

                with st.spinner("Processing your prompt ..."):
                    response = decision_taker.execute(prompt)[0]

                if response["function"] == "ordinary_conversation":
                    st.chat_message("ai", avatar=kevin_avatar).write_stream(
                        stream_text(response["reply"])
                    )
                    st.session_state.messages.append(
                        {"role": "ai", "content": response["reply"]}
                    )

                elif response["function"] == "coding_project":
                    st.chat_message("ai", avatar=kevin_avatar).write_stream(
                        stream_text("Idenified your request as a `coding_project`! ")
                    )
                    st.session_state.messages.append(
                        {
                            "role": "ai",
                            "content": "Idenified your request as a `coding_project`!",
                        }
                    )
                    time.sleep(0.002)

                    # 1. Generate the plan using `planner`
                    with st.spinner("Generating my plan ..."):
                        generated_plan = planner.execute(prompt)
                        model_reply, planner_json_response = planner.parse_response(
                            generated_plan
                        )

                    project_name = planner_json_response["project"]

                    st.chat_message("ai", avatar=kevin_avatar).write_stream(
                        stream_text(model_reply)
                    )
                    st.session_state.messages.append(
                        {"role": "ai", "content": model_reply}
                    )

                    # Write the generated plan in the Kevin Planner tab
                    with planner_area:
                        plan_and_summary = generated_plan[
                            generated_plan.index("Plan") : -3
                        ]
                        st.write_stream(stream_text(f"Project name: {project_name}"))

                        st.write_stream(
                            stream_text(plan_and_summary.replace("[ ]", ""))
                        )

                    # 2. Calculating the keywords
                    with st.spinner("Identifying keywords of your prompt ..."):
                        keyword_extractor = SentenceBert()
                        keywords = keyword_extractor.extract_keywords(prompt)

                    st.chat_message("ai", avatar=kevin_avatar).write_stream(
                        stream_text(
                            "I correctly identified the relevant keywords in your prompt at `Kevin Browser` tab"
                        )
                    )
                    st.session_state.messages.append(
                        {
                            "role": "ai",
                            "content": "I correctly identified the relevant keywords in your prompt at `Kevin Browser` tab",
                        }
                    )

                    with browser_area:
                        st.write_stream(
                            stream_text(
                                "Identified keywords (ordered from left-to-right based on importance): "
                            )
                        )
                        cols = st.columns(len(keywords))

                        for col, word in zip(cols, keywords):
                            with col:
                                st.success(word)

                    # 3. Call the `researcher`
                    with st.spinner("Generating search queries ..."):
                        reseacher_output = reseacher.execute(plan_and_summary, keywords)

                    st.chat_message("ai", avatar=kevin_avatar).write_stream(
                        stream_text(
                            "I 've just generated contextual search queries. Check the `Kevin Browser` tab"
                        )
                    )
                    st.session_state.messages.append(
                        {
                            "role": "ai",
                            "content": "I 've just generated contextual search queries. Check the `Kevin Browser` tab",
                        }
                    )

                    with browser_area:
                        st.write_stream(stream_text("Researcher prepared queries: "))
                        for i, query in enumerate(reseacher_output["queries"]):
                            st.info(f"Query #{i+1}: {query}")

                    model_reply = f"I am doing my research for the following queries on the web: `{ ', '.join(reseacher_output['queries']) }` "
                    st.chat_message("ai", avatar=kevin_avatar).write_stream(
                        stream_text(model_reply)
                    )
                    st.session_state.messages.append(
                        {"role": "ai", "content": model_reply}
                    )

                    # Get the links from each query using `google_search`
                    with st.spinner("Getting results of the search queries ..."):
                        queries_result = search_queries(reseacher_output["queries"])

                    with browser_area:
                        st.write_stream(stream_text("Queries results: "))
                        st.write(queries_result)

                    model_reply = f"Results of `{', '.join(reseacher_output['queries'])}` retrieved successfully. Check out the `Kevin Browser` tab to take a look."
                    st.chat_message("ai", avatar=kevin_avatar).write_stream(
                        stream_text(model_reply)
                    )
                    st.session_state.messages.append(
                        {"role": "ai", "content": model_reply}
                    )

                    # 4. Using the generated plan, user prompts, and search results for generating code
                    with st.spinner("Generating the code ..."):
                        coder_output = coder.execute(
                            generated_plan[
                                generated_plan.index("Plan") : generated_plan.index(
                                    "Summary"
                                )
                            ],
                            prompt,
                            queries_result,
                        )

                    with st.spinner("Writing code at the `Kevin Coder` tab ..."):
                        with coder_area:
                            for item in coder_output:
                                st.write_stream(
                                    stream_text(f"File name: {item['file']}")
                                )
                                st.write_stream(stream_text(item["code"]))

                    st.chat_message("ai", avatar=kevin_avatar).write_stream(
                        stream_text(
                            f"I finished generating the code for `{project_name}`. Check out the `Kevin Coder` tab"
                        )
                    )
                    st.session_state.messages.append(
                        {
                            "role": "ai",
                            "content": f"I finished generating the code for `{project_name}`. Check out the `Kevin Coder` tab",
                        }
                    )

                    # 5. Creating project directories
                    while True:
                        with st.spinner("Preparing project directories ..."):
                            files = prepare_coding_files(coder_output)
                            project_output = project_creator.execute(
                                project_name, files
                            )

                        with project_area:
                            st.code(project_output["code"], line_numbers=True)
                            try:
                                exec(project_output["code"])
                                st.success(
                                    f"`{project_name}` directory is created successfully!"
                                )
                                os.chdir(original_working_dir)

                                with chat:
                                    st.chat_message(
                                        "ai", avatar=kevin_avatar
                                    ).write_stream(stream_text(project_output["reply"]))
                                    st.session_state.messages.append(
                                        {
                                            "role": "ai",
                                            "content": project_output["reply"],
                                        }
                                    )

                                break

                            except Exception as e:
                                st.error(e)
                                os.chdir(original_working_dir)

                                with chat:
                                    st.chat_message(
                                        "ai", avatar=kevin_avatar
                                    ).write_stream(
                                        stream_text(
                                            "Sorry, I made something wrong, I will try again!"
                                        )
                                    )
                                    st.session_state.messages.append(
                                        {
                                            "role": "ai",
                                            "content": "Sorry, I made something wrong, I will try again!",
                                        }
                                    )
                                    time.sleep(2)


if __name__ == "__main__":
    if "runpage" not in st.session_state:
        st.session_state.runpage = welcome_page
    st.session_state.runpage()
