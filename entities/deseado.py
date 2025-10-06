class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    @classmethod
    def get_list(cls):
        deseados = [
            cls("Aguila", "Blanca"),
            cls("Perrito", "Dorado"),
            cls("Baboson", "Brown"),
            cls("Tortuga", "Void"),
            cls("Lobo", "Dark Gray")
        ]
        return deseados
        