import "./PainelResumo.css";
// Fazendo a reutilização dos componentes criados anteriormente...
import NumeroInfo from "../exercicio01/NumeroInfo";
import StatusUsuario from "../exercicio02/StatusUsuario";

// Criando um componente para organizar os dois componentes importados;
function PainelResumo() {
  const usuario = { nome: "João", ativo: true };

  return (
    <div className="painel">
      <h1>Painel de Resumo</h1>

      <div className="sessao">
        <div className="bloco">
          <p>Status do Usuário</p>
          {/* Usando o componente criado anteriormente */}
          <StatusUsuario usuario={usuario} />{" "}
        </div>
        <div className="bloco">
          <p>Par, Ímpar ou Zero</p>
          {/* Usando o componente criado anteriormente */}
          <NumeroInfo numero={5} />{" "}
        </div>
      </div>
    </div>
  );
}

export default PainelResumo;
