import "./StatusUsuario.css";

// Agora a prop passada para o componente é um Objeto;
function StatusUsuario({ usuario }) {
  return (
    <div className="container">
      <h1 className="status">Status do usuário</h1>

      {/*Renderiza o componente passando as propriedades do objeto, ou seja:
        ativo: true = Joao: Ativo
        ativo: false = Inativo*/}

      {usuario.ativo ? (
        <p className="ativo">Usuário ativo: {usuario.nome}</p>
      ) : (
        <p className="inativo">Usuário inativo</p>
      )}
    </div>
  );
}

export default StatusUsuario;
