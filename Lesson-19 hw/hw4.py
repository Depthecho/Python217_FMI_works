# Напишите регулярное выражение, которое соответствует всем строкам, содержащим повторяющуюся букву

import re

text = "book letter python apple banana"
result = re.findall(r"\b(\w*(\w)\2\w*)\b", text)
print(result)


