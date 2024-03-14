"""import psutil
import time

def monitorar_recursos():
    while True:
        # Obter o uso da CPU
        uso_cpu = psutil.cpu_percent(interval=1)
        
        # Obter o uso da memória RAM
        uso_memoria = psutil.virtual_memory().percent
        
        # Obter o uso do disco
        uso_disco = psutil.disk_usage('/').percent
        
        # Imprimir informações
        print(f'Uso da CPU: {uso_cpu}%')
        print(f'Uso da Memória: {uso_memoria}%')
        print(f'Uso do Disco: {uso_disco}%')
        print('-' * 30)
        
        # Aguardar um segundo antes de atualizar novamente
        time.sleep(1)

if __name__ == "__main__":
    monitorar_recursos()"""


"""import wmi
import time"""

"""def monitorar_recursos():
    # Conectar ao WMI
    c = wmi.WMI()

    while True:
        # Obter o uso da CPU
        for processo in c.Win32_PerfFormattedData_PerfOS_Processor():
            uso_cpu = processo.PercentProcessorTime
        
        # Obter o uso da memória RAM
        for memoria in c.Win32_OperatingSystem():
            uso_memoria = int(memoria.FreePhysicalMemory) / int(memoria.TotalVisibleMemorySize) * 100
        
        # Obter o uso do disco
        for disco in c.Win32_PerfFormattedData_PerfDisk_PhysicalDisk():
            if disco.Name == '_Total':
                uso_disco = disco.PercentDiskTime
        
        # Imprimir informações
        print(f'Uso da CPU: {uso_cpu}%')
        print(f'Uso da Memória: {uso_memoria}%')
        print(f'Uso do Disco: {uso_disco}%')
        print('-' * 30)
        
        # Aguardar um segundo antes de atualizar novamente
        time.sleep(1)

if __name__ == "__main__":
    monitorar_recursos()"""



import subprocess
import json

def obter_processos():
    # Executar o comando PowerShell para obter informações sobre os processos
    processo = subprocess.Popen(["powershell", "Get-Process | Select-Object * | ConvertTo-Json"], stdout=subprocess.PIPE)
    saida, _ = processo.communicate()
    
    # Tentar decodificar a saída usando diferentes codificações
    codificacoes = ['utf-8', 'utf-16', 'latin1']  # Tentar utf-8, utf-16 e latin1
    for codificacao in codificacoes:
        try:
            saida_decodificada = saida.decode(codificacao)
            # Se a decodificação for bem-sucedida, parar de tentar outras codificações
            break
        except UnicodeDecodeError:
            continue
    
    # Verificar se a saída não está vazia
    if saida_decodificada.strip():
        # Tentar analisar a saída como JSON
        try:
            processos = json.loads(saida_decodificada)
        except json.decoder.JSONDecodeError:
            print("Erro ao analisar a saída como JSON.")
            processos = []
    else:
        print("A saída está vazia.")
        processos = []
    
    return processos

if __name__ == "__main__":
    processos = obter_processos()
    
    # Exibir informações sobre os processos
    for processo in processos:
        print(processo['ProcessName'], processo['Id'], processo['WorkingSet'])

