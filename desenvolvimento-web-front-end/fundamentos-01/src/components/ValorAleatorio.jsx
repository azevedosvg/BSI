function ValorAleatorio(props) {
  const { min, max } = props;

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
