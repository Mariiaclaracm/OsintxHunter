from theHarvester.lib.core import AsyncFetcher


class SearchCrtsh:
    def __init__(self, word) -> None:
        self.word = word
        self.data: list = []
        self.proxy = False

    async def do_search(self) -> list:
        data: set = set()
        try:
            url = f'https://crt.sh/?q=%25.{self.word}&exclude=expired&deduplicate=Y&output=json'
            response = await AsyncFetcher.fetch_all([url], json=True, proxy=self.proxy)
            response = response[0]
            data = set([(dct['name_value'][2:] if dct['name_value'][:2] == '*.' else dct['name_value']) for dct in response])
            data = {domain for domain in data if (domain[0] != '*' and str(domain[0:4]).isnumeric() is False)}
        except Exception as e:
            print(e)
        clean: list = []
        for x in data:
            pre = x.split()
            for y in pre:
                clean.append(y)
        return clean

    async def process(self, proxy: bool = False) -> None:
        self.proxy = proxy
        data = await self.do_search()
        self.data = data

    async def get_hostnames(self) -> list:
        return self.data
