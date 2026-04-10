// Componente filho que vai enviar dados para o componente pai
export default function IndiretaFilho(props) {
  // Pegamos a função que veio por props
  // Essa função foi passada pelo componente pai
  const cb = props.quandoClicar;

  return (
    <div>
      {/* Quando o botão for clicado:
      executa a função cb (callback)
      e envia os dados como parâmetros */}
      <button onClick={() => cb("João", 57, true)}>Fornecer Informações</button>
    </div>
  );
}
