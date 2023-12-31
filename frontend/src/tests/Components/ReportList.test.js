import { act, fireEvent, render, screen } from '@testing-library/react';
import axios from 'axios';
import React from 'react';
import ReportList from "../../Components/ReportList";
import { reports } from "../Fixtures/Reports";

jest.mock("axios");

jest.mock('../../Components/SectionModal', () => () =>
  <div data-testid="sectionTest" />
);

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

    function expectRowTextContentToActual(array) {
      array.map((column, index) => (
        expect(screen.getAllByTestId('reportRowTest')[index].children.item(1)?.textContent).toEqual(column)
      ))
    }
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

    it('sorts column', async () => {
      fireEvent.click(screen.getAllByTestId('ArrowDownwardIcon')[0])
      expect(screen.getByText("sorted ascending")).toBeInTheDocument();

      fireEvent.click(screen.getAllByTestId('ArrowDownwardIcon')[0])
      expect(screen.getByText("sorted descending")).toBeInTheDocument();
    });

    it('sorts assessment date column in ascending order ', async () => {
      fireEvent.change(screen.getByTestId('rowsDropDown'), { target: { value: 10 } })

      const unSortedAssessmentDateColumn = [
        "2022-02-03", "2021-11-11", "2019-10-09", "2023-02-05", "2020-12-12", "2022-11-10",
      ];

      expectRowTextContentToActual(unSortedAssessmentDateColumn)

      fireEvent.click(screen.queryAllByTestId('ArrowDownwardIcon')[1])

      const sortedAssessmentDateColumn = ["2019-10-09", "2020-12-12", "2021-11-11", "2022-02-03", "2022-11-10", "2023-02-05"]
      expectRowTextContentToActual(sortedAssessmentDateColumn)
    });

    it('sorts assessment date column in decending order ', async () => {
      fireEvent.change(screen.getByTestId('rowsDropDown'), { target: { value: 10 } })

      fireEvent.click(screen.queryAllByTestId('ArrowDownwardIcon')[1])
      fireEvent.click(screen.queryAllByTestId('ArrowDownwardIcon')[1])

      const assessmentDateColumn = ["2023-02-05", "2022-11-10", "2022-02-03", "2021-11-11", "2020-12-12", "2019-10-09"]

      expectRowTextContentToActual(assessmentDateColumn)
    });

    it('renders section modal', async () => {
      const rowSectionClickHandler = screen.getAllByTestId("reportRowTest")[0];
      fireEvent.click(rowSectionClickHandler);

      expect(screen.getByTestId(/sectionTest/)).toBeInTheDocument()
    });

    it('does not renders section modal', async () => {
      expect(screen.queryByTestId(/sectionTest/)).toBeFalsy();
    });
  })
})
