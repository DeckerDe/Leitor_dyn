
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import os
from scipy.interpolate import interp1d

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
        elif self.fam_name == "ME33":
            ax_ind.plot(self.time, self.kin_en, color="olive", linestyle=self.linest, label=self.fam_name + self.size)
        elif self.fam_name == "ME36":
            ax_ind.plot(self.time, self.kin_en, color="olive", linestyle=self.linest, label=self.fam_name + self.size)
        else:
            raise ValueError("Nome da família não especificado no plot da energia cin pelo tempo.")


def delta_kin_area_list(structs):
    me, so, hom = structure_count(structs)
    me = int((me + 1) / 3)
    so = int(so / 3)
    hom = int(hom)
    # print(me)
    # print(so)
    # print(hom)
    delta_kin_me = [np.zeros(me), np.zeros(me), np.zeros(me-1)]
    area_dens_me = [np.zeros(me), np.zeros(me), np.zeros(me-1)]
    delta_kin_so = [np.zeros(so), np.zeros(so), np.zeros(so)]
    area_dens_so = [np.zeros(so), np.zeros(so), np.zeros(so)]
    delta_kin_hom = np.zeros(hom)
    area_dens_hom = np.zeros(hom)

    idx_0250 = 0
    idx_0500 = 0
    idx_1000 = 0
    idx_0250_so = 0
    idx_0500_so = 0
    idx_1000_so = 0
    idx_hom = 0
    for struct in structs:
        # print(struct.fam_name)
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
        elif struct.fam_name[0:3] == "Hom":
            delta_kin_hom[idx_hom] = delta_kin
            area_dens_hom[idx_hom] = struct.area_density
            idx_hom += 1
    for i in range(3):
        area_dens_me[i], delta_kin_me[i] = sorting(area_dens_me[i], delta_kin_me[i])
        area_dens_so[i], delta_kin_so[i] = sorting(area_dens_so[i], delta_kin_so[i])
    area_dens_hom, delta_kin_hom = sorting(area_dens_hom, delta_kin_hom)

    return area_dens_me, area_dens_so, area_dens_hom, delta_kin_me, delta_kin_so, delta_kin_hom


def sorting(l1, l2):
    idx = np.argsort(l1)
    return l1[idx], l2[idx]


def hom_setup(structs):
    for struc in structs:
        if struc.fam_name[0:3] == "Hom":
            default_height = 1200
            struc.area_density = int(struc.size)/default_height


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


def kin_en_dens_line(area_dens_me, area_dens_so, area_dens_hom, delta_kin_me, delta_kin_so, delta_kin_hom):
    """
    Func para organizar os arrays com os resultados de delta kin e dens de area.

    :param area_dens_hom: densidade de area das estruturas homogoneas.
    :param area_dens_so: densidade de area das estruturas em S.
    :param area_dens_me: densidade de area das estruturas de master evans.
    :param delta_kin_me: delta de energia cin das estruturas de master evans.
    :param delta_kin_hom: delta de energia cin das estruturas homogeneas.
    :param delta_kin_so: delta de energia cin das estruturas em S.
    :return: Duas listas de arrays, em ordem kin_en, area_dens da maior pra menor estrutura.
    """
    fig_line_me, ax_lin_me = plt.subplots(figsize=(12, 8))
    fig_line_me.suptitle('Estrutura de Master Evans', fontsize=16)
    fig_line_so, ax_lin_so = plt.subplots(figsize=(12, 8))
    fig_line_so.suptitle('Estrutura em S', fontsize=16)
    fig_line_hom, ax_lin_hom = plt.subplots(figsize=(12, 8))
    fig_line_hom.suptitle('Chapas homogeneas', fontsize=16)
    fig_line_tot, ax_lin_tot = plt.subplots(figsize=(12, 8))
    fig_line_tot.suptitle('Todas as estruturas', fontsize=16)

    ax_lin_me.plot(area_dens_me[0], delta_kin_me[0], marker='o', color='lightsteelblue', label='10mm')
    ax_lin_me.plot(area_dens_me[1], delta_kin_me[1], marker='s', color='cornflowerblue', label='5mm')
    ax_lin_me.plot(area_dens_me[2], delta_kin_me[2], marker='P', color='blue', label='2.5mm')
    ax_lin_so.plot(area_dens_so[0], delta_kin_so[0], marker='o', color='lightcoral', label='10mm')
    ax_lin_so.plot(area_dens_so[1], delta_kin_so[1], marker='s', color='firebrick', label='5mm')
    ax_lin_so.plot(area_dens_so[2], delta_kin_so[2], marker='P', color='red', label='2.5mm')
    ax_lin_hom.plot(area_dens_hom, delta_kin_hom, marker='p', color='gold', label='Homogeneo')
    # Plot do graf de todas
    ax_lin_tot.plot(area_dens_me[0], delta_kin_me[0], marker='o', color='lightsteelblue', label='ME 10mm')
    ax_lin_tot.plot(area_dens_me[1], delta_kin_me[1], marker='s', color='cornflowerblue', label='ME 5mm')
    ax_lin_tot.plot(area_dens_me[2], delta_kin_me[2], marker='P', color='blue', label='ME 2.5mm')
    ax_lin_tot.plot(area_dens_so[0], delta_kin_so[0], marker='o', color='lightcoral', label='SO 10mm')
    ax_lin_tot.plot(area_dens_so[1], delta_kin_so[1], marker='s', color='firebrick', label='SO 5mm')
    ax_lin_tot.plot(area_dens_so[2], delta_kin_so[2], marker='P', color='red', label='SO 2.5mm')
    ax_lin_tot.plot(area_dens_hom, delta_kin_hom, marker='p', color='gold', label='Homogeneo')

    ax_lin_hom.set_xlabel('Massa relativa', fontsize=14)
    ax_lin_me.set_xlabel('Massa relativa', fontsize=14)
    ax_lin_so.set_xlabel('Massa relativa', fontsize=14)
    ax_lin_hom.set_ylabel('Absorção de energia cinética', fontsize=14)
    ax_lin_me.set_ylabel('Absorção de energia cinética', fontsize=14)
    ax_lin_so.set_ylabel('Absorção de energia cinética', fontsize=14)
    ax_lin_me.legend()
    ax_lin_me.grid()
    ax_lin_so.legend()
    ax_lin_so.grid()
    ax_lin_hom.grid()
    ax_lin_tot.grid()
    ax_lin_tot.legend()


def percentage_plot(area_me, area_so, area_hom, delta_me, delta_so, delta_hom):
    """
    Grafico com as porcentagens relativas das estruturas.

    :param area_me: densidade de area master evans
    :param area_so: densidade de area estrutura S
    :param area_hom: densidade de area hom
    :param delta_me: delta de energia cinetica master evans
    :param delta_so: delta de energia cinetica estrutura em S
    :param delta_hom: delta de energia cinetica homogenea
    :return: grafico das percentagens de absorc.
    """

    fig_pe_me, ax_pe_me = plt.subplots(figsize=(12, 8))
    fig_pe_me.suptitle('Grafico de desempenho', fontsize=16)

    fdelta_me = []
    f_area_me = []
    fdelta_so = []
    f_area_so = []

    for idx in range(3):
        fdelta_me.append(interp1d(area_me[idx], delta_me[idx]))
        f_area_me.append(np.linspace(area_me[idx][0], area_me[idx][len(area_me[idx])-1]))
        fdelta_so.append(interp1d(area_so[idx], delta_so[idx]))
        f_area_so.append(np.linspace(area_so[idx][0], area_so[idx][len(area_so[idx]) - 1]))

    fdelta_hom = interp1d(area_hom, delta_hom)
    f_area_hom = np.linspace(area_hom, area_hom[len(area_hom) - 1])

    delta_percent_me = delta_me
    for idx in range(3):
        for jdx in range(len(area_me[idx])):
            delta_percent_me[idx][jdx] = fdelta_me[idx](area_me[idx][jdx])/fdelta_hom(area_me[idx][jdx])
    # Falta um numero nas esturutras de 2.5 entao preciso colocar um zero na frente
    delta_percent_me[2] = np.hstack((0, delta_percent_me[2]))
    area_me[2] = np.hstack((0.35, area_me[2]))

    xpos = np.arange(0, 10)

    for idx in range(3):
        if idx == 0:
            cor = 'lightsteelblue'
            label = '10mm'
        elif idx == 1:
            cor = 'cornflowerblue'
            label = '5mm'
        else:
            cor = 'blue'
            label = '2.5mm'
        bar_width = 0.3
        ax_pe_me.bar(xpos + bar_width*idx, delta_percent_me[idx], bar_width, color=cor, label=label)

    x_labels = area_me[0] * 100
    for idx in range(len(area_me[0])):
        x_labels[idx] = int(x_labels[idx])

    ax_pe_me.set_xticks(np.arange(0, 10))
    ax_pe_me.set_xticklabels(x_labels)
    ax_pe_me.legend(loc='lower right')


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
for i in range(1, len(lines)-1):
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
hom_setup(structures)  # Setup da densidade de area dos homogeneos
area_dens_me, area_dens_so, area_dens_hom, delta_kin_me, delta_kin_so, delta_kin_hom = delta_kin_area_list(structures)
kin_en_dens_line(area_dens_me, area_dens_so, area_dens_hom, delta_kin_me, delta_kin_so, delta_kin_hom)
percentage_plot(area_dens_me, area_dens_so, area_dens_hom, delta_kin_me, delta_kin_so, delta_kin_hom)
for structure in structures:
    # print(structure.kin_en)
    # print(structure.fam_name, structure.size)
    # print(structure.kin_en_i, structure.kin_en_f, (structure.kin_en_i-structure.kin_en_f))
    structure.kin_en_plot()

# ax_scatter.legend(loc='lower right')
ax_ind.legend(loc='lower left')
plt.show()