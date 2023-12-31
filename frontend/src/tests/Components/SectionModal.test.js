import { act, fireEvent, render, screen } from '@testing-library/react';
import axios from 'axios';
import React from 'react';
import SectionModal from "../../Components/SectionModal";
import sections from "../Fixtures/Sections";
jest.mock("axios");

jest.mock('../../Components/FeedbackModal', () => () =>
  <div data-testid="feedbackTest" />
);

const handleClose = jest.fn();

describe('<SectionModal />', () => {
  describe('render modal', () => {
    beforeEach(async () => {
      await axios.get.mockImplementationOnce(() => Promise.resolve({
        status: 200,
        data: sections
      }))

      await act(async () => render(<SectionModal
        open={true}
        onClose={() => handleClose()}
        rowId={1}
        reportName={'anna'}
        reportId={1} />)
      );
    });

    afterAll(() => {
      jest.resetAllMocks();
    });

    function expectRowTextContentToActual(array) {
      array.map((column, index) => (
        expect(screen.getAllByTestId('sectionRowTest')[index].children.item(1)?.textContent).toEqual(column)
      ))
    }

    it('renders table contents', async () => {
      expect(screen.getByText('Sections List: anna')).toBeInTheDocument();
    });

    it('renders sections in the first row', () => {
      const tableRows = screen.getAllByTestId('tableTest')[0]
      expect(tableRows.children.length).toBe(5);
    });

    it('renders the next page', async () => {
      const tableRows = screen.getAllByTestId('tableTest')[0]

      const nextPageButton = screen.getByRole("button", { name: 'Go to next page' });
      fireEvent.click(nextPageButton);

      expect(tableRows.children.length).toBe(2);
    });

    it('renders the previous page', async () => {
      const tableRows = screen.getAllByTestId('tableTest')[0]

      const nextPageButton = screen.getByRole("button", { name: 'Go to next page' });
      fireEvent.click(nextPageButton);

      const prevPageButton = screen.getByRole("button", { name: 'Go to previous page' });
      fireEvent.click(prevPageButton);

      expect(tableRows.children.length).toBe(5);
    });

    it('renders all sections in a single row', async () => {
      const tableRows = screen.getAllByTestId('tableTest')[0]
      fireEvent.change(screen.getByTestId('rowsDropDown'), { target: { value: 10 } })
      expect(tableRows.children.length).toBe(sections.length);
    });

    it('sorts column', async () => {
      fireEvent.click(screen.getAllByTestId('ArrowDownwardIcon')[0])
      expect(screen.getByText("sorted ascending")).toBeInTheDocument();

      fireEvent.click(screen.getAllByTestId('ArrowDownwardIcon')[0])
      expect(screen.getByText("sorted descending")).toBeInTheDocument();
    });

    it('sorts decision column in ascending order ', async () => {
      fireEvent.change(screen.getByTestId('rowsDropDown'), { target: { value: 10 } })

      const unSortedDecisionList = [
        "Met", "Not met", "Met", "TBC", "Met", "Not met", "Not met"
      ];

      expectRowTextContentToActual(unSortedDecisionList)

      fireEvent.click(screen.queryAllByTestId('ArrowDownwardIcon')[1])

      const sortedDecisionList = ["Met", "Met", "Met", "Not met", "Not met", "Not met", "TBC"]
      expectRowTextContentToActual(sortedDecisionList)
    });

    it('sorts decision column in decending order ', async () => {
      fireEvent.change(screen.getByTestId('rowsDropDown'), { target: { value: 10 } })

      fireEvent.click(screen.queryAllByTestId('ArrowDownwardIcon')[1])
      fireEvent.click(screen.queryAllByTestId('ArrowDownwardIcon')[1])

      const descisionList = ["TBC", "Not met", "Not met", "Not met", "Met", "Met", "Met"]

      expectRowTextContentToActual(descisionList)
    });
    it('closes the modal', async () => {
      fireEvent.click(screen.getByTestId('HighlightOffSharpIcon'))

      expect(handleClose).toHaveBeenCalledTimes(1)
    });

    it('renders feedback modal', async () => {
      const rowSectionClickHandler = screen.getAllByTestId("sectionRowTest")[0];
      fireEvent.click(rowSectionClickHandler);

      expect(screen.getByTestId(/feedbackTest/)).toBeInTheDocument()
    });

    it('renders table showing totals for each decision type', async () => {
      const decisionRows = screen.getAllByTestId('decisionRowTest');

      expect(decisionRows[0]?.children.item(0)?.textContent).toEqual("Met")     
      expect(decisionRows[0]?.children.item(1)?.textContent).toEqual("3")

      expect(decisionRows[1]?.children.item(0)?.textContent).toEqual("Not Met")
      expect(decisionRows[1]?.children.item(1)?.textContent).toEqual("3")

      expect(decisionRows[2]?.children.item(0)?.textContent).toEqual("TBC")
      expect(decisionRows[2]?.children.item(1)?.textContent).toEqual("1")

    });

    it('does not renders feedback modal', async () => {
      expect(screen.queryByTestId(/feedbackTest/)).toBeFalsy();
    });
  })
})
