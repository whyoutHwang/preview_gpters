from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # API 설정
    api_key = 'patzOfwn0ViSLYPFy.aea5538e09a00a0fb6b5c3aa8bcd5847a417e8d7d751d0daeddc10ace998fea7'  # 여기에 실제 Airtable API 키를 입력하세요.
    base_id = 'app0zMvReNLuI2eYp'
    table_name = 'tblFYQDJ6l4D9yw7n'
    record_id = 'rec3YHu06AtCsNxfg'

    # API URL
    url = f'https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}'

    # API 요청 헤더
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    # API 호출
    response = requests.get(url, headers=headers)

       # 응답 데이터 파싱
    data = response.json()['fields'] if response.status_code == 200 else {}

    # 데이터를 HTML 템플릿에 전달
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
