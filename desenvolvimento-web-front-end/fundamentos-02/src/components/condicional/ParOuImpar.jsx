// Importa um componente que será usado condicionalmente
import UsuarioInfo from "./UsuarioInfo";

export default function ParOuImpar(props) {
  // Verificando se o número é par ou ímpar
  const isPar = props.numero % 2 === 0;

  return (
    <div>
      {isPar ? <span>Par</span> : <span>Ímpar</span>}
      {isPar && <UsuarioInfo usuario={props.usuario} />}
    </div>
  );
}
