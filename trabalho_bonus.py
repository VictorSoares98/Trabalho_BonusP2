from os import path, system
system('cls')

def salvando_obras(obra):
    with open('obras_arte.txt', 'a') as file:
        file.write(f'{obra.titulo},{obra.data_criacao},{obra.tema},{obra.estilo_artistico},{obra.descricao},{obra.tecnica},{obra.autor},{obra.localizacao}\n')

def carregando_obras():
    obras = []
    if path.exists('obras_arte.txt'):
        with open('obras_arte.txt', 'r') as file:
            for line in file:
                dados = line.strip().split(',')
                obras.append(ObraDeArte(*dados))
    return obras

def salvando_artistas(artista):
    with open('artistas.txt', 'a') as file:
        file.write(f'{artista.nome},{artista.data_nascimento},{artista.local_nascimento},{artista.biografia},{"|".join(artista.estilos)}\n')

def carregando_artistas():
    artistas = []
    if path.exists('artistas.txt'):
        with open('artistas.txt', 'r') as file:
            for line in file:
                dados = line.strip().split(',')
                dados[4] = dados[4].split('|')
                artistas.append(Artistas(*dados))
    return artistas

def salvando_emprestimos(emprestimos):
    with open('emprestimo.txt', 'a') as file:
        file.write(f'{emprestimos.obra},{emprestimos.periodo},{emprestimos.evento},{emprestimos.responsavel},{emprestimos.tema}\n')

def carregando_emprestimos():
    emprestimo = []
    if path.exists('emprestimo.txt'):
        with open('emprestimo.txt', 'r') as file:
            for line in file:
                dados = line.strip().split(',')
                dados[4] = dados[4].split('|')
                emprestimo.append(Emprestimo(*dados))
    return emprestimo

def salvando_visitaGui(visitasGui):
    with open('visitaGui.txt', 'a') as file:
        file.write(f'{visitasGui.tema},{visitasGui.descricao},{visitasGui.obras}')

def carregando_visitaGui():
    visitaGui = []
    if path.exists('visitaGui.txt'):
        with open('visitaGui.txt', 'r') as file:
            for line in file:
                dados = line.strip().split(',')
                dados[4] = dados[4].split('|')
                visitaGui.append(VisitaGuiada(*dados))
    return visitaGui

def salvando_estilo_art(estilo_art):
    with open('estilo_art.txt', 'a') as file:
        file.write(f'{estilo_art.denominacao},{estilo_art.periodo},{estilo_art.descricao},{estilo_art.escola}\n')

def carregando_estilo_art():
    estilo_arts = []
    if path.exists('estilo_art.txt'):
        with open('estilo_art.txt', 'r') as file:
            for line in file:
                dados = line.strip().split(',')
                dados[4] = dados[4].split('|')
                estilo_arts.append(Estilo_Artistico(*dados))
    return estilo_arts

#Classes de função

class Artistas:
    def __init__(self, nome, data_nascimento, local_nascimento, biografia, estilos):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.local_nascimento = local_nascimento
        self.biografia = biografia
        self.estilos = estilos

class Estilo_Artistico:
    def __init__(self, denominacao, periodo, descricao, escola):
        self.denominacao = denominacao
        self.periodo = periodo
        self.descricao = descricao
        self.escola = escola

class ObraDeArte:
    def __init__(self, titulo, data_criacao, tema, estilo_artistico, descricao, tecnica, autor, localizacao):
        self.titulo = titulo
        self.data_criacao = data_criacao
        self.tema = tema
        self.estilo_artistico = estilo_artistico
        self.descricao = descricao
        self.tecnica = tecnica
        self.autor = autor
        self.localizacao = localizacao

class Emprestimo:
    def __init__(self, obra, periodo, evento, responsavel, tema):
        self.obra = obra
        self.periodo = periodo
        self.evento = evento
        self.responsavel = responsavel
        self.tema = tema

class VisitaGuiada:
    def __init__(self, tema, descricao, obras):
        self.tema = tema
        self.descricao = descricao
        self.obras = obras

# Algoritmos de Ordanação
def quicksort(obras, low, high):
    if low < high:
        pi = partition(obras, low, high)
        quicksort(obras, low, pi-1)
        quicksort(obras, pi+1, high)

def partition(obras, low, high):
    
    pivot = obras[high].titulo
    i = low - 1
    for j in range(low, high):
        if obras[j].titulo < pivot:
            i = i + 1
            obras[i], obras[j] = obras[j], obras[i]
    obras[i + 1], obras[high] = obras[high], obras[i + 1]
    return i + 1

#Artistas
def quicksort(artista, low, high):
    if low < high:
        pi = partition(artista, low, high)
        quicksort(artista, low, pi-1)
        quicksort(artista, pi+1, high)

def partition(artista, low, high):
    
    pivot = artista[high].nome
    i = low - 1
    for j in range(low, high):
        if artista[j].nome < pivot:
            i = i + 1
            artista[i], artista[j] = artista[j], artista[i]
    artista[i + 1], artista[high] = artista[high], artista[i + 1]
    return i + 1

#Estilo Artistico
def quicksort(estilo_art, low, high):
    if low < high:
        pi = partition(estilo_art, low, high)
        quicksort(estilo_art, low, pi-1)
        quicksort(estilo_art, pi+1, high)

def partition(estilo_art, low, high):
    
    pivot = estilo_art[high].nome
    i = low - 1
    for j in range(low, high):
        if estilo_art[j].nome < pivot:
            i = i + 1
            estilo_art[i], estilo_art[j] = estilo_art[j], estilo_art[i]
    estilo_art[i + 1], estilo_art[high] = estilo_art[high], estilo_art[i + 1]
    return i + 1

#Emprestimo
def quicksort(emprestimo, low, high):
    if low < high:
        pi = partition(emprestimo, low, high)
        quicksort(emprestimo, low, pi-1)
        quicksort(emprestimo, pi+1, high)

def partition(emprestimo, low, high):
    
    pivot = emprestimo[high].nome
    i = low - 1
    for j in range(low, high):
        if emprestimo[j].nome < pivot:
            i = i + 1
            emprestimo[i], emprestimo[j] = emprestimo[j], emprestimo[i]
    emprestimo[i + 1], emprestimo[high] = emprestimo[high], emprestimo[i + 1]
    return i + 1

#Visita Guiada
def quicksort(visitaGui, low, high):
    if low < high:
        pi = partition(visitaGui, low, high)
        quicksort(visitaGui, low, pi-1)
        quicksort(visitaGui, pi+1, high)

def partition(visitaGui, low, high):
    
    pivot = visitaGui[high].nome
    i = low - 1
    for j in range(low, high):
        if visitaGui[j].nome < pivot:
            i = i + 1
            visitaGui[i], visitaGui[j] = visitaGui[j], visitaGui[i]
    visitaGui[i + 1], visitaGui[high] = visitaGui[high], visitaGui[i + 1]
    return i + 1



def adicionar_obra():
    titulo = input("Título: ")
    data_criacao = input("Data de Criação: ")
    tema = input("Tema: ")
    estilo_artistico = input("Estilo Artístico: ")
    descricao = input("Descrição: ")
    tecnica = input("Técnica: ")
    autor = input("Autor: ")
    localizacao = input("Localização: ")

    obra = ObraDeArte(titulo, data_criacao, tema, estilo_artistico, descricao, tecnica, autor, localizacao)
    salvando_obras(obra)
    print(" A obra de Arte foi adicionada com sucesso, meu parça!")

def listar_obras():
    obras = carregando_obras()
    quicksort(obras, 0, len(obras) - 1)
    for obra in obras:
        print(f"Título da Obra: {obra.titulo}, Autor: {obra.autor}, Data de Criação: {obra.data_criacao}, Estilo: {obra.estilo_artistico}, Tema: {obra.tema}, Técnica: {obra.tecnica}, Localização: {obra.localizacao}, Descrição: {obra.descricao}")

def adicionar_artista():
    nome = input('Nome: ')
    data_nasc = input('Data de Nascimento: ')
    local_nasc = input('Local de Nascimento: ')
    biografia = input('Biografia: ')
    estilos = input("Estilo de Pintura: ")

    artista = Artistas(nome, data_nasc, local_nasc, biografia, estilos)
    salvando_artistas(artista)
    print('O Artista foi adicionado com sucesso, meu chapa!')

def listar_artistas():
    artistas = carregando_artistas()
    quicksort(artistas, 0, len(artistas) -1)
    for artista in artistas:
        print(f'Nome: {artista.nome}, Data de Nascimento: {artista.data_nascimento}, Local de Nascimento: {artista.local_nascimento}, Biografia:{artista.biografia}, Estilos: {artista.estilos}')

def adicionar_estilo_Art():
    denominacao = input('Denominação: ')
    periodo = input('Periodo: ')
    descricao = input('Descrição: ')
    escola = input('Escola: ')

    estilo_art = Estilo_Artistico(denominacao, periodo, descricao, escola)
    salvando_estilo_art(estilo_art)
    print('O estilo artistico foi adicionado com sucesso, meu chapa!')

def listar_estilo_art():
    estilo_arts = carregando_estilo_art()
    quicksort(estilo_arts, 0, len(estilo_arts) -1)
    for estilo_art in estilo_arts:
        print(f'Denominação: {estilo_art.denominacao}, Periodo: {estilo_art.periodo}, Descrição: {estilo_art.descricao}, Escola: {estilo_art.escola}')

def adicionar_emprestimos():
    obra = input('Obra: ')
    periodo = input('Periodo: ')
    evento = input('Evento: ')
    responsavel = input('Responsável: ')
    tema = input("Tema: ")

    emprestimo = Emprestimo(obra, periodo, evento, responsavel, tema)
    salvando_emprestimos(emprestimo)
    print('Emprestimo de Obras foi adicionado com sucesso, meu chapa!')

def listar_emprestimos():
    emprestimos = carregando_emprestimos()
    quicksort(emprestimos, 0, len(emprestimos) -1)
    for emprestimo in emprestimos:
        print(f'Obras: {"|".join(emprestimo.obra)}, Periodo: {emprestimo.periodo}, Evento: {emprestimo.evento}, Responsável: {emprestimo.responsavel}, Tema: {emprestimo.tema},')

def adicionar_visitaGui():
    tema = input('Tema: ')
    descricao = input('Descrição: ')
    obras = input('Obras: ')

    visita_Gui = VisitaGuiada(tema, descricao, obras)
    salvando_visitaGui(visita_Gui)
    print('Visita Guiada foi adicionado com sucesso, meu chapa!')

def listar_visitaGui():
    visistasGui = carregando_visitaGui()
    quicksort(visistasGui, 0, len(visistasGui) -1)
    for visita_Gui in visistasGui:
        print(f'Tema: {visita_Gui.tema}, Descrição: {visita_Gui.descricao}, Obras: {"|".join(visita_Gui.obras)}\n')


#Menu
def menu():
    while True:
        print(30 * "_")
        print("\nMenu:")
        print("1. Adicionar Obra de Arte")
        print("2. Listar Obras de Arte")
        print()
        print("3. Adicionar Artistas")
        print("4. Listar Artistas")
        print()
        print('5. Adicionar Emprestimos')
        print('6. Lista Emprestimos')
        print()
        print('7. Adicionar Visita Guiada')
        print('8. Lista de Visitas Guiadas')
        print()
        print('9. Adicionar Estilos Artisticos')
        print('10. Lista de Estilos Artisticos')
        print()
        print("11. Sair")
        print(30 * "_")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_obra()
        elif escolha == "2":
            listar_obras()
        elif escolha == "3":
            adicionar_artista()
        elif escolha == "4":
            listar_artistas()
        elif escolha == "5":
            adicionar_emprestimos()
        elif escolha == "6":
            carregando_emprestimos()
        elif escolha == "7":
            adicionar_visitaGui()
        elif escolha == "8":
            carregando_visitaGui()
        elif escolha == "9":
            adicionar_estilo_Art()
        elif escolha == "10":
            carregando_estilo_art()
        elif escolha == "11" or escolha == "sair":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
