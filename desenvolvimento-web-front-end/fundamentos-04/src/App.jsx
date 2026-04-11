// Importa os componentes que serão exibidos na tela
import ListaNumeros from "./components/ListaNumeros01";
import ListaAlunos from "./components/ListaAlunos";
import Familia from "./components/Familia";
import FamiliaMembro from "./components/FamiliaMembro";

function App() {
  return (
    // div principal da aplicação
    <div className="App">
      {/* Título geral */}
      <h1>Fundmentos de React</h1>

      {/* ===================== */}
      {/* EXEMPLO 01 */}
      {/* ===================== */}

      <h2>Exemplo 01 - Lista de Números</h2>

      {/* Renderiza o componente que mostra números com map */}
      <ListaNumeros />

      {/* ===================== */}
      {/* EXEMPLO 02 */}
      {/* ===================== */}

      <h2>Exemplo 02 - Lista de Alunos</h2>

      {/* Renderiza lista baseada em um array de objetos */}
      <ListaAlunos />

      {/* ===================== */}
      {/* EXEMPLO 03 */}
      {/* ===================== */}

      <h2>Exemplo 03 - Componente com Filhos</h2>

      {/* 
        Componente que envolve outros componentes (children)
        → passa o sobrenome para todos os filhos automaticamente
      */}
      <Familia sobrenome="Silva">
        {/* Cada filho recebe "nome" diretamente */}
        {/* e "sobrenome" vem do componente Familia */}
        <FamiliaMembro nome="Pedro" />
        <FamiliaMembro nome="Ana" />
        <FamiliaMembro nome="Gustavo" />
      </Familia>
    </div>
  );
}

// Exporta o componente principal da aplicação
export default App;
