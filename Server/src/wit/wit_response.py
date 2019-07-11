class WitResponse:
    def __init__(self, response_text, keywords):
        self.text = response_text
        self.keywords = keywords
        if self.keywords is not None:
            self.success = True
        else:
            self.success = False

    def get_text(self):
        return self.text

    def get_keywords(self):
        return list(self.keywords.keys())

    def has_key(self, key):
        return key in self.get_keywords()

    def get_values(self, key):
        return self.keywords[key]

    def is_success(self):
        return self.success
