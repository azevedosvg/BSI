import Card from "./components/Card";
import Calculadora from "./components/Calculadora";

function App() {
  return (
    <div>
      <Card titulo="Exercício - Calculadora" cor="#f34" aberto={true}>
        <Calculadora />
      </Card>
    </div>
  );
}

export default App;
