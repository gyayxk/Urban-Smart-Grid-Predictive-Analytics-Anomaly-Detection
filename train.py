import torch
import torch.nn as nn
import pandas as pd
from database import engine
from model import EnergyTransformer

def train_ai():
    # 1. Fetch data from DB
    df = pd.read_sql("SELECT consumption FROM energy_consumption", engine)
    
    if len(df) < 20:
        print("Need more data! Run simulator.py for 2-3 minutes first.")
        return

    # 2. Convert data to [Batch, Seq, Features]
    # We use a simple window of the last 10 readings to predict the next
    data_values = df['consumption'].values[-20:] 
    inputs = torch.FloatTensor(data_values[:-1]).view(1, -1, 1) # All except last
    targets = torch.FloatTensor([data_values[-1]]).view(1, 1)    # The last one

    model = EnergyTransformer(feature_size=1)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    print("🚀 Training started...")
    for epoch in range(100):
        optimizer.zero_grad()
        output = model(inputs)
        loss = criterion(output, targets)
        loss.backward()
        optimizer.step()
        
        if epoch % 20 == 0:
            print(f"Epoch {epoch} | Loss: {loss.item():.6f}")

    # 3. SAVE THE WEIGHTS (This creates the file!)
    torch.save(model.state_dict(), "transformer_weights.pth")
    print("✅ Training complete! 'transformer_weights.pth' created.")

if __name__ == "__main__":
    train_ai()