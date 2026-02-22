import torch
import torch.nn as nn

class EnergyTransformer(nn.Module):
    def __init__(self, feature_size=1, num_layers=2, nhead=1):
        super(EnergyTransformer, self).__init__()
        # Added batch_first=True to fix your UserWarning
        encoder_layers = nn.TransformerEncoderLayer(
            d_model=feature_size, 
            nhead=nhead, 
            batch_first=True 
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layers, num_layers)
        self.decoder = nn.Linear(feature_size, 1)

    def forward(self, src):
        # src shape: [batch, seq, features]
        output = self.transformer_encoder(src)
        return self.decoder(output[:, -1, :]) # Return last prediction