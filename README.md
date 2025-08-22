<div align="center">
  <img src="https://raw.githubusercontent.com/VertigoFromOuterSpace/VertigoFromOuterSpace/main/.assets/glitch_divider.svg?v=7" alt="Glitch Divider"/>
</div>

‎ 
[vertigo@desktop ~]$ neofetch‎ 

7777          35            7777‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎vertigo@PC
777           55             777 ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎-----------
777       323755             777 ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎OS: Human/Linux Hybrid
777     759999999995         777 ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎Apelido: Vertigo
777     399999999994          77 ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎Foco: Cibersegurança e inteligência artificial
77      39999999999927         7 ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎Habilidades: Python, WebDevelopment, XSS, PromptInjection
77       736999999957          7 ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎
77       777 15943               ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎████████████████████████████████████████
77       35556494 152            ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎
77        3499995  65            ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎
7          7499993347           
7            232237             
77            39992             
77                              
7                               
  7                             

[vertigo@desktop ~]$ █
‎ 
‎ 
```diff
import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with random values
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

    def forward(self, X):
        # Forward propagation
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = np.tanh(self.z1)  # Activation function
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        exp_scores = np.exp(self.z2)
        self.probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        return self.probs

    def backward(self, X, y, learning_rate):
        # Backward propagation
        delta3 = self.probs
        delta3[range(len(X)), y] -= 1
        dW2 = np.dot(self.a1.T, delta3)
        db2 = np.sum(delta3, axis=0, keepdims=True)
        delta2 = np.dot(delta3, self.W2.T) * (1 - np.power(self.a1, 2))
        dW1 = np.dot(X.T, delta2)
        db1 = np.sum(delta2, axis=0)

        # Update weights
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1

    def train(self, X, y, epochs, learning_rate):
        for i in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)
            if i % 1000 == 0:
                loss = self.calculate_loss(X, y)
                print(f"Epoch {i}, Loss: {loss}")

    def calculate_loss(self, X, y):
        self.forward(X)
        correct_logprobs = -np.log(self.probs[range(len(X)), y])
        data_loss = np.sum(correct_logprobs) / len(X)
        return data_loss
