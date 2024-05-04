from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat


authorization = 'Mjk0MmQ0MmUtNTYyYy00NmY3LTlkYTctYTJhMzIyNmE5MTdhOmJkZTY5ZGE4LTMyZWUtNGNhZC1hNGNmLWIyYTc3NGI4Y2NhMg=='

giga = GigaChat(credentials=authorization,
                model='GigaChat:latest',
                verify_ssl_certs=False
                )

messages = [SystemMessage(content= "Задача - {title_task}"
                                "Разбей данную задачу на подпункты."
                                "Без примеров."
                                "Пиши пункты друг под другом."
                                "Используй нумерацию."
                         )
            ]

while(True):
    title_task = input()
    
    messages.append(HumanMessage(content=title_task))
    answer = giga(messages)
    messages.append(answer)

    print(answer.content)

