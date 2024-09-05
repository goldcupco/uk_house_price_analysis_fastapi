import React from 'react';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material';

const RegionSelector = ({ regions, selectedRegion, onRegionChange }) => {
  return (
    <FormControl fullWidth>
      <InputLabel>Select Region</InputLabel>
      <Select value={selectedRegion} onChange={onRegionChange}>
        {regions.map((region) => (
          <MenuItem key={region} value={region}>
            {region}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export default RegionSelector;