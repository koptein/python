class Rot13:
    def __init__(self,string):
        self.string = string;
        self.alphabet = []
        self.alphabet_upper = []

        for char in map(chr, xrange(97, 123)):
            self.alphabet.append(char)             
        for char in map(chr, xrange(65, 90)):
            self.alphabet_upper.append(char)      

    def setString(self, string):
        self.string = string

    def getString(self):
        return self.string

    def rotate(self):
        output_string = ""
        for letter in self.string:                                                   
            #print letter + " -> " + str(type(letter))                                
                                                                                      
            use = self.alphabet_upper                                                      
            if letter.islower():                                                      
                use = self.alphabet                                                        
                                                                                      
            # Exclude non alpha characters from conversion.                           
            if not letter.isalpha():                                                  
                output_string = output_string+letter                                  
                                                                                      
            else:                                                                     
                myindex  = self.alphabet.index(letter.lower())                             
                if myindex >= 13:                                                     
                    output_string = output_string+use[myindex-13]                     
                else:                                                                 
                    output_string = output_string+use[myindex+13]                     
        return output_string
