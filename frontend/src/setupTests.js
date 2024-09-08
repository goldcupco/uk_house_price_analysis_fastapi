import '@testing-library/jest-dom';
import { configure } from '@testing-library/react';

configure({ asyncUtilTimeout: 50000 });

jest.mock('react-dom/test-utils', () => {
  const original = jest.requireActual('react-dom/test-utils');
  return {
    ...original,
    act: (callback) => {
      const result = callback();
      return result?.then ? result : Promise.resolve(result);
    },
  };
});