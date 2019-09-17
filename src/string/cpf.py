from src.utils.cpf_cnpj_generator import cpf as cpf_generator
import sys, time

class CPF():

    def cpf(self, args = {}):
        
        data = cpf_generator()
        
        for param, value in args.items():

            if(param == '-m'):
                data = value % tuple(data)

        return data


cpf = CPF()

array = []

start = time.time()
for i in range(1000000):
    
    #array.append(cpf.cpf({'-m': "%c%c%c.%c%c%c.%c%c%c.%c%c"}))
    #print(cpf.cpf())
    print(cpf.cpf({'-m': "%c%c%c.%c%c%c.%c%c%c.%c%c"}))

print((time.time() - start) / 60, " minutes")
