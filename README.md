# 🧬 Algoritmo Genético

<p> O algoritmo genético é uma técnica de busca para encontrar a solução ótima (ou aproximada) em problemas de otimização que possuem um número muito grande de combinações. Ele é parte do grupo de algoritmos bioinspirados, e utiliza conceitos da biologia evolutivam como seleção natural, crossover e mutação. </p>
<br>

## 💾 Instalando como módulo
<br>

``` 
git clone https://github.com/joao-savietto/genetic-algorithm.git
cd genetic-algorithm
python setup.py install
```

# 🔎 Exemplo de uso
<p> Você pode ver um exemplo de uso desse módulo <a href="https://github.com/joao-savietto/ga-feature-selection"> nesse repositório</a> </p>

<br>
<hr/>

## ❓ Docs
<p> O módulo contém duas classes: GeneticAlgorithm e Individual</p>
<hr/><br/>

### Individual

```
Individual(data: Dict[object, object], mutation_chance: float)
```
<br/>

<p> Classe base que representa um indivíduo da população. Para usar o algoritmo, você precisa criar uma nova classe que herda  'Individual' e implementa os métodos listados abaixo. O construtor recebe dois parâmetros: `data` e `mutation_chance`. </p>

### Atributos

```
chromossome: List
```

<p> O cromossomo do indivíduo, que representa uma possível solução do problema </p>

```
fitness: int
```

<p> O fitness é um valor numérico que indica o quanto a solução representada pelo indivíduo é boa. O algoritmo tenta maximizar o fitness para encontrar a solução ótima. </p>

```
data: Dict[object, object]
```

<p> Dicionário para passar todos os parâmetros relacionados ao problema </p>

```
mutation_chance: float
```

<p>Chance do cromossomo sofrer mutação após o crossover. Deve ser um valor entre 0 e 1, sendo 1 = 100% de chance. Valores entre 0.1 e 0.3 costumam produzir resultados bons. </p>
</br>

### Métodos

```
def mutate(self)
 ```

<p> Método que faz a mutação no cromossomo, baseado no parâmetro <strong>mutation_chance</strong>. </p>

```
def calculate_fitness(self)
```
<p> Método que faz o cálculo do fitness do indivíduo </p>

```
def random_chromossome(self)
```

<p> Método para inicializar o cromossomo do indivíduo </p>

```
def crossover(self, other):
```

<p> Método que faz o crossover entre dois indivíduos, gerando dois descendentes. Esse método já está implementado, sendo assim herdado pela a classe filha </p>

<hr/>
### GeneticAlgorithm
<p> Implementação do algoritmo genético propriamente dito. O construtor recebe uma instância de 'Individual', utilizada como base para gerar a população inicial. </p>

### Atributos

```
population: List
```

<p> Lista com todos os indivíduos da população </p>

```
history: List
```

<p> Histórico com o melhor fitness encontrado em cada iteração do algoritmo </p>

```
best_history: List
```

<p> Histórico com a evolução do melhor fitness encontrado pelo algoritmo  </p>

```
best_individual: Individual
```

<p> Melhor indivíduo encontrado ao longo das iterações do algoritmo  </p>

### Métodos

```
def truncated_selection(self) -> (List[Individual] | None)
 ```

<p> Método que implementa a seleção truncada. Retorna uma lista com dois indivíduos, ou None caso não seja possível encontrar dois indivíduos com cromossomos diferentes. </p>

```
def run(self, population_size: int = 50, iters: int = 100, mutation_chance: float = 0.15, keep_best_ratio: float=0.3, truncated_selection_ratio: float=0.45, silent: bool = False, early_stopping: bool=True, early_stopping_tol: int = 10):
 ```

<p> Método que inicia o treinamento do algoritmo genético. Existem diversos parâmetros que influenciam nos resultados: </p>
<li> <strong>population_size</strong>: número de indivíduos da população (padrão: 50) </li>
<li> <strong>iters</strong>: número de iterações do algoritmo (padrão: 100) </li>
<li> <strong>mutation_chance</strong>: chance de mutação após o crossover. Um valor muito alto impede o algoritmo de encontrar a solução ótima, e um valor muito baixo impede o algoritmo de explorar soluções diferentes (padrão: 0.15, ou seja 15%) </li>
<li> <strong>keep_best_ratio</strong>: porcentagem dos melhores indivíduos que são preservados entre uma iteração e outra. (padrão: 0.3, ou seja: 30%) </li>
<li> <strong>truncated_selection_ratio</strong>: porcentagem de corte da seleção truncada, para selecionar os indivíduos para crossover (padrão: 0.45, ou seja: 45%) </li>
<li> <strong>silent</strong>: caso definido como True, o algoritmo não vai exibir o resultado do treinamento a cada iteração (padrão: False) </li>
<li> <strong>early_stopping</strong>: interrompe o treinamento do algoritmo caso se passe um determinado número de iterações sem encontrar soluções melhores (padrão: True) </li>
<li> <strong>early_stopping_tol</strong>: número máximo de iterações sem melhoras que o algoritmo vai permitir antes de interromper o treinamento. Só faz efeito se <i> early_stopping</i> for definido como True. (padrão: 10) </li>
<br/>

# 🌱 Atualizações futuras

<li> Mais métodos de seleção serão implementados </li>