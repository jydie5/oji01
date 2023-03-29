import streamlit as st
import openai
#import azure.cognitiveservices.speech as speechsdk
apikey = os.environ['API_KEY']
openai.api_key = apikey

def ask_gpt(question, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "\
            あなたは世界最高のアシスタントです。\
            ただし、敬語は一切使わないでください。\
            友達として接してください。\
             "},
            {"role": "user", "content": question}
        ],
        max_tokens=250,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()




st.title('chatgpt_api_test')

with st.form('aaa'):

    #st.text('chatgptに相談するよ')
    user_input = st.text_area(label='Enter your question here',height=100)
    # 送信ボタンの作成
    submitted = st.form_submit_button(label='Submit')

    # 送信ボタンが押されたときの処理
    if submitted:
        user_question = user_input

    st.write("何か悩んでるんだって？。（終了するには 'q' と入力）")

while True:
    user_question = input("あなたの質問: ")
    if user_question.lower() == 'q':
        break

    ai_response = ask_gpt(user_question)
    st.write("AIの回答: ", ai_response)
