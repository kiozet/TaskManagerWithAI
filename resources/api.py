from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat


def GeneratingPoints(title_task: str) -> str:
    authorization = "Mjk0MmQ0MmUtNTYyYy00NmY3LTlkYTctYTJhMzIyNmE5MTdhOmJkZTY5ZGE4LTMyZWUtNGNhZC1hNGNmLWIyYTc3NGI4Y2NhMg=="
    print(1)
    giga = GigaChat(
        credentials=authorization, model="GigaChat:latest", verify_ssl_certs=False
    )
    print(2)
    messages = [
        SystemMessage(
            content="Задача - {title_task}"
            "Разбей данную задачу на подпункты."
            "Без примеров."
            "Пиши пункты друг под другом."
            "Используй нумерацию."
        )
    ]
    messages.append(HumanMessage(content=title_task))
    answer = giga(messages)
    messages.append(answer)
    print(answer.content)

    return answer.content
