class main:
    def __init__(self,key:dict) -> None:
        self.key = key

    def get_input(self) -> None:
        while True:
            blank_string = str(input("Enter a string to decrypt: "))
            if blank_string.isalpha():
                blank_string = blank_string.lower()
                self.blank_string = blank_string
                break
            else:
                print("input was not valid")
                continue
        
    def encrypt_string(self) -> str:
        output = ""
        for char in self.blank_string:
            for key,value in self.key.items():
                if key == char:
                    output += value
                else:
                    continue
        self.decrypted_string = output
        return(output)
    

    def decrypt_string(self,string: str) -> str:
        output = ""
        string = string.lower()
        string = string.strip()
        if string == "":
            return(self.blank_string)
        else:
            for char in string:
                for key,value in self.key.items():
                    if value == char:
                        output += key
        return(output)
    


if __name__ == "__main__":
    key ={"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}
    main = main(key=key)
    main.get_input()
    print(main.encrypt_string())