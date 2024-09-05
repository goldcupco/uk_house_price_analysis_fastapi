import React from 'react';
import { render, screen } from '@testing-library/react';
import PlotDisplay from './PlotDisplay';

test('renders loading state when no plot data', () => {
  render(<PlotDisplay />);
  const loadingElement = screen.getByTestId('loading-state');
  expect(loadingElement).toBeInTheDocument();
  expect(loadingElement).toHaveTextContent('Loading...');
});

test('renders image when plot data is provided', () => {
  const mockPlotData = 'base64EncodedImageData';
  render(<PlotDisplay plotData={mockPlotData} />);
  const imgElement = screen.getByTestId('plot-image');
  expect(imgElement).toBeInTheDocument();
  expect(imgElement).toHaveAttribute('src', `data:image/png;base64,${mockPlotData}`);
});