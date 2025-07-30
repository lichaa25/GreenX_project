import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

# Define your Graph Convolutional Network (GCN)
class GCN(torch.nn.Module):
    def _init_(self, in_channels, hidden_channels, out_channels):
        super(GCN, self)._init_()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# Reusable training function
def train_gcn(model, data, epochs=100, lr=0.01):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=5e-4)
    model.train()

    for epoch in range(epochs):
        optimizer.zero_grad()
        out = model(data)
        loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0 or epoch == epochs - 1:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
            "import torch; print(torch._version_)"