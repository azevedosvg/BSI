import ParOuImpar from "./components/condicional/ParOuImpar";
import DiretaPai from "./components/comunicacao/DiretaPai";
import IndiretaPai from "./components/comunicacao/IndiretaPai";

export default function App() {
  return (
    <div>
      <h1>React Fundamentos Ex 02</h1>

      <hr />
      <h2>Renderização Condicional</h2>
      <ParOuImpar numero={17} usuario={{ nome: "Gabriel" }} />
      <ParOuImpar numero={20} usuario={{ nome: "Junior" }} />

      <hr />
      <h2>Comunicação Direta entre Pai e Filho</h2>
      <DiretaPai />

      <hr />
      <h2>Comunicação Indireta entre Pai e Filho</h2>
      <IndiretaPai />
    </div>
  );
}
