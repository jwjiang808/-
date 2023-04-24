# 用正则表达式提取

import re

long_text =\
  """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

# 正则表达式模式
pattern = r"(.*?)\n(.{20})\n(?:\d+\. )?(.*?\n(?:LU\d+\n)+)"

# 匹配模式并提取数据
matches = re.findall(pattern, long_text, re.DOTALL)

# 将提取的数据转换为所需的数据格式
data = {
    "name": matches[0][0],
    "lei": matches[0][1],
    "sub_fund": []
}

for sub_match in matches:
    sub_fund = {
        "title": sub_match[2].strip(),
        "isin": re.findall(r"LU\d+", sub_match[2])
    }
    data["sub_fund"].append(sub_fund)

print(data)
