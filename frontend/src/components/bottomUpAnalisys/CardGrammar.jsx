const CardGrammar = ({ grammar }) => {
  return (
    <div className="border border-primary px-3 pb-3 mb-3 stack-card">
      <h4 className="mt-3 border-bottom border-primary">Gramática</h4>
      <div className="vstack gap-1">
        {grammar.map((element, index) => (
          <div className="bg-primary-subtle p-1" key={index}>
            {element}
          </div>
        ))}
      </div>
    </div>
  );
};

export default CardGrammar;