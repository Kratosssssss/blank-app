import streamlit as st

st.set_page_config(layout="wide")
st.image("image/banner.png", use_column_width=True)
tab1, tab2, tab3, tab4 = st.tabs(["1.Upload Feedback Data", " 2️⃣ Preprocessing", " Step 3: Intelligent Scoring", "Step 4. Manage Knowledge Base"])


prompt_textbox_css = """
    <style>
    label {
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 24px !important;
        color: black !important;
    }
    textarea {
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 20px !important;
        color: black !important;
        border: 0.75px solid black !important;  /* Add black border */
    }
    subheader {
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 111px !important;
        color: black !important;
    }
    </style>
"""
st.markdown(prompt_textbox_css, unsafe_allow_html=True)
uploaded_file = None
with tab1:

    st.subheader('Upload the Feedback Datasets', divider='blue')
    # File uploader for the user to upload a file
    uploaded_file = st.file_uploader("uploader", type=["csv", "txt", "pdf", "docx"],
                                     label_visibility="hidden")
    if uploaded_file is not None:
        st.success("The Feedback Dataset has been Uploaded.")

with tab2:
    st.subheader('Prompt Engineering for Feedback Preprocessing', divider='blue')

    st.text_area("1. Persona and task",
                 value="You are an intelligent assistant that helps a human analyst to analyze employee feedback against certain topics presented in a text document.",
                 height=100,  key="11")
    st.text_area("2. Language translation",
                 value="Given a text document of employee feedback, you need to summarize and classify by sentiment, topic and intention.",
                 height=100, key="21")
    st.text_area("3. Name entity reconnection", value='''Step 1. Translate
Translate text document into English.

Step 2. 
Scan through the provided text document and replace all entities of real person names with [Employe Name]. A 'real person name' refers to any full name, first name, or last name that unmistakably identifies an individual person. For instance, names like 'John Smith' or 'Angela Merkel' should be replaced with [Employe Name]”. ''',
                 height=100, key="13")
    st.text_area("4. Summarization", value='''Step 3. Summarize 
This step is to carefully identify and extract the key points without leaving out any critical details. The summary should  keep it concise and easy to understand. Some sentences describe a certain topic from different perspectives. Please follow the context, don't simply treat different sentences as different key points. ''',
                 height=100, key="4")
    st.text_area("5. Topic detection",
                 value="Step 4. Conduct sentiment analysis (example: Strongly Negative, Negative, Neutral, Positive, Strongly Positive), topic classification and intention classification for each key points summarized by step 3.",
                 height=100, key="5")
    st.text_area("6. Sentiment detection",
                 value='''Step 5. Conduct topic classification for each key points summarized by step 3. Each topic only contains one word. If one summary could map to two topics, categorize it to most relevant topic.  Consolidate similar topics into one topic, example consolidate topics "Communication", "Improve communication", "Communication and Collaboration" to "Communication"''',
                 height=100, key="6")
    st.text_area("7. Intent detection",
                 value="Step 6. Conduct intention classification for each key points summarized by step 3.", height=100, key="7")
    st.text_area("8. Output Format", value='''
    Only return the final result in JSON list format strictly follows below specification. Begin with '[' and end with ']'. No additional word. 
    [    {   "SUMMARY": "The budget constraints are challenging",
             "TOPIC": "Budget",
             "SENTIMENT": "Negative",
             "INTENTION": "Suggestion"
             },
         {   "SUMMARY": "Insufficient priority towards training workforce in AI",
             "TOPIC": "Training",
             "SENTIMENT": "Negative",
             "INTENTION": "Criticism"
             }
    ]''', height=100, key="8")

    _, left_button_col, right_button_col = st.columns([13, 1, 1])
    with left_button_col:
        st.button("Save", key="index=1")
        # st.success("Settings saved", label_visibility="hidden")
    with right_button_col:
        st.button("Execute", key="index=2")
        # st.success("Executing...", label_visibility="hidden")

with tab3:
    st.subheader('Set Parameters for Intelligent Scoring', divider='blue')

    # Create columns to organize content
    left_column, middle_column, right_column = st.columns(3)

    # Sentiment Section
    with left_column:
        st.markdown("<h2 style='font-size: 24px;'>1. Sentiment</h2>", unsafe_allow_html=True)
        sentiment_weight = st.number_input("Weight", 0, 100, 50, key="1")

        sentiment_options = {"Strong Negative": -2, "Negative": -1, "Neutral": 0, "Positive": 1, "Strong Positive": 2}
        sentiment_values = {}
        for sentiment, value in sentiment_options.items():
            sentiment_values[sentiment] = st.slider(sentiment, -3, 3, value)

    # Intent Section
    with middle_column:
        st.markdown("<h2 style='font-size: 24px;'>2. Intent</h2>", unsafe_allow_html=True)
        intent_weight = st.number_input("Weight", 0, 100, 50, key="2")

        intent_options = {"Suggestion": 5, "Criticism": 4, "Warning": 3, "Observation": 2, "Complaint": 1}
        intent_values = {}
        for intent, value in intent_options.items():
            intent_values[intent] = st.slider(intent, -3, 3, value)

    # Topic Section
    with right_column:
        st.markdown("<h2 style='font-size: 24px;'>3. Topic</h2>", unsafe_allow_html=True)
        topic_weight = st.number_input("Weight", 0, 100, 50, key="3")

        topic_options = {"Budget": 4, "Communication": 4, "Decision Making": 4, "Efficiency": 2, "Automation": 1,
                         "AI": 5,
                         "Change": 3, "Others": 1}
        topic_values = {}
        for topic, value in topic_options.items():
            topic_values[topic] = st.slider(topic, -3, 3, value)

    # Save Button
    _, right_button_col = st.columns([14, 1])
    with right_button_col:
        st.button("Save", key="index=3")

with tab4:
    st.header('Intelligent Feedback Analyzer', divider='blue')
