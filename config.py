import torch


SUBROOT = f''
ROOT = f'/root/autodl-tmp/VisualKnowledgeTracing'
TRAINED_MODELS_FOLDER = f'{ROOT}/trained_models/'
VKT_DATASET_FOLDER = f'/root/autodl-tmp/VKT_Datasets'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')