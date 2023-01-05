#################IMPORTS FOR 3D ##########################

import kora.install.rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol
from stmol import showmol
import cirpy
import streamlit as st




########################IMPORTS FOR 2D#####################

#import streamlit as st
#from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image





# run c:/Users/Bliss Play/Desktop/chemlabprototype/streamlittttt.py

# running streamlit           streamlit run "c:/Users/NEXUS COMPUTERS/Desktop/Streamlit/streamlittttt.py"

def show(smi, style='stick'):
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.MMFFOptimizeMolecule(mol, maxIters=200)
    mblock = Chem.MolToMolBlock(mol)
    return mblock

def render_mol(xyz):
    xyzview = py3Dmol.view(width=500, height=500)#(width=400,height=400)
    xyzview.addModel(xyz,'mol')
    xyzview.setStyle({'stick':{}})
    xyzview.setBackgroundColor('white')
    xyzview.zoomTo()
    xyzview.spin(True)
    showmol(xyzview,height=500,width=500)

col1, col2 = st.columns(2)

with col1:
    image = Image.open("C:/Users/f/Downloads/LOGO-NEW-DARK.png")
    st.image(image, width=150)


with col2:
    st.text("")
    st.header("Molecular viewer", )


val= st.text_input('Enter the chemical name or Formula','Water') 
valval = cirpy.resolve(val, 'smiles')
blk=show(valval)



tab1, tab2 = st.tabs(["3D MODEL", "2D MODEL"])

with tab1:
    render_mol(blk)

with tab2:
    m= Chem.MolFromSmiles(valval)    
    im=Draw.MolToImage(m)
    final2d= st.image(im)  