try:
    f = open('./Data/readme.txt', mode='r', encoding='utf-8') #  텍스트 파일 오픈
    f2 = open('./Data/writeme.txt',mode='w', encoding='utf-8')

    line = f.read() # read 사용시 한줄 띄움 없어지고, readline 한줄 띄움
    while line:
        print(line)
        f2.write(line)
        line = f.read()

    f2.write("추가 내용입니다.")
    f.close() # 파일 닫기
    f2.close()

    print('파일 작성완료')

except FileNotFoundError as e:
    print('예외발생 : {0}'.format(e))


