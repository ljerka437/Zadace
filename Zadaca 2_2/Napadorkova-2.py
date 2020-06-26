class Napaderror (Exception):
    def __init__(self):
        self.error_message='NAPAD ERROR: Unešena pogrešna vrijednost'
        print("\n Opis greške: {}".format(self.error_message))