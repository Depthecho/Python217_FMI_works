# Напишите регулярное выражение, которое соответствует всем URL-адресам.

import re

text = "The website https://www.wikipedia.com is a great resource for information!"

result = re.findall(r'https://\S+', text)
print(result)
