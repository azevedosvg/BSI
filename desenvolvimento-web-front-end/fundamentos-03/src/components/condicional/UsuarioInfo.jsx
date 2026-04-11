export default function UsuarioInfo(props) {
  const usuario = props.usuario || {};
  const nome = usuario.nome;
  return (
    <div className="box">
      {nome ? (
        <p className="usuario">Seja bem-vindo, {nome} </p>
      ) : (
        <p className="usuario">Seja bem-vindo, visitante! </p>
      )}
    </div>
  );
}
