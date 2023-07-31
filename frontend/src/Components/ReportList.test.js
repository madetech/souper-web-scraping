import { render, screen } from '@testing-library/react';
import React, { useState } from 'react';
import reports from "./../Fixtures/Reports";
import ReportList from "./ReportList";

jest.mock('react', () => ({
  ...jest.requireActual('react'),
  useState: jest.fn()
}));

jest.mock("react-plotly.js", () => ({
  __esModule: true,
  default: jest.fn(() => <div />),
}));

describe('<Reportlist />', () => {
  const page = 0;
  const setPage = jest.fn();

  const rowsPerPage = 5;
  const setRowsPerPage = jest.fn();

  const useStateMock = (useState) => [useState, jest.fn()];
  const setReport = jest.fn();

  window.URL.createObjectURL = jest.fn();

  afterEach(() => {
    window.URL.createObjectURL.mockReset();
  });


  function renderReportListWithMock(page) {
    useState.mockImplementation(useStateMock)
    jest
      .spyOn(React, 'useState')
      .mockImplementationOnce(() => [page, setPage])
      .mockImplementationOnce(() => [rowsPerPage, setRowsPerPage])
      .mockImplementationOnce(() => [reports, setReport])

    render(<ReportList />);
  }

  describe('render table first page', () => {
    beforeEach(() => {
      renderReportListWithMock(page)
    });

    afterEach(() => {
      jest.clearAllMocks();
    });

    it('renders table contents', () => {
      const text = screen.getByText("anna")
      expect(text).toBeInTheDocument();
    });

    it('renders 5 table rows', () => {
      const tableRows = screen.getByTestId('tableTest')

      expect(reports.length).toBe(6)
      expect(tableRows.children.length).toBe(5);
    });
  })

  describe('render table next page', () => {
    beforeEach(() => {
      renderReportListWithMock(1)
    });

    afterEach(() => {
      jest.clearAllMocks();
    });

    it('renders only one table row in the next page', () => {
      const tableRows = screen.getByTestId('tableTest')

      expect(reports.length).toBe(6)
      expect(tableRows.children.length).toBe(1);
    });
  })
})
