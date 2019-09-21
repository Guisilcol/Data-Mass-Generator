from src.utils.cpf_cnpj_generator import cpf as cpf_generator
import sys, time

class CPF():

    def cpf(self, args = {}):
        
        data = cpf_generator()
        
        for param, value in args.items():

            if(param == '-m'):
                data = value % tuple(data)

        return data
