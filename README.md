# acompanhaPreco100ProdutosDurante1Mes (webScraping)
Pra acompanha o preço de um produto o buscapé da conta. Mas numa pesquisa de mercado, acompanhando muitos produtos: webScraping.




## Version 1.0

Inicialmente na primeira biblioteca que testei a kabum e a amazon estavam bloqueando o acesso pois detectavam como acesso de bot (de 10 funcionava 1). O nome da primeira era 'requests', então agora nesta segunda, a biblioteca Selenium, a qual emula um navegador, funcionou 100%. Houveram alguns adendos (citados no final), mas o programa está funcionando bem, já dá pra testar nos próximos dias.

O resultado final é este (executando o programa gera esse gráfico):
![image](https://user-images.githubusercontent.com/30224310/136625419-fa4ad8fb-7c07-456f-8c43-7de30482945e.png)
(07/10 para fins de teste. Já o 08/10 é real.)



Adendos: 
- Um dos problemas enfrentados é ter que tomar cuidado com o número de testes consecutivos, pois os sites detectam bot e bloqueiam o acesso (como foi o caso da magazine luisa, que não está no gráfico devido à esse problema/provavelmente amanhã volte a funcionar).
