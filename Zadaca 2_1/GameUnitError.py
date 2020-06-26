class GameUnitError(Exception):
    def __init__(self,msg='',code=000):
        super().__init__(msg)
        self.error_message = '~'*50+'\n'
        self.error_dict = {
            000: 'ERROR-000: nespecificirana pogreška',
            101: 'ERROR-101: Problem sa zdravometrom',
            102: 'ERROR-102: Problem u napadu! Zanemarujem...'
        }
        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n'