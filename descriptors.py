from padelpy import from_smiles

def generate_descriptors (smiles):
    descriptors = from_smiles(smiles)
    return descriptors

def c_qsar_features (smiles):
    input_features = { }
    descriptors = generate_descriptors(smiles)

    input_features['ATSC6v'] = descriptors['ATSC6v']
    input_features['VR1_Dzp'] = descriptors['VR1_Dzp']
    input_features['VR2_Dzp'] = descriptors['VR2_Dzp']
    input_features['SpMin5_Bhp'] = descriptors['SpMin5_Bhp']
    input_features['ETA_dAlpha_B'] = descriptors['ETA_dAlpha_B']

    features = list(input_features.values())
    return features


def p_qsar_features (smiles):
    input_features = { }
    descriptors = generate_descriptors(smiles)

    input_features['AATS1v'] = descriptors['AATS1v']
    input_features['ATSC4m'] = descriptors['ATSC4m']
    input_features['MATS2i'] = descriptors['MATS2i']
    input_features['GATS2c'] = descriptors['GATS2c']
    input_features['JGI9'] = descriptors['JGI9']

    features = list(input_features.values())
    return features
