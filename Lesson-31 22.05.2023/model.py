import json


class Article:
    def __init__(self, name, author, symbols, publisher, description):
        self.name = name
        self.author = author
        self.symbols = symbols
        self.publisher = publisher
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.author})"


class DecodeError(Exception):
    pass


class Model:
    def __init__(self, filepath):
        self.filepath = filepath
        self.__articles = {}
        try:
            self.data = json.load(open(self.filepath, "r", encoding="utf-8"))
            for article in self.data.values():
                self.__articles[f'{article["name"]} {article["author"]}'] = Article(*article.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, "w") as f:
                f.write('{}')

    @property
    def articles(self):
        return self.__articles

    def save_articles(self):
        dict_articles = {f'{art.name} {art.author}': art.__dict__ for art in self.__articles.values()}
        json.dump(dict_articles, open(self.filepath, "w", encoding="utf-8"))

    def add_new_article(self, article_data):
        new_article = Article(*article_data.values())
        self.__articles[f'{new_article.name} {new_article.author}'] = new_article
        self.save_articles()

    def find_articles(self, key_words):
        articles = []
        for article in self.__articles.values():
            for word in key_words:
                if article in articles:
                    break
                for prop in article.__dict__.values():
                    if word.lower() in prop.lower():
                        articles.append(article)
                        break
        return articles

    def delete_article(self, articles):
        if len(articles) == 0:
            return "No such article was found"
        elif len(articles) == 1:
            article = articles[0]
            key = f'{article.name} {article.author}'
            self.__articles.pop(key)
            self.save_articles()
            return "Article has been deleted"
        elif len(articles) > 1:
            return "So many articles"
