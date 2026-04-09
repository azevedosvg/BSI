import "./NumeroInfo.css"; // Importa o arquivo de estilos; Cada componente pode ter seu próprio CSS;

/*
function NomeDoComponente({prop}) {
  ... 
  return ()
};

*/

// Função (componente) para usar no App.jsx
function NumeroInfo({ numero }) {
  /* 
    numero === 0   ?   "Zero"   :   "Outro"
    condição       ?  se TRUE  :   se FALSE
                   if           else
  */

  // Variável para armazenar o resultado da condição:
  const resultado = numero === 0 ? "Zero" : numero % 2 === 0 ? "Par" : "Ímpar";

  // Variável para definir a classe do elemento (ligação com o CSS do componente):
  const classe =
    resultado === "Zero" ? "zero" : resultado === "Par" ? "par" : "impar";
  // Se o resultado for Zero, a classe será "zero", senão, será par, senão é impar.
  // O resultado é passado para a variável classe que vai ser exibida no App.jsx.
  // No CSS do componente, é definido como a classe vai ser exibida.

  // Aqui, é o que aparece na tela quando o componente é renderizado no App.jsx:
  return (
    <div className="container">
      <h1>Número recebido: {numero}</h1>
      <p className={`resultado ${classe}`}>{resultado}</p>
    </div>
  );
}

// Permite que o componente seja renderizado no App.jsx
export default NumeroInfo;
