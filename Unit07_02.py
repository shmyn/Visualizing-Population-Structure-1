import matplotlib.pyplot as plt
import csv
plt.rc('font', family = 'Malgun Gothic')

f = open('age.csv')
data = csv.reader(f)

ans = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요. : ')
result = []

for row in data:
    if ans in row[0]:
        for i in row[3:]:
            result.append(float(i))
    try: #띄어쓰기를 한 경우도 인식할 수 있도록
        ans = ans.replace(' ', '')
        continue
    except:
        print('잘못 입력하셨습니다. 다시 시도해 주세요.')
        break
        
plt.title('{} 지역의 인구 구조'.format(ans))
plt.style.use('ggplot')
plt.plot(result)
plt.show()