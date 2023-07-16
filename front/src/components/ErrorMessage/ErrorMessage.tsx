import { Alert, CircularProgress, Snackbar } from '@mui/material';
import { useAlertError } from '../../store/useAlertError';

export function ErrorMessage() {
  const { initialState, handleClose } = useAlertError();
  return (
    <>
      {initialState.open && (
        <Snackbar open={initialState.open} autoHideDuration={3000}>
          <Alert
            icon={
              initialState.status === 'info' ? (
                <CircularProgress size={20} />
              ) : null
            }
            onClose={() => handleClose()}
            severity={initialState.status}
            sx={{ width: '100%' }}
          >
            {initialState.message}
          </Alert>
        </Snackbar>
      )}
    </>
  );
}
