import py3Dmol
import rdkit
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw, PandasTools
from stmol import makeobj, render_pdb, showmol

# set basic page config
st.set_page_config(page_title="Streamlit RDKit",
                    page_icon=':test_tube:',
                    layout='centered',
                    initial_sidebar_state='collapsed')

# apply custom css if needed
# with open('assets/styles/style.css') as css:
#     st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.title('Streamlit RDKit Example Project :test_tube:')
    st.markdown("""This app is only a simple example project to test **RDKit** with Streamlit.""")
    # load mol object from sdf file
    df = PandasTools.LoadSDF(filename="example.sdf")
    molid = df['ID'][0]
    mol = df['ROMol'][0]
    # load sdf file as string
    with open("example.sdf", "r", encoding='utf-8') as f:
        sdf = f.read()
    # show mol object as dataframe
    st.header('Molecule Dataframe')
    st.dataframe(df)
    # show id
    st.header('Molecule ID')
    st.info(molid)
    # renders mol object to pillow image object
    img = Draw.MolToImage(mol=mol, size=(720, 720))
    # show image with streamlit
    st.header('Molecule Image')
    st.image(img)
    # show 3d mol object with streamlit
    st.header('Molecule 3D Image')
    xyzview = makeobj(xyz=sdf, molformat='sdf', style='stick', background='white')
    xyzview.setStyle({'cartoon':{'color':'spectrum'}})
    showmol(xyzview, height=720, width=720)
