import "./Produto.css";

function Produto({ produto }) {
  return (
    <div className="container">
      <h1>{produto.nome}</h1>

      {produto.quantidade > 0 && <p className="estoque">Em estoque</p>}
      {/*Se quantidade > 0: mostra "Em estoque" Se não: não mostra nada */}
      {produto.quantidade <= 0 && <p className="esgotado">Produto esgotado</p>}
      {/*Se <= 0: mostra Produto esgotado */}
    </div>
  );
}

// Condição && algo: mostra algo ou mostra nada;

export default Produto;
