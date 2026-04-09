import "./Perfil.css";

function Perfil({ nome, curso, status }) {
  return (
    <div className="perfil">
      <h2>Perfil do Aluno</h2>
      <p>
        <strong>Nome: </strong>
        {nome}
      </p>
      <p>
        <strong>Curso: </strong>
        {curso}
      </p>
      <p className={status === "Atividade concluída!" ? "concluido" : ""}>
        <strong>Status:</strong> {status}
      </p>
    </div>
  );
}

export default Perfil;
