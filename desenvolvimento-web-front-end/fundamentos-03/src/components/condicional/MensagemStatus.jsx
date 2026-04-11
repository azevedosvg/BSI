export default function mensagemStatus(props) {
  const aprovado = props.nota >= 6;

  return (
    <div className="box">
      <p>Nota: {props.nota}</p>
      <p className={aprovado ? "aprovado" : "reprovado"}>
        {aprovado ? "Aprovado" : "Reprovado"}
      </p>
      {aprovado && <p className="parabens">Parabéns pelo resultado!</p>}
    </div>
  );
}
