esc_origem = input().lower()
temp_origem = float(input())
esc_dest = input().lower()

match esc_origem:
    case 'C':
        temp_c = temp_origem
    case 'F':
        temp_c = 0 # inserir fórmula  F -> C 
    case 'K':
        temp_c = 0 # inserir fórmula  K -> C
    case 'R':
        temp_c = 0 # inserir fórmula  R -> C

match esc_Dest:
    case 'C':
        temp_dest = temp_c
    case 'F':
        temp_dest = 0 # inserir fórmula  C -> F
    case 'K':
        temp_dest = 0 # inserir fórmula  C -> K
    case 'R':
        temp_dest = 0 # inserir fórmula  C -> R
        
print(temp_dest)
        