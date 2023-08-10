import { act, render, screen } from '@testing-library/react';
import axios from 'axios';
import React from 'react';
import FeedbackModal from "../../Components/FeebackModal";
import feedback from "../Fixtures/Feedback";

jest.mock("axios");

describe('<FeedbackModalHelper />', () => {
    describe('render modal', () => {
        it('modal shows the feedback list and a close button', async () => {
            const handleClose = jest.fn();

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

            const tableRows = screen.getByTestId('tableTest')

            expect(screen.getByText('Feedback List for section one')).toBeInTheDocument();
            expect(tableRows.children.length).toBe(feedback.length);


        });
    })
})

