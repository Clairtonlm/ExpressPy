import os
import datetime

def main():
    print(f"--------------TESTE DE CHAMADA----------------")
    print("Bem-vindo ao script de teste de chamadas do Seaticall!\n")

    # Solicitar ao usuário que digite o número que vai ser testado (Callerid)
    numero_callerid = input("Digite o número que será testado (Callerid - ex: 8521807018): \n")
    
    # Solicitar ao usuário que digite o número que vai discar (Extension)
    numero_discado = input("Digite o número que vai discar (ex: 085998689105): \n")

    # Captura a data e hora atual
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Definir o formato do callfile
    callfile_content = f"""Channel: local/{numero_discado}@call-test
Callerid: {numero_callerid}
MaxRetries: 2
RetryInterval: 300
WaitTime: 45
Application: Hangup
Set: TIMEOUT(dial)=20
Archive: yes
"""

    # Definir o caminho do callfile
    callfile_path = f"/var/spool/asterisk/outgoing/callfile_{numero_discado}.call"

    # Criar o callfile
    try:
        with open(callfile_path, 'w') as callfile:
            callfile.write(callfile_content)
        print(f"\nCallfile criado com sucesso: {callfile_path}\n")
    except Exception as e:
        print(f"Erro ao criar o callfile: {e}")

    # Exibir o relatório detalhado
    print("Relatório de Chamada:")
    print(f"----------------------------------")
    print(f"Número que foi testado (Callerid): {numero_callerid}")
    print(f"Número que vai ser discado (Extension): {numero_discado}")
    print(f"Data/Hora da discagem: {data_hora}")
    print(f"Status da chamada: Não executado (aguardando chamada)")
    print(f"----------------------------------\n")

if __name__ == "__main__":
    main()