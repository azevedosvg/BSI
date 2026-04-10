// Componente que simula um "if/else" dentro do JSX
export default function If(props) {
  // Garante que children sempre será um array
  // Mesmo que venha apenas um elemento
  const childrenArray = Array.isArray(props.children)
    ? props.children
    : [props.children];

  // Procura dentro dos children algum elemento do tipo "Else"
  const elseChild = childrenArray.find(
    (child) => child.type && child.type.name === "Else",
  );

  // Filtra os elementos que NÃO são "Else"
  // Ou seja, o conteúdo do "if"
  const ifChildren = childrenArray.filter(
    (child) => !(child && child.type && child.type.name === "Else"),
  );

  // Se a condição (test) for verdadeira...
  if (props.test) {
    return ifChildren; // renderiza o conteúdo "normal"
    // Se for falsa, mas existir um <Else>
  } else if (elseChild) {
    return elseChild; // renderiza o conteúdo do <Else>
    // Caso não tenha Else, não renderiza nada
  } else {
    return null;
  }
}

// Componente usado como "Else"
export function Else(props) {
  // Apenas retorna o que estiver dentro dele
  return props.children;
}
