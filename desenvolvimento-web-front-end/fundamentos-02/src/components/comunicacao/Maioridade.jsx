// Componente que recebe dados via props e apenas exibe na tela
export default function MaiorIdade(props) {
  return (
    <div>
      {/* Nome recebido do componente pai */}
      <span>{props.nome} </span>
      {/* Idade recebida */}
      <strong>{props.idade} </strong>
      {/* Exibe um texto baseado no valor booleano (true/false)
        -> operador ternário novamente */}
      <span>{props.nerd ? "Verdadeiro" : "Falso"}</span>
    </div>
  );
}
