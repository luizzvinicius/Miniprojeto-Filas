### Análise dos métodos seguindo a notação do BIG O:

### Equipe
1.João Victor Zignago  
2.Luiz Vinícius

#### Add(element):
**O(n)**: Diferentemente da fila circular, pelo fato de ter que passar por todos os elementos para verificar se o elemento a ser adicionado existe, faz com que ele deixe de ser O(1) e passe a ser O(n).

#### Remove(element):
**O(n)**: Como podemos remover o elemento em qualquer posição da lista, necessitamos encontrá-lo primeiro e em seguida remove-lo, esta operação para encontrar o elemento torna esse método O(n).

#### Contains(element):
**O(n)**: Para saber se o elemento existe na fila é necessário verificar todos os elementos existentes, isso torna o método O(n).

#### List():
**O(n)**: Temos que passar por todos os elementos para poder imprimi-los, tornando o método O(n).

#### Size():
**O(1)**: Como guardamos o valor de quantos elementos estão armazenados na fila.
