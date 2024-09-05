import React from 'react';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material';

const RegionSelector = ({ regions, selectedRegion, onRegionChange }) => {
  return (
    <FormControl fullWidth>
      <InputLabel id="region-select-label">Select Region</InputLabel>
      <Select
        labelId="region-select-label"
        id="region-select"
        value={selectedRegion}
        label="Select Region"
        onChange={onRegionChange}
        data-testid="region-select"
      >
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