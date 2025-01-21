# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

bands = {"Queen" : "Freddy Mercury", "The Beatles" : "Jonh Lennon", "Guns N' Roses" : "Axl Rose", "Nirvana" : "Kurt Cobain"}

print(bands.get("Nirvana")) #-> escreve o value correspondente da key presente entre parênteses
# bands.update({"Key:Value"}) -> adiciona ambos os valores ou substitui um dos termos presentes na lista caso já existir uma key ou value igual
# bands.pop("Key") -> Remove uma determinada chave da lista
# bands.popitem() -> Remove o ultimo da lsita
# bands.clear -> Remove TODA a lsita
# bands.key() -> Seleciona apenas as Key da lista
# bands.value() -> Seleciona apenas os Value da lista
# bands.items() -> Seleciona todas as Key e Value da lista