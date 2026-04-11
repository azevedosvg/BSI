// Importa o React e a função cloneElement
// cloneElement permite modificar um elemento filho (adicionar props, por exemplo)
import React, { cloneElement } from "react";

// O que esse componente faz?
// Pega todos os filhos dentro de <Familia> e injeta as props do pai em cada filho automaticamente.

export default function Familia(props) {
  return (
    <div>
      {/*
        props.children -> são os componentes que estão dentro de <Familia>...<Familia>
        
        map percorre cada filho
        (child = cada componente filho)
        (i = índice, usado como key)
        */}
      {props.children.map((child, i) => {
        return cloneElement(child, {
          ...props, // repassa todas as props do pai para o filho
          key: i,
        }); // adiciona uma key (necessária em listas no React)
      })}
    </div>
  );
}
