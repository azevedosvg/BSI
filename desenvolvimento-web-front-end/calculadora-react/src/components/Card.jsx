import "./Card.css";

function Card(props) {
  return (
    <div className="card">
      {/* Tirei o CSS Inline daqui e coloquei no componente CSS */}
      <div className="card-header">{props.titulo}</div>
      {props.aberto && props.children}
    </div>
  );
}

export default Card;
