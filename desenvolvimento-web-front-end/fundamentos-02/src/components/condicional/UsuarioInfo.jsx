// Importa o componente If e o "Else" personalizado
import If, { Else } from "./If";

export default function UsuarioInfo(props) {
  // Se não vier um usuário, evita erro usando um objeto vazio
  const usuario = props.usuario || {};

  return (
    <div>
      {/* Usa o componente If customizado
      -> testa se existe usuario.nome */}
      <If test={usuario.nome}>
        {/* Se existir, exibe o nome do usuário */}
        <span>
          Seja bem-vindo <strong>{usuario.nome}</strong>!
        </span>

        {/* Se não existir, exibe um mensagem */}
        <Else>
          <span>
            Seja bem-vindo <strong>Amigão</strong>
          </span>
        </Else>
      </If>
    </div>
  );
}
