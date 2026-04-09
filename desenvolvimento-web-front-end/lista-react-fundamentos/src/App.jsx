// Juntando os componenentes...
import NumeroInfo from "./components/exercicio01/NumeroInfo";
import StatusUsuario from "./components/exercicio02/StatusUsuario";
import ClassificacaoNota from "./components/exercicio03/ClassificacaoNota";
import Produto from "./components/exercicio04/Produto";
import PainelResumo from "./components/exercicio05/PainelResumo";

function App() {
  const usuario1 = {
    nome: "João",
    ativo: true,
  };

  const usuario2 = {
    nome: "Maria",
    ativo: false,
  };

  return (
    <div className="app">
      <h2 className="titulo">Lista de exercícios: React Fundamentos</h2>
      <h1 className="infos">
        Disciplina: Desenvolvimento Web Front-End - Christien Lana Rachid
      </h1>
      <h1 className="infos">Nome: Gabriel de Azevedo Silva</h1>
      <p className="enunciado">Exercício 01: Zero, Par ou Ímpar?</p>

      {/* <componente prop={valor} /> */}
      <NumeroInfo numero={0} />
      <NumeroInfo numero={4} />
      <NumeroInfo numero={7} />

      <hr className="separador" />

      <p className="enunciado">Exercício 02: Status do usuário</p>
      <StatusUsuario usuario={usuario1} />
      <StatusUsuario usuario={usuario2} />

      <hr className="separador" />

      <p className="enunciado">Exercício 03: Classificação de Nota</p>
      <ClassificacaoNota nota={9} />
      <ClassificacaoNota nota={7} />
      <ClassificacaoNota nota={5} />
      <ClassificacaoNota nota={3} />

      <hr className="separador" />

      <p className="enunciado">Exercício 04: Produto em estoque</p>
      <Produto produto={{ nome: "Notebook", quantidade: 5 }} />
      <Produto produto={{ nome: "Mouse", quantidade: 0 }} />

      <hr className="separador" />

      <p className="enunciado">Exercício 05: Painel de Resumo</p>
      <PainelResumo />
    </div>
  );
}

export default App;
