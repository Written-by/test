import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 엑셀 파일 경로
excel_file = 'MSS-of-1000-tranco.xlsx'

# 엑셀 파일에서 데이터를 DataFrame으로 읽어오기
df = pd.read_excel(excel_file)

# "error" 값이 있는 행 제거
df = df[df[1] != 'error']

# 문자열을 숫자로 변환
df[1] = pd.to_numeric(df[1], errors='coerce')

# 결측값 제거
df.dropna(inplace=True)

# 0부터 2000까지의 범위로 분할
bins = np.linspace(0, 2000, 100)

# CDF 계산
def calculate_cdf(data, bins):
    hist, bin_edges = np.histogram(data, bins=bins, density=True)
    cdf = np.cumsum(hist)
    return bin_edges[1:], cdf

# CDF 계산
x_values, cdf_values = calculate_cdf(df[1], bins)

# 그래프 그리기
plt.plot(x_values, cdf_values, marker='o', linestyle='-')
plt.xlabel('값')
plt.ylabel('누적 백분율')
plt.title('CDF 그래프')
plt.grid(True)
plt.show()
