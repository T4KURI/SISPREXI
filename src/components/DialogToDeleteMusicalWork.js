import * as React from 'react';

import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';

import CustomAlertWarning from './CustomAlertWarning';

export default function DialogToDelete({
  handleClose,
  handleDelete,
  itemId,
  open,
  title,
 }) {

  return (
    <Dialog
      open={open}
      onClose={handleClose}
      aria-labelledby="alert-dialog-title"
      aria-describedby="alert-dialog-description"
    >
      <DialogTitle id="alert-dialog-title">{title}</DialogTitle>
      <DialogContent>
        <CustomAlertWarning message='También se eliminarán los FONOGRAMAS asociados a esta OBRA MUSICAL' />
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose}>Cancelar</Button>
        <Button onClick={() => handleDelete(itemId)} variant="contained" autoFocus>Eliminar</Button>
      </DialogActions>
    </Dialog>
  );
}