# Escolha Difícil - Desafio Beecrowd 2024

## 📋 Descrição do Problema
Durante um voo, as companhias aéreas oferecem refeições aos passageiros. Normalmente, as aeromoças empurram um carrinho com refeições e perguntam aos passageiros suas preferências de **frango**, **bife** ou **massa** quando chegam à sua fileira.

Neste desafio, o procedimento foi alterado: **primeiro** todos os passageiros informam suas escolhas de refeições, e **depois** a aeromoça verifica se há refeições suficientes disponíveis para atender todos os pedidos. Se o número de refeições disponíveis não for suficiente para alguma das opções, alguns passageiros ficarão sem sua refeição desejada.

**Seu objetivo** é ajudar a aeromoça a determinar quantos passageiros, com base nos pedidos realizados, não conseguirão a refeição escolhida.

## 🚀 Exemplo de Funcionamento
Dado o número de refeições disponíveis e o número de pedidos realizados para cada tipo de refeição, o programa deve calcular quantos passageiros não conseguirão sua escolha preferida.

### 📝 Exemplo de Entrada
```
80 20 40
45 23 48
```

### 💡 Exemplo de Saída
```
11
```

### 📝 Explicação do Exemplo
- **Frango**: 80 disponíveis, 45 pedidos → Todos atendidos.
- **Bife**: 20 disponíveis, 23 pedidos → Faltam 3.
- **Massa**: 40 disponíveis, 48 pedidos → Faltam 8.

**Total** de passageiros sem suas escolhas = 3 (bife) + 8 (massa) = **11**.

## 💻 Solução em Python
O programa recebe dois conjuntos de entradas:
- O primeiro conjunto representa a quantidade de refeições disponíveis para frango, bife e massa.
- O segundo conjunto representa a quantidade de pedidos realizados para frango, bife e massa.

O cálculo é feito subtraindo o número de pedidos da quantidade disponível para cada tipo de refeição. Se a diferença for negativa, significa que há passageiros que não serão atendidos. A soma dessas diferenças resulta na quantidade total de passageiros que ficarão sem suas escolhas.

### 🔧 Código
```python
def main():
    # Lê a quantidade de refeições disponíveis (Ca, Ba, Pa)
    Ca, Ba, Pa = map(int, input().split())
    
    # Lê a quantidade de refeições requisitadas (Cr, Br, Pr)
    Cr, Br, Pr = map(int, input().split())
    
    # Calcula o número de passageiros que ficarão sem suas escolhas
    faltam_frango = max(0, Cr - Ca)
    faltam_bife = max(0, Br - Ba)
    faltam_massa = max(0, Pr - Pa)
    
    # Soma o total de passageiros não atendidos e imprime o resultado
    print(faltam_frango + faltam_bife + faltam_massa)

if __name__ == "__main__":
    main()
```

## 📚 Explicação do Código
1. **Leitura de entrada**:
   - A primeira linha contém três inteiros (`Ca`, `Ba`, `Pa`), que representam o número de refeições disponíveis.
   - A segunda linha contém três inteiros (`Cr`, `Br`, `Pr`), que representam o número de refeições requisitadas.
   
2. **Cálculo de refeições insuficientes**:
   - Calcula quantas refeições faltam para cada tipo (frango, bife, massa).
   - Se a quantidade de pedidos exceder o disponível, a diferença é somada.

3. **Resultado**:
   - O programa imprime a soma das diferenças negativas (ou seja, o total de passageiros não atendidos).

## 🛠️ Como Rodar o Programa
Certifique-se de ter o Python instalado. Salve o código em um arquivo, por exemplo, `escolha_dificil.py`. No terminal, execute:
```bash
python3 escolha_dificil.py
```

## 🏆 Exemplos de Teste
Aqui estão alguns exemplos adicionais para testar o programa:

### Entrada:
```
0 0 0
100 100 100
```
### Saída:
```
300
```

### Entrada:
```
41 42 43
41 42 43
```
### Saída:
```
0
```

---

**Resolução do problema**: ICPC Latin American Regional – 2017
