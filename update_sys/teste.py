"""import psutil

def list_dispositivos():
    dispositivos = []
    for particao in psutil.disk_partitions():
        dispositivo = {
            'dispositivo':particao.device,
            'ponto_de_montagem':particao.mountpoint,
            'tipo':particao.fstype
        }
        dispositivos.append(dispositivo)

    return dispositivos

listar_dispositivos_conectados = list_dispositivos()
for dispositivo in listar_dispositivos_conectados:
    print(f"Dispositivo:{dispositivo['dispositivo']}, Ponto de Montagem: {dispositivo['ponto_de_montagem']}, tipo: {dispositivo['tipo']}\n")"""
