import { act, fireEvent, render, screen } from '@testing-library/react';
import axios from 'axios';
import React from 'react';
import ReportList from "../../Components/ReportList";
import { reports } from "../Fixtures/Reports";

jest.mock("axios");

jest.mock('../../Components/SectionModal', () => () =>
  <div data-testid="sectionTest" />
);

jest.mock("react-plotly.js", () => ({
  __esModule: true,
  default: jest.fn(() => <div />),
}));

describe('<Reportlist />', () => {
  describe('render table first page', () => {
    beforeEach(async () => {
      await axios.get.mockImplementationOnce(() => Promise.resolve({
        status: 200,
        data: { items: reports }
      }))

      await act(async () =>
        render(<ReportList />),
      );
    })

    afterAll(() => {
      jest.resetAllMocks();
    });

    it('renders table contents', () => {
      const text = screen.getByText("anna")
      expect(text).toBeInTheDocument();
    });

    it('renders reports in the first row', () => {
      const tableRows = screen.getByTestId('tableTest')
      expect(reports.length).toBe(6)
      expect(tableRows.children.length).toBe(5);
    });

    it('renders the next page', async () => {
      const tableRows = screen.getByTestId('tableTest')

      const nextPageButton = screen.getByRole("button", { name: 'Go to next page' });
      fireEvent.click(nextPageButton);

      expect(tableRows.children.length).toBe(1);
    });

    it('renders the previous page', async () => {
      const tableRows = screen.getByTestId('tableTest')

      const nextPageButton = screen.getByRole("button", { name: 'Go to next page' });
      fireEvent.click(nextPageButton);

      const prevPageButton = screen.getByRole("button", { name: 'Go to previous page' });
      fireEvent.click(prevPageButton);

      expect(tableRows.children.length).toBe(5);
    });

    it('renders all reports in a single row', async () => {
      const tableRows = screen.getByTestId('tableTest')
      fireEvent.change(screen.getByTestId('rowsDropDown'), { target: { value: 10 } })
      expect(tableRows.children.length).toBe(reports.length);
    });

    it('renders section modal', async () => {
      const rowSectionClickHandler = screen.getAllByTestId("rowTest")[0];
      fireEvent.click(rowSectionClickHandler);

      expect(screen.getByTestId(/sectionTest/)).toBeInTheDocument()
    });

    it('does not renders section modal', async () => {
      expect(screen.queryByTestId(/sectionTest/)).toBeFalsy();
    });
  })
  })
