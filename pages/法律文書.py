import streamlit as st
import openai
import os
apikey = os.environ['API_KEY']
openai.api_key = apikey

st.title('ムカついたから訴える！！')

#OpenAI APIキーを設定する関数
def setup_openai_api():
    openai.api_key = apikey


# ユーザーの入力を取得する関数
def get_user_input() -> str:
    """
    Streamlitのtext_areaウィジェットで、ユーザーからの入力を取得する。
    """
    return st.text_area("具体的に受けた不利益を書いてください", value="原告：\n 被告：\n 内容：")


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

    system_text = "あなたは有能な弁護士です。1,要件の整理: まず最初に、クライアントからの依頼内容を確認し、必要な情報や証拠の整理を行います。\
    書面の目的や対象者、対象期間なども確認しましょう。2,法的根拠の検討: 次に、法的根拠や判例などを確認し、自身の主張を裏付けるための根拠を見つけます。\
    また、相手方の主張や反論に対しても備えて、反論可能な点を把握しておくことが大切です。3,文書の構成: 文書の構成を決定しましょう。\
    基本的に、書面は「序文・主文・結び」の3つに分かれます。序文では、依頼内容や書面の目的を説明し、主文では、自身の主張や根拠を示します。\
    結びでは、求める結論をまとめ、具体的な要求や措置を記載します。4,表現の決定: 書面の表現についても重要です。法律用語や専門用語を適切に使用し、\
    文章を簡潔かつ明確に表現することが必要です。また、文書の対象者に合わせた表現を用いることも大切です。\
    最後は必ず与えられた入力から裁判所に提出する訴文を出力してください。\
    "
    user_text = get_user_input()  # ユーザーの入力を取得する
    is_generate_clicked = st.button("訴状生成！")

    if is_generate_clicked:
        response = generate_response(system_text, user_text)  # OpenAIに問い合わせを送信し、応答を取得する
        display_response(response)  # OpenAIから受け取った応答を表示する


if __name__ == "__main__":
    main()
    
    
    
"""

```python

#以下ソースコード



import streamlit as st
import openai
import os
from chatgpt_secret import apikey
#openai.api_key = ../apikey

st.title('')

#OpenAI APIキーを設定する関数
def setup_openai_api():
    openai.api_key = apikey


# ユーザーの入力を取得する関数
def get_user_input() -> str:
  
    return st.text_area("具体的に受けた不利益を書いてください", value="原告：\n 被告：\n 内容：")

# OpenAIに問い合わせを送信し、応答を取得する関数
def generate_response(system_text: str, user_text: str) -> openai.api_resources.Completion:
 
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
    partial_words = ""
    answer = st.empty()
    for chunk in response:
        if chunk and "delta" in chunk["choices"][0] and "content" in chunk["choices"][0]["delta"]:
            partial_words += chunk["choices"][0]["delta"]["content"]
            answer.write(partial_words)

# アプリケーションのメイン関数
def main():
    setup_openai_api()  # OpenAI APIキーを設定する

    system_text = "あなたは有能な弁護士です。1,要件の整理: まず最初に、クライアントからの依頼内容を確認し、必要な情報や証拠の整理を行います。
    書面の目的や対象者、対象期間なども確認しましょう。2,法的根拠の検討: 次に、法的根拠や判例などを確認し、自身の主張を裏付けるための根拠を見つけます。
    また、相手方の主張や反論に対しても備えて、反論可能な点を把握しておくことが大切です。3,文書の構成: 文書の構成を決定しましょう。
    基本的に、書面は「序文・主文・結び」の3つに分かれます。序文では、依頼内容や書面の目的を説明し、主文では、自身の主張や根拠を示します。
    結びでは、求める結論をまとめ、具体的な要求や措置を記載します。4,表現の決定: 書面の表現についても重要です。法律用語や専門用語を適切に使用し、
    文章を簡潔かつ明確に表現することが必要です。また、文書の対象者に合わせた表現を用いることも大切です。
    最後は必ず与えられた入力から裁判所に提出する訴文を出力してください。
    "
    user_text = get_user_input()  # ユーザーの入力を取得する
    is_generate_clicked = st.button("訴状生成！")

    if is_generate_clicked:
        response = generate_response(system_text, user_text)  # OpenAIに問い合わせを送信し、応答を取得する
        display_response(response)  # OpenAIから受け取った応答を表示する

if __name__ == "__main__":
    main()
```


"""