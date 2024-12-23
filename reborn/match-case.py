# match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleanner and syntax is more readble

def regioes(uf):
    match uf:
        case "RS" | "SC" | "PR": # Pipe == OR
            print("Pertence a região sul do país")
        case "SP" | "ES" | "RJ" | "MG":
            print("Pertence a região sudeste do país")
        case "GO" | "MT" | "MS" | "DF":
            print("Pertence a região centro-oeste do país")
        case "BA" | "SE" | "RN" | "PA" | "CE" | "PI" | "AL" | "PB" | "MA":
            print("Pertence a região nordeste do país")
        case "AM" | "RR" | "RO" | "AP" | "AC" | "TO" :
            print("Pertence a região norte do país")
        case _: # _ == wild card
            print("UF inválida, tente novamente.")

regioes("SP")