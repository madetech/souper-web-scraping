import { render, screen } from '@testing-library/react';
import React, { useState }  from 'react';
import ReportList from "./ReportList";

jest.mock('react', () => ({
...jest.requireActual('react'),
useState: jest.fn()
}));

const useStateMock = useState;

const setState = jest.fn();
const state = [{"id": "1", "assessment_date":"14/06/2023","name":"anna","overall_verdict":"pass","stage":"Alpha"},
               {"id": "2", "assessment_date":"14/09/2023","name":"ross","overall_verdict":"pass","stage":"beta"}]

test('renders table contents', () => {
    useStateMock
      .mockImplementation(() => [state, setState]);

    render(<ReportList />);

    const text = screen.getByText("anna")
    expect(text).toBeInTheDocument();
  });

test('renders table rows', () => {
    useStateMock
        .mockImplementation(() => [state, setState]);

    render(<ReportList />);

    const tableRows = screen.getByTestId('tableTest')
    expect(tableRows.children.length).toBe(2);
});
  