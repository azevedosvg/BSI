// Importar o hook useState (serve para controlar os estados dos componentes)
import { useState } from "react";
// Importa o componente filho
import IndiretaFilho from "./IndiretaFilho";

export default function IndiretaPai() {
  // Estados que vão armazenar os dados recebidos do filho
  const [nome, setNome] = useState("");
  const [idade, setIdade] = useState(0);
  const [nerd, setNerd] = useState(false);

  // Função que será enviada para o filho
  // O filho vai chamar essa função passando dados como parâmetro
  function fornecerInformacoes(nome, idade, nerd) {
    setNome(nome); // Atualiza o nome
    setIdade(idade); // Atualiza a idade
    setNerd(nerd); // Atualiza o nerd (bool)
  }

  return (
    <div>
      {/* Exibe os valores atuais do estado */}
      <span>{nome} </span>
      <strong>{idade} </strong>
      {/* Mostra "Verdadeiro" ou "Falso" baseado no valor booleano */}
      <span>{nerd ? "Verdadeiro" : "Falso"}</span>

      {/* Passamos a função para o filho
      -> isso permite comunicação do filho para o pai (indireta) */}
      <IndiretaFilho quandoClicar={fornecerInformacoes} />
    </div>
  );
}
