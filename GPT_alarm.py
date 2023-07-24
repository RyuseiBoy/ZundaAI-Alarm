from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)
from voicevox import text_to_voice

def main():
    llm = ChatOpenAI(temperature=0)

    message = input() #ToDoリストを入力,例・水を飲む\n・ランニング\n・朝ごはんを作る

    messages = [
        SystemMessage(content="あなたはAI機能付き目覚まし時計です。ToDoリストが入力されるので、それを見て私を起こすためのメッセージをください。\n語尾を「のだ。」にしてください。\n例:\n入力:・水を飲む\n・ランニング\n・朝ごはんを作る\n出力:\n起きて！朝なのだ。まずは水を飲んで目を覚ますのだ。ランニングして身体を温めるのだ。僕と朝ごはんを食べるのだ！"),
        HumanMessage(content=message)
    ]

    response = llm(messages)
    print(response.content)
    #text_to_voice(response)

if __name__ == '__main__':
    main()