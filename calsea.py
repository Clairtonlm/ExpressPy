import os
import datetime

def main():
    print(f"--------------TESTE DE CHAMADA----------------")
    print("Bem-vindo ao script de teste de chamadas do Seaticall!\n")

    # Solicitar ao usuário que digite o número para Callerid
    numero_callerid = input("Digite o número que deve discar (Callerid): \n")
    
    # Solicitar ao usuário que digite o número que vai discar
    numero_discado = input("Digite o número que vai discar (Extension): \n")
    
    # Solicitar ao usuário que digite a operadora
    operadora = input("Digite a operadora do número que vai discar: \n")

    # Captura a data e hora atual
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Definir o formato do callfile
    callfile_content = f"""Channel: SIP/1000
Callerid: {numero_callerid}
MaxRetries: 0
RetryInterval: 60
WaitTime: 30
Context: call-test
Extension: {numero_discado}
Priority: 1
"""

    # Definir o caminho do callfile
    callfile_path = f"/var/spool/asterisk/outgoing/callfile_{numero_discado}.call"

    # Criar o callfile
    try:
        with open(callfile_path, 'w') as callfile:
            callfile.write(callfile_content)
        print(f"\nCallfile criado com sucesso: {callfile_path}")
    except Exception as e:
        print(f"Erro ao criar o callfile: {e}")

    # Exibir o relatório detalhado
    print("\nRelatório de Chamada:")
    print(f"----------------------------------")
    print(f"Número que foi testado (Callerid): {numero_callerid}")
    print(f"Número para o qual discamos (Extension): {numero_discado}")
    print(f"Operadora: {operadora}")
    print(f"Data/Hora da discagem: {data_hora}")
    print(f"Status da chamada: Não executado (aguardando chamada)")
    print(f"----------------------------------\n")

if __name__ == "__main__":
    main()