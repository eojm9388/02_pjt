# Project 2

## `csv`파일 불러와서 `numpy`와 `pandas`로 데이터 처리

#### 라이브러리 불러오기

```python
import csv
import numpy as np
import pandas as pd
```

#### `numpy`를 사용하여 데이터 불러오는 함수 생성

```python
def file_open_by_numpy():
    # np.loadtxt(구분자 = ',', 데이터 타입: string)
    np_arr = np.loadtxt('archive/NFLX.csv', delimiter=",", encoding='cp949', dtype=str)
    return np_arr

arr = file_open_by_numpy()
arr = arr[:, :-2]
```
> `numpy`에서는 2차원 배열의 슬라이싱을 쉽게 할 수 있다 `arr[:, :-2]`

#### `pandas`로 데이터 프레임 생성하기

```python
# 컬럼명 지정하면서 생성하기
# 인덱스명도 지정하면서 할 수 있다.
columns=arr[0]
arr = np.delete(arr, 0, 0)
df = pd.DataFrame(arr, columns=columns)
df
```

## `matplotlib` 사용하기
라이브러리 불러오기
`import matplotlib.pyplot as plt`

### csv 파일 경로를 불러와 파일 읽어오기
```python
# CSV 파일 경로
csv_path = "archive/NFLX.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(0, 5))

# DataFrame 출력
df
```

데이터프레임 데이터 타입 확인하기
- `df.dtypes`

데이터 타입 바꾸기 (문자열 -> 날짜형식)
- `df["Date"] = pd.to_datetime(df["Date"])`

그래프 출력하기
```python
date_year = df[df['Date'].dt.year>=2021]
date_year['Date']
date_year['Close']

# 그래프 그리기 (가로, 세로 축에 표시될 데이터를 차례로 기입)
plt.plot(date_year['Date'], date_year['Close'])

# 그래프 제목 설정
plt.title('NFLX Close Price')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Close Price')

# 그래프 표시
plt.show()
```

> 데이터 요소를 불러오는 방법은 리스트 요소를 불러오는 방법과 같다!

```python
date_after_2021 = df[df['Date'].dt.year>=2021]

max_price = max(date_after_2021['Close'])
min_price = min(date_after_2021['Close'])
```

데이터프레임에 열 추가
```python
new_date.insert(loc=1, column='month', value = new_date['Date'].dt.month)
```

데이터프레임 그룹화 

groupby의 요소의 순서에 따라 정렬 우선순위가 달라진다

```python
new_data = date_after_2021.groupby([date_after_2021['Date'].dt.year, date_after_2021['Date'].dt.month]).mean()
new_data['Close']
new_data
```

데이터 축 회전시키기
```python
plt.xticks(rotation=45)
```