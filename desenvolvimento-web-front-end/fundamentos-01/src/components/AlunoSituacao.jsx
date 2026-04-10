// Esse componente recebe dados via "props";
// (props) são como parâmetros passados para o componente.

function AlunoSituacao(props) {
  // Aqui usamos um operador ternário:
  // se a nota for >= 7 -> retorna "Aprovado"
  // senão retorna "Recuperação".
  const status = props.nota >= 7 ? "Aprovado" : "Recuperação";
  // Math.ceil arredonda o valor para cima.
  const notaInt = Math.ceil(props.nota);

  return (
    <div>
      {/* Exibe um título que vem das props */}
      <h2>{props.titulo}</h2>
      <p>
        {/* Exibe o nome do aluno */}
        <strong>{props.aluno} </strong>
        tem nota
        {/* Exibe a nota do aluno */}
        <strong> {notaInt} </strong>e está
        {/* Exibe o status do aluno */}
        <strong> {status}</strong>
      </p>
    </div>
  );
}

export default AlunoSituacao;
