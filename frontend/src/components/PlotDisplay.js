import React from 'react';
import { Box } from '@mui/material';

const PlotDisplay = ({ plotData }) => {
  if (!plotData) {
    return <Box sx={{ height: 400, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>Loading...</Box>;
  }

  return (
    <Box sx={{ height: 400, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <img
        src={`data:image/png;base64,${plotData}`}
        alt="House Price Plot"
        style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }}
      />
    </Box>
  );
};

export default PlotDisplay;