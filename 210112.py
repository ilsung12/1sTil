# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

# 외부 설치 패키지 테스트


import simplejson as json

test_dict = {'1': 95, '4': 77, '3:': 65, '5': 100, '2': 88}

# simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=15 * ' '))  # indent = 들여쓰기 함수


# 가상환경 실행/해제 -> acrivate, deactivate
# pip -m install -----
# pip list
# simplejson - 패키지 -> 설치가 잘안되어서 자꾸 에러가 남
# Pip 업데이트, 경로 설정? 으로 해결함 (구글링으로 해결....; simplejson 의존성)

# 느낀점 : 구글링을 잘 이용하면 안되는것도 해결이 가능하다라는걸 다시한번 느끼게 됨
