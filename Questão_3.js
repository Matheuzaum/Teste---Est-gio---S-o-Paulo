// Importa o módulo fs para manipulação de arquivos
const fs = require('fs');

// Lê o arquivo JSON de faturamento mensal
fs.readFile('Exemplo Faturamento Mensal Questão 3.json', 'utf8', (err, data) => {
    if (err) {
        console.error('Erro ao ler o arquivo:', err);
        return;
    }

    // Converte o conteúdo do arquivo para um objeto JavaScript
    const jsonData = JSON.parse(data);

    // Acessa o array de faturamento dentro do objeto
    const faturamentoMensal = jsonData.faturamento;

    // Verifica se faturamentoMensal é realmente um array
    if (!Array.isArray(faturamentoMensal)) {
        console.error('Dados de faturamento não são um array.');
        return;
    }

    // Filtra os dias com faturamento para ignorar dias sem faturamento
    const diasComFaturamento = faturamentoMensal.filter(dia => dia.valor > 0);

    // Calcula o menor e o maior valor de faturamento
    const menorFaturamento = Math.min(...diasComFaturamento.map(dia => dia.valor));
    const maiorFaturamento = Math.max(...diasComFaturamento.map(dia => dia.valor));

    // Calcula a média mensal
    const somaFaturamento = diasComFaturamento.reduce((total, dia) => total + dia.valor, 0);
    const mediaMensal = somaFaturamento / diasComFaturamento.length;

    // Conta o número de dias em que o faturamento foi superior à média mensal
    const diasAcimaDaMedia = diasComFaturamento.filter(dia => dia.valor > mediaMensal).length;

    // Exibe os resultados
    console.log(`Menor valor de faturamento: R$ ${menorFaturamento.toFixed(2)}`);
    console.log(`Maior valor de faturamento: R$ ${maiorFaturamento.toFixed(2)}`);
    console.log(`Número de dias com faturamento acima da média mensal: ${diasAcimaDaMedia}`);
});