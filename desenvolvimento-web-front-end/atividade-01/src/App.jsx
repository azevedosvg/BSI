import { useState } from "react";
import Perfil from "./components/Perfil";
import Acao from "./components/Acao";
import "./index.css";

function App() {
  const [status, setStatus] = useState("Estudando React");

  const alterarStatus = () => {
    setStatus("Atividade concluída!");
  };

  return (
    <div className="container">
      <h1>Painel Interativo do Aluno</h1>

      <Perfil
        nome="Gabriel Azevedo"
        curso="Sistemas de Informação"
        status={status}
      />

      <Acao alterarStatus={alterarStatus} />
    </div>
  );
}

export default App;
