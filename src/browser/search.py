from googlesearch import search as s


class GoogleSearch:
    def __init__(self):
        self.query_result = []

    def search(self, query):
        try:
            for result in s(query, num_results=5):
                self.query_result.append(result)

            return self.query_result

        except Exception as err:
            return err

    def get_first_link(self):
        return self.query_result[0]
