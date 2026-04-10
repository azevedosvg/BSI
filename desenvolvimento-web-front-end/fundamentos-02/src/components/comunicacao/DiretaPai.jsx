import MaiorIdade from "./MaiorIdade";

// Componente pai (ele chama outros componentes)
export default function DiretaPai() {
  return (
    <div>
      {/* Aqui estamos passando dados diretamente para o componente filho (props)
      nome -> string
      idade -> numero (por isso isso {}) 
      nerd -> boolean 
      */}
      <MaiorIdade nome="Junior" idade={20} nerd={true} />

      {/* Outro uso do mesmo componente, mas com valores diferentes */}
      <MaiorIdade nome="Gabriel" idade={17} nerd={false} />
    </div>
  );
}
