import streamlit as st
import openai
import os
apikey = os.environ['API_KEY']
openai.api_key = apikey

#OpenAI APIキーを設定する関数
def setup_openai_api():
    openai.api_key = apikey

#st.title('自分用chatgpt')
def render()->st:
    bg_img = '''
    <style>
    .stApp {
      background-image: url("https://pbs.twimg.com/media/Ew201O2UYAMyJO7?format=jpg&name=large");
      background-size: cover;
      background-repeat: no-repeat;
    }
    </style>
    '''

    return st.markdown(bg_img, unsafe_allow_html=True)
render()
st.markdown('''
<h1 style='font-size: 64px; font-family: serif; text-align: right; margin-top: 84px;'>自分用chatgpt</h1>

<div style='font-size: 12px; width: 28rem; text-align: right; margin: auto 0 auto auto'>2000トークン</div>
''', unsafe_allow_html=True)

# ユーザーの入力を取得する関数
def get_user_input() -> str:
    """
    Streamlitのtext_areaウィジェットで、ユーザーからの入力を取得する。
    """
    return st.text_area("chatGPT-3.5-turboエンジン", value="")


# OpenAIに問い合わせを送信し、応答を取得する関数
def generate_response(system_text: str, user_text: str) -> openai.api_resources.Completion:
    """
    OpenAIのChatCompletion APIを使って、ユーザーの入力に応答する。
    Args:
        system_text (str): システムの名前（例：アシスタントAI）
        user_text (str): ユーザーの入力

    Returns:
        openai.api_resources.Completion: OpenAIから返された応答
    """
    message = [{"role": "system", "content": system_text}, {"role": "user", "content": user_text}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        max_tokens=2000,
        temperature=0,
        stream=True
    )
    return response


# OpenAIから受け取った応答を表示する関数
def display_response(response: openai.api_resources.Completion):
    """
    OpenAIから受け取った応答をStreamlitのウィジェット上に表示する。
    Args:
        response (openai.api_resources.Completion): OpenAIから返された応答
    """
    partial_words = ""
    answer = st.empty()
    for chunk in response:
        if chunk and "delta" in chunk["choices"][0] and "content" in chunk["choices"][0]["delta"]:
            partial_words += chunk["choices"][0]["delta"]["content"]
            answer.write(partial_words)


# アプリケーションのメイン関数
def main():
    setup_openai_api()  # OpenAI APIキーを設定する

    system_text = "アシスタントAI"
    user_text = get_user_input()  # ユーザーの入力を取得する
    is_generate_clicked = st.button("回答")

    if is_generate_clicked:
        response = generate_response(system_text, user_text)  # OpenAIに問い合わせを送信し、応答を取得する
        display_response(response)  # OpenAIから受け取った応答を表示する


if __name__ == "__main__":
    main()