# Напишите регулярное выражение, которое соответствует всем строкам, начинающимся с гласной и заканчивающимся
# на согласную

import re

text = "all day python date science work encoding"
result = re.findall(r'\b[aeiouAEIOU]\w*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]\b', text)

print(result)

