#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:50:46 2020

@author: kesaprm
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles



df_skin = pd.read_csv('Genes_skin.csv')
df_tongue = pd.read_csv('Genes_tongue.csv')
df_human = pd.read_csv('HumanData2_8056.csv')

df_skin = df_skin.fillna('')
df_skin = df_skin.apply(lambda x: x.astype(str).str.upper())
df_tongue = df_tongue.fillna('')
df_tongue = df_tongue.apply(lambda x: x.astype(str).str.upper())
df_human = df_human.fillna('')
df_human = df_human.apply(lambda x: x.astype(str).str.upper())


skin_up_24_common = set(df_skin['Upregulated_0-24'])& set(df_human['Gene'])
skin_up_120_common = set(df_skin['Upregulated_24-120'])& set(df_human['Gene'])
skin_up_240_common = set(df_skin['Upregualated_120-240'])& set(df_human['Gene'])
skin_down_24_common = set(df_skin['Downregulated_0-24'])& set(df_human['Gene'])
skin_down_120_common = set(df_skin['Downregulated_24-120'])& set(df_human['Gene'])
skin_down_240_common = set(df_skin['Downregulated_120-240'])& set(df_human['Gene'])

all_skin = set(df_skin['Upregulated_0-24']) | set(df_skin['Upregulated_24-120']) | set(df_skin['Upregualated_120-240']) | set(df_skin['Downregulated_0-24']) | set(df_skin['Downregulated_24-120']) |  set(df_skin['Downregulated_120-240'])
all_up_skin = set(df_skin['Upregulated_0-24']) | set(df_skin['Upregulated_24-120']) | set(df_skin['Upregualated_120-240'])
all_down_skin = set(df_skin['Downregulated_0-24']) | set(df_skin['Downregulated_24-120']) |  set(df_skin['Downregulated_120-240'])

tongue_up_24_common = set(df_tongue['Upregulated_0-24'])& set(df_human['Gene'])
tongue_up_120_common = set(df_tongue['Upregulated_24-120'])& set(df_human['Gene'])
tongue_up_240_common = set(df_tongue['Upregualated_120-240'])& set(df_human['Gene'])
tongue_down_24_common = set(df_tongue['Downregulated_0-24'])& set(df_human['Gene'])
tongue_down_120_common = set(df_tongue['Downregulated_24-120'])& set(df_human['Gene'])
tongue_down_240_common = set(df_tongue['Downregulated_120-240'])& set(df_human['Gene'])

all_tongue = set(df_tongue['Upregulated_0-24']) | set(df_tongue['Upregulated_24-120']) | set(df_tongue['Upregualated_120-240']) | set(df_tongue['Downregulated_0-24']) | set(df_tongue['Downregulated_24-120']) |  set(df_tongue['Downregulated_120-240'])
all_up_tongue = set(df_tongue['Upregulated_0-24']) | set(df_tongue['Upregulated_24-120']) | set(df_tongue['Upregualated_120-240'])
all_down_tongue = set(df_tongue['Downregulated_0-24']) | set(df_tongue['Downregulated_24-120']) |  set(df_tongue['Downregulated_120-240'])

all_all = set(all_skin) | set(all_tongue)

all_common = set(all_all) & set(df_human['Gene'])
up_skin_common = set(all_up_skin)  & set(df_human['Gene'])
down_skin_common = set(all_down_skin) & set(df_human['Gene'])
up_tongue_common = set(all_up_tongue)  & set(df_human['Gene'])
down_tongue_common = set(all_down_tongue) & set(df_human['Gene'])
all_skin_common = set(all_skin) & set(df_human['Gene'])
all_tongue_common =set(all_tongue) & set(df_human['Gene'])


# pd.Series(list(all_common)).to_csv("Human_genes/mouse_human_common_genes.csv", index=True)
# pd.Series(list(up_skin_common)).to_csv("Human_genes/mouseUpSkin_human_common_genes.csv", index=True)
# pd.Series(list(down_skin_common)).to_csv("Human_genes/mouseDownSkin_human_common_genes.csv", index=True)
# pd.Series(list(up_tongue_common)).to_csv("Human_genes/mouseUpTongue_human_common_genes.csv", index=True)
# pd.Series(list(down_tongue_common)).to_csv("Human_genes/mouseDownTongue_human_common_genes.csv", index=True)
# pd.Series(list(all_skin_common)).to_csv("Human_genes/mouseSkin_human_common_genes.csv",index=True)
# pd.Series(list(all_tongue_common)).to_csv("Human_genes/mouseTongue_human_common_genes.csv",index=True)

out = venn2([all_all, set(df_human['Gene'])],set_labels=('Mouse','Human'),alpha=0.6)
out.get_patch_by_id('11').set_color('yellow')
plt.show()

# for text in out.set_labels:
#     text.set_fontsize(10)
# for text in out.subset_labels:
#     text.set_fontsize(8)
# plt.show()

# predefined_neutrophils=['Stfa2l1', 'ly6g6d', 'cd177']
# pre_M1 = ['slfn4', 'Fpr1','Slfn1','Gp', 'Ccrl2', 'Fpr2', 'Cxcl10', 'Oasl1', 'Tlr2', 'Itgal', 'Herc', 'Cd300lf', 'Saa3', 'rsad2', 'mx1', 'Pyhin1', 'stat', 'cd80', 'ccl3', 'ccl2', 'ccl4']
# pre_M2 = ['MMP9', 'MMP13']


# pre_M1_U = [x.upper() for x in pre_M1]
# pre_neutrophils_U = [x.upper() for x in predefined_neutrophils]

# set(pre_M1_U) & set(df_human['Gene'])
# set(pre_neutrophils_U) & set(df_human['Gene'])
