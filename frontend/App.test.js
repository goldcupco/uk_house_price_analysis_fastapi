import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

describe('App component', () => {
  test('renders without crashing', () => {
    render(<App />);
    expect(document.body).toBeTruthy();
  });

  test('renders UK House Price Analysis title', () => {
    render(<App />);
    const titleElement = screen.getByText(/UK House Price Analysis/i);
    expect(titleElement).toBeInTheDocument();
  });

  test('does not render learn react link', () => {
    render(<App />);
    const learnReactElement = screen.queryByText(/learn react/i);
    expect(learnReactElement).not.toBeInTheDocument();
  });
});