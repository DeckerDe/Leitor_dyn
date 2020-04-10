# TODO: Verificar dados para entender o motivo de mudar o comportamento entre as estruturas.
# TODO: Programar gr[aficos individuais.

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import os

matplotlib.rc('xtick', labelsize=11)
matplotlib.rc('ytick', labelsize=11)


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
        Faz o gráfico da energia cinética pelo tempo, hoje é necessário criar um ax_ind dentro de uma fig
        para que tudo funcione.
        :return: Ordem para um ax chamado ax_ind fazer o gráfico de energia cinética pelo tempo.
        """

        if self.fam_name == "Hom":
            ax_ind.plot(self.time, self.kin_en, color="green", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "SO09":
            ax_ind.plot(self.time, self.kin_en, color="black", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "SO18":
            ax_ind.plot(self.time, self.kin_en, color="blue", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "SO23":
            ax_ind.plot(self.time, self.kin_en, color="peru", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME10":
            ax_ind.plot(self.time, self.kin_en, color="red", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME14":
            ax_ind.plot(self.time, self.kin_en, color="crimson", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME07":
            ax_ind.plot(self.time, self.kin_en, color="yellow", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "SO14":
            ax_ind.plot(self.time, self.kin_en, color="darkorchid", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME19":
            ax_ind.plot(self.time, self.kin_en, color="dodgerblue", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME22":
            ax_ind.plot(self.time, self.kin_en, color="sandybrown", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME25":
            ax_ind.plot(self.time, self.kin_en, color="gold", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME28":
            ax_ind.plot(self.time, self.kin_en, color="fuchsia", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME31":
            ax_ind.plot(self.time, self.kin_en, color="olive", linestyle=self.linest, label=self.fam_name + self.size)
        else:
            raise ValueError("Nome da família não especificado no plot da energia cin pelo tempo.")

    # def kin_en_scatter(self):
    #     """
    #     Faz o gráfico da energia cinética pela densidade de area, hoje é necessário criar um ax_sctr dentro de uma fig
    #      para que tudo funcione.
    #     :return: Ordem para um ax chamado ax_ind fazer o gráfico de energia cinética pelo tempo.
    #     """
    #     delta_kin = self.kin_en_i - self.kin_en_f
    #     if self.fam_name == "Hom":
    #         if self.size == "0600":
    #             self.area_density = 0.5
    #         else:
    #             self.area_density = 1.0
    #         # ax_scatter.scatter(self.area_density, delta_kin, color="green", label=self.fam_name + self.size)
    #     elif self.fam_name == "SO09":
    #         ax_scatter.scatter(self.area_density, delta_kin, color="black", marker=self.marker,
    #                            label=self.fam_name + self.size)
    #     elif self.fam_name == "SO18":
    #         ax_scatter.scatter(self.area_density, delta_kin, color="blue", marker=self.marker,
    #                            label=self.fam_name + self.size)
    #     elif self.fam_name == "ME10":
    #         ax_scatter.scatter(self.area_density, delta_kin, color="red", marker=self.marker,
    #                            label=self.fam_name + self.size)
    #     elif self.fam_name == "ME14":
    #         ax_scatter.scatter(self.area_density, delta_kin, color="crimson", marker=self.marker,
    #                            label=self.fam_name + self.size)
    #     elif self.fam_name == "ME07":
    #         ax_scatter.scatter(self.area_density, delta_kin, color="yellow", marker=self.marker,
    #                            label=self.fam_name + self.size)
    #     elif self.fam_name == "SO14":
    #         ax_scatter.scatter(self.area_density, delta_kin, color="darkorchid", marker=self.marker,
    #                            label=self.fam_name + self.size)
    #     elif self.fam_name == "ME19":
    #         ax_scatter.scatter(self.area_density, delta_kin, color="dodgerblue", marker=self.marker,
    #                            label=self.fam_name + self.size)
    #     elif self.fam_name == "ME22":
    #         ax_scatter.scatter(self.area_density, delta_kin, color="sandybrown", marker=self.marker,
    #                            label=self.fam_name + self.size)
    #     elif self.fam_name == "ME25":
    #         ax_scatter.scatter(self.area_density, delta_kin, color="gold", marker=self.marker,
    #                            label=self.fam_name + self.size)
    #     else:
    #         raise ValueError("Nome da família não especificado no scatter kin_en vs area.")
    #


def sorting(l1, l2):
    idx = np.argsort(l1)
    return l1[idx], l2[idx]


def structure_count(structs):
    ME = 0
    SO = 0
    HOM = 0
    for struc in structs:
        if struc.fam_name[0:2] == "ME":
            ME += 1
        elif struc.fam_name[0:2] == "SO":
            SO += 1
        elif struc.fam_name[0:3] == "Hom":
            HOM += 1
        else:
            raise ValueError("Nome da família não especificado no contador de estruturas.")
    return ME, SO, HOM


def kin_en_dens_line(structs):
    """
    Func para organizar os arrays com os resultados de delta kin e dens de area.

    :param structs: lista de estruturas
    :return: Duas listas de arrays, em ordem kin_en, area_dens da maior pra menor estrutura.
    """
    fig_line_me, ax_lin_me = plt.subplots(figsize=(12, 8))
    fig_line_me.suptitle('Estrutura de Master Evans', fontsize=16)
    fig_line_so, ax_lin_so = plt.subplots(figsize=(12, 8))
    fig_line_so.suptitle('Estrutura em S', fontsize=16)
    me, so, hom = structure_count(structs)
    me = int((me + 1) / 3)
    so = int(so / 3)
    print(me)
    print(so)
    delta_kin_me = [np.zeros(me), np.zeros(me), np.zeros(me-1)]
    area_dens_me = [np.zeros(me), np.zeros(me), np.zeros(me-1)]
    delta_kin_so = [np.zeros(so), np.zeros(so), np.zeros(so)]
    area_dens_so = [np.zeros(so), np.zeros(so), np.zeros(so)]

    idx_0250 = 0
    idx_0500 = 0
    idx_1000 = 0
    idx_0250_so = 0
    idx_0500_so = 0
    idx_1000_so = 0
    for struct in structs:
        delta_kin = struct.kin_en_i - struct.kin_en_f
        if struct.fam_name[0:2] == "ME":
            if struct.size == "0250":
                delta_kin_me[2][idx_0250] = delta_kin
                area_dens_me[2][idx_0250] = struct.area_density
                idx_0250 += 1
            elif struct.size == "0500":
                delta_kin_me[1][idx_0500] = delta_kin
                area_dens_me[1][idx_0500] = struct.area_density
                idx_0500 += 1
            elif struct.size == "1000":
                delta_kin_me[0][idx_1000] = delta_kin
                area_dens_me[0][idx_1000] = struct.area_density
                idx_1000 += 1
        elif struct.fam_name[0:2] == "SO":
            if struct.size == "0250":
                delta_kin_so[2][idx_0250_so] = delta_kin
                area_dens_so[2][idx_0250_so] = struct.area_density
                idx_0250_so += 1
            elif struct.size == "0500":
                delta_kin_so[1][idx_0500_so] = delta_kin
                area_dens_so[1][idx_0500_so] = struct.area_density
                idx_0500_so += 1
            elif struct.size == "1000":
                delta_kin_so[0][idx_1000_so] = delta_kin
                area_dens_so[0][idx_1000_so] = struct.area_density
                idx_1000_so += 1
    for i in range(3):
        area_dens_me[i], delta_kin_me[i] = sorting(area_dens_me[i], delta_kin_me[i])
        area_dens_so[i], delta_kin_so[i] = sorting(area_dens_so[i], delta_kin_so[i])

    ax_lin_me.plot(area_dens_me[0], delta_kin_me[0], marker='o', color='lawngreen', label='10mm')
    ax_lin_me.plot(area_dens_me[1], delta_kin_me[1], marker='s', color='dodgerblue', label='5mm')
    ax_lin_me.plot(area_dens_me[2], delta_kin_me[2], marker='P', color='red', label='2.5mm')
    ax_lin_so.plot(area_dens_so[0], delta_kin_so[0], marker='o', color='seagreen', label='10mm')
    ax_lin_so.plot(area_dens_so[1], delta_kin_so[1], marker='s', color='steelblue', label='5mm')
    ax_lin_so.plot(area_dens_so[2], delta_kin_so[2], marker='P', color='crimson', label='2.5mm')
    ax_lin_me.set_xlabel('Densidade de área', fontsize=14)
    ax_lin_so.set_xlabel('Densidade de área', fontsize=14)
    ax_lin_me.set_ylabel('Absorção de energia cinética', fontsize=14)
    ax_lin_so.set_ylabel('Absorção de energia cinética', fontsize=14)
    ax_lin_me.legend()
    ax_lin_me.grid()
    ax_lin_so.legend()
    ax_lin_so.grid()


fig_ind, ax_ind = plt.subplots(figsize=(12, 8))
# fig_sct, ax_scatter = plt.subplots(figsize=(12, 8))
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
        # print(fam_name)
        size = name[1]
        size = size.rsplit('.')
        size = size[0]
        # print(size)
        file_name = os.path.join("Arquivos_Sim_leitura", fil)

        structures.append(Sim(file_name, fam_name, size))
        structure_counter += 1

# print("Contador de estruturas", structure_counter)
areas_arq = open("Arquivos_Sim_leitura/areas.txt", 'r')
lines = areas_arq.readlines()
for i in range(1, len(lines)):
    # print(i)
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

# Plot da kin_en pela densidade de area.
kin_en_dens_line(structures)

for structure in structures:
    # print(structure.kin_en)
    # print(structure.fam_name, structure.size)
    # print(structure.kin_en_i, structure.kin_en_f, (structure.kin_en_i-structure.kin_en_f))
    structure.kin_en_plot()
    # structure.kin_en_scatter()

# ax_scatter.legend(loc='lower right')
ax_ind.legend(loc='lower left')
plt.show()