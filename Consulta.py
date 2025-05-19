from datetime import datetime

consultas = []

def menu():
    while True:
        print("\n--- Sistema de Agendamento ---")
        print("1. Agendar consultas")
        print("2. Listar consultas")
        print("3. Cancelar consultas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")  
        if opcao.isdigit() and 1 <= int(opcao) <= 4: 
            return int(opcao) 
        else:
            print("Opção inválida! Digite um número de 1 a 4.")

def validar_data(data):
    try:
        data_obj = datetime.strptime(data, "%d/%m/%Y").date()
        data_atual = datetime.now().date()
        if data_obj >= data_atual:
            return True
        else:
            print("Data inválida. Apenas datas futuras ou de hoje são permitidas.")
            return False
    except ValueError:
        print("Formato de data inválido. Use DD/MM/AAAA (ex: 20/05/2025).")
        return False

def validar_horario(horario):
    try:
        horario_obj = datetime.strptime(horario, "%H:%M").time()
        horario_inicio = datetime.strptime("11:00", "%H:%M").time()
        horario_fim = datetime.strptime("19:00", "%H:%M").time()
        if horario_inicio <= horario_obj <= horario_fim:
            return True
        else:
            print("Horário fora do intervalo permitido (11:00 - 19:00).")
            return False
    except ValueError:
        print("Formato de horário inválido. Use HH:MM (ex: 14:00).")
        return False

def agendar_consulta():
    print("\n--- Agendar Consulta ---")
    nome_paciente = input("Nome do paciente: ")
    especialidade = input("Especialidade (ex: Cardiologia, Pediatria): ")

    while True:
        data = input("Data da consulta (ex: 20/05/2025): ")
        if validar_data(data):
            break

    while True:
        horario = input("Horário da consulta (ex: 14:00): ")
        if validar_horario(horario):
            break

    consulta = {"paciente": nome_paciente, "especialidade": especialidade, "data": data, "horario": horario}
    consultas.append(consulta)
    print("Consulta agendada com sucesso!")

def listar_consultas():
    print("\n--- Consultas Agendadas ---")
    if len(consultas) == 0:
        print("Nenhuma consulta agendada.")
    else:
        for i, consulta in enumerate(consultas, start=1):
            print(f"{i}. {consulta['paciente']} - {consulta['especialidade']} - {consulta['data']} - {consulta['horario']}")

def cancelar_consulta():
    print("\n--- Cancelar Consulta ---")
    listar_consultas()
    if len(consultas) > 0:
        try:
            opcao = int(input("Digite o número da consulta que deseja cancelar: "))
            if 1 <= opcao <= len(consultas):
                consulta_removida = consultas.pop(opcao - 1)
                print(f"Consulta de {consulta_removida['paciente']} cancelada com sucesso!")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    else:
        print("Não há consultas para cancelar.")

def executar_sistema():
    while True:
        opcao = menu()
        if opcao == 1:
            agendar_consulta()
        elif opcao == 2:
            listar_consultas()
        elif opcao == 3:
            cancelar_consulta()
        elif opcao == 4:
            print("Saindo do sistema...")
            break

executar_sistema()
