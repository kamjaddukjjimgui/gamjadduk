ss= input("문자열 입력:")
if ss.isalpha():
    print("글자입니다")
elif ss.isdigit():
    print("숫자입니다")
elif ss.isalnum():
    print("숫자+글자입니다.")
