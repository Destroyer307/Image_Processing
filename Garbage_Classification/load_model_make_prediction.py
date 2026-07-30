import torch
from model_create import GarbageClassifier

device = "cuda" if torch.cuda.is_available() else "cpu"

model_save_path = "models/GargabeClassification"

loaded_model = GarbageClassifier(input_shape = 3 , output_shape = 12)

loaded_model.load_state_dict(
    torch.load(model_save_path)
)