def analizar_usuarios(usuarios):
    autorizado = []
    bloqueado = []
    sem_idade = []
    
    total_de_autorizado = 0
    total_sem_idade = 0
    
    for usuario in usuarios:
        idade = usuario.get('idade')
        
        if idade is None:
            sem_idade.append(usuario)
            total_sem_idade += 1
       
        
        else:
            if idade >= 18:
                    autorizado.append(usuario)
                    total_de_autorizado += 1
            else:
                        bloqueado.append(usuario)
  
    return autorizado, bloqueado, sem_idade, total_de_autorizado, total_sem_idade



# analizar_usuarios
 
usuarios = [
    {"nome": "Ana", "idade": 17},
    {"nome": "Carlos", "idade": 25},
    {"nome": "João", "idade": 30},
    {"nome": "Maria"}
]

resultado = analizar_usuarios(usuarios)

autorizado = resultado[0]
bloqueados = resultado[1]
sem_idade = resultado[2]

print('Autorizados:')
for usuario in autorizado:
     print(usuario['nome'])
print()

print('Bloqueados')
for usuario in bloqueados:
     print(usuario['nome'])
print()

print('Sem_Idade')  
for usuario in sem_idade:
     print(usuario['nome'])
print()


resultado = analizar_usuarios(usuarios)
print('Total autorizados:', resultado[3])
print('Total sem idade:', resultado[4])
print('Total bloqueados:', len(resultado[1]))
