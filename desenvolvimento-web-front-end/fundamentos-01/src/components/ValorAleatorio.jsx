// Componente que recebe um intervalo (min e max) via props;
function ValorAleatorio(props) {
  // Aqui, usei desestruturação:
  // em vez de props.min e props.max, podemos usar direto min e max.
  const { min, max } = props;

  // Math.random() gera um número entre 0 e 1
  // multiplicamos pelo intervalo (max - min)
  // somamos o min para ajustar o início do intervalo
  // parseInt remove a parte decimal (deixa o número inteiro)
  const aleatorio = parseInt(Math.random() * (max - min)) + min;

  return (
    <div>
      <h2>Valor Aleatório</h2>
      <p>
        <strong>Valor mínimo: </strong> {min}
        <br />
        <strong>Valor máximo: </strong> {max}
        <br />
        <strong>Valor escolhido: </strong> {aleatorio}
      </p>
    </div>
  );
}

export default ValorAleatorio;
