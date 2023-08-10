import { act, fireEvent, render, screen } from '@testing-library/react';
import axios from 'axios';
import React from 'react';
import FeedbackModal from "../../Components/FeedbackModal";
import feedback from "../Fixtures/Feedback";

jest.mock("axios");

const handleClose = jest.fn();

describe('<FeedbackModalHelper />', () => {
  beforeEach(async () => {
    await axios.get.mockImplementationOnce(() => Promise.resolve({
      status: 200,
      data: feedback

    }))

    const baseProps = {
      sectionId: 1,
      sectionTitle: "section one",
    };

    await act(async () => render(
      <FeedbackModal {...baseProps} open={true} onClose={handleClose} />,
    ));

  });

  afterAll(() => {
    jest.resetAllMocks();
  });


  describe('render modal', () => {
    it('shows the feedback list', async () => {
      const tableRows = screen.getByTestId('tableTest')
      expect(screen.getByText('Feedback List for section one')).toBeInTheDocument();
      expect(feedback.length).toBe(6)
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

    it('renders all feedback in a single row', async () => {
      const tableRows = screen.getByTestId('tableTest')
      fireEvent.change(screen.getByTestId('rowsDropDown'), { target: { value: 10 } })
      expect(tableRows.children.length).toBe(6);
    });

    it('closes the modal', async () => {
      fireEvent.click(screen.getByTestId('HighlightOffSharpIcon'))

      expect(handleClose).toHaveBeenCalledTimes(1)
    });
  })
})

