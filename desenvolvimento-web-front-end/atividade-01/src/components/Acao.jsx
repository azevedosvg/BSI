import "./Acao.css";

function Acao({ alterarStatus }) {
  return (
    <div>
      <button onClick={alterarStatus}>Concluir Atividade</button>
    </div>
  );
}

export default Acao;
