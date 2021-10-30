import csv


class RemoverFavoritos:
    def __init__(self, musica):
        self._musica = musica
        
        musica_remover = [self._musica]

        musicas = None
        with open("favoritos.csv") as arquivo:
            musicas = arquivo.read().splitlines()
    
        for i in musica_remover:
            try:
                if i in musicas:
                    musicas.pop(musicas.index(i))
                else:
                    print(i + " is not found in the file")
            except ValueError:
                pass
    
        with open("favoritos.csv", "a", newline='') as arquivo:
            arquivo.seek(0)
            arquivo.truncate()
            musicaWriter = csv.writer(arquivo)
            for name in musicas:
                musicaWriter.writerow([str(name)])
        arquivo.close()


class AdicionarFavoritos:
    def __init__(self, musica):
        self._musica = musica

        with open('favoritos.csv', mode='r+', encoding='utf-8') as arquivo:
            lista = arquivo.readlines()
    
            if not f'{self._musica}\n' in lista:
                arquivo.write(self._musica + '\n')
                # print(self._musica)
            else:
                print("A música já é selecionada como Favorita!")
        arquivo.close()