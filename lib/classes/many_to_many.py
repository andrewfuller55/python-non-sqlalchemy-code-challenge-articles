class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    def articles(self):
        return [article for article in Article.all if article.author == self]
        pass

    def magazines(self):
        non_unique_magazines = [article.magazine for article in self.articles()]
        return list(set(non_unique_magazines))
        pass

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        pass

    def topic_areas(self):
        non_unique_topics = [article.magazine.category for article in self.articles()]
        if len(non_unique_topics) == 0:
            return None
        else:
            return list(set(non_unique_topics))
        pass

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            raise ValueError(
                "Author must be a non-empty string"
            )

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        pass

    def contributors(self):
        non_unique_contributors = [article.author for article in self.articles()]
        return list(set(non_unique_contributors))
        pass

    def article_titles(self):
        titles_list = [article.title for article in self.articles()]
        if len(titles_list) == 0:
            return None
        else:
            return titles_list
        pass

    def contributing_authors(self):
        unique_contributors = [article.author for article in self.articles() if len(self.articles()) > 2]
        if len(unique_contributors) == 0:
            return None
        else:
            return unique_contributors
        pass