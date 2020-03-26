# TODO: Verificar dados para entender o motivo de mudar o comportamento entre as estruturas.
# TODO: Programar gr[aficos individuais.

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
    sqr_height = -1
    sqr_width = -1
    sqr_area = -1
    surf_area = -1
    area_density = -1

    def __init__(self, file, fam_name, size):
        arq_read = pd.read_csv(file, skiprows=2)
        self.kin_en = arq_read.iloc[:, 2]
        self.time = arq_read.iloc[:, 1]

        self.kin_en *= 1e-6

        self.kin_en_i = self.kin_en[0]
        self.kin_en_f = self.kin_en[len(self.kin_en)-1]

        self.fam_name = fam_name
        self.size = size

        if size == "1000":
            self.linest = "solid"
            self.marker = "o"
        elif size == "0500":
            self.linest = "dotted"
            self.marker = "s"
        elif size == "0250":
            self.linest = "dashed"
            self.marker = "P"
        else:
            self.linest = "dashdot"

    def kin_en_plot(self):
        """
        Faz o gráfico da energia cinética pelo tempo, hoje é necessário criar um ax_ind dentro de uma fig para que tudo funcione.
        Cada família deve ter seu estilo de gráfico. A mesma cor, porém com estilos diferentes de linha.
        :return: Ordem para um ax chamado ax_ind fazer o gráfico de energia cinética pelo tempo.
        """

        if self.fam_name == "Hom":
            ax_ind.plot(self.time, self.kin_en, color="green", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "SO00":
            ax_ind.plot(self.time, self.kin_en, color="black", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "SO05":
            ax_ind.plot(self.time, self.kin_en, color="blue", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME00":
            ax_ind.plot(self.time, self.kin_en, color="red", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME05":
            ax_ind.plot(self.time, self.kin_en, color="crimson", linestyle=self.linest, label=self.fam_name + self.size)
        else:
            raise ValueError("Nome da família não especificado.")

    def kin_en_scatter(self):
        """
        Faz o gráfico da energia cinética pelo tempo, hoje é necessário criar um ax_ind dentro de uma fig para que tudo funcione.
        Cada família deve ter seu estilo de gráfico. A mesma cor, porém com estilos diferentes de linha.
        :return: Ordem para um ax chamado ax_ind fazer o gráfico de energia cinética pelo tempo.
        """
        delta_kin = self.kin_en_i - self.kin_en_f
        if self.fam_name == "Hom":
            self.area_density = 1
            # ax_scatter.scatter(self.area_density, delta_kin, color="green", label=self.fam_name + self.size)
        elif self.fam_name == "SO00":
            ax_scatter.scatter(self.area_density, delta_kin, color="black", marker=self.marker,
                               label=self.fam_name + self.size)
        elif self.fam_name == "SO05":
            ax_scatter.scatter(self.area_density, delta_kin, color="blue", marker=self.marker,
                               label=self.fam_name + self.size)
        elif self.fam_name == "ME00":
            ax_scatter.scatter(self.area_density, delta_kin, color="red", marker=self.marker,
                               label=self.fam_name + self.size)
        elif self.fam_name == "ME05":
            ax_scatter.scatter(self.area_density, delta_kin, color="crimson", marker=self.marker,
                               label=self.fam_name + self.size)
        else:
            raise ValueError("Nome da família não especificado.")


fig_ind, ax_ind = plt.subplots(figsize=(12, 8))
fig_sct, ax_scatter = plt.subplots(figsize=(12, 8))
structures = []
structure_counter = 0

# Realiza a leitura dos dados de cada arquivo. E gera uma lista de estruturas.
for fil in os.listdir("Arquivos_Sim_leitura"):
    if fil.endswith(".uhs"):
        name = fil
        # print(fil)

        name = name.split('_')
        # print(name)
        fam_name = name[0]
        #print(fam_name)
        size = name[1]
        size = size.rsplit('.')
        size = size[0]
        #print(size)
        file_name = os.path.join("Arquivos_Sim_leitura", fil)

        structures.append(Sim(file_name, fam_name, size))
        # print(structures[structure_counter].linest)
        structure_counter += 1

# print(len(structures))

areas_arq = open("Arquivos_Sim_leitura/areas.txt", 'r')
lines = areas_arq.readlines()
for i in range(1, len(lines)):
    line_split = lines[i].split()
    name = line_split[0]
    name_split = name.split('_')
    fam = name_split[0]
    size = name_split[1]
    # print(fam, size)
    height = float(line_split[2])
    width = float(line_split[4])
    area = float(line_split[6])
    # print(height, width, area)
    # Inclusao destes dados nas estruturas.
    for structure in structures:
        if fam == structure.fam_name and size == structure.size:
            structure.sqr_height = height
            structure.sqr_width = width
            structure.surf_area = area
            structure.sqr_area = height*width
            structure.area_density = structure.surf_area/structure.sqr_area

areas_arq.close()

for structure in structures:
    #print(structure.kin_en)
    print(structure.fam_name, structure.size)
    print(structure.kin_en_i, structure.kin_en_f, (structure.kin_en_i-structure.kin_en_f))
    structure.kin_en_plot()
    structure.kin_en_scatter()

ax_scatter.legend(loc='lower right')
ax_ind.legend(loc='lower left')
plt.show()