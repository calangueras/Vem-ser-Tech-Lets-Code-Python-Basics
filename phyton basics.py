#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Helho, World")
#aula_02


# In[10]:


preco = 19.99
print(preco, type(preco))
#aula_03


# In[21]:


cidade = 'Uberaba'
print(cidade, type(cidade))
#aula_03


# In[23]:


disponivel = True
print(disponivel, type(disponivel))
#aula_03


# In[27]:


disponivel = False
print(disponivel)
print(disponivel, type(disponivel))
#aula_03


# In[2]:


x = 5


# In[7]:


print(x)


# In[30]:


x = 50
y = 2
print(x + y)
print(x - y)
print(x / y)
print(x * y)
#aula_04


print(type(x))
#aula_03

# In[31]:


print(x // y)
print(x % y)
print(x ** y)
#aula_04


# In[32]:


a = 2 + 3  # Soma
b = 2 - 3  # Subtração
c = 2 * 3  # Multiplicação
d = 2 / 3  # Divisão
e = 2 // 3 # Divisão inteira
f = 2 ** 3 # Potência
g = 2 % 3  # Resto de divisão

print (a, b, c, d, e, f, g)
#aula_04


# In[40]:


temCafe = True
TemPao = False
print(not temCafe) #not = conectivo nao inversao
print(temCafe or TemPao) #or = conectivo ou pelo menos 1 condição tem que ser verdadeira
print(temCafe and TemPao) # and do conectivo e as duas condições tem que ser verdadeiras
#aula_04


# In[44]:


dolar = 7.00
real = 1
print(dolar > real)
print(real < dolar)
print(real > dolar)
print(dolar < real)
print(dolar == real)
print(dolar<=real)
print(dolar>=real)
print(dolar!=real)
#aula_04


# In[48]:


idade = input("Informe sua idade: ")
print("A sua idade é: ", idade, " anos", type(idade))
#aula05


# In[49]:


idade = int(idade)
print(idade, type(idade))
#aula05


# In[52]:


salario_mensal = input("Digite seu salario mensal: ")
salario_mensal = float(salario_mensal)

gasto_mensal = input("Digite seu gasto mensal: ")
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print("O valor do seu salario anual é: ", salario_total, "E o seu gasto anual é de: ", gasto_total, "E o valor total economizado é :", montante_economizado)
#aula05

valor_passagem = 5.40
valor_corrida = input("Qual o valor da corrida: ")
if float(valor_corrida) <= valor_passagem * 5:
    print("Pague a corrida")
if float(valor_corrida) >= valor_passagem * 5:
    print("Pegue o ônibus")
    
valor_passagem = 5.40
valor_corrida = input("Qual o valor da corrida: ")
if float(valor_corrida) <= valor_passagem * 5:
    print("Pague a corrida")
else:
    print("Pegue o ônibus")   
    #aula06


# In[18]:


valor_passagem = 5.40

valor_corrida = input("Qual o valor da corrida: ")

if float(valor_corrida) <= valor_passagem * 5:
    print("Pague a corrida")
else:
    if float(valor_corrida) <= valor_passagem * 6:
        print("Aguarde um instante, o valor pode abaixar")
    else:
        print('Pegue o ônibus')
        #aula06


# In[25]:


valor_passagem = 5.40

valor_corrida = input("Qual o valor da corrida: ")

if float(valor_corrida) <= valor_passagem * 5:
    print("Pague a corrida")
elif float(valor_corrida) <= valor_passagem * 6:
    print("Aguarde um instante, o valor pode abaixar")
else:
    print('Pegue o ônibus')
    #aula06


# In[3]:


contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, "item limpo")
    else:
        print(contador, "itens limpos")
print("Todas as louças limpas")        
#aula7


# In[8]:


contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        continue
    print(contador, "itens limpos")
    
print("Todas as louças limpas")        
#aula7


# In[7]:


texto = input("Digite uma senha")

while texto != 'abc':
 texto = input("Senha invalida. Tente novamente")

print("Acesso permitido")  
#aula7

