import React from 'react';
import { render, screen } from '@testing-library/react';
import TabPanel from './TabPanel';
test('renders children when selected', () => {
  render(
    <TabPanel value={0} index={0}>
      Test Content
    </TabPanel>
  );
  const contentElement = screen.getByText(/Test Content/i);
  expect(contentElement).toBeInTheDocument();
});

test('does not render children when not selected', () => {
  render(
    <TabPanel value={1} index={0}>
      Test Content
    </TabPanel>
  );
  const contentElement = screen.queryByText(/Test Content/i);
  expect(contentElement).not.toBeInTheDocument();
});