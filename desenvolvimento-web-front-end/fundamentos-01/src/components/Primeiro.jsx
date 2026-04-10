// Aqui estamos criando uma função chamada "Primeiro";
// Em React, funções assim são chamadas de "componentes".
function Primeiro() {
  // Cria uma variável chamada "msg";
  // Ela guarda um texto que vai ser mostrado na tela.
  const msg = "Seja bem-vindo(a)!";

  // O return define o que será exibido no navegador.
  return (
    // Tudo precisa estar dentro de um único elemento pai (nesse caso, uma div).
    <div>
      {/* HTML básico */}
      <h2>Primeiro Componente</h2>
      {/* Aqui eu exibo o conteúdo da variável "msg". As chaves {} são usadas para usar JavaScript dentro do HTML (JSX). */}
      <p>{msg}</p>
    </div>
  );
}

// Aqui se exporta o componente;
// Isso permite que ele seja usado em outros arquivos do projeto.
export default Primeiro;
