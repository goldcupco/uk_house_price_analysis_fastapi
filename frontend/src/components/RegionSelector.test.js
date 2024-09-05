import React from 'react';
import { render, screen } from '@testing-library/react';
import RegionSelector from './RegionSelector';

test('renders region selector', () => {
  const mockRegions = ['Region1', 'Region2'];
  render(
    <RegionSelector
      regions={mockRegions}
      selectedRegion="Region1"
      onRegionChange={() => {}}
    />
  );
  const selectElement = screen.getByTestId('region-select');
  expect(selectElement).toBeInTheDocument();
  expect(screen.getByLabelText('Select Region')).toBeInTheDocument();
});