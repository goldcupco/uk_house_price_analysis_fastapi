import React from 'react';

const PlotDisplay = ({ plotData }) => {
  if (!plotData) {
    return <div>Loading...</div>;
  }
  return (
    <div>
      <img src={`data:image/png;base64,${plotData}`} alt="House Price Plot" style={{ width: '100%' }} />
    </div>
  );
};

export default PlotDisplay;