from jsonhandler import JSONContext


with JSONContext('file_1.json', 'file_2.json', 'file_3.json') as (file_1, file_2, file_3):
    file_1.name = "Pepa"
    file_1.surname = "Novak"

    file_2.genus = "Drosera"
    file_2.species = "Drosera rotundifolia"

    file_3.type = "acid"
    file_3.name = "acetic acid"
    file_3.formula = "CH3COOH"
