// Componente que representa um membro da família
export default function FamiliaMembro(props) {
  return (
    <div>
      {/* Nome recebido via props */}
      {props.nome}
      {/* Sobrenome recebido via props (geralmente do componente Familia) */}
      <strong>{props.sobrenome}</strong>
    </div>
  );
}
