import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


class Sim:
    """
    Classe base para cada um dos arquivos de dados.

    Attributes:
        file: Nome do arquivo onde está localizada a simulação.
        fam_name (string): Nome da familia, identificado como o primeiro conjunto antes do underscore.
        size (string): Tamanho da estrutura, atualmente pode ser 10mm = 1000, 5mm = 0500, 2.5mm = 0250.
    """
    fam_name: "Family not Determined"
    size: "Size not determined"

    def __init__(self, file, fam_name, size):
        arq_read = pd.read_csv(file, skiprows=2)
        self.kin_en = arq_read.iloc[:, 1]
        self.time = arq_read.iloc[:, 2]

        self.kin_en *= 1e-6

        self.fam_name = fam_name
        self.size = size

        if size == "10000":
            self.linest = "solid"
        elif size == "0500":
            self.linest = "dotted"
        elif size == "0250":
            self.linest = "dashed"
        else:
            self.linest = "dashdot"

    def plott(self): # Adicionar qualificadores para o plot
        """
        Faz o gráfico da energia cinética pelo tempo, hoje é necessário criar um ax_ind dentro de uma fig para que tudo funcione.
        Cada família deve ter seu estilo de gráfico. A mesma cor, porém com estilos diferentes de linha.
        :return: Ordem para um ax chamado ax_ind fazer o gráfico de energia cinética pelo tempo.
        """

        if self.fam_name == "Hom":
            ax_ind.plot(self.kin_en, self.time, color="green", linestyle=self.linest)
        elif self.fam_name == "SO00":
            ax_ind.plot(self.kin_en, self.time, color="yellow", linestyle=self.linest)
        elif self.fam_name == "SO05":
            ax_ind.plot(self.kin_en, self.time, color="blue", linestyle=self.linest)
        elif self.fam_name == "MEa1":
            ax_ind.plot(self.kin_en, self.time, color="red", linestyle=self.linest)
        else:
            raise ValueError("Nome da família não especificado.")


fig_ind, ax_ind = plt.subplots(figsize=(12, 8))
structures = []
structure_counter = 0

for fil in os.listdir("Arquivos_Sim_leitura"):
    if fil.endswith(".uhs"):
        name = fil
        # print(fil)

        name = name.split('_')
        # print(name)
        fam_name = name[0]
        print(fam_name)
        size = name[1]
        size = size.rsplit('.')
        size = size[0]
        print(size)
        file_name = os.path.join("Arquivos_Sim_leitura", fil)

        structures.append(Sim(file_name, fam_name, size))
        print(structures[structure_counter].linest)
        structure_counter += 1

print(len(structures))


for structure in structures:
    structure.plott()

plt.show()
# Consigo ler os arquivos e criar um objeto leitura por arquivo, agora falta unir os graficos e dar uma garibada.
# Falta também definir o grafico conjunto e relativo, assim como o jeito de atualizar os arquivos.
