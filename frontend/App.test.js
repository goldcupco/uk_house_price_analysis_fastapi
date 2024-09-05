import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders UK House Price Analysis title', () => {
  render(<App />);
  const titleElement = screen.getByText(/UK House Price Analysis/i);
  expect(titleElement).toBeInTheDocument();
});