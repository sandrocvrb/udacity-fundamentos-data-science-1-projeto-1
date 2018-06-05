# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import sys

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")


# TAREFA 1
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

for index, row in enumerate(data_list[:20]):
    print("- Amostra {}: {}".format(index + 1, row))

input("Aperte Enter para continuar...")


# TAREFA 2
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for index, row in enumerate(data_list[:20]):
    print("- Gênero da amostra {}: {}".format(index + 1, row[-2]))

input("Aperte Enter para continuar...")


# TAREFA 3
def column_to_list(data, index):
    """Extrai, de uma lista de listas, uma coluna pela posição desejada retornando uma lista com todos os valores.

    Arguments:
        data {list} -- Lista contendo todas as colunas extraídas do arquivo CSV.
        index {int} -- Posição da coluna a ser extraída.

    Returns:
        list -- Lista contendo todos os valores da coluna extraída.
    """

    column_list = []

    for row in data:
        column_list.append(row[index])

    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4

male = 0
female = 0
for row in column_to_list(data_list, -2):
    if row.lower() == "female":
        female += 1
    elif row.lower() == "male":
        male += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """Retorna a quantidade de homens e mulheres que utilizaram o serviço.

    Arguments:
        data_list {list} -- Lista contendo os dados completos obtidos do CSV lido.

    Returns:
        list -- Lista contendo a quantidade de homens na primeira posição e de mulheres na segunda posição.
    """

    male = 0
    female = 0

    for row in column_to_list(data_list, -2):
        if row.lower() == "female":
            female += 1
        elif row.lower() == "male":
            male += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """Retorna o gênero mais popular dentre os que utilizaram o serviço.

    Arguments:
        data_list {list} -- Lista contendo os dados completos obtidos do CSV lido.

    Returns:
        string -- "Masculino", "Feminino" ou "Igual".
    """

    male, female = count_gender(data_list)

    if male > female:
        result = "Masculino"
    elif female > male:
        result = "Feminino"
    else:
        result = "Igual"

    return result


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 7
print("\nTAREFA 7: Verifique o gráfico!")


def count_user_type(data_list):
    """Retorna a quantidade de cada tipo de usuário que utilizou o serviço.

    Arguments:
        data_list {list} -- Lista contendo os dados completos obtidos do CSV lido.

    Returns:
        list -- Lista contendo a quantidade de "customer" na primeira posição, "dependent" na segunda posição e "subscriber" na terceira posição.
    """

    customer = 0
    dependent = 0
    subscriber = 0

    for row in column_to_list(data_list, -3):
        if row.lower() == "customer":
            customer += 1 
        elif row.lower() == "dependent":
            dependent += 1
        elif row.lower() == "subscriber":
            subscriber += 1

    return [customer, dependent, subscriber]


types = ["Customer", "Dependent", "Subscriber"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 8
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque a coluna 'gênero' também possui valores vazios, ou seja, nem todos os registros estão com a informação preenchida."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# Você não deve usar funções prontas parTODO isso, como max() e min().


def calculate_min(values):
    """Calcula o valor mínimo entre os valores de uma lista.

    Arguments:
        values {list} -- Lista com números

    Returns:
        Número
    """

    n = calculate_len(values)

    if n < 1:
        return None
    else:
        min_value = sys.maxsize
        for v in values:
            if v < min_value:
                min_value = v
        return min_value


def calculate_max(values):
    """Calcula o valor máximo entre os valores de uma lista.

    Arguments:
        values {list} -- Lista com números

    Returns:
        Número
    """

    n = calculate_len(values)

    if n < 1:
        return None
    else:
        max_value = -sys.maxsize + 1
        for v in values:
            if v > max_value:
                max_value = v
        return max_value


def calculate_mean(values):
    """Calcula a média entre os valores de uma lista.

    Arguments:
        values {list} -- Lista com números

    Returns:
        Número
    """

    return calculate_sum(values) / calculate_len(values)


def calculate_median(values):
    """Calcula a mediana entre os valores de uma lista.

    Arguments:
        values {list} -- Lista com números

    Returns:
        Número
    """

    n = calculate_len(values)

    if n < 1:
        return None
    if n % 2 == 1:
        return calculate_sorted(values)[n//2]
    else:
        return calculate_sum(calculate_sorted(values)[n//2-1:n//2+1])/2


def calculate_sum(values):
    """Calcula a soma entre os valores de uma lista.

    Arguments:
        values {list} -- Lista com números

    Returns:
        Número
    """

    result = 0.

    for v in values:
        result += v

    return result


def calculate_len(values):
    """Calcula a quantidade de itens de uma lista.

    Arguments:
        values {list} -- Lista com números

    Returns:
        Número
    """

    result = 0

    for v in values:
        result += 1

    return result


def calculate_sorted(values):
    """Reordena os itens de uma lista.

    Arguments:
        values {list} -- Lista com números

    Returns:
        Lista reordenada
    """
    less = []
    pivotList = []
    more = []

    if len(values) <= 1:
        return values
    else:
        pivot = values[0]
        for i in values:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = calculate_sorted(less)
        more = calculate_sorted(more)

        return less + pivotList + more


trip_duration_list = [int(duration) for duration in column_to_list(data_list, 2)]

min_trip = calculate_min(trip_duration_list)
max_trip = calculate_max(trip_duration_list)
mean_trip = calculate_mean(trip_duration_list)
median_trip = calculate_median(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#   """
#   Função de exemplo com anotações.
#   Argumentos:
#       param1: O primeiro parâmetro.
#       param2: O segundo parâmetro.
#   Retorna:
#       Uma lista de valores x.
#   """

input("Aperte Enter para continuar...")


# TAREFA 12 - Desafio! (Opcional)
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
    """Retorna a quantidade de cada valor distinto encontrado em uma lista.

    Arguments:
        column_list {list} -- Lista contendo os valores a serem contados.

    Returns:
        tuple -- Retorna duas listas: a primeira contém os valores distintos encontrados; a segunda contém a quantidade de cada valor distinto encontrado.
    """

    item_types = []
    count_items = []

    for item in column_list:
        if item in item_types:
            count_items[item_types.index(item)] += 1
        else:
            item_types.append(item)
            count_items.append(1)

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
