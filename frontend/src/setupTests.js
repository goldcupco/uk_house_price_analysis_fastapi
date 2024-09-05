// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom

import '@testing-library/jest-dom';
import { configure } from '@testing-library/react';
import { act } from 'react-dom/test-utils';


configure({ asyncUtilTimeout: 50000 });

// Mock the act function to suppress the warning
jest.mock('react-dom/test-utils', () => ({
  ...jest.requireActual('react-dom/test-utils'),
  act: (callback) => callback(),
}));
