import pandas as pd
import openai

# 데이터셋 불러오기
data = pd.read_csv("twcs.csv")

# 데이터 전처리
tweets = data[data['inbound'] & data['response_tweet_id'].isnull()]  # 고객의 문의만 추출

# OpenAI API 설정
api_key = "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"  # API 키를 입력하세요
openai.api_key = api_key


def generate_response(prompt):
    result = openai.Completion.create(
        engine="text-davinci-002",  # 올바른 엔진 이름으로 수정되었습니다!
        prompt=prompt,
        max_tokens=50,  # 응답 길이 조절
        n=1,
        temperature=0.8
    )
    return result.choices[0].text.strip()


# 사용자 인터페이스
while True:
    user_prompt = input("고객 문의를 입력해주세요 (종료하려면 'q'를 입력해주세요): ")

    if user_prompt.lower() == 'q':
        break

    prompt = f"{user_prompt}\nWrite the best possible response:"
    response = generate_response(prompt)

    print(f"\n응답: {response}\n")
