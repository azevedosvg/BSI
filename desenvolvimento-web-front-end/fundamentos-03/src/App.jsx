import "./App.css";
import ParOuImpar from "./components/condicional/ParOuImpar";
import UsuarioInfo from "./components/condicional/UsuarioInfo";
import MensagemStatus from "./components/condicional/MensagemStatus";

export default function App() {
  return (
    <div className="container">
      <h1>React Fundamentos - Exemplo 01</h1>

      <div className="secao">
        <h2>Exemplo 01 - Par ou Ímpar</h2>
        <ParOuImpar numero={10} />
        <ParOuImpar numero={7} />
      </div>

      <div className="secao">
        <h2>Exemplo 02 - Usuário</h2>
        <UsuarioInfo usuario={{ nome: "Gabriel" }} />
        <UsuarioInfo usuario={{}} />
      </div>

      <div className="secao">
        <h2>Exemplo 03 - Situação do Aluno</h2>
        <MensagemStatus nota={8} />
        <MensagemStatus nota={4} />
      </div>
    </div>
  );
}
