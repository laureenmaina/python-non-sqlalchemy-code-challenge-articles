class Author:
    def __init__(self, name):
        if not isinstance(name,str):
            raise ValueError("Name must be a string")
        if len(name)==0:
            raise ValueError("Name must have more than 0 characters")

        self._name = name      
        self._articles = []
        self._magazines=[]

    @property
    def name(self):
       return self._name

    @name.setter
    def name(self, name):
       if isinstance(name, str) and len(name) > 0:
        self._name = name
       else:
          raise ValueError("Cannot change author's name")
    def articles(self,magazine,title):
      return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self,magazine,title)
       

    def topic_areas(self):
        categories={article.magazine.category for 
                    article in Article.all if article.author==self}
        return list(categories) if categories else None
        
    
       
class Magazine:
    def __init__(self, name, category):
    
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and (2 <= len(value) <= 16):
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        # if not self._articles:
        #     return None
        # return [article.title for article in self._articles]
        pass

    def contributing_authors(self):
        # if not self._articles:
        #     return None
        # author_counts = {}
        # for article in self._articles:
        #     if article.author in author_counts:
        #         author_counts[article.author] += 1
        #     else:
        #         author_counts[article.author] = 1
        # return [author for author, count in author_counts.items() if count > 2] or None
        pass


class Article:
    all=[]
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and (5 <= len(title) <= 50):
            if not hasattr(self, '_title') or self._title is None:
                self._title = title
            else:
                raise AttributeError("Cannot change title after it is set")
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")


