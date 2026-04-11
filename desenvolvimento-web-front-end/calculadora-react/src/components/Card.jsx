import "./Card.css";

function Card(props) {
  return (
    <div className="card" style={{ border: `3px solid ${props.cor}` }}>
      <div className="card-header" style={{ backgroundColor: props.cor }}>
        {props.titulo}
      </div>

      {props.aberto && props.children}
    </div>
  );
}

export default Card;
