import { render, screen } from '@testing-library/react';
import React, { useState } from 'react';
import ReportList from "../../Components/ReportList";
import { reports } from "../Fixtures/Reports";
import { sections } from "../Fixtures/Sections";

jest.mock('react', () => ({
  ...jest.requireActual('react'),
  useState: jest.fn()
}));

describe('<Reportlist />', () => {

  const useStateMock = (useState) => [useState, jest.fn()];

  const setReport = jest.fn();
  const setSection = jest.fn();
  const open = false;
  const setOpen = jest.fn();
  const reportId = 0;
  const reportName = '';
  const setReportId = jest.fn();
  const setReportName = jest.fn();

  const page = 0;
  const setPage = jest.fn();
  const rowsPerPage = 5;
  const setRowsPerPage = jest.fn();

  function renderReportListWithMock() {
    useState.mockImplementation(useStateMock)
    jest
      .spyOn(React, 'useState')
      .mockImplementationOnce(() => [reports, setReport])
      .mockImplementationOnce(() => [reportId, setReportId])
      .mockImplementationOnce(() => [reportName, setReportName])
      .mockImplementationOnce(() => [sections, setSection])
      .mockImplementationOnce(() => [open, setOpen])

    render(<ReportList />);
  }

  describe('render table first page', () => {
    beforeEach(() => {
      renderReportListWithMock()
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

      useState.mockImplementation(useStateMock)
      jest
        .spyOn(React, 'useState')
        .mockImplementationOnce(() => [reports, setReport])
        .mockImplementationOnce(() => [reportId, setReportId])
        .mockImplementationOnce(() => [reportName, setReportName])
        .mockImplementationOnce(() => [sections, setSection])
        .mockImplementationOnce(() => [open, setOpen])
        .mockImplementationOnce(() => [0, setPage])
        .mockImplementationOnce(() => [rowsPerPage, setRowsPerPage])
        .mockImplementationOnce(() => [1, setPage])
        .mockImplementationOnce(() => [rowsPerPage, setRowsPerPage])

      render(<ReportList />);
    });

    afterEach(() => {
      jest.clearAllMocks();
    });

    it('renders report in the next page', async () => {
      const tableRows = screen.getByTestId('tableTest')

      expect(reports.length).toBe(6)
      expect(tableRows.children.length).toBe(1);
    });
  })
})
