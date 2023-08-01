import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import React, { useState } from 'react';
import reports from "./../Fixtures/Reports";
import sections from "./../Fixtures/Sections";
import ReportList from "./ReportList";

jest.mock('react', () => ({
  ...jest.requireActual('react'),
  useState: jest.fn()
}));

/* jest.mock("react-plotly.js", () => ({
  __esModule: true,
  default: jest.fn(() => <div />),
}));
 */
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

 /*  window.URL.createObjectURL = jest.fn();

  afterEach(() => {
    window.URL.createObjectURL.mockReset();
  });
 */
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
      renderReportListWithMock()
    });

    afterEach(() => {
      jest.clearAllMocks();
    });

    xit('renders report in the next page', async() => {

      const row = await screen.findByRole('button', {name: /Go to next page/i})
      userEvent.click(row);
      const text = screen.getByText("jenna")
      expect(text).toBeInTheDocument();

    });
  })

  xdescribe('render modal', () => {
    beforeEach(() => {
      renderReportListWithMock()
    });

    afterEach(() => {
      jest.clearAllMocks();
    });

    it('renders modal', async() => {
      const row = await screen.findAllByTestId('rowTest')
      userEvent.click(row[0]);
      const modal = screen.getAllByTestId('modalTest')
      expect(modal).toBeInTheDocument();

    });
  })

})
