import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import ModalHelper from '../../Helpers/ModalHelper';

describe('<ModalHelper />', () => {
    describe('render modal', () => {
        it('modal shows the children and a close button', () => {
            const handleClose = jest.fn()
            render(
                <ModalHelper open={true} onClose={handleClose}>
                    <div>test</div>
                </ModalHelper>,
            )
            
            expect(screen.getAllByText('test')).toBeTruthy()

            fireEvent.click(screen.getByTestId('HighlightOffSharpIcon'))

            expect(handleClose).toHaveBeenCalledTimes(1)
        });
    })
})

