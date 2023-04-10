# Напишите регулярное выражение, которое соответствует всем строкам, содержащим хотя бы одно слово, начинающееся
# с заглавной буквы

import re

text = "Hello bye Apple banana Pen Phone"

result = re.findall(r'\b[A-Z]\w*\b', text)
print(result)