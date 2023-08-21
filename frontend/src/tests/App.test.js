import { render, screen } from '@testing-library/react';
import React from 'react';
import App from '../App';

describe('<App />', () => {

  it('renders table', async () => {
    render(<App />);
    const text = screen.getAllByRole("table");
    expect(text[0]).toBeInTheDocument();
  });

  it('renders pagination', async () => {
    render(<App />);

    const text = screen.getAllByText("Rows per page:");
    expect(text[0]).toBeInTheDocument();
  });
})

