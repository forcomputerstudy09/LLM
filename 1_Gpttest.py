import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.getenv("API_KEY")
)

# temperature : 출력의 무작위성(창의성). 얜 범위가 0.0 <= x < 1.0
# 값이 낮을수록 결정론적 (늘 비슷한 값이 나오도록 해주겠다. 라는 뜻.), 값이 높을수록 무작위성.(1에 가까울수록 창의적인 텍스트가 나오는것.)
# 0.0: 항상 같은 입력 -> 같은 출력 (언제 쓰냐: 답, 수학, 정답형 질문)
# 0.x: 적당한 무작위성 (언제 쓰냐: 마케팅 문구, 스토리 작성)

# "role": "user" : 난 바로 질문을 할거다 라는 것. 시스템 가스라이팅 없이 일단 질문만 해볼게.
# "content": "왜 강남은 강남이라고 할까요?" -> 유저가 이제 뭐라고 질문을 했는지.

response = client.chat.completions.create(
    model =  "gpt-4.1-2025-04-14",
    messages = [
        {"role": "user", "content": "왜 강남은 강남이라고 할까요?"}
    ], temperature = 0.0
)
# print(response)
print(response.choices[0].message.content)