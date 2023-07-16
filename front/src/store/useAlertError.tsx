import { AlertColor } from '@mui/material';
import { create } from 'zustand';

type InitialState = {
  message: string;
  open?: boolean;
  status: AlertColor | undefined;
};

type UseAlertError = {
  initialState: InitialState;
  handleError: (error: InitialState) => void;
  handleClose: () => void;
};

const initialState: InitialState = {
  message: '',
  open: false,
  status: 'error',
};

export const useAlertError = create<UseAlertError>((set) => ({
  initialState,
  handleError: (error: InitialState) => {
    set((prev) => ({
      ...prev,
      initialState: { ...error, open: true },
    }));
    setTimeout(() => {
      set((prev) => ({
        ...prev,
        initialState,
      }));
    }, 3000);
  },
  handleClose: () => {
    set((prev) => ({
      ...prev,
      initialState,
    }));
  },
}));
