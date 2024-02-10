from descriptors import c_qsar_features, p_qsar_features
from models import c_qsar, p_qsar

def predict_activity(input_dict):
    model = input_dict['model']
    smiles = input_dict['smiles']

    if model == 'c-qsar':
        features = c_qsar_features(smiles)
        bioactivity = c_qsar(features)
        return bioactivity
    
    if model == 'p-qsar':
        features = p_qsar_features(smiles)
        bioactivity = p_qsar(features)
        return bioactivity


    