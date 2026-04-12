import Card from "./components/Card";
import Calculadora from "./components/Calculadora";

function App() {
  return (
    <div className="container">
      <Card titulo="Informações sobre o projeto" aberto={true} tipo="info">
        <div className="info-card">
          <p>
            <span>Nome do curso: </span> Sistemas de Informação
          </p>

          <p>
            <span>Disciplina: </span> Desenvolvimento Web Front-End
          </p>

          <p>
            <span>Aluno: </span> Gabriel de Azevedo Silva
          </p>

          <p>
            <span>Professor: </span> Christien Lana Rachid
          </p>

          <br />
          <hr />
          <br />
          <h2 className="subtitulo">Sobre o projeto:</h2>
          <p>
            Este projeto consiste no desenvolvimento de uma calculadora
            utilizando React, com foco no aprendizado de estados, lógica de
            programação e manipulação de interface no desenvolvimento front-end.
          </p>
          <br />

          <p>
            A aplicação simula uma calculadora funcional baseada em interações
            por botões, proporcionando uma experiência semelhante a uma
            calculadora tradicional.
          </p>
          <br />
          <hr />
          <br />

          <h2 className="subtitulo">Funcionalidades da aplicação:</h2>

          <ul>
            <li>
              Operações básicas: adição, subtração, multiplicação e divisão;
            </li>
            <li>Entrada de números através de botões;</li>
            <li>
              Armazenamento de operação em duas etapas (primeiro e segundo
              valor);
            </li>
            <li>Exibição do cálculo em tempo real no display;</li>
            <li>Botão de apagar (remove o último dígito);</li>
            <li>Botão de limpar (reset completo da calculadora);</li>
            <li>Execução do cálculo com o botão de igual;</li>
            <li>Suporte a números decimais.</li>
          </ul>
        </div>
      </Card>
      <Card titulo="Área de desenvolvimento do exercício" aberto={true}>
        <Calculadora />
      </Card>
    </div>
  );
}

export default App;
