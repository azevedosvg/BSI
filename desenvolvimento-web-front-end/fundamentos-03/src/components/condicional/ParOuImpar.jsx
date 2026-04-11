export default function ParOuImpar(props) {
  const isPar = props.numero % 2 === 0;
  return (
    <div className="box">
      <p>Número Recebido: {props.numero}</p>
      <p className={isPar ? "Par" : "Ímpar"}>{isPar ? "Par" : "Ímpar"}</p>
    </div>
  );
}
