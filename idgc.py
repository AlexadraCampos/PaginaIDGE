import re

class IDGC:
    def Brazil_CPF_Validator(self, cpf: str) -> bool:
        cpf = re.sub(r'\D', '', cpf)
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF deve conter 11 dígitos numéricos!")
            return False
        if cpf == cpf[0] * 11:
            print("CPF inválido: todos os números são iguais!")
            return False
        pesoTotalD1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = 11 - (pesoTotalD1 % 11)
        if digito1 >= 10:
            digito1 = 0
        pesoTotalD2 = sum(int(cpf[i]) * (11 - i) for i in range(9)) + digito1 * 2
        digito2 = 11 - (pesoTotalD2 % 11)
        if digito2 >= 10:
            digito2 = 0
        return cpf[-2:] == f"{digito1}{digito2}"

    def Brazil_CNPJ_Validator(self, cnpj: str) -> bool:
        cnpj = re.sub(r'\D', '', cnpj)
        if not cnpj.isdigit() or len(cnpj) != 14:
            print("CNPJ deve conter 14 dígitos numéricos!")
            return False
        if cnpj == cnpj[0] * 14:
            print("CNPJ inválido: todos os números são iguais!")
            return False
        
        def calcula_digito(cnpj, pesos):
            soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
            digito = 11 - (soma % 11)
            return 0 if digito >= 10 else digito
        
        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6] + pesos1
        
        digito1 = calcula_digito(cnpj, pesos1)
        digito2 = calcula_digito(cnpj + str(digito1), pesos2)
        
        return cnpj[-2:] == f"{digito1}{digito2}"

    def Argentina_DNI_Validator(self, dni: str) -> bool:
        dni = re.sub(r'\D', '', dni)
        if not dni.isdigit() or len(dni) not in [7, 8]:
            print("DNI deve conter 7 ou 8 dígitos numéricos!")
            return False
        return True
    
    def Argentina_CUIL_Validator(self, cuil: str) -> bool:
        cuil = re.sub(r'\D', '', cuil)
        if not cuil.isdigit() or len(cuil) != 11:
            print("CUIL deve conter 11 dígitos numéricos!")
            return False
        
        coeficientes = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5]
        soma = sum(int(cuil[i]) * coeficientes[i] for i in range(10))
        digito_verificador = 11 - (soma % 11)
        if digito_verificador == 11:
            digito_verificador = 0
        elif digito_verificador == 10:
            digito_verificador = 9
        
        return int(cuil[-1]) == digito_verificador

# Testando a validação
jif = IDGC()
cpf = "306.559.490-03"
cnpj = "11.222.333/0001-81"
dni = "12345678"
cuil = "20-12345678-3"

if jif.Brazil_CPF_Validator(cpf):
    print("CPF válido")
else:
    print("CPF inválido")

if jif.Brazil_CNPJ_Validator(cnpj):
    print("CNPJ válido")
else:
    print("CNPJ inválido")

if jif.Argentina_DNI_Validator(dni):
    print("DNI válido")
else:
    print("DNI inválido")

if jif.Argentina_CUIL_Validator(cuil):
    print("CUIL válido")
else:
    print("CUIL inválido")
