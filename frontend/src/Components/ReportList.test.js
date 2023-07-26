import { render, screen } from '@testing-library/react';
import React, { useState } from 'react';
import ReportList from "./ReportList";

jest.mock('react', () => ({
...jest.requireActual('react'),
useState: jest.fn()
}));

describe('<Reportlist />', () => {
  const page = 0;
  const setPage = jest.fn();
  
  const rowsPerPage = 5;
  const setRowsPerPage = jest.fn();

  const useStateMock = (useState) => [useState, jest.fn()];
  const setReport = jest.fn();
  const report = [
    {
      id: "1",
      assessment_date: "14/06/2023",
      name: "anna",
      overall_verdict: "pass",
      stage: "Alpha"
    },
    {
      id: "2",
      assessment_date: "14/06/2023",
      name: "losy",
      overall_verdict: "pass",
      stage: "Alpha"
    },
    {
      id: "3",
      assessment_date: "14/06/2023",
      name: "jack",
      overall_verdict: "pass",
      stage: "Alpha"
    },
    {
      id: "4",
      assessment_date: "14/06/2023",
      name: "lucas",
      overall_verdict: "pass",
      stage: "Alpha"
    },
    {
      id: "5",
      assessment_date: "14/07/2023",
      name: "emma",
      overall_verdict: "pass",
      stage: "Alpha"
    },
    {
      id: "6",
      assessment_date: "14/06/2022",
      name: "jenna",
      overall_verdict: "pass",
      stage: "Alpha"
    }
  ];

  function renderReportListWithMock(page){
    useState.mockImplementation(useStateMock) 
    jest
      .spyOn(React, 'useState')
      .mockImplementationOnce(() => [page, setPage]) 
      .mockImplementationOnce(() => [rowsPerPage, setRowsPerPage]) 
      .mockImplementationOnce(() => [report, setReport]) 

    render(<ReportList />);
  }

  describe('render table first page ', () => {
    beforeEach(() => {
      renderReportListWithMock(page)
    });

    afterEach(() => {
      jest.clearAllMocks();
    });

    it('renders table contents', () => { 
        const text =  screen.getByText("anna")
        expect(text).toBeInTheDocument();
      });

    it('renders 5 table rows', () => {
        const tableRows = screen.getByTestId('tableTest')
        
        expect(report.length).toBe(6)
        expect(tableRows.children.length).toBe(5);
    });
    }) 

  describe('render table next page ', () => {
    beforeEach(() => {
      renderReportListWithMock(1)
    });
  
    afterEach(() => {
      jest.clearAllMocks();
    });

    it('renders only one table row in the next page', () => {
        const tableRows = screen.getByTestId('tableTest')
        
        expect(report.length).toBe(6)
        expect(tableRows.children.length).toBe(1);
    });
    }) 
})
