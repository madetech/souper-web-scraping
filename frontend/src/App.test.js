import { render, screen } from '@testing-library/react';
import App from './App';

test('renders table', () => {
  render(<App />);
  const text = screen.getByRole("table");
  expect(text).toBeInTheDocument();
});
