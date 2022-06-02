import os

def formata(num):
    final = ''
    if float(num) > 1000:
        num = f'{float(num) / 1000:.2f}'
        final = 'KB'
        if float(num) > 1000:
            num = f'{float(num) / 1000:.2f}'
            final = 'MB'                        #em vez do f strin eu podia usar round(num, 2) para só ter 2 casas decimais
            if float(num) > 1000:
                num = f'{float(num) / 1000:.2f}'
                final = 'GB'
                if float(num) > 1000:
                    num = f'{float(num) / 1000:.2f}'
                    final = 'TB'
                    if float(num) > 1000:
                        num = f'{float(num) / 1000:.2f}'
                        final = 'PB'

    else:
        final = 'B'
    return f'{num} {final}'.replace('.', ',')


caminho_procura = input('Digite um caminho -> ')
termo_procura = input('Digite um termo de pesquisa -> ')
print()
contador = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura): #vai caminhar naquele caminho de procura ali que eu escolhi

    for arquivo in arquivos: # join junta e splitext divide
        if termo_procura in arquivo:  # vai pegar só os arquivos que começam com o termo de procura
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo) # tá juntando a raiz, o local de onde ele vem e o arquivo, assim você descobre o caminho
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo) # vai desempacotar o nome do arquivo e a extensão dele, MP4, txt, jpeg, etc
                tamanho = os.path.getsize(caminho_completo) # vai pegar o tamanho de cada arquivo, eu botei caminho_completo e não caminho_procura pq eu quero o tamanho individual de cada arquivo e não o tamanho da pasta mãe
                print(f'Encontrei um arquivo que possui o termo "{termo_procura}" ')  # o tamanho sempre vem em byte, eu vou fazer uma função depois que converte dinamicamente
                print(f'Nome -> {nome_arquivo}')
                print(f'Tipo -> {ext_arquivo}')
                print(f'Tamanho -> {formata(tamanho)}')
                print(f'Tamanho em bits -> {tamanho}')
                print()
            except PermissionError as error:
                print('Não possui permissão')
            except FileNotFoundError as error:
                print('Arquivo não encontrado')
            except Exception as error:
                print('Erro desconhecido', error)

print(f'{contador} arquivo(s) encontrado(s)')