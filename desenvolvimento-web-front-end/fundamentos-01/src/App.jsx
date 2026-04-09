import Primeiro from "./components/Primeiro.jsx";
import AlunoSituacao from "./components/AlunoSituacao.jsx";
import ValorAleatorio from "./components/ValorAleatorio.jsx";

function App() {
  return (
    <div>
      <Primeiro />
      <br />
      <br />

      <AlunoSituacao titulo="Situação do Aluno" aluno="Gabriel" nota={10} />
      <br />
      <br />

      <ValorAleatorio min={1} max={60} />
    </div>
  );
}

export default App;
