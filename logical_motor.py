import re
#Crear clase que represente un simbolo para una preposición
class Symbol:
    
    #Constructor de la clase 
    def __init__(self, sentence: str, value= True):
        self.sentence = sentence
        self.value = value
        
    #Definir como interactua el operador '=='
    def __eq__(self, other):
        if isinstance(other, Symbol):
            if self.sentence == other.sentence:
                return True
            else:  
                return False
        else:
            return False
    
    #Definir como se comporta cuando se vuelve quiere usar como indice
    def __hash__(self):
        return hash(self.sentence)
    
    #Definir como se comporta cuando se vuelve un str o se llama print()
    def __str__(self):
        return f"{self.sentence}"
    
    #Metodo para retornar la forma del simbolo
    def get_formula(self):
        return self.sentence

#Crear clase que represente el simbolo '¬' o No
class No:
    #Constructor de la clase
    def __init__(self, symbol: Symbol):
        self.symbol = symbol
            
    
    #Definir como interactua el operador '=='
    def __eq__(self, other):
        if isinstance(other, No):
            if self.symbol.sentence == other.symbol.sentence:
                return True
            else:
                return False
        else:
            return False
    
    #Definir como se comporta cuando se vuelve quiere usar como indice
    def __str__(self):
        return self.get_formula()
    #Metodo para retornar la formula
    def get_formula(self):
        base_string = f" ¬({self.symbol})"
        count_nor_char = base_string.count("¬")
        if(count_nor_char % 2 == 0):
            match = re.findall(r'[a-zA-Z0-9\sñ>/-]+', base_string)
            if match:
                extracted_string = ''.join(match)
                extracted_string = re.sub(' +', ' ', extracted_string)
                
                return extracted_string.strip()
            else:
                raise ValueError("No alphanumeric values found.")
        else:
            return f" ¬({self.symbol})"
    #Metodo para evaluar la formula y retornar un simbolo actualizado, al igual que actualizar el simbolo
    def evaluar(self):
        if self.symbol.value:
            return False
        else:
            return True
    #Metodo para crear un nuevo simbolo basado en la operacion hecha
    def create_symbol(self):
        return Symbol(self.get_formula(), self.evaluar())
    
#Crear clase que represente el simbolo 'v' u Or
class Or:
    
    def __init__(self, *disjunctions):
        self.disjunctions = []
        for d in disjunctions:
            if isinstance(d, Symbol):
                self.disjunctions.append(d)
            else:
                raise TypeError ("Invalid type in the disjunctions")
    
    #Definir como interactua el operador '=='
    def __eq__(self, other):
        if isinstance(other, Or) and len(other.disjunctions) == len(self.disjunctions):
            comp_test = True
            for i in range(0, len(self.disjunctions)):
                if self.disjunctions[i] != other.disjunctions[i]:
                    comp_test = False
                    break
            
            return comp_test
        else:
            return False
    #Definir como se comporta cuando se vuelve un str o se llama print()
    def __str__(self):
        empty_str = ""
        for d in self.disjunctions:
            empty_str += str(d) + " OR "
        ret_string = empty_str[:-4]
        return ret_string
            
    #Metodo para retornar la formula
    def get_formula(self):
        empty_str = ""
        for d in self.disjunctions:
            empty_str += d.get_formula() + " V "
        ret_string = empty_str[:-3]
        return ret_string
    #Metodo para evaluar la formula y retornar un simbolo actualizado, al igual que actualizar el simbolo
    def evaluar(self):
        for d in self.disjunctions:
            if d.value:
                return True
        return False
    #Metodo para crear un nuevo simbolo basado en la operacion hecha
    def create_symbol(self):
        return Symbol(self.get_formula(), self.evaluar())
                
#Crear clase que represente el simbolo '∧' o And
class And:
    
    def __init__(self, *conjunctions):
        self.conjunctions = []
        for c in conjunctions:
            if isinstance(c, Symbol):
                self.conjunctions.append(c)
            else:
                raise TypeError ("Invalid type in the conjunctions")
    #Definir como interactua el operador '=='
    def __eq__(self, other):
        if isinstance(other, And) and len(other.conjunctions) == len(self.conjunctions):
            comp_test = True
            for i in range(0, len(self.conjunctions)):
                if self.conjunctions[i] != other.conjunctions[i]:
                    comp_test = False
                    break
            return comp_test
        else:
            return False
    #Definir como se comporta cuando se vuelve un str o se llama print()
    def __str__(self):
        empty_str = ""
        for c in self.conjunctions:
            empty_str += str(c) + " AND "
        ret_string = empty_str[:-5]
        return ret_string
            
    #Metodo para retornar la formula
    def get_formula(self):
        empty_str = ""
        for c in self.conjunctions:
            empty_str += c.get_formula() + " ∧ "
        ret_string = empty_str[:-3]
        return ret_string
    
    #Metodo para evaluar la formula y retornar un simbolo actualizado, al igual que actualizar el simbolo
    def evaluar(self):
        for c in self.conjunctions:
            if not c.value:
                return False
        return True
    #Metodo para crear un nuevo simbolo basado en la operacion hecha
    def create_symbol(self):
        return Symbol(self.get_formula(), self.evaluar())

     
#Crear clase que represente el simbolo '->' o Entonces
class Condicional:
    
    def __init__(self, symbol_1, symbol_2):
        if isinstance(symbol_1, Symbol) and isinstance(symbol_2, Symbol):
            self.condition = symbol_1
            self.consequence = symbol_2
        else:
            raise TypeError("Invalid type to create a Condition")
    
    def __eq__(self, other):
        
        if isinstance(other, Condicional) and other.condition == self.condition and other.consequence == self.consequence:
            return True
        else:
            return False
    def __str__(self):
        return f"{self.condition} -> {self.consequence}"
    
    def get_formula(self):
        return f"{self.condition} -> {self.consequence}"
    
    def evaluar(self):
        if self.consequence.value:
            return True
        else:
            if self.condition:
                return False
            else:
                return True
            
    def create_symbol(self):
        return Symbol(self.get_formula(), self.evaluar())
    
#Crear clase que represente el simbolo '<->' o Si y solo si
class Bicondicional:
    
    def __init__(self, condcons_1, condcons_2):
        if isinstance(condcons_1, Symbol) and isinstance(condcons_2, Symbol):
            self.condcons_1 = condcons_1
            self.condcons_2 = condcons_2
        else:
            raise TypeError("Invalid type to create a Bicondicional")
    
    def __eq__(self, other):
        if isinstance(other, Bicondicional) and other.condcons_1 == self.condcons_1 and other.condcons_2 == self.condcons_2:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.condcons_1} <-> {self.condcons_2}"
    
    def get_formula(self):
        return f"{self.condcons_1} <-> {self.condcons_2}"
    
    def evaluar(self):
        if self.condcons_1 == self.condcons_2:
            return True
        else:
            return False
            
    def create_symbol(self):
        return Symbol(self.get_formula(), self.evaluar())
    
        