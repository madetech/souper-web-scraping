import { act, fireEvent, render, screen } from '@testing-library/react';
import axios from 'axios';
import React from 'react';
import SectionModal from "../../Components/SectionModal";
import sections from "../Fixtures/Sections";
jest.mock("axios");

jest.mock('../../Components/FeedbackModal', () => () =>
  <div data-testid="feedbackTest" />
);

jest.mock("react-plotly.js", () => ({
  __esModule: true,
  default: jest.fn(() => <div />),
}));

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
    it('renders table contents', async () => {
      expect(screen.getByText('Sections List: anna')).toBeInTheDocument();
    });

    it('renders sections in the first row', () => {
      const tableRows = screen.getByTestId('tableTest')
      expect(tableRows.children.length).toBe(5);
    });

    it('renders the next page', async () => {
      const tableRows = screen.getByTestId('tableTest')

      const nextPageButton = screen.getByRole("button", { name: 'Go to next page' });
      fireEvent.click(nextPageButton);

      expect(tableRows.children.length).toBe(2);
    });

    it('renders the previous page', async () => {
      const tableRows = screen.getByTestId('tableTest')

      const nextPageButton = screen.getByRole("button", { name: 'Go to next page' });
      fireEvent.click(nextPageButton);

      const prevPageButton = screen.getByRole("button", { name: 'Go to previous page' });
      fireEvent.click(prevPageButton);

      expect(tableRows.children.length).toBe(5);
    });

    it('renders all sections in a single row', async () => {
      const tableRows = screen.getByTestId('tableTest')
      fireEvent.change(screen.getByTestId('rowsDropDown'), { target: { value: 10 } })
      expect(tableRows.children.length).toBe(sections.length);
    });

    it('closes the modal', async () => {
      fireEvent.click(screen.getByTestId('HighlightOffSharpIcon'))

      expect(handleClose).toHaveBeenCalledTimes(1)
    });

    it('renders feedback modal', async () => {
      const rowSectionClickHandler = screen.getAllByTestId("rowTest")[0];
      fireEvent.click(rowSectionClickHandler);

      expect(screen.getByTestId(/feedbackTest/)).toBeInTheDocument()
    });

    it('does not renders feedback modal', async () => {
      expect(screen.queryByTestId(/feedbackTest/)).toBeFalsy();
    });
  })
})
