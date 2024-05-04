import base64
import requests
import uuid
import json


client_id = '2942d42e-562c-46f7-9da7-a2a3226a917a'
secret = 'bde69da8-32ee-4cad-a4cf-b2a774b8cca2'
authorization = 'Mjk0MmQ0MmUtNTYyYy00NmY3LTlkYTctYTJhMzIyNmE5MTdhOmJkZTY5ZGE4LTMyZWUtNGNhZC1hNGNmLWIyYTc3NGI4Y2NhMg=='

#authorization = кодированный и далее декодированный client_id and secret
#credentials = f"{client_id}:{secret}"
#encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
#print(encoded_credentials == authorization)

def get_token(authotization_token, scope='GIGACHAT_API_PERS'):
    
    #создаем индетификатор uuid (36 знаков)
    rq_uid = str(uuid.uuid4())

    #api url
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
  
    #заголовки
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rq_uid,
        'Authorization': 'Basic Mjk0MmQ0MmUtNTYyYy00NmY3LTlkYTctYTJhMzIyNmE5MTdhOmJkZTY5ZGE4LTMyZWUtNGNhZC1hNGNmLWIyYTc3NGI4Y2NhMg=='
    }

    #тело запроса
    payload = {
        'scope': scope
    }

    try:
        #делаем post запрос с отключенной ssl верификацией
        response = requests.post(url, headers=headers, data=payload, verify=False)
        return response
    except requests.RequestException as e:
        print(f"Ошибка: {str(e)}")
        return -1

response = get_token(authorization)
if response != 1:
  #print(response.text)
  giga_token = response.json()['access_token']
     

def get_chat_comlition(authotization_token, user_massage):
        
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    #подготовка данных в формате json
    payload = json.dumps({
        "model": "GigaChat", 
        "messages": [
            {
            "role": "system",
            "content": "Разбей данную задачу на под пункты"
            },
            {
                "role": "user",  #роль отправителя
                "content": user_massage #сообщение
            }
        ],
        "temperature": 1,  #температура генерации
        "top_p": 0.1,  #параметр top_p для контроля разнообразия ответов
        "n": 1,  #количество возвращаемых ответов
        "stream": False,  #потоковая ли передача ответов
        "max_tokens": 512,  #максимальное количество токенов в ответе
        "repetition_penalty": 1,  #штраф за повторения
        "update_interval": 0  #интервал обновления (для потоковой передачи)
    })  

    #заголовки
    headers = {
        'Content-Type': 'application/json',  #тип содержимого - JSON
        'Accept': 'application/json',  #принимаем ответ в формате JSON
        'Authorization': f'Bearer {authotization_token}'  #токен авторизации
    }

    #выполнение POST-запроса и возвращение ответа
    try:
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        return response
    except requests.RequestException as e:
        print(f"Произошла ошибка: {str(e)}")
        return -1
    
user_massage = input()

answer = get_chat_comlition(giga_token, user_massage)

answer.json() 

print(answer.json()['choices'][0]['message']['content'])
